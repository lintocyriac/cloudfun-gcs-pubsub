- Create a bucket 
- Create cloud function with trigger as cloud storage and event type On (finalizing/creating) file in the selected bucket
- give the cloud function runtimne account has sufficent permission to read the data from that bucket
- write the cloud function and choose the enty point



choose your cloud function artifacts  to create cloud run 

Go to eventarc and create a trigger
- choose service account which have read data from cloud storage and publish it to pubsub
- trigger type cloud storage google.cloud.storage.object.v1.finalized
- select a cloud run service (in here you have to choose the the function which we already created)

