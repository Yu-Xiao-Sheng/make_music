from flask import Flask, request, jsonify, render_template, send_file
import os
from werkzeug.utils import secure_filename
from mp4_to_enhanced_mp3 import process_mp4_file

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'mp4'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Process the MP4 file
        sample_rate = request.form.get('sample_rate', default=48000, type=int)
        bit_rate = request.form.get('bit_rate', default=320, type=int)
        enhanced_mp3_path = process_mp4_file(file_path, sample_rate, bit_rate)
        
        filename = os.path.basename(enhanced_mp3_path)
        response = send_file(enhanced_mp3_path, as_attachment=True, download_name=filename.encode('utf-8').decode('latin1'), mimetype='audio/mpeg')
        
        # 删除临时文件
        os.remove(file_path)
        os.remove(enhanced_mp3_path)
        
        return response
    else:
        return jsonify({'error': 'Invalid file type'}), 400

from flask import Flask, request, jsonify, render_template

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(host='0.0.0.0', debug=True)