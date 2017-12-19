# Description

This is an reference for building and deploying with [tito](https://github.com/dgoodwin/tito) it consists of a
python hello world, mock and tito configuration files.

# Example

To run this I created a temporary repository at `/tmp/testrepo` by:

```
mkdir /tmp/testrepo
createrepo /tmp/testrepo
bash -c 'cd /tmp/testrepo; python -m SimpleHTTPServer' &
```

This will create an empty repository where `hellopy` will be automatic deployed.

# Running

```
tito release testrepo                       # Build and deploy to testrepo.
mock -r epel-7-x86_64.cfg --install hellopy # Install the package in a brand new chroot, this is for testing depencies.
```

# Demo

[![asciicast](https://asciinema.org/a/1A4Uo8Fl872Kr393VwFYmkJkF.png)](https://asciinema.org/a/1A4Uo8Fl872Kr393VwFYmkJkF)

# Configuration

- `epel-7-x86-64.cfg`: This is the same of `/etc/mock/epel-7-x86_64.cfg` with some additions.
  - `config_opts['rpmbuild_networking'] = True`: This add supports for networking on the chroot.
  - I added the `testrepo` at the end of yum repository
- `.tito/releasers.conf`: This hold the repository where tito will deploy after building. The
  repository is passed to the `tito release` command. For example `tito release testrepo`.

# References:

https://github.com/dgoodwin/tito
https://github.com/rpm-software-management/mock
https://fedoraproject.org/wiki/Using_Mock_to_test_package_builds


