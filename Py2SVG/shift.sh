#!/bin/bash

main() {
    if [ "$#" -ne 1 ]; then 
        echo "You must pass in the filename of the GCode output file"
        exit 0
    fi

    echo "Converting the SVG to GCode"
    python svg2gcode.py "$1"

    echo "Shifting the GCode Values"
    python shift.py "$1"

    echo "Removing Excess G28"
    python g28.py "$1"
}

main "$@"