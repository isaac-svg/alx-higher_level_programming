#!/bin/bash
# This script is used to send POST request with a json data
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
