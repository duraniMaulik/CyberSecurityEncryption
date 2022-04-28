# scrambled_alphabet
 
from microbit import *
 
# unusual cipher - granted by RANDOM.ORG
def unusual(text):
    alpha  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    crypta = "l7sb3{9u1knd:rt6icyvhfz28e'xwp,g}5ao4 jqm"
    result = ""
 
    for letter in text:
        letter = letter.upper()
        index = alpha.find(letter)
        result = result + crypta[index]
 
    return result
 
# The script starts executing statements from here.
 
sleep(1000)
 
print("Set your keyboard to CAPS LOCK.")
print()
 
while True:
    plaintext = input("Enter a CAPS LOCK string: ")
    
    result = unusual(plaintext)
 
    print("result =", result)
