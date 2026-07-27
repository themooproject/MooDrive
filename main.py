from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
pasta = "files"

arquivos = os.listdir(pasta)

@app.route("/")
def index():

    return render_template("index.html", arquivos=arquivos)

@app.route("/search")
def search():

    palavra_chave = request.args.get('q', '').strip()

    arquivos_filtrados = [item for item in arquivos if palavra_chave.lower() in item.lower()]

    return render_template(
        "search.html", 
        arquivos=arquivos_filtrados,
        palavra_chave=palavra_chave
    )
@app.route("/upload", methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(pasta, filename))
    arquivos.append(filename)
    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):

    return send_from_directory(pasta, filename, as_attachment=True)

@app.route('/visualizar/<filename>')
def view_file(filename):

    return send_from_directory(pasta, filename)

if __name__ == '__main__':
    app.run()