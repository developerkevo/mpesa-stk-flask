from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import time
import base64

app = Flask(__name__)


@app.route('/search', methods = ['POST'])
def api_message():
    data = request.data
    print(data)
    return "already run"


timestamp = str(time.strftime("%Y%m%d%H%M%S"))

password = base64.b64encode(bytes(u'174379' + 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919' + timestamp, 'UTF-8'))


consumer_key = "eJepaVL23aXzJLniwrsd1ZvvNi3b2riE"
consumer_secret = "9rgisVwWIGaZhUsA"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key,consumer_secret))

print(r.text)


access_token = "{}".format(r.text)
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = { "Authorization": "Bearer %s" % access_token }
request = {
      "BusinessShortCode": "174379",
      "Password": "{}".format(password),
      "Timestamp": "{}".format(timestamp),
      "TransactionType": "CustomerPayBillOnline",
      "Amount": "", #pass this from the form
      "PartyA": "",# pass this from the form
      "PartyB": "174379",
      "PhoneNumber": "",
      "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
      "AccountReference": "SCO 306 Demo STK push",
      "TransactionDesc": "Group 8 Mpesa test"
}

response = requests.post(api_url, json = request, headers=headers)

print(response.text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
