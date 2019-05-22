# w251-assignments - HW3

### Bucket URL
<https://s3.dal.us.cloud-object-storage.appdomain.cloud/test-rm-w251-bucket/>

### Sample image URL
<https://s3.dal.us.cloud-object-storage.appdomain.cloud/test-rm-w251-bucket/05c75504-7b4e-435d-b944-e52b222e299a.jpg>

### Naming of Topics
-   Topic in the Cloud MQTT Broker - "cl/faceimgtopic"
-   Topic in the JetsonTX2 MQTT Broker - "tx/faceimgtopic"

### Since message payload size is not small and there are not strong criteria to receive all the messages exactly once, the value of QoS - 1 have been used for all the client/topic subscription.   