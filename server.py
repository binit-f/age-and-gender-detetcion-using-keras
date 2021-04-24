import mainn as AAG
from flask import Flask
from flask import request
import requests
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import sys
from flask_cors import CORS
from  PIL import Image


app = Flask(__name__,static_url_path='')
CORS(app)


@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/img',methods=['POST'])
def imageCaption():
	f = request.files['file']
	print(f)
	#f.save(secure_filename(f.filename))
	image = AAG.ageAndGender(f)
	return image


if __name__ == '__main__':
	app.run(debug=True)    