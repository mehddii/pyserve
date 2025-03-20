from .message import HttpMessage
from .methods import Method

class HttpRequest(HttpMessage):
    """
    
    """

    _methods = {
        Method.GET : 'get',
        Method.POST : 'post',
        Method.DELETE : 'delete',
        Method.PUT : 'put'
    }
    
    def __init__(self, methode : str, resource : str, **headers):
        self.__message = f"{methode.strip() if methode.upper() in self.methods else 'GET'} {resource.strip()}"
        super().__init__(self.__message, **headers)
    
    def get_message(self):
        return self.__message
    
    def bytes(self):
        return super().all_bytes()
    