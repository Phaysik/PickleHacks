#!/bin/bash

main() {
    echo "Installing requirements to convert an image into a SVG"
    
    pip install Pillow
}

main "$@"