import socket
import des
import sys
from time import sleep

# this will serve as the "client" for our implementation
def Main():
        host = "127.0.0.1"
        port = 5001
        #necessary to connect to the server
        mySocket = socket.socket()
        mySocket.connect((host,port))
        
        message = input("Enter the message you want to encrypt -> ")
        key = "0A1B2C3D4E5F6071"
        #encrypting the message using DES
        finalEncryptedMessage = des.bin2hex(des.encrypt(message, key))
        print("Encrypted message = " + finalEncryptedMessage)

        #have the communication go on forever
        while message != 'q':

                #prints the pretty loading bar
                des.sending()

                #encrypting the message
                finalEncryptedMessage = des.bin2hex(des.encrypt(message, key))
                #sending the message
                mySocket.send(finalEncryptedMessage.encode())
                #receiving the response from the other user
                data = mySocket.recv(1024).decode()
                print("Received from server = " + data)
                #decrypting the other user's message
                decryptedMessage = des.decrypt(data, key)
                if not data:
                        break
                print ("Decrypted Message = " + des.bin2string(decryptedMessage))
                print("\n")
                #setting up the message all over again....
                message = input("Enter the message you want to encrypt -> ")
                finalEncryptedMessage = des.bin2hex(des.encrypt(message, key))
                print("Encrypted message = " + finalEncryptedMessage)
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()
    