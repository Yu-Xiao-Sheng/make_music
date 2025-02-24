from pydub import AudioSegment

def convert_mp4_to_mp3(input_file, output_file):
    # 读取 MP4 文件
    video = AudioSegment.from_file(input_file, format="mp4")
    
    # 导出为 MP3 文件
    video.export(output_file, format="mp3")
    print(f"文件已成功转换并保存为: {output_file}")

# 示例用法
# input_file = "resource/a7faa5cbe7b12634e9638874c1e3078b.mp4"
# output_file = "resource/a7faa5cbe7b12634e9638874c1e3078b.mp3"
# convert_mp4_to_mp3(input_file, output_file)