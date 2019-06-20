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
```python
s = "Python syntax highlighting"
print s
```
#### Output Screenshot 

#### Any modification and suggestion are welcome 


