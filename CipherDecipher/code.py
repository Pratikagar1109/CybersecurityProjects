def encrypt(text,shift):
    result=""
    i=0
    for i in range(len(text)):
        char=text[i]

        if char.isupper():
             result += chr((ord(char) + shift - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        else:
            result += char

    return result


def decrypt(text,shift):

    result=""
    i=0

    for i in range(len(text)):

        char=text[i]

        if char.isupper():
            result += chr((ord(char) - shift -65) % 26 + 65)
        
        elif char.islower():
            result += chr((ord(char) - shift -97 ) % 26 + 97)

        else:
            result += char
    
    return result;
                          
                        

if __name__ == "__main__":
    text=str(input("ENTER THE STRING TO BE ENCYPTED"))
    shift =int(input("enter the value of shift"))

    
    print("Original Text: ", text)
    print("Shift: ", shift)
    
    # Encrypt the text
    encrypted_text = encrypt(text, shift)
    print("Encrypted Text: ", encrypted_text)


    decrypted_text = decrypt(encrypted_text,shift)
    print("Decrypted text: ", decrypted_text)