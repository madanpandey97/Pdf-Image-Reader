
from flask import Flask,app, render_template, request, abort, jsonify, send_file
from werkzeug import secure_filename
import filetest
import os
import subprocess
import datetime
app=Flask(__name__)


@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        uploaded_files = request.files.getlist("file[]")
    root_dir = os.getcwd()
    instance_name = 'instance'
    now_time = datetime.datetime.today()
    nTime_dir = now_time.strftime("%d-%m-%Y_%H-%M-%S")
    path =  os.path.join(instance_name+nTime_dir)
    if not os.path.exists(path):
        os.makedirs(path)

    input_pdf_dir =os.makedirs(os.path.join(path, 'input'))

    processed_dir = os.makedirs(os.path.join(path, 'processed'))
    root_dir = os.getcwd()
    for file in uploaded_files:
        file.save((os.path.join(path, 'input', secure_filename(file.filename))))
    path_new = path+'\\input'
    processed_path = path+'\\processed'
    new_processed_directory = os.path.join(root_dir, processed_path)
    # os.chdir(new_working_directory)
    print(new_processed_directory)
    return jsonify(filetest.total_data_extraction(path_new, path, new_processed_directory))



#
# @app.route('/uploader', methods = ['GET', 'POST'])
# def uploader_file():
#     if request.method == 'POST':
#         uploaded_files = request.files.getlist("file[]")
#
#     work_dir = os.makedirs(os.path.join(app.instance_path, 'input'), exist_ok=True)
#
#     now_time = datetime.datetime.today()
#     nTime_dir = now_time.strftime("%d-%m-%Y,  %H:%M:%S")
#     path =  os.path.join(work_dir+nTime_dir)
#
#
#
#     processed_dir =  os.makedirs(os.path.join(app.instance_path, 'processed'), exist_ok=True)
#     root_dir = os.getcwd()
#     for file in uploaded_files:
#         file.save((os.path.join(app.instance_path, 'input', secure_filename(file.filename))))
#     # path = 'instance\\input'
#     print(os.listdir())
#     return jsonify(filetest.total_data_extraction(path))
#







if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=True)
