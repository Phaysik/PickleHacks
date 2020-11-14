#!/bin/bash

main() {
    echo "You must install ChromeDriver 86"
    echo "You must also add the ChromeDriver executable to your PATH"
    echo "Installing the requirements to scrape websites"
    
    pip install selenium
    pip install requests
    pip install validators
}

main "$@"