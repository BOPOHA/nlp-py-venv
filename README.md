# nlp-py-venv
Python virtual environment for NLP proxy

# test

    $ docker build . --tag nlp-venv
    $ docker run -v /tmp:/mnt -it  nlp-venv bash -c 'cp ~/rpmbuild/{SRPMS,RPMS/x86_64}/*.rpm  /mnt/'
    $ ls /tmp/*rpm
    /tmp/nlp-py-venv-1.0.0-1.el7.src.rpm
    /tmp/nlp-py-venv-1.0.0-1.el7.x86_64.rpm

 for LIB in `find   /usr/lib64/ -type f -name "libopenblas*.so"`; do echo $LIB; LD_PRELOAD=$LIB /builddir/venv/bin/python numpy-benchmark.py ; done
