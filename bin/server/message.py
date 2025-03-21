import re

from abc  import ABC, abstractmethod
from copy import deepcopy

class HttpMessage(ABC):
    """

    """
    
    def __init__(self, first_line : str, headers : dict[str, list], body : bytes | None = None) -> None:
        self._first_line : str             = first_line
        self._headers : dict[str, list]    = headers
        self._body : bytes | None          = body
    
    @property
    def first_line(self) -> str:
        return self._first_line
    
    @property
    def headers(self) -> dict[str, list]:
        # Prevents mutating the values (lists) of the headers   
        return deepcopy(self._headers)
    
    @property
    def body(self) -> bytes | None:
        return self._body
    
    def get_header(self, header : str) -> list | None:
        header = header.split("-")
        for i in range(len(header)):
            header[i] = header[i].capitalize()
        header = "-".join(header)
        return self._headers.get(header, [])
    
    def add_header(self, header : str, *values : str) -> None:
        values = list(values)
        if self._validate(header, values):
            header = header.split("-")
            for i in range(len(header)):
                header[i] = header[i].capitalize()
            header = "-".join(header)
            
            if self.headers.get(header, None) is not None:
                self._headers[header].extend(values)
            else:
                self._headers[header] = values
        else:
            raise ValueError("Header is not valide.")
    
    # Should be overriden by child classes
    @abstractmethod
    def _validate(self, header : str, value : list) -> bool:
        pass
            
    @staticmethod
    def _str_to_bytes(string : str, encoding : str = "utf-8") -> bytes:
        return string.encode(encoding)
    
    @staticmethod
    def _bytes_to_str(all_bytes : bytes, decoding : str = "utf-8") -> str:
        return all_bytes.decode(decoding)
    
    def get_all_bytes(self) -> bytes:
        message = [self._first_line]

        for header, values in self._headers.items():
            if header.lower() in {
                "set-cookie",
                "www-authenticate",
                "proxy-authenticate",
                "cookie",
                "trailer",
                "authentication-info",
                "proxy-authentication-info",
            }:
                for value in values:
                    message.append(f"{header}: {value}")
            else:
                message.append(f"{header}: {', '.join(values)}")

        message.append("\r\n")
        message = '\r\n'.join(message)
        
        return self._str_to_bytes(message) + (self._body if self._body is not None else b"")
    
    def _headers_stringify(self) -> str:
        headers = []
        for header, values in self._headers.items():
            if header.lower() in {
                "set-cookie",
                "www-authenticate",
                "proxy-authenticate",
                "cookie",
                "trailer",
                "authentication-info",
                "proxy-authentication-info",
            }:  
                for value in values:
                    headers.append(f"{header}: {value}")  
            else:
                headers.append(f"{header}: {', '.join(values)}")
        return '\r\n'.join(headers)
            
    def __str__(self) -> str:
        content_type = self.get_header("Content-Type")
        
        # Only text content is supported for now 
        body = None
        for value in content_type:
            if re.match(r"(^text/|/text$)", value):
                try:
                    body = self._bytes_to_str(self._body)
                except UnicodeDecodeError:
                    pass
        
        
        return f"{self._first_line}\r\n{self._headers_stringify()}\r\n\r\n{body if body is not None else ''}" 
    
    def __repr__(self) -> str:
        return f"<HttpMessage {self.first_line}>"