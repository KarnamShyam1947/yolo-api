import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

# Use a service account.
cred = credentials.Certificate('agritech-1947ls.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

def add_record(email:str, id:str, image_url:str='', label='', result = ''):
    db.collection('notifications').document(id).set({
        'id' : id,
        'email' : email,
        'imageUrl': image_url,
        'label' : label,
        'result' : result,
        'timestamp' : str(datetime.datetime.now())
    })