Name:           hellopy
Version:        0.0.12
Release:        1%{?dist}
Summary:        Testing.

License:        MIT
URL:            http://www.example.com
Source0:        hellopy-%{version}.tar.gz

BuildRequires:  python2, python2-setuptools, python-rpm-macros, python2-rpm-macros
Requires:       python2

%global debug_package %{nil}

%description
Some testing software.


%prep
%setup -q

%build
python2 setup.py bdist

%check
python2 setup.py test

%install
%py2_install


%files
%python2_sitelib/*
%{_bindir}/hello

%changelog
* Tue Jun 19 2018 Daniel Hilst Selli <daniel@gmail.com> 0.0.12-1
- 

* Mon Jun 18 2018 Daniel Hilst Selli <daniel@gmail.com> 0.0.11-1
- Add bin/hello script to spec %%files (daniel@gmail.com)
- Add bin/hello. (daniel@gmail.com)
- Testing (daniel@gmail.com)
- Update spec (daniel@versatushpc.com.br)
- Update spec (daniel@versatushpc.com.br)
- Update spec. (daniel@versatushpc.com.br)
- Update spec. (daniel@versatushpc.com.br)
- Update macros. (daniel@versatushpc.com.br)
- Update spec. (daniel@versatushpc.com.br)
- Update spec. (daniel@versatushpc.com.br)
- Update spec (daniel@versatushpc.com.br)
- Update spec (daniel@versatushpc.com.br)
- Update spec (daniel@versatushpc.com.br)
- Update spec (daniel@versatushpc.com.br)
- Update spec (daniel@versatushpc.com.br)
- Update spec (daniel@versatushpc.com.br)
- Update spec (daniel@versatushpc.com.br)
- Update spec (daniel@versatushpc.com.br)
- Rename macros.foo (daniel@versatushpc.com.br)
- Update spec (daniel@versatushpc.com.br)
- Update spec (daniel@versatushpc.com.br)
- Try %%include (daniel@versatushpc.com.br)
- Revert "Update README.md" (daniel@versatushpc.com.br)
- Update README.md (daniel@versatushpc.com.br)
- Update README.md (daniel@versatushpc.com.br)
- Add testrepo (daniel@versatushpc.com.br)
- Update README.md (daniel@versatushpc.com.br)

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
