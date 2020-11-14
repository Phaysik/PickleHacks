main() {
    if [ "$#" -ne 8 ]; then
        echo "You must pass 8 arguments to this script"
        exit 0
    fi
    
    echo "Deleting the concatenated image, if it exists"
    rm -rf concatenated.png

    python combine.py "$1" "$2" "$3" "$4" "$5" "$6" "$7" "$8"
}

main "$@"