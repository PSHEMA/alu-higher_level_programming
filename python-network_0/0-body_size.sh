#!/bin/bash
#A script that shows the Content length
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
