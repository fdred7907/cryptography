# to make a simple shift cipher with shift distance d

def shift_cipher(plain_text,shift_dist):
    cipher_text=""
    for char in plain_text:
        if char.isupper():
            temp = ((ord(char)+int(shift_dist)-65)%26)+65
            cipher_text += chr(temp)
        elif char.islower():
            temp = ((ord(char)+int(shift_dist)-97)%26)+97
            cipher_text += chr(temp)
        else:
            temp = int(char)+int(shift_dist)%9
            cipher_text += str(temp)
    return cipher_text


plain_text = input("Enter the message to send")

shift_dist = input("Enter the shift distance to encode")

cipher_text = shift_cipher(plain_text,shift_dist)

print(f"The encoded message is {cipher_text}")


        