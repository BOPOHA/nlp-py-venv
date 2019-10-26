%global		debug_package       %{nil}
%global     __os_install_post   %{nil}
%define		venvname            venv
%define		coprbuilddir        /builddir/
%if 0%{?rhel}  == 7
%define     pyversion           python37
%else
%define     pyversion           python3
%endif

Name:		nlp-py-venv
Version:	1.0.12
Release:	1%{?dist}
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
BuildRequires:  python37-Cython
Requires:       %{pyversion}
Requires:       openblas-threads

%description
    Python environment for NPL proxy

%prep
    echo '[openblas]' > ~/.numpy-site.cfg
    echo 'libraries = openblasp' >> ~/.numpy-site.cfg
    %{pyversion} -m venv --system-site-packages %{coprbuilddir}%{venvname}
    #%{coprbuilddir}%{venvname}/bin/pip install --no-binary :all: --disable-pip-version-check Cython==0.29.13
    %{coprbuilddir}%{venvname}/bin/pip install --no-binary :all: --disable-pip-version-check -r %{SOURCE0}
    %{coprbuilddir}%{venvname}/bin/python  -m spacy download en
    # download nltk things:
    %{coprbuilddir}%{venvname}/bin/python -c "import nltk; nltk.download('punkt');"

    # just test to import numpy lib:
    %{coprbuilddir}%{venvname}/bin/python -c "import numpy; numpy.show_config();"
    # just test to import spacy lib:
    %{coprbuilddir}%{venvname}/bin/python -c "import spacy; nlp = spacy.load('en');"


%install
    %{__mkdir} -p %{buildroot}%{coprbuilddir}
    %{__cp} -pr %{coprbuilddir}%{venvname} %{buildroot}%{coprbuilddir}%{venvname}

%files

    %{coprbuilddir}%{venvname}

%clean
    %{__rm} -rf %{buildroot}

%changelog
* Fri Oct 25 2019 Anatolii Vorona <vorona.tolik@gmail.com>
- update nlp-py-venv with nlc things
- python 3.7.2 -> 3.7.4

* Fri Jan 25 2019 Anatolii Vorona <vorona.tolik@gmail.com>
- init nlp-py-venv
