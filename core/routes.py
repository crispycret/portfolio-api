


from . import app

@app.route("/")
def index():
    return {'status': 200, 'msg': 'index', 'body': {}}


    