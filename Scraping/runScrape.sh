#!/bin/bash

main() {
    echo "Make sure to run 'requirements.sh' before running this"

    if [ "$#" -ne 1 ]; then
        echo "Only pass in one argument to the script"
        exit 0 
    fi

    if [ -d "./Images" ]; then
        echo "Deleting all the images in ./Images/"
        rm -rf ./Images/*
    else
        echo "Creating an Images folder"
        mkdir Images
    fi

    python scrape.py "$1"
}

main "$@"