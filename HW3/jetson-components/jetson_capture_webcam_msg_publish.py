#Reference - https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html

import numpy as np
import cv2
import paho.mqtt.client as mqtt #import the client1
import time
import base64

#local mqtt container's IP
tx_broker_address="172.17.0.2"

print("Creating client instance - tx broker")
client_tx = mqtt.Client("TX2CL1") #create new instance
print("Connecting to TX broker")
client_tx.connect(tx_broker_address) #connect to broker

def get_and_save_wm_image():	
    cap = cv2.VideoCapture(1)
    count = 0

    #limit to 20 frames to avoid overflowing local disk and cloud storage
    while(count <= 20):
	    # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rc, faceimg = cv2.imencode(".jpg", frame) 
		
        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
		
        publish_msg(faceimg)
		
        count += 1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
	
def publish_msg(fimg):
    msg = fimg.tobytes()

    print("Publishing message to cloud topic", "tx/faceimgtopic")
    client_tx.publish("tx/faceimgtopic", msg)
	
get_and_save_wm_image()