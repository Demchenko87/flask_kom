from view import *

class AddAbout(FlaskForm):
    content = CKEditorField('Описание')

class AddContact(FlaskForm):
    content = CKEditorField('Описание')

class AddRuladdcomp(FlaskForm):
    content = CKEditorField('Описание')

class AddRules(FlaskForm):
    content = CKEditorField('Описание')

class AddPost(FlaskForm):
    title = StringField('title')
    introtext = TextAreaField('introtext')
    tit = StringField('tit')
    key = StringField('key')
    des = TextAreaField('des')
    image = FileField('image', validators=[FileAllowed(IMAGES, 'Only images are accepted.')])
    content = CKEditorField('content')


class AddDivorced(FlaskForm):
    title = StringField('title')
    image = FileField('image', validators=[FileAllowed(IMAGES, 'Only images are accepted.')])


class AddCompany(FlaskForm):
    title = StringField('title')
    href = StringField('href')
    map = TextAreaField('map')
    content = CKEditorField('Описание')
    slug = StringField('slug')
    divorced_id = StringField('divorced_id')
    image = FileField('image', validators=[FileAllowed(IMAGES, 'Only images are accepted.')])

class AddComment(FlaskForm):
    name = StringField('name', [validators.required()])
    city = StringField('city', [validators.required()])
    # email = StringField('email')
    stars = StringField('stars', [validators.required()])
    content = TextAreaField('content', [validators.required()])
    datetime = StringField('datetime', [validators.required()])
    # user_id = StringField('user_id')
    company_id = StringField('company_id', [validators.required()])
