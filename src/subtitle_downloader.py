import logging
import sys
import os
import hashlib
import requests

valid_extensions = frozenset([".avi", ".mp4", ".mkv", ".mpg", ".mpeg", ".mov", ".rm", ".vob", ".wmv", ".flv", ".3gp", ".3g2"])


def main():
    logging.basicConfig(filename="subtitle.log", level=logging.INFO)
    logging.info("Starting with the arguments...." + str(sys.argv))

    if len(sys.argv) == 1:
        print "No file Name is given. Exiting....!!!"
        sys.exit(1)

    for path in sys.argv:
        if os.path.isdir(path):
            for dir_path, _, file_names in os.walk(path):
                for file_name in file_names:
                    file_path = os.path.join(dir_path, file_name)
                    download_subtitle(file_path)
        else:
            download_subtitle(path)


def download_subtitle(path):
    base_path, extension = os.path.splitext(path)
    if extension in valid_extensions:
        if not os.path.exists(path + ".srt"):
            headers = {'User-Agent': 'SubDB/1.0 (subtitle-downloader/1.0; http://github.com/sjsupersumit/subtitleDownloader)'}
            url = "http://api.thesubdb.com/?action=download&hash=" + get_hash(path) + "&language=en"
            session = requests.session()
            response = session.get(url, headers=headers)
            if response.status_code == 200:
                with open(base_path + ".srt", "wb") as subtitle:
                     subtitle.write(response)
                     logging.info("Subtitle successfully downloaded for " + path)
            else:
                logging.info("couldn't found the subtitles for " + path + " HTTP STATUS_CODE:" + str(response.status_code))


def download_from_opensubtitle(path):
    pass





def get_hash(file_path):
    logging.info("Trying to read " + file_path + " for hash Genration...")
    read_size = 64 * 1024
    with open(file_path, 'rb') as f:
        data = f.read(read_size)
        f.seek(-read_size, os.SEEK_END)
        data += f.read(read_size)
    return hashlib.md5(data).hexdigest()


if __name__ == '__main__':
    main()
