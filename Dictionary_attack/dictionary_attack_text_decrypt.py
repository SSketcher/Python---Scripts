import matplotlib.pyplot as plt
import numpy as np
import unidecode


#Opening text file encoded with Latin-1
with open ('C:/Users/menta/Desktop/STiOD Lab 2/dane/17_tekst.txt', "rb") as myfile: # , encoding = "Latin-1"
    text=myfile.readline()
    print(text) #.decode('utf8')  #.decode('iso-8859-1')
    

#Opening text file where first line is number remaining lines in the file
#Parsing a lines of strings of numbers separated with space in to list of lists containing numbers
with open ('C:/Users/menta/Desktop/STiOD Lab 2/dane/hasla.txt', "r") as myfile:
    keys = []
    length = myfile.readline()
    for i in range(int(length)):
        temp = myfile.readline()
        keys.append(list(int(ch) for ch in temp.split()))

#Function changing a character in to an ASCII decimal code
def toASCII(input_text):
    orginal_text = []
    for i in range(len(input_text)):
        char = input_text[i]
        orginal_text.append(ord(char))
    return orginal_text

#Function changing an ASCII decimal code in to a character
def fromASCII(input_data):
    text = ""
    for n in input_data:
        text += chr(n)
    return text

#Function doing dictionary attack taking text in form of the ASCII codes for each character and a list of keys
def dictionaryAttack(text,dictionary):
    #Decripting function
    def decrypt(input_data,key_):
        decipher = []
        if len(key_)<len(input_data):
            temp = key_
            while len(key_)<len(input_data):
                key_ += temp

        for i in range(len(input_data)):
            foo = input_data[i] - key_[i]
            if foo > 255:
                foo = (foo % 255) - 1
            if foo < 0:
                foo = foo + 256
            decipher.append(foo)
        return decipher

    #Function checking if text is decrepted by checking if it's elements are in range of 32 - 132
    def ifASCII(text):
        counter = 0
        for ch in text:
            if ch in range(32,132):
                counter += 1
            else:
                continue
        if counter >= (len(text)*0.75):
            return True
        else:
            return False
    
    key_n = 0
    for key in dictionary:
        print("Used key: " + str(key_n))
        solution = decrypt(text,key)
        if ifASCII(solution):
            return solution
        else:
            key_n += 1
            continue

    return "False"


data = toASCII(text)

result = dictionaryAttack(data,keys)

if result != "False":
    print(fromASCII(result))
else:
    print(result)
