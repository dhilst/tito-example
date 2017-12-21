Name:           hellopy
Version:        0.0.10
Release:        1%{?dist}
Summary:        Testing.

License:        MIT
URL:            http://www.example.com
Source0:        hellopy-%{version}.tar.gz
Source1:        http://localhost:8000/macros.foo

BuildRequires:  python2, python2-setuptools, python-rpm-macros, python2-rpm-macros
Requires:       python2

%global debug_package %{nil}
%define SRC %_builddir/%{name}-%{version}\*

%include %{SOURCE1}

%description
Some testing software.

%prep
%setup -q

%build
echo %foo
python2 setup.py bdist

%check
python2 setup.py test

%install
%py2_install


%files
%python2_sitelib/*

%changelog
* Mon Dec 18 2017 Daniel Hilst Selli <daniel@versatushpc.com.br> 0.0.10-1
- Add config and releasers (daniel@versatushpc.com.br)

* Mon Dec 18 2017 Daniel Hilst Selli <daniel@versatushpc.com.br> 0.0.9-1
- 

* Mon Dec 18 2017 Daniel Hilst Selli <daniel@versatushpc.com.br> 0.0.8-1
- Update autodock.spec (daniel@versatushpc.com.br)

* Mon Dec 18 2017 Daniel Hilst Selli <daniel@versatushpc.com.br> 0.0.7-1
- Update autodock.spec (daniel@versatushpc.com.br)
- Update autodock.spec (daniel@versatushpc.com.br)
- Add README. (danielhilst@gmail.com)

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
