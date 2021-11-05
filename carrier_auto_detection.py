# coding = utf-8
import hashlib
import json

import requests


class KuaiDi100:
    def __init__(self):
        self.ApiKey = ''  # You can find your ApiKey on https://app.kd100.com/api-managment
        self.Secret = ''  # You can find your Secret on https://app.kd100.com/api-managment 
        self.url = 'https://www.kd100.com/api/v1/carriers/detect'  

    def track(self, num):
        """
        Request Parameters
        :param tracking_number: tracking number
        :return: requests.Response.text
        """
        param = {
            'tracking_number': num
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


result = KuaiDi100().track('9926933413')
print(result)