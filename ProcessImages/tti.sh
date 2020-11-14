main() {
    if [ ! -d "./Images" ]; then
        echo "Creating an Images folder"
        mkdir Images
    fi

    python tti.py 
}

main "$@"