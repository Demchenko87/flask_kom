import os
from models import *
from flask import send_from_directory, render_template, request, make_response, redirect, url_for
from flask_security import login_required
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditor, CKEditorField, upload_success, upload_fail
from wtforms import StringField, IntegerField, validators, TextAreaField, HiddenField, SelectField
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_wtf.file import FileField, FileAllowed, FileRequired
import datetime
now = datetime.datetime.now()
from wtforms.validators import DataRequired, ValidationError

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
csv_file = UploadSet('files', ('csv',))
configure_uploads(app, csv_file)
ckeditor = CKEditor(app)

from blocks.sitemap_robots import *
from blocks.upload_function import *
from blocks.flaskform import *
from blocks.errorpage import *

@app.route('/')
def index():
    divorecd = Divorced.query.all()
    return render_template('index.html', divorecd=divorecd)

@app.route('/divorced/<int:id>/<slug>')
def divorced_detail(id, slug):

    divorced = Divorced.query.filter(Divorced.slug == slug).first()
    divorced_f = Divorced.query.filter(Divorced.id == id).first()
    return render_template('divorced_detail.html', divorced_f=divorced_f, divorced=divorced)

@app.route('/divorced/company/<int:id>/<slug>', methods=['GET', 'POST'])
def company(id, slug):
    form = AddComment()
    coments_all = Company.query.all()

    comments = Comments.query.filter(id == Comments.company_id)
    # company_s = Company.query.filter(Company.slug == slug).first()
    company = Company.query.filter(Company.id == id).first()
    datetime = now.strftime("%d-%m-%Y %H:%M")
    if form.validate_on_submit():
        new_comment = Comments(name=form.name.data,
                               city=form.city.data,
                               # email=form.email.data,
                               stars=form.stars.data,
                               content=form.content.data,
                               datetime=form.datetime.data,
                               # user_id=form.user_id.data,
                               company_id=form.company_id.data,
                               )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(request.referrer)
        #return redirect(url_for('company'))

    return render_template('company_detail.html', company=company, coments_all=coments_all, form=form, comments=comments, datetime=datetime)


@app.route('/admin')
@login_required
def admin():
    return render_template('admin/base.html')

@app.route('/about')
def about():
    about = AboutUs.query.all()
    return render_template('about.html', about=about)

@app.route('/about/add', methods=['GET', 'POST'])
@login_required
def add_about():
    form = AddAbout()
    about = AboutUs.query.all()
    if form.validate_on_submit():
        new_about = AboutUs(content=form.content.data)
        db.session.add(new_about)
        db.session.commit()
        return redirect(url_for('add_about'))
    return render_template('admin/add_about.html', admin=True, form=form, about=about)



@app.route('/premium')
def premium():
    premium = Premium.query.all()
    return render_template('premium.html', premium=premium)

@app.route('/contact')
def contact():
    contact = Contact.query.all()
    return render_template('contact.html', contact=contact)

@app.route('/rules_add_company')
def ruladdcomp():
    ruladdcomp = Ruladdcomp.query.all()
    return render_template('rules_add_company.html', ruladdcomp=ruladdcomp)

@app.route('/rules')
def rules():
    rules = Rules.query.all()
    return render_template('rules.html', rules=rules)

@app.route('/search', methods=['GET', 'POST'])
def search():
    search = request.args.get('search')

    if search:
        posts = Post.query.filter(Post.title.contains(search) | Post.introtext.contains(search))
        company = Company.query.filter(Company.title.contains(search))
    else:
        posts = Post.query.all()
    return render_template('search.html', posts=posts, company=company)

@app.route('/admin/contact/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_contact(id):
    contact = Contact.query.get(id)
    if request.method == 'POST':
        contact.content = request.form['content']
        db.session.commit()
        return redirect(request.referrer)
    else:
        return render_template('admin/edit_contact.html', admin=True, contact=contact)


# @app.route('/add/contact', methods=['GET', 'POST'])
# @login_required
# def add_contact():
#     form = AddContact()
#     contact = Contact.query.all()
#     if form.validate_on_submit():
#         new_contact = Contact(content=form.content.data)
#         db.session.add(new_contact)
#         db.session.commit()
#         return redirect(url_for('add_contact'))
#     return render_template('admin/add_contact.html', admin=True, form=form, contact=contact)

@app.route('/admin/ruladdcomp/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_ruladdcomp(id):
    ruladdcomp = Ruladdcomp.query.get(id)
    if request.method == 'POST':
        ruladdcomp.content = request.form['content']
        db.session.commit()
        return redirect(request.referrer)
    else:
        return render_template('admin/edit_ruladdcomp.html', admin=True, ruladdcomp=ruladdcomp)

@app.route('/admin/rules/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_rules(id):
    rules = Rules.query.get(id)
    if request.method == 'POST':
        rules.content = request.form['content']
        db.session.commit()
        return redirect(request.referrer)
    else:
        return render_template('admin/edit_rules.html', admin=True, rules=rules)


# @app.route('/about/delete/<int:id>', methods=['GET'])
# @login_required
# def delete_about(id):
#     about = AboutUs.query.filter_by(id=id).first()
#     db.session.delete(about)
#     db.session.commit()
#     return redirect(request.referrer)

@app.route('/admin/about/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_about(id):
    about = AboutUs.query.get(id)
    if request.method == 'POST':
        about.content = request.form['content']
        db.session.commit()
        return redirect(request.referrer)
    else:
        return render_template('admin/edit_about.html', admin=True, about=about)

@app.route('/admin/premium/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_premium(id):
    premium = Premium.query.get(id)
    if request.method == 'POST':
        premium.content = request.form['content']
        db.session.commit()
        return redirect(request.referrer)
    else:
        return render_template('admin/edit_premium.html', admin=True, premium=premium)

@app.route('/admin/posts')
@login_required
def all_blog():
    posts = Post.query.all()
    return render_template('admin/posts.html', posts=posts)

@app.route('/admin/posts/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_posts(id):
    post = Post.query.get(id)
    if request.method == 'POST':
        post.content = request.form['content']
        post.title = request.form['title']
        post.introtext = request.form['introtext']
        post.tit = request.form['tit']
        post.key = request.form['key']
        post.des = request.form['des']
        if request.files['image'].filename == '':
            pass
        else:
            image_url_main = photos.save(request.files["image"])
            post.image = 'images/' + image_url_main
        try:
            db.session.commit()
            return redirect(request.referrer)
        except:
            return "При редактировании произошла ошибка"
    else:
        return render_template('admin/edit_post.html', admin=True, post=post)

@app.route('/admin/post/add', methods=['GET', 'POST'])
@login_required
def add_post():
    form = AddPost()

    if form.validate_on_submit():
        image_url_main = photos.save(form.image.data)
        image_url = 'images/' + image_url_main
        new_post = Post(content=form.content.data, title=form.title.data, image=image_url, introtext=form.introtext.data, tit=form.tit.data, key=form.key.data, des=form.key.data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('all_blog'))
    return render_template('admin/add_post.html', admin=True, form=form)

@app.route('/admin/post/delete/<int:id>', methods=['GET'])
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(request.referrer)

@app.route('/admin/divorecd')
@login_required
def all_divorced():
    divorced = Divorced.query.all()
    return render_template('admin/divorced.html', divorced=divorced)

@app.route('/admin/divorecd/add', methods=['GET', 'POST'])
@login_required
def add_divorced():
    form = AddDivorced()
    divorced = Divorced.query.all()
    if form.validate_on_submit():
        if request.files['image'].filename == '':
            image_url = 'images/placeholder.webp'
        else:
            image_url_main = photos.save(form.image.data)
            image_url = 'images/' + image_url_main
        new_divorced = Divorced(title=form.title.data, image=image_url)
        db.session.add(new_divorced)
        db.session.commit()
        return redirect(url_for('all_divorced'))
    return render_template('admin/add_divorecd.html', admin=True, form=form, divorced=divorced)

@app.route('/admin/divorecd/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_divorecd(id):
    divorecd = Divorced.query.get(id)
    if request.method == 'POST':
        divorecd.title = request.form['title']


        if request.files['image'].filename == '':
            pass
        else:
            image_url_main = photos.save(request.files["image"])
            divorecd.image = 'images/' + image_url_main
        try:
            db.session.commit()
            return redirect(request.referrer)
        except:
            return "При редактировании произошла ошибка"
    else:
        return render_template('admin/edit_divrecd.html', admin=True, divorecd=divorecd)

@app.route('/admin/divorecd/delete/<int:id>', methods=['GET'])
@login_required
def delete_divorecd(id):
    divorecd = Divorced.query.filter_by(id=id).first()
    db.session.delete(divorecd)
    db.session.commit()
    return redirect(request.referrer)

@app.route('/admin/company')
@login_required
def all_company():
    company = Company.query.all()
    return render_template('admin/company.html', company=company)

@app.route('/admin/company/add', methods=['GET', 'POST'])
@login_required
def add_company():
    form = AddCompany()
    divorced = Divorced.query.all()
    company = Company.query.all()
    if form.validate_on_submit():
        if request.files['image'].filename == '':
            image_url = 'images/placeholder.webp'
        else:
            image_url_main = photos.save(form.image.data)
            image_url = 'images/' + image_url_main
        new_company = Company(title=form.title.data, divorced_id=form.divorced_id.data, image=image_url, href=form.href.data, map=form.map.data, content=form.content.data)
        db.session.add(new_company)
        db.session.commit()
        return redirect(url_for('all_company'))
    return render_template('admin/add_company.html', admin=True, form=form, company=company, divorced=divorced)

@app.route('/admin/company/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_company(id):
    divorced = Divorced.query.all()
    company = Company.query.get(id)
    if request.method == 'POST':
        company.title = request.form['title']
        company.href = request.form['href']
        company.map = request.form['map']
        company.content = request.form['content']
        company.slug = request.form['slug']
        company.divorced_id = request.form['divorced_id']
        if request.files['image'].filename == '':
            pass
        else:
            image_url_main = photos.save(request.files["image"])
            company.image = 'images/' + image_url_main
        try:
            db.session.commit()
            return redirect(request.referrer)
        except:
            return "При редактировании произошла ошибка"
    else:
        return render_template('admin/edit_company.html', admin=True, company=company, divorced=divorced)

@app.route('/admin/company/delete/<int:id>', methods=['GET'])
@login_required
def delete_company(id):
    company = Company.query.filter_by(id=id).first()
    db.session.delete(company)
    db.session.commit()
    return redirect(request.referrer)

@app.route('/admin/comments')
@login_required
def all_comment():
    comments = Comments.query.all()
    return render_template('admin/all_comments.html', admin=True,  comments=comments )

@app.route('/admin/comment/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_comment(id):
    comment = Comments.query.get(id)
    if request.method == 'POST':
        comment.publish = request.form['publish']

        # comment.id = request.form['id']
        # comment.name = request.form['name']
        # comment.city = request.form['city']
        # comment.stars = request.form['stars']
        # comment.content = request.form['content']

        # comment.datetime = request.form['datetime']
        # comment.company_id = request.form['company_id']
        try:
            db.session.commit()
            return redirect(request.referrer)
        except:
            return "При редактировании произошла ошибка"
    return render_template('admin/edit_comment.html', admin=True, comment=comment)


@app.route('/admin/comment/delete/<int:id>', methods=['GET'])
@login_required
def delete_comment(id):
    comment = Comments.query.filter_by(id=id).first()
    db.session.delete(comment)
    db.session.commit()
    return redirect(request.referrer)




# class AddPremium(FlaskForm):
#     content = CKEditorField('Описание')
# @app.route('/premium/add', methods=['GET', 'POST'])
# @login_required
# def add_premium():
#     form = AddPremium()
#     premium = Premium.query.all()
#     if form.validate_on_submit():
#         new_premium = Premium(content=form.content.data)
#         db.session.add(new_premium)
#         db.session.commit()
#         return redirect(url_for('add_premium'))
#     return render_template('admin/add_premium.html', admin=True, form=form, premium=premium)
#

# @app.route('/admin/importexport')
# @login_required
# def impexp():
#     return render_template('admin/importexport.html', admin=True)
#
# @app.route('/export', methods=['GET', 'POST'])
# def export_file():
#     file_name = 'base.csv'
#     path_file = app.config['UPLOADED_FILES_DEST'] + '/' + file_name
#     with open(path_file, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile, delimiter=";")
#         post = Product.query.all()
#         writer.writerow(["name", "price", "stock", "description", "image", "image2", "image3", "image4"])
#         for i in post:
#             writer.writerow([i.name, i.price, i.stock, i.description, i.image, i.image2, i.image3, i.image4])
#     return render_template('admin/export.html', path_file=path_file, admin=True)
#
# @app.route('/import', methods=['GET', 'POST'])
# def import_file():
#     form = AddUpload()
#     if request.method == 'POST':
#
#         if request.form.get('choce') == '0':
#             if form.validate_on_submit():
#                 file_url = csv_file.save(form.file.data)
#                 path_file = app.config['UPLOADED_FILES_DEST'] + '/' + file_url
#                 delete_model = Product.query.delete()
#                 with open(path_file, newline='') as csvfile:
#                     reader = csv.DictReader(csvfile, delimiter=";")
#                     for row in reader:
#                         post = Product(name=row['name'], price=row['price'], stock=row['stock'], description=row['description'], image=row['image'], image2=row['image2'], image3=row['image3'], image4=row['image4'])
#                         db.session.add(post)
#                         db.session.commit()
#                     os.remove(path_file)
#                 return redirect(url_for('index'))
#         else:
#                 if form.validate_on_submit():
#                     file_url = csv_file.save(form.file.data)
#                     path_file = app.config['UPLOADED_FILES_DEST'] + '/' + file_url
#                     with open(path_file, newline='') as csvfile:
#                         reader = csv.DictReader(csvfile, delimiter=";")
#                         for row in reader:
#                             post = Product(name=row['name'], price=row['price'], stock=row['stock'], description=row['description'], image=row['image'], image2=row['image2'], image3=row['image3'], image4=row['image4'])
#                             db.session.add(post)
#                             db.session.commit()
#                         os.remove(path_file)
#                     return redirect(url_for('index'))
#     return render_template('admin/import.html', form=form, admin=True)






