import socket
import des

#this will serve as the "server" for our implementation

def Main():
    host = "127.0.0.1"
    port = 5002
    #necessary to initiate the server
    mySocket = socket.socket()
    mySocket.bind((host,port))

    print("Waiting for connection.....")
    #listens for a user to connect
    mySocket.listen(2)
    #getting the user's connection info
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))

    while True:
            #receiving the response from the other user
            data = conn.recv(1024).decode()
            print("Received from client = " + data)
            #decrypting the other user's message
            key = "0A1B2C3D4E5F6071"
            decryptedMessage = des.decrypt(data, key)
            if not data:
                    break
            print ("Decrypted Message = " + decryptedMessage)
            print("\n")
            message = input("Enter the message you want to encrypt -> ")
            #encrypting the message using DES
            finalEncryptedMessage = des.bin2hex(des.encrypt(message, key))
            print("Encrypted message = " + finalEncryptedMessage)
            #prints the pretty loading bar
            des.sending()
            #sending the message
            conn.send(finalEncryptedMessage.encode())
 
    conn.close()
     
if __name__ == '__main__':
    Main()
