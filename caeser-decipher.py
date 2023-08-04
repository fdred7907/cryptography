# brute forcing deciphering caesar cipher
import string
import json


def create_decoders():
    decoders = {}
    for shift_distance in range(26):
        tempdec = {}
        for i in range(26):
            letupp = string.ascii_uppercase[i]
            letlow = string.ascii_lowercase[i]
            temp = (i + shift_distance)%26
            subupp = string.ascii_uppercase[temp]
            sublow = string.ascii_lowercase[temp]
            tempdec[subupp] = letupp
            tempdec[sublow] = letlow
        decoders[shift_distance] = tempdec
    return decoders

def create_corpus():
    f = open('words_dictionary.json')
    dict = json.load(f)
    return dict

def create_corpus_from_txt():
    count = 0
    corpus = {}
    with open("words_dict.txt") as f:
        for line in f:
            count += 1
            val = line.split()
            corpus[count] = val[0]
    return corpus


if __name__ == "__main__":
    msg = input("\n Please enter the encrypted message \n")
    decodedmsgs = {}
    decoders = create_decoders()
    # print(decoders)
    for i in range(26):
        key = str(i)
        decodedmsgs[key] = ""
        for letter in msg:
            if letter in decoders[i]:
                decodedmsgs[key] += decoders[i][letter]
            else :
                decodedmsgs[key] += letter
    corpus = create_corpus_from_txt()
    # print(list(corpus.values())[:100])
    print("\n The decoded messages for all caesar ciphers are : \n")
    print("One of these will be readable if it is a Caesar Cipher \n")
    for i in range(1,26):
        print(f"\n {decodedmsgs[str(i)]} \n")
        mtclen = 0
        msglen = len(decodedmsgs[str(i)])
        corpuslist = corpus.values()
        # print(corpuslist)
        for word in corpuslist:
            if word in decodedmsgs[str(i)].lower():
                mtclen += 1
        # if mtclen/msglen > 0.5:
            # final = i
            # break
        print(f"Number of matches for {decodedmsgs[str(i)]} is {mtclen}")
    # print(f"\n The original message is {decodedmsgs[str(i)]} \n")

