#!/bin/bash
# This script  makes a request to 0.0.0.0:5000/catch_me
# and makes the server respond with You Got Me!
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
