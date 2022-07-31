import os
from pytube import YouTube

SOURCE_PATH = './video_to_download.txt'
SAVE_PATH = '/home/antoine/Videos/Youtube'

def get_lines(filepath):
    lines = []
    with open(filepath, 'r') as file:
        lines = [line.rstrip('\n') for line in file]
    return lines

def update_file(filepath, lines):
    with open(filepath, 'w') as file:
        file.writelines(lines)

def download_video(link):
    video = YouTube(link)
    dest = os.path.join(SAVE_PATH, video.author)
    try:
        video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(dest)
        print(f'Successfully download {video.title} by {video.author}')
    except:
        return False
    return True

if __name__ == '__main__':
    links = get_lines(SOURCE_PATH)
    failed = []

    for idx, link in enumerate(links):
       if not download_video(link):
           failed.append(link)

    update_file(SOURCE_PATH, failed)
