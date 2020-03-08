

from flask import Flask, request, render_template, send_file
import converter
import zipfile
import os

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text. upper()
    converter.compressVideo([processed_text],10)
    return processed_text

@app.route('/file-download/')
def file_download():
    return render_template('file.html')

@app.route('/return-file/')
def return_file():
	zipFolder = zipfile.ZipFile('videos.zip','w', zipfile.ZIP_DEFLATED) 
	for root, directs, files in os.walk('./video'):
		if os.path.exists('./video/.DS_Store'):
			os.remove('./video/.DS_Store')
		for f in files:
			#print(f)
			zipFolder.write('./video/' + str(f))
	zipFolder.close()
	print('zip close')
	# for root, directs, files in os.walk('./video'):
	# 	for f in files:
	# 		print(f)
	# 		os.remove(f)
	os.system("rm videos/*")
	return send_file('videos.zip', mimetype ='zip', attachment_filename = 'videos.zip', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host="0.0.0.0", port=80)