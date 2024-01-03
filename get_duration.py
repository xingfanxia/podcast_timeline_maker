from pathlib import Path
import subprocess
import datetime
import os

def video_length_seconds(filename):
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            "--",
            filename,
        ],
        capture_output=True,
        text=True,
    )
    try:
        return float(result.stdout)
    except ValueError:
        raise ValueError(result.stderr.rstrip("\n"))

print('''
***********生成时间轴***********
powered by ffprobe & python :)
********************************
''')
def format_timedelta(td):
    seconds = int(td.total_seconds())
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)

prev = datetime.timedelta(seconds=0)
for f in sorted(Path("/Users/xingfanxia/Downloads/warhammer/audios").glob("*.m4a")):
    print(format_timedelta(prev), " -- ", os.path.splitext(os.path.basename(f))[0])
    # Assuming video_length_seconds function exists and returns the length of the video in seconds
    cur_duration = datetime.timedelta(seconds=video_length_seconds(f))
    running_sum = cur_duration + prev
    prev = running_sum


'''
Make Concat Version
for f in *.mp4 ; do echo file \'$f\' >> list.txt; done && ffmpeg -f concat -safe 0 -i list.txt -c copy combined.mp4 && rm list.txt
for f in *.m4a ; do echo file \'$f\' >> list.txt; done && ffmpeg -f concat -safe 0 -i list.txt -c copy combined.m4a && rm list.txt

video download
yt-dlp --cookies-from-browser chrome -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" https://www.youtube.com/watch\?v\=xYdLeKX6NLk\&list\=PLe1YdiKWcqPR-6p2DOrs2wszsDiA1Pxi3\&pp\=iAQB -o "%(playlist)s EP%(playlist_index)s - %(title)s.%(ext)s"
yt-dlp --cookies-from-browser chrome -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"  https://www.youtube.com/@bohaixiaoli -o "%(playlist)s EP%(playlist_index)s - %(title)s.%(ext)s"

audio download
yt-dlp --cookies-from-browser chrome -f "bestaudio[ext=m4a]" https://www.youtube.com/watch\?v\=xYdLeKX6NLk\&list\=PLe1YdiKWcqPR-6p2DOrs2wszsDiA1Pxi3\&pp\=iAQB -o "%(playlist)s EP%(playlist_index)s - %(title)s.%(ext)s"
'''