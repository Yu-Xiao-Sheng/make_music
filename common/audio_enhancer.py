from pydub import AudioSegment
from pydub.utils import mediainfo

def enhance_audio(input_file, output_file, new_sample_rate=48000, min_bitrate=320):
    # 读取音频文件
    audio = AudioSegment.from_file(input_file)
    
    # 获取当前采样率和比特率
    current_sample_rate = audio.frame_rate
    info = mediainfo(input_file)
    current_bitrate = int(info['bit_rate']) // 1000  # 转换为 kbps

    print(f"当前采样率: {current_sample_rate} Hz")
    print(f"当前比特率: {current_bitrate} kbps")

    # 设置新的采样率
    audio = audio.set_frame_rate(new_sample_rate)

    # 确保比特率至少为指定的最小比特率
    new_bitrate = max(current_bitrate, min_bitrate)

    # 导出新的 MP3 文件
    audio.export(output_file, format="mp3", bitrate=f"{new_bitrate}k")
    print(f"新文件已导出: {output_file}，采样率: {new_sample_rate} Hz，比特率: {new_bitrate} kbps")

# 示例用法
# input_file = "resource/窗台边的春日_增强版.mp3"
# output_file = "resource/窗台边的春日_超级增强版.mp3"
# enhance_audio(input_file, output_file)