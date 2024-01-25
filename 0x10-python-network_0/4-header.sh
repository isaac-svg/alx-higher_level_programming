#!/bin/bash
# Gets the body with a header variable X-School-User-Id
curl -s -H "X-School-User-Id: 98" "$1"
