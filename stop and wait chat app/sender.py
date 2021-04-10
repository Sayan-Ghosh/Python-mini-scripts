import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8000

serversocket.bind((host,port))

data = "Hello reciever"

serversocket.listen(5)
print ('Sender listening')

while(True):
	clientsocket, address = serversocket.accept()
	print("Reciever "+str(address)+" connected")

	while (True):
		data = input("Enter data to send:")
		encoded_data = data.encode()

		clientsocket.send(encoded_data)
		encoded_data = clientsocket.recv(1024)
		data = encoded_data.decode()
		print("Recieved data:" +data)

		
