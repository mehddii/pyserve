from .message import HttpMessage

class HttpRequest(HttpMessage):
    """
    
    """

    methods = {'GET', 'POST'}
    
    def __init__(self, methode : str, resource : str, **headers):
        self.__message = f"{methode.strip() if methode.upper() in self.methods else 'GET'} {resource.strip()}"
        super().__init__(self.__message, **headers)
    
    def get_message(self):
        return self.__message
    
    def bytes(self):
        return super().all_bytes()
    