from view import *
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.errorhandler(403)
def unauthorized_page(e):
    return render_template('403.html'), 403
