FROM centos:centos7
ENV LANG=en_US.utf8
RUN yum install epel-release -y
RUN yum install python36-devel gcc rpm-build -y
WORKDIR /root/rpmbuild/SPECS/
COPY nlp-py-venv.spec .
COPY requirements.txt /root/rpmbuild/SOURCES/
RUN rpmbuild -ba nlp-py-venv.spec
CMD /bin/bash
