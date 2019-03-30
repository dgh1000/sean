
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

# Use the application default credentials
cred = credentials.Certificate(
    '/Users/Mike/Dropbox/projects/auth/mikeandsean-simple.json'
)
project_id = "mikeandsean"
#bucket_id = "hansel-e34d2.appspot.com"
bucket_id = "hansel-e34d2"
bucket_id = "mikeandsean-38045.appspot.com"


firebase_admin.initialize_app(cred, {
  'storageBucket': bucket_id
})

bucket = storage.bucket()



for n in bucket.list_blobs():
    print(n.name)
    n.download_to_filename("test.jpg")

