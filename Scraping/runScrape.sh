main() {
    echo "Make sure to run 'requirements.sh' before running this"

    if [ "$#" -ne 1 ]; then
        echo "Only pass in one argument to the script"
        exit 0 
    fi

    echo "Deleting all the images in ./Images/"
    rm -rf ./Images/*

    python scrape.py "$1"
}

main "$@"