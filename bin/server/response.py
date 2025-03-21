import re

from .message import HttpMessage
from .status  import *

class HttpResponse(HttpMessage):
    """
    
    """

    def __init__(self, status : StatusCode, http_version : float = 1.1, **headers):
        
        
        
        first_line = f"{http_version} {status} {description}"
        
        
        for header in headers:
            if re.match("(\w+_\w+)", "") is None:
                raise ValueError("All headers must be in the format word_word_..._word")
        
        for header, values in headers.items():
            pass
        
        self.__message = f"{status} {description}"
        super().__init__(self.__message, **headers)
        
    def get_message(self):
        return self.__message
    
    def bytes(self):
        return super().all_bytes()