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
prev = datetime.timedelta(seconds=0)
for f in sorted(Path("/Users/xingfanxia/Downloads/袁腾飞/拿破仑").glob("*.m4a")):
    print(str(prev).split(".")[0], " -- ", os.path.splitext(os.path.basename(f))[0].split(' ', 1)[1]) 
    cur_duration = datetime.timedelta(seconds=video_length_seconds(f))
    running_sum = cur_duration + prev
    prev = running_sum
