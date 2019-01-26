%global		debug_package       %{nil}
%global     __os_install_post   %{nil}
%define		venvname            venv

Name:		nlp-py-venv
Version:	1.0.0
Release:	1%{?dist}
Summary:	Python environment for NLP proxy

License:	MIT
Source0:    requirements.txt

BuildRequires:  python36-devel
BuildRequires:  gcc
Requires:       python36

%description
    Python environment for NPL proxy

%prep
    python36 -m venv %{venvname}
    %{venvname}/bin/pip install -r %{SOURCE0}

%install
    %{__cp} -pr %{_builddir}/%{venvname} %{buildroot}/%{venvname}

%files

    /%{venvname}

%clean
    %{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Fri Jan 25 2019 Anatolii Vorona <vorona.tolik@gmail.com>
- init nlp-py-venv
