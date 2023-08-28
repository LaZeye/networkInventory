from flask import Flask, render_template
import logging

#Syslog
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('my_app.log')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.addHandler(file_handler) 
logger.info('... this is an info message.')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    loggers = [app.logger, logging.getLogger('werkzeug')]
    for logger in loggers:
        logger.addHandler(file_handler)
    app.run(debug=True)
