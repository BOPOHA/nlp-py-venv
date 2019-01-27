%global		debug_package       %{nil}
%global     __os_install_post   %{nil}
%define		venvname            venv
%define		coprbuilddir        /builddir/

Name:		nlp-py-venv
Version:	1.0.1
Release:	1%{?dist}
Summary:	Python environment for NLP proxy

License:	MIT
Source0:    requirements.txt

BuildRequires:  python36-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
Requires:       python36

%description
    Python environment for NPL proxy

%prep
    python36 -m venv %{coprbuilddir}%{venvname}
    %{coprbuilddir}%{venvname}/bin/pip install --no-binary :all: -r %{SOURCE0}

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
