#python based random letter shifter

import string
import random

def create_dict():
    encoder = {}
    decoder = {}
    shift_list = []
    count = 0
    for i in range(26):
        upplet = string.ascii_uppercase[i]
        done = False
        while done == False:
            shift = random.randrange(0,26)
            uppsub = string.ascii_uppercase[(i + shift)%26]
            if uppsub not in encoder.values():
                lowlet = string.ascii_lowercase[i]
                # uppsub = string.ascii_uppercase[(i + shift)%26]
                lowsub = string.ascii_lowercase[(i + shift)%26]
                encoder[upplet] = uppsub
                encoder[lowlet] = lowsub
                decoder[uppsub] = upplet
                decoder[lowsub] = lowlet
                done = True
    return [encoder,decoder]

def encoder_fun(msg,encoding):
    cipher = ""
    for char in msg:
        if char in encoding:
            cipher += encoding[char]
        else:
            cipher += char
    return cipher


def decoder_fun(msg,decoding):
    return encoder_fun(msg,decoding)

if __name__ == "__main__":
    ciphers = create_dict()
    print(ciphers[0])
    print(f"\n {ciphers[1]}")
    choice = 4
    # choice = int(input("Enter : 1 to encode \n 2 to decode \n 0 to quit \n"))
    while choice != 0:
        msg = input("\n Enter the message \n")
        choice = int(input("Enter : 1 to encode \n 2 to decode \n 0 to quit \n"))
        if choice == 1:
            print(encoder_fun(msg,ciphers[0]))
        elif choice == 2:
            print(decoder_fun(msg,ciphers[1]))
        elif choice != 0:
            print("Invalid Choice") 
        else:
            exit()
    
    



