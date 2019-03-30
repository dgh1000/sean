
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

# Use the application default credentials
cred = credentials.Certificate(
    './mikeandsean-38045-firebase-adminsdk-p3j4r-2194fec1e0.json'
)
project_id = "mikeandsean"
#bucket_id = "hansel-e34d2.appspot.com"
#bucket_id = "hansel-e34d2"
bucket_id = "mikeandsean-38045.appspot.com"


firebase_admin.initialize_app(cred, {
  'storageBucket': bucket_id
})

bucket = storage.bucket()

for n in bucket.list_blobs():
    print(n.name)
    n.download_to_filename(n.name)


def upload_blob(bucket, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    #storage_client = storage.Client()
    #bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

upload_blob(bucket, "kids.jpg","kids.jpg")

def delete_blob(bucket, blob_name):
    """Deletes a blob from the bucket."""
    #storage_client = storage.Client()
    #bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.delete()

    print('Blob {} deleted.'.format(blob_name))

delete_blob(bucket, "rainbow.jpeg")
