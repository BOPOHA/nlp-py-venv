FROM centos:centos7
ENV LANG=en_US.utf8
RUN yum install epel-release -y
RUN yum install python36-devel gcc gcc-c++ make rpm-build -y
RUN useradd -ms /bin/bash worker
RUN mkdir /builddir/ && chown worker: /builddir
USER worker
RUN mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
COPY nlp-py-venv.spec /home/worker/rpmbuild/SPECS/
COPY requirements.txt /home/worker/rpmbuild/SOURCES/
RUN rpmbuild -ba home/worker/rpmbuild/SPECS/nlp-py-venv.spec
CMD /bin/bash
