for file in markdowns/*.md; do pandoc -i $file -o "${file%.*}.html"; done