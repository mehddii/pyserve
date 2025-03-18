from .message import HttpMessage

class HttpResponse(HttpMessage):
    """
    
    """

    def __init__(self, status : int, description : str, **headers):
        self.__message = f"{status} {description}"
        super().__init__(self.__message, **headers)
        
    def get_message(self):
        return self.__message
    
    def bytes(self):
        return super().all_bytes()