%global		debug_package       %{nil}
%global     __os_install_post   %{nil}
%global     __python3           python37
%define		venvname            venv
%define		coprbuilddir        /builddir/
%if 0%{?rhel}  == 7
%define     pyversion           python37
%else
%define     pyversion           python3
%endif

Name:		nlp-py-venv
Version:	1.0.18
Release:	2%{?dist}
Summary:	Python environment for NLP proxy

License:	MIT
Source0:    requirements.txt

AutoReqProv: no
BuildRequires:  %{pyversion}-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openblas-devel

BuildRequires:  %{pyversion}-Cython

Requires:       %{pyversion}
Requires:       openblas-threads

%description
    Python environment for NPL proxy

%prep
    %{pyversion} -m venv %{coprbuilddir}%{venvname}
    %{coprbuilddir}%{venvname}/bin/pip install \
        --disable-pip-version-check \
        -r %{SOURCE0}
    %{coprbuilddir}%{venvname}/bin/python  -m spacy download en
    # download nltk things:
    %{coprbuilddir}%{venvname}/bin/python -c "import nltk; nltk.download('punkt', download_dir='%{coprbuilddir}%{venvname}/nltk_data');"

    # just test to import numpy lib:
    %{coprbuilddir}%{venvname}/bin/python -c "import numpy; numpy.show_config();"
    # just test to import spacy lib:
    %{coprbuilddir}%{venvname}/bin/python -c "import spacy; nlp = spacy.load('en');"
    # just test nltk's 'punkt' resource
    %{coprbuilddir}%{venvname}/bin/python -c 'from nltk import sent_tokenize as st; st("This is a sentence. This is another.")'

%install
    %{__mkdir} -p %{buildroot}%{coprbuilddir}
    %{__cp} -pr %{coprbuilddir}%{venvname} %{buildroot}%{coprbuilddir}%{venvname}

%files

    %{coprbuilddir}%{venvname}

%clean
    %{__rm} -rf %{buildroot}

%changelog
* Fri Oct 25 2019 Anatolii Vorona <vorona.tolik@gmail.com>
- disable building with no-binary :all:
- update nlp-py-venv with nlc things
- python 3.7.2 -> 3.7.4

* Fri Jan 25 2019 Anatolii Vorona <vorona.tolik@gmail.com>
- init nlp-py-venv
