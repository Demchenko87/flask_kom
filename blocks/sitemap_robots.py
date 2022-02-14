from view import *
@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
@app.route("/sitemap.xml")
def sitemap_xml():
    posts = Post.query.all()
    response = make_response(render_template("sitemap.xml", posts=posts))
    response.headers['Content-Type'] = 'application/xml'
    return response
