from flask import Flask,jsonify,request, redirect
app = Flask(__name__)
import requests
import json
SSLCZ_SESSION_API = 'https://sandbox.sslcommerz.com/gwprocess/v4/api.php'
import uuid
from werkzeug.local import LocalProxy

def get_session(name, credit):
    post_data={
    "store_id": "<your sslcommerz id>",
    "store_passwd": "<your sslcommerz pass>",
    "total_amount": credit,
    "currency": "BDT",
    "tran_id":uuid.uuid4(),
    "success_url": "http://ssltest.com:5000/success",
    "fail_url": "http://ssltest.com:5000/fail",
    "cancel_url": "http://ssltest.com:5000/cancel",
    "cus_name": name,
    "cus_email": "cust@yahoo.com",
    "cus_add1": "Dhaka",
    "cus_add2": "Dhaka",
    "cus_city": "Dhaka",
    "cus_state": "Dhaka",
    "cus_postcode": "1000",
    "cus_country": "Bangladesh",
    "cus_phone": "01711111111",
    "cus_fax": "01711111111",
    "ship_name": "Customer Name",
    "ship_add1": "Dhaka",
    "ship_add2": "Dhaka",
    "ship_city": "Dhaka",
    "ship_state": "Dhaka",
    "ship_postcode": "1000",
    "ship_country": "Bangladesh",
    "multi_card_name": "mastercard,visacard,amexcard",
    "value_a": "ref001_A",
    "value_b": "ref002_B",
    "value_c": "ref003_C",
    "value_d": "ref004_D",
    "shipping_method": "YES",
    "product_name": "credit",
    "product_category": "general",
    "product_profile": "general"
    }

    response = requests.post(SSLCZ_SESSION_API, post_data)

    return(response.json()["sessionkey"],response.json()["GatewayPageURL"])


@app.route('/get-ssl-session',methods = ['POST'])
def get_ssl_session():
    name = request.get_json().get("name");
    amount = request.get_json().get("credit")

    session, gateway = get_session(name, amount);
    
    return jsonify({"session": session, "gatewayPageUrl":gateway}) 

@app.route('/success',methods = ['POST'])
def success():
    response = request.form
    # process your data store it or do anything you prefer

    return redirect('http://localhost:3000/success');

@app.route('/fail',methods = ['POST'])
def fail():
    response = request.form

    return redirect('http://localhost:3000/fail');

@app.route('/cancel',methods = ['POST'])
def cancel():
    response = request.form

    return redirect('http://localhost:3000/cancel');


if __name__ == "__main__":
     app.run()