alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

#Defining the function
def caesar(dir_given, original_text, shift_amount):

    #Process for encryption
    if dir_given == "encode":
        cipher_txt = ""

        #Loop to carry letters forward
        for letter in original_text:
            new_ltr_pos = 0
            if letter in alphabet:
                new_ltr_pos = alphabet.index(letter) + shift_amount
                if new_ltr_pos > 25:
                    new_ltr_pos -= 26
                cipher_txt += alphabet[new_ltr_pos]
            else:
                cipher_txt += letter
        print("")
        print(f"Here is the encoded result: {cipher_txt}")

    #Process for decryption
    if dir_given == "decode":
        decrypted_txt = ""

        #Loop to carry letters backward
        for letter in original_text:
            new_ltr_pos = 0
            if letter in alphabet:
                new_ltr_pos = alphabet.index(letter) - shift_amount
                if new_ltr_pos < 0:
                    new_ltr_pos += 26
                decrypted_txt += alphabet[new_ltr_pos]
            else:
                decrypted_txt += letter
        print("")
        print(f"Here is the decoded result: {decrypted_txt}")


#Print logo and while loop to run the programme until prompted to end.
print(logo)

start_cipher = "yes"
while start_cipher == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #calling the function
    caesar(direction, text, shift)
    start_cipher = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
