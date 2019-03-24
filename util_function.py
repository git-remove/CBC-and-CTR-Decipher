# xor two hex strings of different lengths
def hexxor(hex_a, hex_b):     
    if len(hex_a) > len(hex_b):
        return "".join([hex(int(x, 16) ^ int(y, 16))[2:] for (x, y) in zip(hex_a[:len(hex_b)], hex_b)])
    else:
        return "".join([hex(int(x, 16) ^ int(y, 16))[2:] for (x, y) in zip(hex_a, hex_b[:len(hex_a)])])

# print a hex string, two chars separated by separator
def print_hex(str, separator):
   if len(str) == 0 :
      return -1
   for char in str[:-1]:
      print("{:02x}".format(ord(char)), end = separator)
   print("{:02x}".format(ord(str[-1])))

# convert hex string into character by ascii table
# for example input "4161", output "Aa"
def print_ascii(hex_string):
    result = ""
    for i in range(int(len(hex_string)/2)):
        ascii_num = int(hex_string[2 * i], 16) * 16 + int(hex_string[2 * i + 1], 16)
        result = result + chr(ascii_num)
    print(result)