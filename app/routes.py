from app import app

#####################
#   View Functions  #
#####################


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'

