#!/bin/bash

if [ ! -d "venv" ]; then
    mkdir venv
    echo "Create venv/"
else
    echo "Found venv/"
    rm -rf venv/*
    echo "Cleaned venv/*"
fi

python -m venv venv

echo "Successed venv environment created."
