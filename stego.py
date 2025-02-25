import cv2

# Reading the encrypted image
img = cv2.imread("encryptedImage.jpg")  # Path to the encrypted image

# Input passcode for decryption
pas = input("Enter passcode for Decryption: ")

# Reading the passcode from the saved file
with open("password.txt", "r") as f:
    password = f.read()

# Dictionary for converting integers back to characters
c = {}
for i in range(255):
    c[i] = chr(i)

# Initialize variables for extracting the hidden message
message = ""
n = 0
m = 0
z = 0

# Decrypt the message if the passcode matches
if password == pas:
    for i in range(1000):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    
        
        # Check for the end of the message (using a null character as the end marker)
        if message[-1] == "\x00":
            break
    
    print("Decrypted message:", message.strip('\x00'))  # Remove any null characters
else:
    print("Incorrect passcode! You are not authorized to decrypt the message.")
