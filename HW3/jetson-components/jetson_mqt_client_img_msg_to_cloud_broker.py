import paho.mqtt.client as mqtt 
import time

#jetson mqtt broker container's IP
tx_broker_address="172.17.0.2"
#cloud vm IP (mqtt broker)
cl_broker_address = "xxx.xx.xxx.xx"

print("Creating client instance - tx broker")
client_tx = mqtt.Client("TX2CL2") #create new client instance
print("Connecting to TX broker")
client_tx.connect(tx_broker_address) #connect to jetson mqtt broker

print("Creating client instance - cloud broker")
client_cl = mqtt.Client("CLDCL") #create new client instance
print("Connecting to Cloud broker")
client_cl.connect(cl_broker_address) #connect to cloud mqtt broker

def on_message(client, userdata, message):
    print("message received " ,str(message.payload))
    print("message userdata " , userdata)
    print("message client " , client)

    send_message_to_cloud_broker(message)

def send_message_to_cloud_broker(message):
    print("Publishing message to cloud topic", "cl/faceimgtopic")
    
    try:
        client_cl.publish("cl/faceimgtopic", message.payload, qos=1)
    except Exception as inst:
        print(inst) 

def start_tx_listener_client(client, userdata, flags, rc):      
    print("Subscribing to topic","tx/faceimgtopic")
    client_tx.subscribe("tx/faceimgtopic")

client_tx.on_message=on_message #attach function to callback
client_tx.on_connect = start_tx_listener_client 

#continue listening and publishing
client_tx.loop_forever()
client_cl.loop_forever()