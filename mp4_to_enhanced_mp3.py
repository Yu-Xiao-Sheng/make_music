import os
from common.mp4_2_mp3 import convert_mp4_to_mp3
from common.audio_enhancer import enhance_audio

def process_mp4_file(mp4_file_path, sample_rate=48000, bit_rate=320):
    # 将 MP4 文件转换为 MP3 文件
    # 构建 MP3 文件的输出路径
    base, _ = os.path.splitext(mp4_file_path)
    mp3_file_path = f"{base}.mp3"
    
    # 将 MP4 文件转换为 MP3 文件
    convert_mp4_to_mp3(mp4_file_path, mp3_file_path)
    
    # 构建增强版 MP3 文件的输出路径
    base, ext = os.path.splitext(mp3_file_path)
    enhanced_mp3_output_path = f"{base}_增强版{ext}"
    
    # 增强 MP3 文件的音频质量
    enhance_audio(mp3_file_path, enhanced_mp3_output_path, sample_rate, bit_rate)
    
    # 构建增强版 MP3 文件的输出路径
    base, ext = os.path.splitext(mp3_file_path)
    enhanced_mp3_output_path = f"{base}_增强版{ext}"
    
    # 将增强后的 MP3 文件保存到输出路径
    os.rename(enhanced_mp3_output_path, enhanced_mp3_output_path)
    
    return enhanced_mp3_output_path

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python mp4_to_enhanced_mp3.py <mp4_file_path> [<sample_rate> <bit_rate>]")
        sys.exit(1)
    
    mp4_file_path = sys.argv[1]
    sample_rate = int(sys.argv[2]) if len(sys.argv) > 2 else 48000
    bit_rate = int(sys.argv[3]) if len(sys.argv) > 3 else 320
    
    enhanced_mp3 = process_mp4_file(mp4_file_path, sample_rate, bit_rate)
    print(f"Enhanced MP3 file saved at: {enhanced_mp3}")
