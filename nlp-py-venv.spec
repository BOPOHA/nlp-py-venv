%global		debug_package       %{nil}
%global     __os_install_post   %{nil}
%define		venvname            venv
%define		coprbuilddir        /builddir/
%define     pyversion           python37

Name:		nlp-py-venv
Version:	1.0.3
Release:	1%{?dist}
Summary:	Python environment for NLP proxy

License:	MIT
Source0:    requirements.txt

BuildRequires:  %{pyversion}-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
Requires:       %{pyversion}

%description
    Python environment for NPL proxy

%prep
    %{pyversion} -m venv %{coprbuilddir}%{venvname}
    %{coprbuilddir}%{venvname}/bin/pip install --no-binary :all: -r %{SOURCE0}
    %{coprbuilddir}%{venvname}/bin/python  -m spacy download en

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
* Fri Jan 25 2019 Anatolii Vorona <vorona.tolik@gmail.com>
- init nlp-py-venv
