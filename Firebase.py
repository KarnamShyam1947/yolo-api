import pyrebase
import datetime
import uuid
import firestore

config = {
    "apiKey": "AIzaSyDR7jMMHJrMtJ10cGW21NCnQA8dYscdotE",
    "authDomain": "agritech-1947ls.firebaseapp.com",
    "projectId": "agritech-1947ls",
    "storageBucket": "agritech-1947ls.appspot.com",
    "messagingSenderId": "88388988117",
    "appId": "1:88388988117:web:18ac81dd73344ef653465c",
    "measurementId": "G-25KHE0BG20",
    "databaseURL" : 'https://agritech-1947ls-default-rtdb.firebaseio.com/'
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
storage  = firebase.storage()

def upload_image(img_path:str, label:str, result:str):
    unique_id = str(uuid.uuid1())
    path = 'notification_images/{}'.format(unique_id)

    storage.child(path).put(img_path)

    email = 'admin@gmail.com'
    user = auth.sign_in_with_email_and_password(email,'admin@shyam')
    url = storage.child(path).get_url(user['idToken'])

    firestore.add_record(email, unique_id, url, label, result)

    return url



def main():
    img_path = "images/test.png"

    upload_image(img_path, 'label', 'result')

if __name__ == '__main__' : 
    main()