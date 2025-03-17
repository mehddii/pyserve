from .request import HttpRequest
from .response import HttpResponse
import socket

class HttpServer:
    """
    
    """
    
    def __init__(self, adress : tuple[str, int], **kwargs) -> None:
        self.__address    = adress
        self.__param      = kwargs
        self.__socket     = None
        self.__connection = None
        self.__request    = None 
    
    def create_server(self) -> None:
        if self.__socket == None:
            self.__socket : socket.Socket = socket.create_server(self.__address, **self.__param)
        else:
            raise RuntimeError('Server is already running')

    def start_connection(self, size : int = 1024) -> None:
        if self.__socket != None:
            self.__connection, address = self.__socket.accept()
            data = str(self.__connection.recv(size), 'utf-8').split('\r\n')

            message = data[0].split(' ')
            methode = message[0].strip()
            resource = message[1].strip()

            headers = None
            if len(data) > 1:
                headers = {}
                for header in data[1:]:
                    if header.strip() != "":
                        header = header.strip().split(" ")
                        key = header[0].replace(":", "").replace("-", "")
                        value = header[1]
                        headers[key] = value

            if headers is not None:
                self.__request = HttpRequest(methode, resource, **headers)
            else:
                self.__request = HttpRequest(methode, resource)          
        else:
            raise RuntimeError('No server is running on this address')
        
    def send(self, request : HttpResponse | HttpResponse) -> None:
        try:
            self.__connection.sendall(request.bytes())
        except AttributeError:
            raise RuntimeError('Connection is not established')
        self.close()
    
    def get_request(self):
        return self.__request
    
    def get_message(self):
        return self.__request.get_message()

    def close(self):
        self.__connection.close()
