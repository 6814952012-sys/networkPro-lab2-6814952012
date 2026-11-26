import socket

# สร้าง UDP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ที่อยู่และพอร์ตของ server (udp_server คือชื่อ service ใน docker-compose)
server_address = ("udp_server", 8080)

try:
    message = "Hello from UDP client"

    print("Sending message to server...")
    client_socket.sendto(message.encode(), server_address)

    # รอรับการตอบกลับจาก server
    response, server = client_socket.recvfrom(1024)
    print(f"Response from server: {response.decode()}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    client_socket.close()
    