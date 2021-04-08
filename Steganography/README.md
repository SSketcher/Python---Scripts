# Steganography
## General info
This is ma aprouch on steganography using least significant bit method. 

>Steganography is the practice of concealing a message within another message or a physical object. In computing/electronic contexts, a computer file, message, image, or video is concealed within another file, message, image, or video. The word steganography comes from Greek steganographia, which combines the words steganós (στεγανός), meaning "covered or concealed", and -graphia (γραφή) meaning "writing".
[Steganography Wiki](https://en.wikipedia.org/wiki/Steganography)

This projeckt containcs python script for encoding and decoding the text file into the image and from the image. Ther is only one thing to remember we always need at least ((7 * number_of_characters) + 30)/3 pixels if we want to hide a text in the image.

## Technologies
* Python 3.6

Libraries:
* Pilow

## Sources and helpful materials
[Steganography Wiki](https://en.wikipedia.org/wiki/Steganography)

[Image Steganography Using LSB](http://www.ijstr.org/final-print/dec2019/-Image-Steganography-Using-Lsb.pdf)