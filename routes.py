from flask import Flask, render_template, request, redirect, url_for, flash
from core.face_net import CelebModel, CelebModelOperations
import os
import logging
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/images/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

logger = logging.getLogger('fr.main')
celeb_model = CelebModel()
    

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template('upload.html')


@app.route("/face_recognition", methods=["POST"])
def face_recognizer():
    if request.method == 'POST':

        # check if the post request has the file part
        if 'image_file' not in request.files:
            return redirect(url_for('index'))
        file = request.files['image_file']

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return redirect(url_for('index'))

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            celeb_identity = CelebModelOperations.recognize_celebs(
                file_path, celeb_model.fr_model
            )
            return render_template('result.html', image_path=file_path, celeb_identity=celeb_identity)

    return redirect(url_for('index'))


@app.route("/new_celeb")
def celeb_form():
    return render_template('celeb_form.html')


@app.route("/add_celeb", methods=['POST'])
def add_celeb():
    if request.method == 'POST':

        # check if the post request has the file part
        if 'image_file' not in request.files:
            return redirect(url_for('index'))
        file = request.files['image_file']

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return redirect(url_for('index'))

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            celeb_name = request.form['celeb_name']

            celeb_id = CelebModelOperations.add_new_celeb(
                file_path, celeb_name, celeb_model.fr_model
            )
            if celeb_id:
                flash('ID {celeb_id}: {celeb_name}, added to the database.'.format(
                    celeb_name=celeb_name, celeb_id=celeb_id
                ))
            else:
                flash('Error: Face not found or Encoding exists!')
            return redirect(url_for('celeb_form'))


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'many random bytes'
    app.run()
