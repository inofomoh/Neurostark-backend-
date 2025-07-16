
from flask import Flask, request, jsonify, send_file
import os
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/generate', methods=['POST'])
def generate_film():
    image = request.files.get('image')
    script = request.form.get('script')
    genre = request.form.get('genre')

    if not image or not script or not genre:
        return jsonify({'error': 'Missing fields'}), 400

    # Save uploaded image
    uid = str(uuid.uuid4())
    image_path = os.path.join(UPLOAD_FOLDER, f"{uid}.jpg")
    image.save(image_path)

    # Simulate AI film generation (placeholder)
    output_path = os.path.join(RESULT_FOLDER, f"{uid}_film.mp4")
    with open(output_path, 'wb') as f:
        f.write(b"FAKE_VIDEO_CONTENT")

    return jsonify({
        'status': 'success',
        'download_url': f'/download/{uid}'
    })

@app.route('/download/<uid>', methods=['GET'])
def download(uid):
    path = os.path.join(RESULT_FOLDER, f"{uid}_film.mp4")
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
