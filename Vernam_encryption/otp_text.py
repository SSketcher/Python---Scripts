import matplotlib.pyplot as plt
import numpy as np


def toASCII(input_text):      #ACII characters to nuemric valeus
    orginal_text = []
    for i in range(len(input_text)):
        char = input_text[i]
        orginal_text.append(ord(char))
    return orginal_text

def fromASCII(input_data):      #nuemric valeus to ACII characters
    text = ""
    for n in input_data:
        text += chr(n)
    return text

def key_gen(length):      #key generating function
    key = []
    for _ in range(length):     # _ as a throwaway variable
        key.append(int(np.random.randint(32, 126, 1)))
    return key

def encrypt(input_data,key_):      #encypting function
    cipher = []
    if len(key_)<len(input_data):
        temp = key_
        while len(key_)<len(input_data):
            key_ += temp
    for i in range(len(input_data)):
        cipher.append((input_data[i] + key_[i])%126)
    return cipher

def decrypt(input_data,key_):      #decypting function
    cipher = []
    if len(key_)<len(input_data):
        temp = key_
        while len(key_)<len(input_data):
            key_ += temp
    for i in range(len(input_data)):
        cipher.append((input_data[i]-key_[i])%126)
    return cipher

def list_to_string(key_list):      #function translate list into string
    key = ''
    for i in range(len(key_list)):
        key += str(key_list[i]) + ','
    key = key[:-1]
    return key

def string_to_list(key_string):      #function translate string of numbers into list of numbers
    key = []
    key_strlist = key_string.split(',')
    try:
        key = map(int, key_strlist)
        key = list(key)
    except:
        raise ValueError("Key error...")
    return key

def makeHist(text, text_shifted):     #function for drawing histograms
    fig, axs = plt.subplots(2, 1, constrained_layout=True)      #setting subplot 
    fig.suptitle('Comparison of the characters distribution', fontsize=16)       #setting figure title

    axs[0].hist(toASCII(text), bins = list(range(32,126)))       #making histogram and adding it to the subplot
    axs[0].set_title('Histogram of original text')      #setting tittle of histogram
    axs[0].set_xlabel('Characters')     # x axis name
    axs[0].set_ylabel('Frequency')      # y axis name


    axs[1].hist(text_shifted, bins = list(range(32,126)))       #making histogram and adding it to the subplot
    axs[1].set_title('Histogram of shifted text')
    axs[1].set_xlabel('Characters')
    axs[1].set_ylabel('Frequency')

    plt.show()

def main():     #main function
    print('Do you want encrypt or decrypt text?')
    flag = input('Enter enc or dec: ')     #entering the flag to set performed operation
    if flag.lower() != 'enc' and flag.lower() != 'dec':       #checking if the flag was set correctly
        raise ValueError("You entered wrong value")

    path = input('Enter the file path: ')
    if type(path) != str:       #path must be a string
        raise TypeError("Path must be a string")
    with open (path, "r", encoding = "utf-8") as myfile:
        text = myfile.read()
    
    if flag.lower() == 'enc':       #checking if the flag was set to encrypt
        s = int(input('Enter key length: '))     #entering the key length
        key = key_gen(s)

        text_mod = encrypt(toASCII(text), key)       #encrypting text

        print('Do you whant to save key to text file?')
        sav = input('Enter Y or N: ')        #entering the flag for saving the result
        if sav.upper() != 'Y' and sav.upper() != 'N':       #checking if the flag was set correctly
            raise ValueError("You entered wrong value")
        
        if sav.upper() == 'Y':       #checking if the saving flag was set to Y
            with open ('key.txt', "wt", encoding = "utf-8") as myfile:        #saving result
                myfile.write(list_to_string(key))
        elif sav.upper() == 'N':       #checking if the saving flag was set to N
            pass

    elif flag.lower() == 'dec':       #checking if the flag was set to decrypt
        path = input('Enter the path to the text file containing the key: ')        #loading key from txt file
        if type(path) != str:       #path must be a string
            raise TypeError("Path must be a string")
        with open (path, "r", encoding = "utf-8") as myfile:
            key_str = myfile.read()
        key = string_to_list(key_str)       #translating input key string into list

        text_mod = decrypt(toASCII(text), key)       #decrypting text
    else:       #if the flag was set wrong
        print('Something went wrong ... sorry')

    print('Do you whant to save result?')
    sav = input('Enter Y or N: ')        #entering the flag for saving the result
    if sav.upper() != 'Y' and sav.upper() != 'N':       #checking if the flag was set correctly
        raise ValueError("You entered wrong value")
    
    if sav.upper() == 'Y':       #checking if the saving flag was set to Y
        with open ('result_text.txt', "wt", encoding = "utf-8") as myfile:        #saving result
            myfile.write(fromASCII(text_mod))
    elif sav.upper() == 'N':       #checking if the saving flag was set to N
        print(fromASCII(text_mod))      #displaying result
    else:       #if the flag was set wrong
        print('Something went wrong ... sorry')

    print('Do you whant to show histogram')
    his = input('Enter Y or N: ')        #entering the flag for making histogram
    if his.upper() != 'Y' and his.upper() != 'N':       #checking if the flag was set correctly
        raise ValueError("You entered wrong value")
    
    if his.upper() == 'Y':       #checking if the his was set to Y
        makeHist(text,text_mod)      #using makeHist() function
    elif his.upper() == 'N':       #checking if the his was set to N
        pass      #doing nothing
    else:       #if the flag was set wrong
        print('Something went wrong ... sorry')

    
if __name__ == "__main__":
    main()