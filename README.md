# todoapp
 Quick And Easy To Use, Anytime, Anywhere! "Plan Your Day Better,Get Your Life Organized" Helps You Keep Track Of Your Tasks

• to build the image for the execution environment of our dbms project
we add a tag name so that we can easily identify our image with a name 

docker build -t dbms-project .

• to run the docker, we use the below code -it here refers to interactive terminal and -p 8000:8000 ,the first port is the host port, what you would connect to from outside the container. the second is the port inside the container that your service is listening on

docker run -it -p 8000:8000 dbms-project

• the below code is used to list all the containers in the docker

docker ps -a

• we need to login with docker hub account in order to push our file onto dockerhub

docker login

• we tag the created image with a new name for the docker hub account

docker tag dbms-project drstrange01/dbms-project:0.0.1

• below code is used to push the image to docker hub repositories

docker push drstrange01/dbms-project:0.0.1

•below code is used to pull the image from docker hub account

docker pull drstrange01/dbms-project:0.0.1
