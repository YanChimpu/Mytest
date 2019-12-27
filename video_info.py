import ffmpeg
import sys

# 执行probe执行
probe = ffmpeg.probe("test.mp4")
video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
if video_stream is None:
    print('No video stream found', file=sys.stderr)
    sys.exit(1)
# 宽度
width = int(video_stream['width'])
# 高度
height = int(video_stream['height'])
# 帧数
num_frames = int(video_stream['nb_frames'])
# 时长
time = (video_stream['duration'])
# 比特率
bitrate = (video_stream['bit_rate'])

print('width: {}'.format(width))
print('height: {}'.format(height))
print('num_frames: {}'.format(num_frames))
print('time: {}'.format(time))
print('bitrate: {}'.format(bitrate))

# 查看全部信息
print(video_stream)