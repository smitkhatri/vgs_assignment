from flask import Flask, request
import json
import requests

app = Flask(__name__)

username = 'UScWgjcXfoMcsrRaz9o5WLHm'
password = '2f502502-4c7b-4aa8-ae6c-3886ffdffb73'
forward_proxy = 'tntnpizkevu.sandbox.verygoodproxy.com:8080'
reverse_proxy = 'tntnpizkevu.SANDBOX.verygoodproxy.com'


def tokenize_via_reverse_proxy(original_data):
	r = requests.post(
		'https://{}/post'.format(reverse_proxy),
		data=original_data,
		headers={"Content-type": "application/json", "VGS-Log-Request": "all"}
	)
	print(r.status_code)
	assert r.status_code == 200
	return r.json()['data']


def reveal_via_forward_proxy(tokenized_data):
    r = requests.post(
        'https://httpbin.verygoodsecurity.io/post',
        data=tokenized_data,
        headers={"Content-type": "application/json", "VGS-Log-Request": "all"},
        proxies={
            "https": "https://{}:{}@{}".format(username, password, forward_proxy),
            "http": "https://{}:{}@{}".format(username, password, forward_proxy)
        },
        verify='vgs_cert_sandbox.pem'
    )
    assert r.status_code == 200
    return r.json()['data']

@app.route("/data", methods=['POST'])
def endpoint_One():

	data_recieved = request.data
	if data_recieved:
		if isinstance(data_recieved,dict):
			if "secret" in data_recieved:
				return json.dumps(data_recieved)
			
	return json.dumps({"secret":"secret Key"})


@app.route("/send", methods=['POST'])
def endpoint_two():
	
	data_recieved = request.data.decode("utf-8")
	print(data_recieved)
	tokenized_value = json.loads(data_recieved)

	revealed_value = reveal_via_forward_proxy(tokenized_value)
	print(revealed_value)

	assert original_value == revealed_value
	print("Test passed")

	
	url = "https://echo.apps.verygood.systems/post"
	response = requests.post(url, data = original_value)
	data_to_send = response.json()
	return json.dumps(data_to_send)
	
if __name__ ==  '__main__':
	app.run("0.0.0.0", 8080)
	
	