import os
import requests
from bot import send_text_message
import time


TOKEN = str(os.environ.get("TOKEN"))
TIMEOUT = 60

warehouses = {'Электросталь': 120762}


def get_coefficients(warehouses):
    url = 'https://supplies-api.wildberries.ru/api/v1/acceptance/coefficients?warehouseIDs=120762'
    headers = {'Authorization': TOKEN}

    resp = requests.get(url, headers=headers)
    with open('test.json', 'w') as f:
        f.write(resp.text)
    return resp.json()


def compose_string(coofs_boxes):
    s = ""
    for coof in coofs_boxes:
        s += coof['date'] + " " + str(coof['coefficient']) + '\n'
    return s

while True:
    coofs = get_coefficients(warehouses)
    coofs_boxes = []
    for coof in coofs:
        if coof['boxTypeName'] == 'Короба':
            coofs_boxes.append(coof)

    send_text_message(compose_string(coofs_boxes))
    time.sleep(TIMEOUT)



# def get_warehouses():
#     url = 'https://supplies-api.wildberries.ru/api/v1/warehouses'
#     headers = {'Authorization': TOKEN}

#     resp = requests.get(url, headers=headers)
#     with open('test.json', 'w') as f:
#         f.write(resp.text)





get_coefficients(warehouses)
