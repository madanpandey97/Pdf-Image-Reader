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


