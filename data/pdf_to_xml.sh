#!/bin/bash


set -euo pipefail
find . -type f -name "._*" -delete
find . -type f -name '*.pdf' > input.log

while IFS= read -r var; do
    echo "processing $var"
    pipenv run python full_text_extract.py --pdf-file $var --output $var.out 
done < "input.log"
