
import openai




import flask

@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html', name='Sebi')



if __name__ == '__main__':
    APP.debug=True
    APP.run()

