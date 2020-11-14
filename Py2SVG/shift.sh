main() {
    echo "This file must be run after turning the svg into gcode"

    if [ "$#" -ne 1 ]; then 
        echo "You must pass in the filename of the gcode output file"
        exit 0
    fi

    python shift.py "$1"
}

main "$@"