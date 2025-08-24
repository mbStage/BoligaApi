
import os
from flask import Flask, send_from_directory, render_template_string, url_for

app = Flask(__name__)

IMAGE_FOLDERS = "C:\\Users\\falds\\Documents\\Martin\\Git\\BoligaApi\\images"  # Put your images in this folder (relative to app.py)

@app.route('/')
def index():
    # List all files in IMAGE_FOLDER
    
    files = []
    for IMAGE_FOLDER in os.listdir(IMAGE_FOLDERS):
        folder_path = os.path.join(IMAGE_FOLDERS, IMAGE_FOLDER)
        if os.path.isdir(folder_path):
            for f in os.listdir(folder_path):
                file_path = os.path.join(folder_path, f)
                if os.path.isfile(file_path):
                    # Store relative path for serving
                    files.append(f"{IMAGE_FOLDER}/{f}")


    # Simple HTML template to show images with direct links
    
    html = """
    <html>
    <head><title>Local Disk Pictures</title></head>
    <body>
        <h1>Pictures from Local Disk</h1>
        {% for file in files %}
            <div style="margin:10px;display:inline-block;">
                <img src="{{ url_for('serve_image', filename=file) }}" style="max-width:300px;max-height:300px;"><br>
                {{file}}<br>
                <a href="{{ url_for('serve_image', filename=file) }}" target="_blank">Direct Link</a>
            </div>
        {% endfor %}
    </body>
    </html>
    """
    return render_template_string(html, files=files)

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDERS, filename)

if __name__ == "__main__":
    app.run(debug=True)