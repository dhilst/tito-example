Name:           hellopy
Version:        0.0.3
Release:        1%{?dist}
Summary:        Testing.

License:        MIT
URL:            http://www.example.com
Source0:        hellopy.tar.gz

BuildRequires:  python3 >= 3.6, python3-setuptools, python3-rpm-macros, python-rpm-macros
Requires:       python3 >= 3.6 

%global debug_package %{nil}
%define SRC %_builddir/%{name}-%{version}

%description
Some testing software.


%prep
%setup -q

%build
python3 %SRC/setup.py bdist

%check
python3 %SRC/setup.py test

%install
%py3_install


%files
%python3_sitelib/*

%changelog
* Sun Dec 17 2017 Daniel Hist Selli <danielhilst@gmail.com> 0.0.3-1
- 

* Sun Dec 17 2017 Daniel Hist Selli <danielhilst@gmail.com> 0.0.2-1
- new package built with tito

* Sat Dec 16 2017 Daniel Hist Selli <danielhilst@gmail.com>
- 
