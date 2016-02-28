#!/usr/bin/env bash

#!/bin/bash

for i in "$@"
 do
    echo "calling script with argument\n"
    echo "$i"
    python /Users/sumit.jha/Documents/personal/SubtitleDownloader/src/imdb_info.py "$i" 2>&1 | tee /dev/null


  done

