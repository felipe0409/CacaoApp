from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Esto permite peticiones desde otras aplicaciones (como tu app Android)

# Carpeta donde se guardarán las imágenes
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No se encontró la imagen en la petición'}), 400
    image = request.files['image']
    classification = request.form.get('classification', 'sin clasificar')
    
    if image.filename == '':
        return jsonify({'error': 'El archivo no tiene nombre'}), 400

    # Guarda la imagen en una carpeta según la clasificación
    folder = os.path.join(UPLOAD_FOLDER, classification)
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, image.filename)
    image.save(filepath)

    # Aquí podrías agregar más lógica para analizar la imagen o guardarla en una base de datos

    return jsonify({'message': 'Imagen subida correctamente', 'filepath': filepath}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)