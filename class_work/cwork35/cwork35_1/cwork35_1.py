####################################################################
# Сокеты:
# Серверный
# Клиентский

# import socket
#
#
# URLS = {
#     "/": "index page",
#     "/blog": "blog page"
# }
#
#
# def parser_request(request):
#     parsed = request.split()
#     print(parsed)
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != "GET":
#         return "HTTP/1.1 405 Method Not Allowed!\n\n", 405
#     if url not in URLS:
#         return "HTTP/1.1 404 Page Not Found!\n\n", 404
#     return "HTTP/1.1 200 OK!\n\n", 200
#
#
# def generate_response(request):
#     method, url = parser_request(request)
#     headers, code = generate_headers(method, url)
#     body = URLS.get(url, "Errors 404")
#     return (headers + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(("127.0.0.1", 5000))  # 127.0.0.1:5000 локальный ip адрес
#     server_socket.listen()
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#         print(f"Клиент : {addr} => \n{request.decode("utf-8")}\n")
#
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close()
#
#
# if __name__ == '__main__':
#     run()

from view import blog, index
import socket

URLS = {
    "/": index,
    "/blog": blog
}


def parser_request(request):
    try:
        parsed = request.split()
        if len(parsed) < 2:
            print("Invalid request format")
            return None, None
        method = parsed[0]
        url = parsed[1]
        return method, url
    except Exception as e:
        print(f"Error parsing request: {e}")
        return None, None


def generate_headers(method, url):
    if method != "GET":
        return "HTTP/1.1 405 Method Not Allowed!\n\n", 405
    if url not in URLS:
        return "HTTP/1.1 404 Page Not Found!\n\n", 404
    return "HTTP/1.1 200 OK!\n\n", 200


def generate_content(code, url):
    if code == 404:
        return '<h1>404</h1><h3>Page Not Found!</h3>'
    if code == 405:
        return '<h1>405</h1><h3>Method Not Allowed!</h3>'

    content = URLS[url]()
    if content is None:
        return '<h1>500</h1><h3>Internal Server Error!</h3>'
    return content


def generate_response(request):
    method, url = parser_request(request)
    if method is None or url is None:
        headers = "HTTP/1.1 400 Bad Request!\n\n"
        body = "Bad Request"
        return (headers + body).encode()

    headers, code = generate_headers(method, url)
    body = generate_content(code, url)
    return (headers + body).encode()


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 5000))  # 127.0.0.1:5000 локальный ip адрес
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)

        # Декодирование запроса и вывод в консоль
        try:
            decoded_request = request.decode("utf-8")
        except UnicodeDecodeError as e:
            print(f"Error decoding request: {e}")
            decoded_request = ""

        print(f"Клиент : {addr} => \n{decoded_request}\n")

        response = generate_response(decoded_request)
        client_socket.sendall(response)
        client_socket.close()


if __name__ == '__main__':
    run()
