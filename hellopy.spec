Name:           hellopy
Version:        0.0.4
Release:        1%{?dist}
Summary:        Testing.

License:        MIT
URL:            http://www.example.com
Source0:        hellopy-%{version}.tar.gz

BuildRequires:  python3, python3-setuptools, python2-setuptools, python-rpm-macros, python3-rpm-macros, python2-rpm-macros
Requires:       python3, python2

%global debug_package %{nil}
%define SRC %_builddir/%{name}-%{version}

%description
Some testing software.

%prep
%setup -q

%build
python2 %SRC/setup.py bdist
python3 %SRC/setup.py bdist

%check
python2 %SRC/setup.py test
python3 %SRC/setup.py test

%install
%py2_install
%py3_install


%files
%python2_sitelib/*
%python3_sitelib/*

%changelog
* Sun Dec 17 2017 Daniel Hist Selli <danielhilst@gmail.com> 0.0.4-1
- Fix spec (danielhilst@gmail.com)

* Sun Dec 17 2017 Daniel Hist Selli <danielhilst@gmail.com> 0.0.3-1
- 

* Sun Dec 17 2017 Daniel Hist Selli <danielhilst@gmail.com> 0.0.2-1
- new package built with tito

* Sat Dec 16 2017 Daniel Hist Selli <danielhilst@gmail.com>
- 
