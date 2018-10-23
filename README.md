This python code is written to create an application server and protect it using the service of VGS. 

The application server has two endpoints, POST /data and POST /send. POST /data will store the data and POST /send will relay the data to the VGS echo service and return the response.

Using the proxy server, VGS service will encrypt the payload of the client.
