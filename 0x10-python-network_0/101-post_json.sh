#!/bin/bash
# Script that sends a GET request to URL and displays body of response

curl -s -X GET -H "X-School-User-Id: 98" "$1"
