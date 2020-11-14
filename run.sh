#!/bin/bash

scraping() {
    cd "./Scraping"

    ./requirements.sh
    ./runScrape.sh "$1"

    cd "./Images"

    echo "Deleting all previous images in the processing bay"
    rm -rf ../../ProcessImages/Images/*

    echo "Moving 4 random images over to the processing bay"
    ls | shuf -n 4 | xargs -i mv {} "../../ProcessImages/Images"

    cd "../"
    cd "../"
}

images() {
    cd "./ProcessImages"

    comicImages=()

    for entry in $(ls ./Images/*)
    do
        comicImages+=($entry)
    done

    ./requirements.sh
    ./tti.sh

    textImages=()

    for textEntry in {0..4}
    do
        textImages+=("./Images/file$textEntry.png")
    done

    ./combine.sh ${comicImages[0]} ${textImages[0]} ${comicImages[1]} ${textImages[1]} ${comicImages[2]} ${textImages[2]} ${comicImages[3]} ${textImages[3]}

    cd "../"
}

pngtosvg() {
    cd "./LineDraw"

    ./requirements.sh
    ./line.sh "$1"

    cd "../"
}

svgtogcode() {
    cd "./Py2SVG"

    ./shift.sh "$1"

    cd "../"
}

main() {
    scraping "$1"

    images

    pngtosvg "../ProcessImages/Images/concatenated.png"

    svgtogcode "../LineDraw/output/out"
}

main "$@"