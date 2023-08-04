# an optimised shift cipher
# only one time processing -> rest only searching through dictionary -> so more efficient
# neatly solves problem of punctuations , digits and other non-substitutables

def subs_dict(shift_dist):
    encoding = {}
    decoding = {}
    for i in range(26):
        char_upp = chr(i+65)
        sub_upp = chr(((i+int(shift_dist))%26)+65)
        char_low = chr(i+97)
        sub_low = chr(((i+int(shift_dist))%26)+97)

        encoding[char_upp] = sub_upp
        encoding[char_low] = sub_low

        decoding[sub_upp] = char_upp
        decoding[sub_low] = char_low
    return encoding,decoding

def encoder(msg,encoding):
    cipher = ""
    for char in msg:
        if char in encoding:
            cipher += encoding[char]
        else:
            cipher += char
    return cipher


def decoder(msg,decoding):
    return encoder(msg,decoding)

if __name__ == "__main__":
    shift_dist = input("What is the shifting distance ?")
    encoding,decoding = subs_dict(shift_dist)
    print(encoding)
    msg = input("What do you want to convert ?")
    cod = int(input("Please enter 1 for coding, 2 for decoding"))

    if cod == 1:
        print(encoder(msg,encoding))
    else:
        print(decoder(msg,decoding))
    
