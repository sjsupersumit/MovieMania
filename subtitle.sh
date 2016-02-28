#!/bin/bash

for i in "$@"
 do
    echo "\n calling script with argument.."
    echo " $i"
    python /Users/sumit.jha/Documents/personal/SubtitleDownloader/src/subtitle_downloader.py "$i"
  done

