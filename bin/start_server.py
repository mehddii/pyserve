import re
from server.server import HttpServer
from server.response import HttpResponse

def main():
    ADDR = ("localhost", 1234)
    
    server = HttpServer(ADDR, reuse_port=True)

    while True:
        server.start_connection()
        
        if re.findall(r"^\w* /$", server.get_message()):
            print("Request:\t", server.get_request())
            html_content = """
            <html>
                <head><title>Pyserve</title></head>
                <body>
                    <h1>Welcome to Pyserve!</h1>
                    <p>This is a basic response to your GET request.</p>
                </body>
            </html>
            """
            response = HttpResponse(200, 'OK', body=html_content)
            server.send(response)
            print("Response:\t", response)
        else:
            print("Request:\t", server.get_request())
            response = HttpResponse(404, 'NOT FOUND')
            server.send(response)
            print("Response:\t", response)

if __name__ == "__main__":
    main()