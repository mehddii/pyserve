import socket
import logging

from .request import HttpRequest
from .response import HttpResponse
from .utility import parse_request


logging.getLogger(__name__)


class HttpServer:
    """
    
    """
    
    def __init__(self, host : str, port : int) -> None:
        self.__host : str                        = host
        self.__port : int                        = port
        self.__address : tuple[str, int]         = (host, port)
        self.__socket  : socket.socket           = socket.create_server(self.__address, reuse_port=True)
        self.__connection : None | socket.socket = None
        #self.__request    = None 

    def start_connection(self) -> None:        
        if self.__socket is not None:
            logging.info(f"Starting server at http:://{self.__host}:{self.__port}")
            
            self.__connection, address = self.__socket.accept()
            logging.info(f'Connecting to {address}')
            
            request = ''
            while True:
                data = self.__connection.recv(1024)
                
                if data == None:
                    break
                
                request += data
            
            methode, resource, headers = parse_request(request)
            
            
            if headers is not None:
                self.__request = HttpRequest(methode, resource, **headers)
            else:
                self.__request = HttpRequest(methode, resource) 
                
            logging.info(self.__request.get_message())         
        else:
            raise RuntimeError('No server is running on this address')
        
    def send(self, response : HttpResponse) -> None:
        try:
            self.__connection.sendall(response.bytes())
        except AttributeError:
            raise RuntimeError('Connection is not established')
        self.close()
    
    def get_request(self):
        return self.__request
    
    def get_message(self):
        return self.__request.get_message()

    def close(self):
        self.__connection.close()
