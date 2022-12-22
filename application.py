# This is a sample Python script.
import allure
import requests
import random

#
# class Application(object):
#     def __init__(self, base_address):
#         self.base_address = base_address
#
#     def post(self, path="/", params=None, data=None, json=None, headers=None):
#         with allure.step(f'POST request to {path}'):
#             return requests.post(url=self.base_address+path, params=params, data=data, json=json, headers=headers)
#
#     def get(self, path="/", params=None, headers=None):
#         with allure.step(f'POST request to {path}'):
#             return requests.get(url=self.base_address+path, params=params, headers=headers)

@staticmethod
def random_email():
    letters_eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'l', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                   'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return "{0}@{1}.rr".format(''.join(str(e) for e in random.choices(letters_eng, k=5)),
                               ''.join(str(e) for e in random.choices(letters_eng, k=5)))