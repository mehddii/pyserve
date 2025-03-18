from .request import HttpRequest
from .response import HttpResponse
from .utility import parse_request
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
            
            methode, resource, headers = parse_request(self.__connection.recv(size))
            
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
