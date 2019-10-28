FROM centos:centos7
ENV LANG=en_US.utf8
RUN yum install epel-release -y
COPY provision/copr.repo.internal /etc/yum.repos.d/copr.repo
RUN yum install python37-devel gcc gcc-c++ make rpm-build \
    openblas-devel Cython lapack64-devel gcc-gfortran -y
RUN useradd -ms /bin/bash worker
RUN mkdir /builddir/ && chown worker: /builddir
USER worker
RUN mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
COPY --chown=worker:worker nlp-py-venv.spec /home/worker/rpmbuild/SPECS/
COPY --chown=worker:worker requirements.txt /home/worker/rpmbuild/SOURCES/
RUN rpmbuild -ba /home/worker/rpmbuild/SPECS/nlp-py-venv.spec
CMD /bin/bash
