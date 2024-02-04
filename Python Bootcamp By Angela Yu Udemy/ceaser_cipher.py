'''
Type 'encode' to encrypt, type "decode' to decrypt:
encode
Type your message:
Hello World!
Type the shift number:
9
Here's the encoded result: qnuux gxbum!
Type "yes' if you want to go again. Otherwise type 'no'.
yes
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message: anuux gxbum!
Type the shift number:
9
Here's the decoded result: hello world!
Type "yes' if you want to go again. Otherwise type 'no'.
'''


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    direction = input("Type 'encode' for encrypt\nType 'decode' for decrypt\n")
    text = input("Type your message: ").lower()
    shift = int(input("Enter the number of shifts: "))

    def encrypt(text, shifts):
        cipher = ""
        for char in text:
            if char not in alphabets:
                cipher += char
            else:
                index = alphabets.index(char)
                new_index = (index + shifts) % 26  # Use modulo to wrap around within the valid range.
                cipher += alphabets[new_index]
        return cipher

    if direction == "encode":
        result = encrypt(text, shift)
        print("Encrypted text:", result)
    elif direction == "decode":
        result = encrypt(text, -shift)
        print("Decrypted text:", result)
    else:
        print("Invalid input! Please type either 'encode' or 'decode.")
    repeat = input("Type 'yes' if you want to go again. Otherwise, type 'no': ")
    if repeat.lower() != 'yes':
        break
