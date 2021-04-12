import matplotlib.pyplot as plt

def fromASCII(input_data):      #ACII characters to nuemric valeus
    text = ""
    for n in input_data:
        text += chr(n)
    return text

def toASCII(input_text):      #nuemric valeus to ACII characters
    orginal_text = []
    for i in range(len(input_text)):
        char = input_text[i]
        orginal_text.append(ord(char))
    return orginal_text

def encrypt(input_data,s):      #encypting function
    result = []
    for i in range(len(input_data)):
        foo = (input_data[i] + s)%122
        result.append(foo + 32)
    return result

def decrypt(input_data,s):      #decypting function
    result = []
    for i in range(len(input_data)):
        foo = input_data[i] - 32
        result.append((foo - s)%122)
    return result

def makeHist(text, text_shifted):     #function for drawing histograms
    fig, axs = plt.subplots(2, 1, constrained_layout=True)      #setting subplot 
    fig.suptitle('Comparison of the tonal distribution in the  images.', fontsize=16)       #setting figure title

    axs[0].hist(text_shifted, bins = list(range(32,122)))       #making histogram and adding it to the subplot
    axs[0].set_title('Histogram of shifted image')      #setting tittle of histogram
    axs[0].set_xlabel('Colors')     # x axis name
    axs[0].set_ylabel('Frequency')      # y axis name


    axs[1].hist(toASCII(text), bins = list(range(32,122)))       #making histogram and adding it to the subplot
    axs[1].set_title('Histogram of original image')
    axs[1].set_xlabel('Colors')
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

    s = int(input('Enter value of shift: '))     #entering the shift valueenc
    
    if flag.lower() == 'enc':       #checking if the flag was set to encrypt
        text_mod = encrypt(toASCII(text), s)       #encrypting text
    elif flag.lower() == 'dec':       #checking if the flag was set to decrypt
        text_mod = decrypt(toASCII(text), s)       #decrypting text
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