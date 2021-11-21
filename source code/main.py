from flask import Flask, redirect, url_for, render_template,request,send_from_directory,flash
from werkzeug.utils import secure_filename
import os
from chaosTheory import chaosTheory
import cv2
import numpy as np

UPLOAD_FOLDER = 'static/uploads/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/",methods=['GET', 'POST'])
def home():
	return render_template("about.html")

@app.route("/about",methods=['GET', 'POST'])
def about():
	return render_template("about.html")

@app.route("/encode",methods=['GET', 'POST'])
def encode():
	if request.method == 'POST':
		# get user input fields
		image = request.files['file']
		ctKey1 = request.form['ctKey1']
		ctKey2 = request.form['ctKey2']
		output = request.form['output'] + '.png'

		# key input validation
		x = chaosTheory()
		ctKey = x.validateChaosKey(ctKey1, ctKey2)

		if (ctKey !=None):
			try:
				# opening uploaded image
				imageName = secure_filename(image.filename)
				image.save(os.path.join(app.config['UPLOAD_FOLDER'], imageName))
				imagePath = UPLOAD_FOLDER + imageName
				image = cv2.imread(imagePath)

				# encryting image (chaos theory)
				resultImg = x.imgEncryption(imagePath, ctKey)
				if (resultImg is not None):
					outputPath = 'static/uploads/'+ output
					cv2.imwrite(outputPath, resultImg)
					os.remove(imagePath)
					return render_template('decode.html', filename=outputPath)

				# if chaoskey results in an overflow error
				else:
					return render_template('encode.html',filename='overflow_error')

			# if process error occurs along the way
			except:
				return render_template('encode.html',filename='general_error')

		# if inputted password is invalid
		else:
			return render_template("encode.html",filename= 'password_error')

	# if submit button not pressed
	else:
		return render_template("encode.html")

@app.route("/decode",methods=['GET', 'POST'])
def decode():
		if request.method == 'POST':
			# get user input fields
			image = request.files['file']
			ctKey1 = request.form['ctKey1']
			ctKey2 = request.form['ctKey2']
			output = request.form['output'] + '.png'

			# key input validation
			x = chaosTheory()
			ctKey = x.validateChaosKey(ctKey1, ctKey2)

			if (ctKey !=None):
				try:
					# opening uploaded image
					imageName = secure_filename(image.filename)
					image.save(os.path.join(app.config['UPLOAD_FOLDER'], imageName))
					imagePath = UPLOAD_FOLDER + imageName

					# decrypting image (chaos theory)
					resultImg = x.imgDecryption(imagePath, ctKey)
					if (resultImg is not None):
						outputPath = 'static/uploads/'+ output
						cv2.imwrite(outputPath, resultImg)
						return render_template('decode.html', filename=outputPath)

					# if chaoskey results in an overflow error
					else:
						return render_template('decode.html',filename='overflow_error')

				# if process error occurs along the way
				except:
					return render_template('decode.html',filename='general_error')

			# if inputted password is invalid
			else:
				return render_template("decode.html",filename= 'password_error')

		# if submit button not pressed
		else:
			return render_template("decode.html")

if __name__ == "__main__":
	app.run(debug = True)
