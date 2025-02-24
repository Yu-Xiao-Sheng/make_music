# MP4 to Enhanced MP3 Converter

这是一个使用Flask构建的Web应用程序，用于将MP4文件转换为增强版MP3。

## 先决条件

- Python 3.x
- pip
- FFmpeg（用于处理多媒体文件）

## 安装

1. 克隆此存储库：
   ```bash
   git clone <repository-url>
   cd make_music
   ```

2. 创建并激活虚拟环境（可选）：
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

4. 安装 FFmpeg：
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```

## 运行应用

1. 确保`uploads`目录存在：
   ```bash
   mkdir -p uploads
   ```

2. 启动Flask应用：
   ```bash
   python app.py
   ```

3. 在浏览器中打开`http://127.0.0.1:5000`，使用应用程序。

## 部署

- 可以使用任何支持Python的Web服务器（如Gunicorn）来部署此应用。
- 确保在生产环境中关闭调试模式。