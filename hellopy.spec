Name:           hellopy
Version:        0.0.6
Release:        1%{?dist}
Summary:        Testing.

License:        MIT
URL:            http://www.example.com
Source0:        hellopy-%{version}.tar.gz

BuildRequires:  python2, python2-setuptools, python-rpm-macros, python2-rpm-macros
Requires:       python2

%global debug_package %{nil}
%define SRC %_builddir/%{name}-%{version}

%description
Some testing software.

%prep
%setup -q

%build
python2 %SRC/setup.py bdist

%check
python2 %SRC/setup.py test

%install
%py2_install


%files
%python2_sitelib/*

%changelog
* Sun Dec 17 2017 Daniel Hist Selli <danielhilst@gmail.com> 0.0.6-1
- 

* Sun Dec 17 2017 Daniel Hist Selli <danielhilst@gmail.com> 0.0.5-1
- Update spec (danielhilst@gmail.com)
- Port to python2 (danielhilst@gmail.com)

* Sun Dec 17 2017 Daniel Hist Selli <danielhilst@gmail.com> 0.0.4-1
- Fix spec (danielhilst@gmail.com)

* Sun Dec 17 2017 Daniel Hist Selli <danielhilst@gmail.com> 0.0.3-1
- 

* Sun Dec 17 2017 Daniel Hist Selli <danielhilst@gmail.com> 0.0.2-1
- new package built with tito

* Sat Dec 16 2017 Daniel Hist Selli <danielhilst@gmail.com>
- 
