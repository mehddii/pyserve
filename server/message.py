import re

class HttpMessage:
    """
    
    """

    http_version = 'HTTP/1.1'

    def __init__(self, message : str, **headers) -> None:
        request_format = f"{message} {self.http_version}"
        response_format = f"{self.http_version} {message}"
        self.__message        = f"{response_format if re.match(r'^\d+\w*', message) else request_format}"
        self.__headers : dict = headers
        self.__body = headers.get('body', None)
    
    def get_header(self, title):
        return f"{self.__message}\n{self.__headers.get(title, None)}"
    
    def get_body(self):
        if self.__body:
            return str(self.__body)
        return self.__body
    
    def all_bytes(self):
        request = self.__message + '\r\n'

        for header, value in self.__headers.items():
            request += header + ": " + value + "\r\n"


        request += "\r\n" + (self.__body if self.__body != None else "")


        return bytes(request, "utf-8")
    
    def __str__(self):
        return self.__message