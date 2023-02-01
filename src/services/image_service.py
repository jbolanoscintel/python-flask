
from werkzeug.utils import secure_filename
import os
from src import app

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


class image_service:
    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def upload_file(self, file):
        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
