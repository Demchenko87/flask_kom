class Configuration(object):
    DEBUG = False
    CKEDITOR_FILE_UPLOADER = 'upload'

    UPLOADED_PHOTOS_DEST = 'static/images'
    UPLOADED_FILES_DEST = 'static/files'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///komentish.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'mysecret'
    # -- security
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'


