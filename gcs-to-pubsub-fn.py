

import json

def publish_json_to_pubsub(data, context):
  """
  A Cloud Function triggered by Eventarc when a JSON file is created in GCS.
  It reads the file content and publishes it to a Pub/Sub topic.

  Args:
      event: A CloudEvents object containing event data.
      context: The Cloud Function execution context.
  """

  
  # Create a GCS client (assuming ADC for service account access)
  from google.cloud import storage
  storage_client = storage.Client()

  # Download the JSON file
  bucket = storage_client.bucket(data["bucket"])
  blob = bucket.blob(data['name'])
  data = blob.download_as_string().decode("utf-8")
  eventList = data.split("\n")

  print("Downloaded data: \n")
  print(data)

  from google.cloud import pubsub_v1

  publisher = pubsub_v1.PublisherClient()

  project_id = "<project_id>"
  topic_name = "pubsub_to_bq"
  topic_path = publisher.topic_path(project_id, topic_name)

  for event in eventList:
    if len(event) <= 0:
      continue
    print("Publishing: ", event)
    data = event.encode("utf-8")
    
    future = publisher.publish(topic_path, data)
    print(future.result())

  return "Done!!"
