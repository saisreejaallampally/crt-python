# n = int(input("Enter decimal number: "))
# binary = ""
# while n > 0:
#     rem = n % 2
#     binary = str(rem) + binary
#     n //= 2
# print("Binary:", binary)


# n = input("Enter binary number: ")
# power = 0
# decimal = 0
# for digit in n[::-1]:
#     decimal += int(digit) * (2 ** power)
#     power += 1
# print("Decimal:", decimal)


# n = int(input("Enter decimal number: "))
# octal = ""
# while n > 0:
#     rem = n % 8
#     octal = str(rem) + octal
#     n //= 8
# print("Octal:", octal)


# n = input("Enter octal number: ")
# power = 0
# decimal = 0
# for digit in n[::-1]:
#     decimal += int(digit) * (8 ** power)
#     power += 1
# print("Decimal:", decimal)


# n = input("Enter hexadecimal number: ")
# decimal = int(n, 16)
# print("Decimal:", decimal)


# n = int(input("Enter decimal number: "))
# print("Hexadecimal:", hex(n)[2:].upper())


# binary = input("Enter binary number: ")
# decimal = int(binary, 2)
# octal = oct(decimal)[2:]
# print("Octal:", octal)


# octal = input("Enter octal number: ")
# decimal = int(octal, 8)
# binary = bin(decimal)[2:]
# print("Binary:", binary)


# hexa = input("Enter hexadecimal number: ")
# decimal = int(hexa, 16)
# binary = bin(decimal)[2:]
# print("Binary:", binary)


# binary = input("Enter binary number: ")
# decimal = int(binary, 2)
# hexa = hex(decimal)[2:].upper()
# print("Hexadecimal:", hexa)


# octal = input("Enter octal number: ")
# decimal = int(octal, 8)
# hexa = hex(decimal)[2:].upper()
# print("Hexadecimal:", hexa)


# hexa = input("Enter hexadecimal number: ")
# decimal = int(hexa, 16)
# octal = oct(decimal)[2:]
# print("Octal:", octal)