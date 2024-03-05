from distutils.log import debug 
from fileinput import filename 
from flask import *
import shutil
import os
import subprocess
import ast 

app = Flask(__name__) 

upload_folder = 'uploads'
app.config['UPLOAD_FOLDER'] = upload_folder  # set configuration var to make the value of UPLOAD_FOLDER available thruout the Flask application

@app.route('/') 
def main(): 
	return render_template("index.html") 


# /upload 
# This is a function that's called whenever a script file is uploaded 
#
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
		return render_template("ACK_run.html", name = f.filename)


# parse()
# This is a function that checks for how many inputs are needed from a script. 
# This should send a JSON to the frontend to add more input boxes. 
# Searches for a variable with the name `argNum`, example shown below 
# ```
# argNum = 0
# ```
@app.route('/parse', methods = ['POST'])
def parse(script_name: str) -> int:   
	with open(script_name, "r") as f:  
		code = f.readlines()
		first_line = code[0].split()
		argNum = 0 
		try: 
			if ("argNum" in first_line): 
				argNum = first_line[-1]

		except: 
			print("Couldn't find argNum :(")

	return argNum




# /run 
# After importing a script, run the script with the suppliedi nputs 
@app.route('/run', methods = ['POST'])
def run():
	script = request.form.get('script_filename')
	if os.path.isfile(script):

		argNum = parse(script)
		print(argNum)
		# with open("Physics_submissions.zst", 'r') as f:
			# try:

		# TODO: Work on making this more dynamic and responsive 
		# for taking in inputs 
		subprocess.run(["python", script], input='physics_submissions.csv\nphysics_comments.csv', shell=True, text=True, check=True)
		return render_template("ACK_run.html", name = script)
		# except subprocess.CalledProcessError as e:
		# 	return render_template("error.html", message=f"Error running script: {e}")

if __name__ == '__main__': 
	app.run(debug=True)
