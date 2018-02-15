alphabet = " !\"#$%'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~" 
key = "|}~ !\"#$%'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{"

def encrypt(message):
    result =""

    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]

    return result

def decrypt(message):
    result =""

    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]

    return result


unencrypted_message = "A long time ago, in a galaxy far, far, away..."
encrypted_message = encrypt(unencrypted_message)
decrypted_message = decrypt(encrypted_message)

print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)
