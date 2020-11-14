main() {
    if [ "$#" -ne 8 ]; then
        echo "You must pass 8 arguments to this script"
        exit 0
    fi

    echo "Deleting all previously created images"
    rm -rf *.png

    echo "This bash script expects the input to follow: TopLeft_Text Image_Name TopRight_Text Image_Name BottomLeft_Text Image_Name BottomRight_Text Image_Name"

    python tti.py "$1" "$2" "$3" "$4" "$5" "$6" "$7" "$8"
}

main "$@"