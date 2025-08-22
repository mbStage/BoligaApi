
import os
from flask import Flask, send_from_directory, render_template_string, url_for

app = Flask(__name__)

IMAGE_FOLDER = "C:\\Users\\falds\\Documents\\Martin\\Git\\BoligaApi\\images\\Åkandevej 20"  # Put your images in this folder (relative to app.py)

@app.route('/')
def index():
    # List all files in IMAGE_FOLDER
    files = [f for f in os.listdir(IMAGE_FOLDER) if os.path.isfile(os.path.join(IMAGE_FOLDER, f))]
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
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)