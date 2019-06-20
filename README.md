# Pdf-Image-Reader-
## Extracting all the image associated with pdf and identify all the text embedded in Image 

#### Technology Used 
* Python 3.7
* Poppler ( reading pdfs image ) 
* Tesseracts
* Flask ( for makeing APIs)
* Postman ( for visualizing api ) 


#### System Environment 
 * Windows
 * Ubuntu (only few modification will required ) 
 
#### Procedure 

Make virtual environments( Use Anaconda platform for better visualization) and install all the necessary requirement mentioned.
Download poppler tools and extract it, open the bin folder and place your python executable file there. Open the postman and run the python executable and pass the localhost url to the postman as POST request. You also need to pass list of pdfs which need to be executed.
after execution, Programe will dynamically create and process directory based on timestamp. The programe is created in such a way that you can pass a batch of files as a POST request.


#### Sample Code

    ##### Flask module for all Image_data_extraction 
     
  ```  
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
    
 ```
 ##### Data processing module 
```
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
```
#### Output Screenshot 
![Output image](https://ibb.co/Kjc9s0w)

#### Any modification and suggestion are welcome 


