FROM centos:7
WORKDIR /app
RUN yum install python3-pip -y && pip3 install python-nomad prometheus-client 
COPY ./src/nomad_exporter .
CMD ["main.py"]
ENTRYPOINT ["python3"]