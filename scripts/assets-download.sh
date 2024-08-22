#!/bin/bash

if [ ! -d "assets" ]; then
    mkdir assets
    echo "Create assets/"
else
    echo "Found assets/"
    rm -rf assets/*
    echo "Cleaned assets/*"
fi

wget -P assets https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
