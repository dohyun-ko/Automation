from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd


cred = credentials.Certificate('./keys/cat-project-firebase.json')
firebase_admin.initialize_app(cred)
# Make sure you have your GOOGLE_APPLICATION_CREDENTIALS environment variable set to the path of your service account key file
db = firestore.client()

def make_csv(collection_name, drop_by=None):
    docs = db.collection(collection_name).stream()

    data = []
    for doc in docs:
        data.append(doc.to_dict())

    df = pd.DataFrame(data)

    if drop_by:
        df = df.drop_duplicates(drop_by)

    df.to_csv(collection_name + '.csv', index=False)


make_csv('visit', "uuid")
make_csv('gifts', "uuid")
make_csv('results', "uuid")
make_csv('phones', "uuid")