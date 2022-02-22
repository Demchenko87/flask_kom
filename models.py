from app import db, app
from datetime import datetime
import re
from flask_security import UserMixin, RoleMixin

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(100), nullable=True)
    title = db.Column(db.String(160))
    slug = db.Column(db.String(140), unique=True)
    introtext = db.Column(db.Text)
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    tit = db.Column(db.String(100), nullable=True)
    key = db.Column(db.String(100), nullable=True)
    des = db.Column(db.Text, nullable=True)


    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)
class AboutUs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    def __repr__(self):
        return '<AboutUs id: {}, content: {}>'.format(self.id, self.content)
class Premium(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    def __repr__(self):
        return '<Premium id: {}, content: {}>'.format(self.id, self.content)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)

class Ruladdcomp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)

class Rules(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)


# subs = db.Table('subs',
#
#                 db.Column('divorced_id', db.ForeignKey('divorced.id'))
#                 )
#, secondary=subs,

class Divorced(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160))
    image = db.Column(db.String(100), nullable=True)
    slug = db.Column(db.String(140), unique=True)
    companys = db.relationship("Company", backref=db.backref('divorced'))

    def __init__(self, *args, **kwargs):
        super(Divorced, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Divorced id: {}, title: {}>'.format(self.id, self.title)


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160))
    image = db.Column(db.String(100), nullable=True)
    slug = db.Column(db.String(140), unique=True)
    href = db.Column(db.String(100), nullable=True)
    content = db.Column(db.Text)
    map = db.Column(db.Text)
    comments = db.relationship("Comments", backref=db.backref('company'))
    divorced_id = db.Column(db.Integer, db.ForeignKey('divorced.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super(Company, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Company id: {}, title: {}>'.format(self.id, self.title)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(160))
    city = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    stars = db.Column(db.String(140))

    content = db.Column(db.Text)
    publish = db.Column(db.String(140))
    datetime = db.Column(db.String(100), nullable=True)
    # user_id = db.Column(db.String(160))
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)


# ---- Flask Security
roles_users = db.Table('roles_users', db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
                       )
#----- end flask security

#---Create User and Role user
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))


#----end Create User and Role user


#
# class Seo(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     title = db.Column(db.String(100), unique=True)
#     keyw = db.Column(db.String(100), unique=True)
#     desc = db.Column(db.Text)
#
