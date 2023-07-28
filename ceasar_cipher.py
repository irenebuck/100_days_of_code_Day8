alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Ceaser cipher encrypts or decrpyts user text.  https://en.wikipedia.org/wiki/Caesar_cipher
def ceasar(e_or_d, user_text, shift_num):
    ciphered = ""
    if e_or_d == "encode":
        for letter in user_text:
            index = alphabet.index(letter)
            new_index = index + shift_num
            new_letter = alphabet[new_index]
            ciphered += new_letter
        print(f'The encoded text is {ciphered}.')
    else:
        for letter in user_text:
            index = alphabet.index(letter)
            new_index = index - shift_num
            new_letter = alphabet[new_index]
            ciphered += new_letter
        print(f'The decoded text is {ciphered}.')


ceasar(e_or_d=direction, user_text=text, shift_num=shift)


# Another way to write this in a more concise way
def caesar(start_text, shift_amount, cipher_direction):
    output = ""
    if cipher_direction == "decode":
        shift_amount *= -1     # this allows the shifting to decode in line 37, subtracting value
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        output += alphabet[new_position]
    print(f"Here's the {direction}d result: {output}.")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)