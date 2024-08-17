define config.python_callbacks = [ "python_callback" ]

init python:
    import socket

    def send_prompt(prompt):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', 65432))
            s.sendall(prompt.encode('utf-8'))
            data = s.recv(1024)
        return data.decode('utf-8')

label start:
    $ prompt = "Enter your prompt here"
    $ response = send_prompt(prompt)
    "Response: [response]"
    return
