import firebase_admin
from firebase_admin import credentials, db
from pathlib import Path
import os


class FirebaseObject:
    ref = None

    def __init__(self):
        if FirebaseObject.ref is None:
            cred = credentials.Certificate("/home/susmit/PycharmProjects/ERP-ISE/classes/iseinfo-a85d2-firebase-adminsdk-vm5bf-b3f8ec12e7.json")
            app = firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://iseinfo-a85d2.firebaseio.com/'
            })

            FirebaseObject.ref = db.reference()


    @staticmethod
    def reference():
        return FirebaseObject.ref

