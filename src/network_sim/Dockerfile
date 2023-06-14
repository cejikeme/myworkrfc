FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y mininet iputils-ping
RUN apt-get install -y git
RUN  apt-get install -y sudo
# Install Python 3 and pip
RUN apt-get install -y python3 python3-pip

# Set the default Python version
RUN ln -s /usr/bin/python3 /usr/bin/python

#Install Scapy
RUN pip install scapy

#install mininet
RUN git clone https://github.com/mininet/mininet
WORKDIR /mininet
RUN ls
#RUN util/install.sh -a

# Set the IP address
ENV IP_ADDRESS 192.168.0.1


# Set the working directory
WORKDIR /home/
CMD ["bash"]

