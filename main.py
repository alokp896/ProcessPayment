import requests
from flask import Flask,request,abort
import json
from payment import Card
from external import ExternalPayment


app = Flask(__name__)


@app.route("/ProcessPayment", methods=['POST'])
def payment():
    if request.method == 'POST':
        data = request.get_data(as_text=True)
        if not data:
            print("No data found, Please check the request data")
            abort(400)
        request_data = json.loads(data)
        card_data = Card()
        print("request data {}".format(request_data))
        try:
            if not card_data.verify_input(**request_data):
                print("card Details are invalid, Please check and resend")
                abort(400)
        except:
            abort(400)
        try:
            print("payment status: started")
            payment_status = ExternalPayment(card_data.Amount, card_data)
            payment_successful = payment_status.make_payment()
            if payment_successful:
                return {"status code": 200}
            else:
                abort(400)
        except:
            abort(500)
    else:
        abort(400)


if __name__ == '__main__':
    app.run(debug = True)