main() {
    if [ "$#" -ne 8 ]; then
        echo "You must pass 8 arguments to this script"
        exit 0
    fi

    echo "This bash script expects the input to follow: TopLeft_Comic TopLeft_Text TopRight_Comic TopRight_Text BottomLeft_Comic BottomLeft_Text BottomRight_Comic BottomRight_Text"
    
    echo "Deleting the concatenated image, if it exists"
    rm -rf concatenated.png

    python combine.py "$1" "$2" "$3" "$4" "$5" "$6" "$7" "$8"
}

main "$@"