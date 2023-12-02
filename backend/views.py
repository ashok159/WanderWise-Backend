import pyrebase
import os

config = {
    "apiKey": "AIzaSyD8shOB-dL4kxBD_PTXGw6xxUn-Ohfkoew",
    "authDomain": "wanderwise-896f5.firebaseapp.com",
    "projectId": "wanderwise-896f5",
    "storageBucket": "wanderwise-896f5.appspot.com",
    "messagingSenderId": "172009442176",
    "appId": "1:172009442176:web:c0e019364d7fc62a0e4f65",
    "measurementId": "G-2YT560JGBS",
}

firebase = pyrebase.initialize_app(config)
db = firebase.storage()

data = db.child('your_path').get().val()

print("Data from Firebase Database:")
print(data)