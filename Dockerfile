# FROM python:3.10

# # RUN mkdir -p /usr/src

# WORKDIR /worker

# # COPY  ./requirements.txt /worker/requirements.txt
# COPY  requirements.txt .

# RUN pip install -r requirements.txt

# COPY ./worker ./worker

# EXPOSE 3000

# # CMD ["ls", "-la"]
# CMD ["python", "./worker/worker-mqtt.py"]

#docker build -t testdockerpy . command to create the image
#docker stop $(docker ps -a -q) stop container
#docker rm $(docker ps -a -q) delete stoped containers
#docker rmi  delete image
#docker run -p 4000:3000 testdockerpy  run container

FROM python:3.10

COPY  ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

WORKDIR /usr/app/src/
COPY worker-mqtt.py router.py database_manager.py ./

EXPOSE 3000
