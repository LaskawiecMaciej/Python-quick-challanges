"""Ouput should be International Morse Code, and use the standard conventions for symbols not defined inside the ITU recommendation (see Resources).
Input value can be lower or upper case.
Input string can have digits.
Input string can have some special characters (e.g. comma, colon, apostrophe, period, question mark, exclamation mark).
One space " " is expected after each character, except the last one."""



char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}






# Text to morse code
txt=input(str("Input text you wish to be changed to morse code: "))
txt=txt.upper()
ls=list(txt.strip())
morseList=[]
for i in ls:
    morseList.append(char_to_dots[i])
print("".join(morseList))


dots_to_char  = {v: k for k, v in char_to_dots.items()}

#Morse code to text
Mcode=input(str("Input code you wish to be changed to text. Spaces between chars are necessary: "))
McodeList=list(Mcode.split())
TextList=[]
for i in McodeList:
    if i in dots_to_char:
        TextList.append(dots_to_char[i])
    else:
        print("Invalid code")
print("".join(TextList))




