from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from autograder.autograder import compile_and_run

app = Flask(__name__)

# Define the path for uploaded files
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'cpp'}

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        cpp_file = request.files.get('cpp_file', None)
        if cpp_file and allowed_file(cpp_file.filename):
            filename = secure_filename(cpp_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            cpp_file.save(filepath)
            results, log = compile_and_run(filepath)
            return render_template('results.html', results=results, log=log)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
