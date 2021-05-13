import pandas as pd

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("fir-6db11-firebase-adminsdk-8vanl-45102f04ef.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u'water')
# Import data
df = pd.read_csv('import_intern.csv')
tmp = df.to_dict(orient='records')
list(map(lambda x: doc_ref.add(x), tmp))
