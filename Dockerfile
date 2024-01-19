FROM jenkins/jenkins:lts-jdk11

USER root
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv net-tools

COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt