# This is a sample Python script.
from NewsAbstractor import NewsAbstractor

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # news()
    # news_abstractor = NewsAbstractor()
    # news_abstractor.news()

    storage_client = storage.Client()

    # The name for the new bucket
    bucket_name = "my-new-bucket"

    # Creates the new bucket
    bucket = storage_client.create_bucket(bucket_name)

    print(f"Bucket {bucket.name} created.")

