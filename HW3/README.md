# w251-assignments - HW3

### Bucket URL
<https://s3.dal.us.cloud-object-storage.appdomain.cloud/test-rm-w251-bucket/>

### Sample image URL
<https://s3.dal.us.cloud-object-storage.appdomain.cloud/test-rm-w251-bucket/14cd8227-083e-40a3-b201-7350eb7bad72.jpg>

### Naming of Topics
-   Topic in the Cloud MQTT Broker - "cl/faceimgtopic"
-   Topic in the JetsonTX2 MQTT Broker - "tx/faceimgtopic"

### Since message payload size is not small and there are not strong criteria to receive all the messages from the consumer, the default value of QoS - 0 have been used for all the client/topic subscription. 