# Mirror A2P Twilio
This project, search all entities related to A2P in twilio (phone numbers, messaging services, campaign, A2P brand information and Profile information) and get the information, then you can audit any problem faster using the DB

# Run the project
After of download the project you can run
```
    make up
````

# Create User
Open a terminal/bash from the same instance that are you runing
```
    docker exec -it a2p_twilio_capp bash
    make create_user
```
# Execute the task
```
    mrq-run --queue medium "tasks.twilio.GetInformation" '{"a": 1}'
```

# Issues
- The MRQ has a problem with the version of gevent > 1.4, for this reason we use the python 3.6