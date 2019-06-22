import os
import shutil
import subprocess
import glob
import re
import datetime
import json
from flask import Flask, render_template, request, abort, jsonify, send_file

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def total_data_extraction(input_dir, path ,new_processed_directory):
    '''Pass the input directory where all the pdf file is availble'''
    print(input_dir)
    testing_for_json_data={}
    for filename in glob.glob(os.path.join(input_dir, '*.pdf')):
        dir_name = re.split("[.]",filename)[-2]
        image_working_directory = os.path.basename(dir_name)
        print(dir_name)
        now = datetime.datetime.today()
        nTime = now.strftime("%d-%m-%Y")
        dest = os.path.join(image_working_directory+nTime)
        new_dest = os.path.join(path, dest)
        print(new_dest)
        pdf_input_name = os.path.basename(input_dir)
        pro_dir = 'instance\processed'
        testing_for_json_data[image_working_directory] = image_exporter(filename, output_dir=new_dest, image_name=pdf_input_name)
        shutil.move(filename, new_processed_directory+'\\'+(filename.split("\\")[-1]))

    return testing_for_json_data



def image_exporter(pdf_path, output_dir,image_name):
    '''pass the pdf path and output path, here outpur director
    is creating on run time'''
    print('running')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print('running4')
    cmd = ['pdfimages', '-all', pdf_path,
           '{}/prefix'.format(output_dir)]
    subprocess.call(cmd)
    image_data = image_reader(output_dir)
    print(image_data)
    return image_data


def image_reader(image_path):
    '''pass the image path as input, it will return all
    the text carried by images in dictonary format convert it to json accordingly'''
    data = {}
    for imgname in glob.glob(os.path.join(image_path, '*.png')):
        pytesseract.pytesseract.tesseract_cmd = r'Your Tessarect path'
        #print(pytesseract.image_to_string(Image.open('xy.png')))
        test_json = pytesseract.image_to_string(Image.open(imgname))
        extractText = " ".join(test_json.split())
        img_temp = os.path.basename(imgname)
        data[img_temp] =extractText
        print('running and testing filename'+imgname)
    return data
