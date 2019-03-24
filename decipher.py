from util_function import *
import argparse
from Crypto.Cipher import AES

mode_CBC = 1
mode_CTR = 0

# split the cipher text into 16 bytes blocks
def split_cipher_text(cipher_text, cipher_text_splitted):
    if len(cipher_text) % 32 != 0:
        raise Exception("Cipher text in CBC mode should be padded into multiply of 32!")
    block_num = int( len(cipher_text) / 32 )
    for i in range(block_num):
        cipher_text_splitted.append(cipher_text[32 * i: 32 * (i + 1)])


# eliminate PKCS5 padding
def eliminate_PKCS5_padding(text):
    last_byte = int(text[-2]) * 16 + int(text[-1])
    text = text[:-last_byte * 2]
    return text

# decipher for CBC mode using AES
def CBC_decipher(key, cipher_text, IV):
    cipher_text_splitted = []
    split_cipher_text(cipher_text, cipher_text_splitted)
    middle_level = []
    plain_text = ''
    aes_cipher = AES.new(bytes.fromhex(key))
    for i in range(len(cipher_text_splitted)):
        current_text = bytes.fromhex(cipher_text_splitted[-(i + 1)])
        aes_decipher_result = aes_cipher.decrypt(current_text).hex()
        middle_level.append(aes_decipher_result)
    for i in range(len(middle_level)):
        if i == 0:
            opera1 = IV
        else:
            opera1 = cipher_text_splitted[i - 1]
        opera2 = middle_level[-(i + 1)]
        plain_text = plain_text + hexxor(opera1, opera2)
    print_ascii(eliminate_PKCS5_padding(plain_text))

# decipher for CTR mode using AES
def CTR_decipher(key, cipher_text, IV):
    aes_cipher = AES.new(bytes.fromhex(key))
    block_length = int (len(cipher_text) / 32) + 1 
    opera1 = ""
    for i in range(block_length):
        message_encrypting = IV
        message_encrypting = hex((int(message_encrypting, 16) + i))[2:]
        aes_decipher_result = aes_cipher.encrypt(bytes.fromhex(message_encrypting)).hex()
        opera1 = opera1 + aes_decipher_result
    print_ascii(hexxor(opera1, cipher_text))

def main():
    parser = argparse.ArgumentParser(description='Process arguments.')
    parser.add_argument('--mode', type = str, help = 'whether it is CBC or CTR mode, --mode=CBC or --mode=CTR')
    args = parser.parse_args()
    if args.mode != None:
        if args.mode == 'CTR':
            mode = mode_CTR
        else:
            mode = mode_CBC
    else:
        mode = mode_CBC
    key = input()
    cipher_text = input()
    IV = cipher_text[:32]
    cipher_text = cipher_text[32:]
    if mode == mode_CBC:
        CBC_decipher(key, cipher_text, IV)
    else:
        CTR_decipher(key, cipher_text, IV)
    


if __name__ == "__main__":
    main()