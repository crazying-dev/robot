import socket
import robot.config as config
import threading
import atexit
import json
import robot.main_run as main_run

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_sock.bind(("0.0.0.0", config.port))

server_sock.listen(5)
print(f"I listen 0.0.0.0:{config.port} now")

atexit.register(server_sock.close)


def main():
	while True:
		client_sock, addr = server_sock.accept()
		atexit.register(client_sock.close)
		print(f"I accepted connection from {addr}")
		
		data = client_sock.recv(1024).decode("utf-8")
		print(f"I get meaasge form {addr} the data lenght {len(data)}")
		
		data = json.loads(data)
		
		client_sock.send(str(main_run.main(data)).encode("utf-8"))
		
		client_sock.close()
		atexit.unregister(client_sock.close)


def run():
	threading.Thread(target=main).start()
