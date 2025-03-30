from google.cloud import storage
import datetime

BUCKET_NAME = "my-dr-backup-bucket"
FILES_TO_BACKUP = ["/path/to/data/file1.db", "/path/to/data/file2.log"]

def upload_to_gcs():
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)

    for file in FILES_TO_BACKUP:
        blob = bucket.blob(f"backups/{datetime.datetime.now().strftime('%Y-%m-%d')}/{file.split('/')[-1]}")
        blob.upload_from_filename(file)
        print(f"Uploaded {file} to {blob.name}")

if __name__ == "__main__":
    upload_to_gcs()
