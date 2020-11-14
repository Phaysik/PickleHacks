main() {
    if [ -d "./Images" ]; then
        echo "Deleting all the images in ./Images/"
        rm -rf ./Images/*
    else
        echo "Creating an Images folder"
        mkdir Images
    fi

    python tti.py 
}

main "$@"