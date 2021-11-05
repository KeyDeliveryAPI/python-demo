# coding = utf-8
import hashlib
import json

import requests


class KuaiDi100:
    def __init__(self):
        self.ApiKey = ''  # You can find your ApiKey on https://app.kd100.com/api-managment
        self.Secret = ''  # You can find your Secret on https://app.kd100.com/api-managment 
        self.url = 'https://www.kd100.com/api/v1/tracking/realtime'  

    def track(self, com, num, phone, ship_from, ship_to):
        """
        Request Parameters
        :param carrier_id: carrier ID
        :param tracking_number: tracking number
        :param phone: sender & recipient phone number (fill in with a mobile phone number or landline number)
        :param ship_from: sender city
        :param ship_to: recipient city. The tracking frequency will be increased when the shipment arrives at the recipient city.
        :param area_show: Adding this field means using the administrative area determination feature.0: close (default) 1: return data about area_name, location, order_status_description
        :param order: false Returned data sort: desc(default), asc.
        :return: requests.Response.text
        """
        param = {
            'carrier_id': com,
            'tracking_number': num,
            'phone': phone,
            'ship_from': ship_from,
            'ship_to': ship_to,
            'area_show': 1,
            'order': 'desc'
        }

        param_str = json.dumps(param)
        temp_sign = param_str + self.ApiKey + self.Secret
        md = hashlib.md5()
        md.update(temp_sign.encode())
        sign = md.hexdigest().upper()

        headers = {
            'API-Key': self.ApiKey,
            'signature': sign,
            'Content-Type': 'application/json'
        }
        
        response = requests.request("POST", self.url, headers=headers, data=param_str)
        
        return response.text  


result = KuaiDi100().track('dhlen', '9926933413', '95279527', 'Toronto, Canada', 'Los Angeles, CA, United States')
print(result)