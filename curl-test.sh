#!/bin/bash

curl -X POST http://localhost:5000/api/timeline_post -d 'name=Kristen&email=intentuskristen@gmail.com
&content=Testing endpoints with postman and curl!'

# getting the endpoint
curl http://localhost:5000/api/timeline_post