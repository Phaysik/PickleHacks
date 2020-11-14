#!/bin/bash

main() {
    source ./run.sh $(cat run.txt)
}

main "$@"