# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.10
#  This installs a Python image into the Docker image. This is also the version of Python that will run the application in the container

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
# this command copiesthe requirements.txt to the working directory of the docker

RUN pip install --no-cache-dir -r requirements.txt
# this installs the required libariries/dependencies from the requirements.txt

# Mounts the application code to the image
COPY . code
# this command is used to copy all the files from current directory to the code folder in docker working directory

WORKDIR /code
# this command changes the working directory to /code

EXPOSE 8000
# this command releases the port 8000 within the container so that we can run our dbms project

# runs the production server
ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "0.0.0.0:8000"]

# these two commands are required to start the server and run the application