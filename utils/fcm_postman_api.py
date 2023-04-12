import requests
import json
from keys import keys

firebase_service_key = keys['firebase_service_key']
android_emulator_token = keys['android_emulator_token']
my_agri_tech_fcm_token = keys['my_agri_tech_fcm_token']

def prepare_header(service_key=firebase_service_key):
    header_json = {
        "Content-Type" : "application/json",
        "Authorization" : "key={}".format(service_key)
    }

    return header_json

def prepare_body(image_url, device_token=android_emulator_token, message='', title = ''):
    payload = {
        "registration_ids": [
            device_token,
            my_agri_tech_fcm_token
        ],

        "notification": {
            "body": message,
            "title": title,
            "android_channel_id": "high_importance_channel",
            "image": image_url,
            "sound" : True
        }
    }

    payload_data = json.dumps(payload)

    return payload_data

def send_notification(header, payload):
    response = requests.post('https://fcm.googleapis.com/fcm/send' , data=payload, headers = header)

    return response

def main():
    message = "Testing with python requests module and parameters"
    title = "Testing"

    header_data = prepare_header(firebase_service_key)
    payload_data = prepare_body(android_emulator_token, message, title)

    response = send_notification(header_data, payload_data)

    print(response.status_code)
    if response.status_code == 200:
        print('Notification send successfully.....')

    else:
        print('error')

if __name__ == '__main__' : 
    main()