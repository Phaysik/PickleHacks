#!/bin/bash

main() {
    echo "Installing requirements to process and handle images"
    
    pip install Pillow
}

main "$@"