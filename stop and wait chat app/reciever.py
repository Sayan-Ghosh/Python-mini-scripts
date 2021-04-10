import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sender_host = "localhost"
sender_port = 8000

s.connect((sender_host,sender_port))

while (True):
	encoded_data = s.recv(1024)

	data = encoded_data.decode()
	print("Recieved data:" +data)
	data = input("Enter data to send:")
	encoded_data = data.encode()
	s.send(encoded_data)

s.close()
