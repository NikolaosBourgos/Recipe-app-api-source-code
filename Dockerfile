# the alpine is a lightweight version
FROM python:3.7-alpine
MAINTAINER Nikolaos Bourgos

#Set the python unbuffered environment variable to 1. This tells python to run
#in unbuffered mode, recommended when running python within docker a container.
#The reason behind this is not allow python to buffer the outputs and instead
#print them directly and this avoids some complications
ENV PYTHONUNBUFFERED 1

#Install dependencies
#copy the requirements.txt file from the directory adjacent to the dockerfile
#and paste it inside the docker image
COPY ./requirements.txt /requirements.txt
#install the dependencies using pip
RUN pip install -r /requirements.txt
#Make a directory within the docker image where we will store our app source code
#first create an empty folder called "app"
RUN mkdir /app
#then switch into the "app" folder and make it the default directory.Thus any
#application we run from our docker container will run starting from the "app"
#folder (unless we specify otherwise)
WORKDIR /app
#copy from our local machine the "app" folder and to the "app" folder inside
#the docker image.
COPY ./app /app

#Create a user that is going to run our application using docker
RUN adduser -D user
#The -D means this user is only for running applications
#then switch to that user
USER user

#Finaly to build this image open a powershell within this folder and type the
#command "docker build ."
