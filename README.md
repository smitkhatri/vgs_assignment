## Simple Server to secure payload using VGS services

#### Requirements
1. Python 3.6
2. Flask

#### Explanation

The application server has two endpoints, 
```POST [server-url]:80/data```

```POST [server-url]:80/send.```

#### Running the application
1. ```python3 vgs_assignmnet.py```

2. Send the payload using the VGS reverse Proxy (This service will call the endpoint_two of the assignment) and return back the 
```curl -X POST \
  https://tntnpizkevu.sandbox.verygoodproxy.com/send \
  -H 'Content-Type: application/json' /
  -d '{"secret":"blah blah"}'
```
This should return the following json
```
{
    "args": {},
    "data": "{\"secret\":\"blah blah\"}",
    "files": {},
    "form": {},
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close",
        "Content-Length": "22",
        "Host": "echo.apps.verygood.systems",
        "User-Agent": "python-requests/2.20.0"
    },
    "json": {
        "secret": "blah blah"
    },
    "origin": "34.214.15.195, 100.102.188.192",
    "url": "https://echo.apps.verygood.systems/post"
}
```
