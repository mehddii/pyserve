def parse_request(request : bytes):
    data = str(request, 'utf-8').split('\r\n')

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

    return methode, resource, headers
