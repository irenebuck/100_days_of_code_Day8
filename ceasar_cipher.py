alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

# Ceaser cipher encrypts or decrpyts user text.  https://en.wikipedia.org/wiki/Caesar_cipher
# Only letters are encoded/decoded
def caesar(start_text, shift_amount, cipher_direction):
    output = ""
    if cipher_direction == "decode":
        shift_amount *= -1     # this allows the shifting to decode in line 37, subtracting value
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            output += alphabet[new_position]
        else:
            output += char     # captures the non-alphabet values and spaces
    print(f"Here's the {direction}d result: {output}.")

go_again = True

while go_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise, type 'no'.")

    if result == 'no':
        go_again = False
        print("Goodbye!")