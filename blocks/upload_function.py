from view import *

@app.route('/images/upload/<path:filename>')
def uploaded_files(filename):
    path = 'static/images/upload'
    return send_from_directory(path, filename)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('upload')
    extension = f.filename.split('.')[-1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')
    f.save(os.path.join('static/images/upload', f.filename))
    url = url_for('uploaded_files', filename=f.filename)
    return upload_success(url, filename=f.filename)
