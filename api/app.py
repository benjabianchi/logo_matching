import os
import urllib.request
#from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
from tm_functions import template_detector

## Montar en memoria UPLOADS con docker:  https://docs.docker.com/storage/tmpfs/


ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg'])
app = Flask(__name__)
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

UPLOAD_FOLDER = 'images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/multiple-files-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'files[]' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp

	files = request.files.getlist('files[]')
	th = request.form.getlist("th")
	th = float(th[0])
	print(th)
	errors = {}
	success = False
	file_names = []

	for file in files:
		if file and allowed_file(file.filename):
			print(file.filename)
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			file_names.append(filename)
			success = True
		else:
			errors[file.filename] = 'File type is not allowed'

	if success and errors:
		errors['message'] = 'File(s) successfully uploaded'
		resp = jsonify(errors)
		resp.status_code = 500
		return resp
	if success:
		result = template_detector(os.path.join(app.config['UPLOAD_FOLDER'], file_names[0]),os.path.join(app.config['UPLOAD_FOLDER'], file_names[1]),th=th)
		#print(result)
		detection = 0 if result == 0 else 1
		#print(detection)
		resp = jsonify({'message' : 'Files successfully uploaded',"detection":str(detection)})
		resp.status_code = 201
		print(file_names)
		print(os.path.join(app.config['UPLOAD_FOLDER'],file_names[0]))
		#result = template_detector(os.path.join(app.config['UPLOAD_FOLDER'], file_names[0]),os.path.join(app.config['UPLOAD_FOLDER'], file_names[1]),th=0.975)
		print(result)
		return resp
	else:
		resp = jsonify(errors)
		resp.status_code = 500
		return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000,debug=True)
