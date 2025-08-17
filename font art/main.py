# import pyfiglet


# name = input("Enter your name:")
# print("======================================")
# print("banner2-D")
# print("Doom")
# print("Digital")
# print("Diamond")
# print("epic")


# font_style = input("chose fontes avbve the list:")


# font = pyfiglet.figlet_format(f"(name)",f"(font_style)")


# print(font)






import pyfiglet

name = input("Enter your name: ")
print("======================================")
print("banner2-D")
print("Doom")
print("Digital")
print("Diamond")
print("epic")

font_style = input("Choose a font from the list above: ")

try:
    font = pyfiglet.figlet_format(name, font=font_style)
    print(font)
except pyfiglet.FontNotFound:
    print(f"Error: Font '{font_style}' not found. Please choose a valid font.")
