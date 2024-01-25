#!/bin/bash
# Checks the length of the body
curl -s "$1" | wc -c
