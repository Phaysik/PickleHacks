#!/bin/bash

main() {
    echo "Converting the Concatenated Image into a SVG"

    python -c "import linedraw; linedraw.sketch('$1')"
}

main "$@"