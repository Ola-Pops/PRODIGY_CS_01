# This is a Caesar Cipher encoder and decoder made by Olamide Pops.

# Create dictionaries for the characters (Uppercase, lowercase and special characters)
alphabet_lower  = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Function to get the shift value
def get_shift():
    print('What is the shift?')
    return int(input())

# Function to get the message
def get_message():
    print('What message do you want to encrypt or decrypt?')
    return input()

# Translation dictionary for all characters
def create_translation_dicts(shift):
    translateAlphaL = {}
    translateAlphaU = {}
    for i in range(26):
        translateAlphaL[alphabet_lower[i]] = alphabet_lower[(i + shift) % 26]
        translateAlphaU[alphabet_upper[i]] = alphabet_upper[(i + shift) % 26]
    return translateAlphaL, translateAlphaU

# Function to translate the message
def translate_message(message, translateAlphaL, translateAlphaU):
    cypherText = ''
    for letter in message:
        if letter in translateAlphaL:
            cypherText += translateAlphaL[letter]
        elif letter in translateAlphaU:
            cypherText += translateAlphaU[letter]
        else:
            cypherText += letter
    return cypherText

# Encryption Function
def encrypt():
    shift = get_shift()
    message = get_message()
    translateAlphaL, translateAlphaU = create_translation_dicts(shift)
    encrypted_message = translate_message(message, translateAlphaL, translateAlphaU)
    print('Encrypted message:', encrypted_message)

#Decryption with shift provided
def decrypt_with_shift():
	message = get_message()
	shift = -get_shift()  # Reverse the shift for decryption
	translateAlphaL, translateAlphaU = create_translation_dicts(shift)
	decrypted_message = translate_message(message, translateAlphaL, translateAlphaU)
	print('Decrypted message:', decrypted_message)

#Decryption without shift (brute)
def decrypt_brute():
	message = get_message()
	for i in range(26):
		shift = i
		translateAlphaL, translateAlphaU = create_translation_dicts(shift)
		decrypted_message = translate_message(message, translateAlphaL, translateAlphaU)
		print('Decrypted message could be:', decrypted_message)
		
# Decryption Function
def decrypt():
	while True:
		print('Do you know the shift?\n Type "Y" to reply Yes, "N" for No and "Q" to quit')
		choice = input().upper()
		if choice == "Y":
			decrypt_with_shift()
			break
		elif choice == "N":
			decrypt_brute()
			break
		elif choice == "Q":
			break
		else:
			print('Invalid choice, please enter "Y", "N", or "Q"')

# Function to choose between encryption and decryption
def encrypt_or_decrypt():
    while True:
        print('To encrypt a message type "E", to decrypt a message type "D", to quit type "Q"')
        choice = input().upper()
        if choice == "E":
            encrypt()
        elif choice == "D":
            decrypt()
        elif choice == "Q":
            break
        else:
            print('Invalid choice, please enter "E", "D", or "Q"')

encrypt_or_decrypt()
