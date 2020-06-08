from PIL import Image

with open ("tekst.txt", "r") as myfile:     #Reading text file
    text = myfile.read()
    lista = [format(ord(i), 'b') for i in text]     #Converting each character into byte representation
    binary = ''
    for i in range(len(lista)):     #Making sure every character has the same amount of bytes
        if len(lista[i]) != 7:      #Charactera used to write text in english are max 7 bytes 
            lista[i] = '0' + lista[i]
            binary += lista[i]
        else:
            binary += lista[i]
    binary += '111111111111110'         #Adding end of text flag 


def encode(filename,binary):        #Encoding text in image
    i = 0       #Amount of written bytes
    with Image.open(filename) as img:       #Reading image
        width, height = img.size
        for x in range(0, width):       #Iterating through columns of pixels
            for y in range(0, height):      #Iterating through rows of pixels
                pixel = list(img.getpixel((x, y)))      #Geting current pixel data
                for n in range(0,3):        #Iterating through RGB valeus
                    if(i < len(binary)):        #Checking if there are any bytes to write
                        pixel[n] = pixel[n] & ~1 | int(binary[i])       #Writing bytes by changing last byte of each color
                        i+=1        #Incrementing amount of written data
                img.putpixel((x,y), tuple(pixel))       #Converting rgb values into modified image
        img.save("source_secret.png", "PNG")        #Saving modified image


def decode(filename):       #Decoding text from image
    binary = []
    with Image.open(filename) as img:        #Reading image
        width, height = img.size
        for x in range(0, width):
            for y in range(0, height):
                pixel = list(img.getpixel((x, y)))
                for n in range(0,3):
                    binary.append(pixel[n]&1)       #Reading last byte of each pixel

    length = 0
    for i in range(len(binary)):        #Looking for end of text flag 
        temp = (''.join(str(n) for n in binary[i:i+15]))
        if temp == '111111111111110':
            length = i      #Setting length of text on starting position of flag
            break
    
    text = ''
    for i in range(0, length, 7):       #Decoding text of bytes 
        dec = int(''.join(str(b) for b in binary[i:i+7]), 2)
        text += chr(dec)
    return text     #returning decoded text


encode("NASA_logo.png", binary)

decoded_text = decode("source_secret.png")
print(decoded_text)