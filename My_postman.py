import requests
import json

def prepare_header():
    header = {
        "Content-Type" : "application/json"
    }

    header_json = json.dumps(header)

    return header_json

def prepare_body():
    payload = {
        "b64" : "Hello"
    }

    payload_data = json.dumps(payload)

    return payload_data

def send_request(header, payload):
    response = requests.post('http://127.0.0.1:5000/upload-base64' , headers=header, data=payload)

    return response

def main():
    header = prepare_header()
    payload = prepare_body()

    # resp = send_request(header, payload)
    # print(resp)

    code = requests.get('http://127.0.0.1:5000/upload-base64')
    print(code)

    # response = requests.post('http://127.0.0.1:5000/upload-base64' , header, payload)
    # print(response)

if __name__ == '__main__' : 
    main()