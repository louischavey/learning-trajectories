from distutils.log import debug 
from fileinput import filename 
from flask import *
import shutil
import os
import subprocess
app = Flask(__name__) 

upload_folder = 'uploads'
app.config['UPLOAD_FOLDER'] = upload_folder  # set configuration var to make the value of UPLOAD_FOLDER available thruout the Flask application

@app.route('/') 
def main(): 
	return render_template("index.html") 

@app.route('/upload', methods = ['POST']) 
def success(): 
	f = request.files['file'] 
	if f:
		if f.filename == '':
			f.filename = "Untitled"
		f.save(f.filename)
		file_copy = f"{os.path.splitext(f.filename)[0]}_copy{os.path.splitext(f.filename)[1]}"
		shutil.copy2(os.path.realpath(f.filename), os.path.realpath(file_copy))
		os.remove(f.filename)
		return render_template("ACK_reupload.html", name = f.filename)

@app.route('/run', methods = ['POST'])
def run():
	script = request.form.get('script_filename')
	if os.path.isfile(script):
		#return script
		# path = 'run.py'
		# spawn subprocess w/ default input of physics_comments
		#try:
		subprocess.run(["python", script], shell=True, check=True)
			# output = subprocess.check_output(['python', 'run.py'], stderr=subprocess.STDOUT, universal_newlines=True)
			# return jsonify({"output": output}), 200
		return render_template("ACK_run.html", name = script)
		#except subprocess.CalledProcessError as e:
		# 	return jsonify({'error':f'Script execution failed: {e.output}'}, 500)	
		# create a new output file

if __name__ == '__main__': 
	app.run(debug=True)
