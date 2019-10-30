%global		debug_package       %{nil}
%global     __os_install_post   %{nil}
%define		venvname            venv
%define		coprbuilddir        /builddir/
%define		mkl_lib_dir         /opt/intel/mkl/lib/intel64/
%if 0%{?rhel}  == 7
%define     pyversion           python37
%else
%define     pyversion           python3
%endif

Name:		nlp-py-venv
Version:	1.0.15
Release:	4%{?dist}
Summary:	Python environment for NLP proxy

License:	MIT
Source0:    requirements.txt

BuildRequires:  %{pyversion}-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openblas-devel
BuildRequires:  lapack64-devel
BuildRequires:  gcc-gfortran
BuildRequires:  intel-mkl-64bit
Requires:       %{pyversion}
Requires:       openblas-threads

%description
    Python environment for NPL proxy

%prep
    echo '[openblas]' > ~/.numpy-site.cfg
    echo 'libraries = openblasp' >> ~/.numpy-site.cfg
    echo '[mkl]' >> ~/.numpy-site.cfg
    echo 'library_dirs = %{mkl_lib_dir}' >> ~/.numpy-site.cfg
    echo 'include_dirs = /opt/intel/mkl/include/' >> ~/.numpy-site.cfg
    echo 'mkl_libs = mkl_rt' >> ~/.numpy-site.cfg
    echo 'lapack_libs = mkl_rt' >> ~/.numpy-site.cfg
    %{pyversion} -m venv %{coprbuilddir}%{venvname}
    find /opt/intel/mkl/lib/intel64/
    find /opt/intel/mkl/include/
    source /opt/intel/bin/compilervars.sh intel64
    %{coprbuilddir}%{venvname}/bin/pip install \
        --no-binary :all: --disable-pip-version-check \
        -r %{SOURCE0}
    %{coprbuilddir}%{venvname}/bin/python  -m spacy download en
    # download nltk things:
    %{coprbuilddir}%{venvname}/bin/python -c "import nltk; nltk.download('punkt', download_dir='%{coprbuilddir}%{venvname}/nltk_data');"

    # just test to import numpy lib:
    %{coprbuilddir}%{venvname}/bin/python -c "import numpy; numpy.show_config();"
    # just test to import spacy lib:
    %{coprbuilddir}%{venvname}/bin/python -c "import spacy; nlp = spacy.load('en');"


%install
    %{__mkdir} -p %{buildroot}%{coprbuilddir}
    %{__cp} -pr %{coprbuilddir}%{venvname} %{buildroot}%{coprbuilddir}%{venvname}

    %{__mkdir} -p  %{buildroot}%{mkl_lib_dir}
    %{__cp}    -pr %{mkl_lib_dir}*.so %{buildroot}%{mkl_lib_dir}

    %{__mkdir} -p  %{buildroot}/etc/ld.so.conf.d/
    echo %{mkl_lib_dir} > %{buildroot}/etc/ld.so.conf.d/mkl-intel64.conf


%files

    %{coprbuilddir}%{venvname}
    %{mkl_lib_dir}*.so
    /etc/ld.so.conf.d/mkl-intel64.conf


%clean
    %{__rm} -rf %{buildroot}


%post
    ldconfig


%postun
    ldconfig


%changelog
* Fri Oct 25 2019 Anatolii Vorona <vorona.tolik@gmail.com>
- added intel-mkl-64bit libs
- update nlp-py-venv with nlc things
- python 3.7.2 -> 3.7.4

* Fri Jan 25 2019 Anatolii Vorona <vorona.tolik@gmail.com>
- init nlp-py-venv
