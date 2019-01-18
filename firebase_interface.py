import firebase_admin
import json
from firebase_admin import credentials, db

cred = credentials.Certificate("iseinfo-a85d2-firebase-adminsdk-vm5bf-b3f8ec12e7.json")
app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iseinfo-a85d2.firebaseio.com/'
})

ref = db.reference()


def fetch_teachers():
    data = ref.child('Teacher').get()
    r = {}

    for d in data:
        print(d)


fetch_teachers()
