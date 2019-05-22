import paho.mqtt.client as mqtt 
import time
import cloud_img_uploader_to_bucket
import base64
import uuid

#cloud mqtt broker container's IP 
cl_broker_address="172.17.0.3"
print("Creating client instance - cl broker")
client_cl = mqtt.Client("TX2CL") #create new instance

def on_message(client, userdata, message):
    print("message received " ,str(message.payload))
    print("message userdata " , userdata)
    print("message client " , client)
    process_and_upload_obj_to_cloud_storage(message)
   
def process_and_upload_obj_to_cloud_storage(message):
    try:
        #create a unique name of the image file
        img_name = str(uuid.uuid4()) + '.jpg'
        img_path = "./images/" + img_name

        #convert base64 string to jpg image file
        with open(img_path, "wb") as fh:
            fh.write(bytearray(message.payload))

        #pass the image to upload in the bucket - test-rm-w251-bucket
        cloud_img_uploader_to_bucket.multi_part_upload("test-rm-w251-bucket", img_name, img_path)
    except Exception as inst:
        print(inst)

def start_cl_listener_client(client, userdata, flags, rc):
    print("Subscribing to topic","cl/faceimgtopic")

    #subscribe to the face image topic in the cloud broker
    client_cl.subscribe("cl/faceimgtopic")

client_cl.on_message=on_message #attach function to callback
print("Connecting to CL broker")
client_cl.connect(cl_broker_address) #connect to broker
client_cl.on_connect = start_cl_listener_client

#continue listening
client_cl.loop_forever()
