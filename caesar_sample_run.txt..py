def shift(letter, shift_amount):
    unicode = ord(letter) + shift_amount
    if unicode > 126:
        shift_amount = shift_amount - 95
    elif unicode < 32:
        shift_amount = shift_amount + 95

    new_letter = chr(unicode)

    return new_letter

def encrypt(message, shift_amount):
    result = ""

    for letter in message:
        result += shift(letter, shift_amount)

        return result

def decrypt(message, shift_amount):    
    return encrypt(message, -(shift_amount))

unencrypted_message ="aaaaaaaaaaaaaaa"
encrypted_message = encrypt(unencrypted_message, 3)
decrypted_message = decrypt(encrypted_message, 3)

print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)
