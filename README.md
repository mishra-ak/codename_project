# codename_project
Codename_project members comprises of Shubham Sharma,Anchal Gupta and Akshay Mishra all pursuing B.TECH from SRM in CSE.

The objective of this project is to create extension which helps in detecting tags of the stackoverflow questions using Deep Learning technology.

This repo contains files for our  major project.We have folder for chrome extension.This folder contains javascript files used 
for building the chrome extension and json file which is the configuration file for our extension.It also contains icon of our extension.

Then we have app.py file which is the flask file used for creating the local server.Extension will interact with this server which will receive input,feed to the model and give back the output.For now this is implemented on the frontend which i have designed for the demo purpose of my members.

Demo Frontend is contained in templates folder.In this demo app only me and my members can sign in using our registration numbers and names.

Then complete model is contained in .ipynb file which contains the complete implementation of our model.
Model implementation:
    First I imported data from Google BigQuery to Google Drive.
    Then i mount my drive and read the data using panda.
    Then i preprocess my data.
    After that i tokenize my input data.
    Then convert the labels into 1-hot array.
    Then i designed my model using keras which is tensorflow api.
    Then i trained my model on that data for 4 epochs.
    Then i saved my model.

.pkl file contains serialized tokens of input data.
.h5 file contains serialized model.
model_prediction.py contains the class which receives input data tokenize it and then feed it to the model after loading it.
prediction.py is the file which import the above module and interact with class memeber function.
That's it..


    
