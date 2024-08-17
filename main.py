import requests
import socket
import json
from rich.logging import RichHandler
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, handlers=[RichHandler()])
logger = logging.getLogger(__name__)

# Function to get response from the API
def get_response(prompt, api_url):
    payload = {
        "prompt": prompt,
        "max_tokens": 100
    }
    response = requests.post(api_url, json=payload)
    return response.json()["choices"][0]["text"]

# Set up socket server
def start_server(api_url):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(1)
    logger.info("Server started, waiting for connections...")

    while True:
        conn, addr = server_socket.accept()
        logger.info(f"Connected by {addr}")
        data = conn.recv(1024)
        if not data:
            break
        prompt = data.decode('utf-8')
        response = get_response(prompt, api_url)
        conn.sendall(response.encode('utf-8'))
        logger.info(f"Sent response: {response}")

    conn.close()

if __name__ == "__main__":
    api_url = "http://localhost:5000/v1/completions"  # Change this to your API endpoint
    start_server(api_url)
