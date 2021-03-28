import unittest
from main import app
import requests
import json
url = 'http://127.0.0.1:5000'

class MyTestCase(unittest.TestCase):
    def test_endpoint(self):
        response = requests.post("{}/ProcessPayment".format(url))
        self.assertEqual(response.status_code, 400)
    def test(self):
        card_data_1 = {"CreditCardNumber": "1234567890123456", "CardHolder": "Alok", "SecurityCode": "111",
                       "ExpirationDate": "2022/11/12", "Amount": 47}
        card_data_2 = {"CreditCardNumber": "1234567890123456", "CardHolder": "Alok", "SecurityCode": "111",
                       "ExpirationDate": "2022/11/12", "Amount": 357}
        card_data_3 = {"CreditCardNumber": "1234567890123456", "CardHolder": "Alok", "SecurityCode": "111",
                       "ExpirationDate": "2022/11/12", "Amount": 800}
        card_data_4 = {"CreditCardNumber": "qwer123456ijiojw", "CardHolder": "", "SecurityCode": "111",
                       "ExpirationDate": "2022/1/1", "Amount": 387.3}
        card_data_5 = {"CreditCardNumber": "1234567890123456", "CardHolder": "Alok", "SecurityCode": "111",
                       "ExpirationDate": "2019/11/12", "Amount": 67.3}
        response_1 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_1),
                                   headers={"Content-Type": "application/json"})
        response_2 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_2),
                                   headers={"Content-Type": "application/json"})
        response_3 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_3),
                                   headers={"Content-Type": "application/json"})
        response_4 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_4),
                                   headers={"Content-Type": "application/json"})
        response_5 = requests.post("{}/ProcessPayment".format(url), data=json.dumps(card_data_5),
                                   headers={"Content-Type": "application/json"})
        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_2.status_code, 200)
        self.assertEqual(response_3.status_code, 200)
        self.assertEqual(response_4.status_code, 200)
        self.assertEqual(response_5.status_code, 400)

if __name__ == '__main__':
    unittest.main()
