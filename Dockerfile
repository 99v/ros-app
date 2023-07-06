# This is an auto generated Dockerfile for ros:ros-base
# generated from docker_images/create_ros_image.Dockerfile.em
FROM ros:noetic-ros-core-focal

# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    python3-rosdep \
    python3-rosinstall \
    python3-vcstools \
    && rm -rf /var/lib/apt/lists/*

SHELL ["/bin/bash", "-c"] 
#==========
RUN apt-get update \
 && apt-get install --assume-yes --no-install-recommends --quiet \
        software-properties-common \
 && add-apt-repository universe \
 && apt-get update \
 && apt-get install --assume-yes --no-install-recommends --quiet \
        python3 \
        python3-pip \
        python3-venv \
 && apt-get clean all

RUN pip install --no-cache --upgrade pip setuptools


#RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app

RUN python3 -m venv venv
RUN source venv/bin/activate
RUN pip3 install Flask 

EXPOSE 5000
#CMD python3 ./index.py
#CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]



#==========

# bootstrap rosdep
RUN rosdep init && \
  rosdep update --rosdistro $ROS_DISTRO

# install ros packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-noetic-ros-base=1.5.0-1* \
    && rm -rf /var/lib/apt/lists/*

