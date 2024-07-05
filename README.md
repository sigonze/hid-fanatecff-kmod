# hid-fanatecff-kmod

:exclamation: | Still under development
------------- | -----------------------

Spec files for the kernel module hid-fanatecff [gotzl/hid-fanatecff](https://github.com/gotzl/hid-fanatecff). 
Add Linux kernel driver for FANATEC devices.

## Installation

dnf
```
sudo dnf copr enable sigonze/hid-fanatecff-kmod
sudo dnf install hid-fanatecff
```

:exclamation: rpm-ostree (NOT WORKING needs to be adapted)
```
sudo wget "https://copr.fedorainfracloud.org/coprs/sigonze/hid-fanatecff-kmod/repo/fedora-$(rpm -E %fedora)/sigonze-hid-fanatecff-fedora-$(rpm -E %fedora).repo" -O /etc/yum.repos.d/_copr_sigonze-hid-fanatecff-kmod.repo
sudo rpm-ostree install hid-fanatecff
```

## Copr Build status

Package | Build Status
------- | ------------
hid-fanatecff | [![badge](https://copr.fedorainfracloud.org/coprs/sigonze/hid-fanatecff-kmod/package/hid-fanatecff/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/sigonze/hid-fanatecff-kmod/package/hid-fanatecff/)
hid-fanatecff-kmod | [![badge](https://copr.fedorainfracloud.org/coprs/sigonze/hid-fanatecff-kmod/package/hid-fanatecff-kmod/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/sigonze/hid-fanatecff-kmod/package/hid-fanatecff-kmod/)


## Useful commands for testing

How to test
```
mkdir -p ~/rpmbuild/SOURCES
rpmbuild --undefine '_disable_source_fetch' --define "kernels $(uname -r)" -bs *.spec
mock --enable-network -r fedora-rawhide-x86_64 --rebuild --resultdir=/tmp/mockbuild/ ~/rpmbuild/SRPMS/hid-fanatecff-*.src.rpm
```

Generate RPM files:
```
rpmbuild --undefine '_disable_source_fetch' --define "kernels $(uname -r)" -ba *.spec
```

Verify the generated files:
```
$ ls ~/rpmbuild/RPMS/x86_64/
hid-fanatecff-1.0-1.20240704git1243729.fc40.x86_64.rpm
kmod-hid-fanatecff-6.9.7-200.fc40.x86_64-1.0-1.20240704git1243729.fc40.x86_64.rpm
```

Check files content:
```
$ rpm -qpl ~/rpmbuild/RPMS/x86_64/*.rpm
/usr/lib/udev/rules.d/99-fanatec.rules
/lib/modules/6.9.7-200.fc40.x86_64/extra
/lib/modules/6.9.7-200.fc40.x86_64/extra/hid-fanatecff
/lib/modules/6.9.7-200.fc40.x86_64/extra/hid-fanatecff/hid-fanatec.ko.xz
```

Verify dependencies:
```
$ rpm -qp --requires ~/rpmbuild/RPMS/x86_64/*.rpm
$ rpm -qp --provides ~/rpmbuild/RPMS/x86_64/*.rpm
```

Manual installation:
```
sudo dnf install ~/rpmbuild/RPMS/x86_64/*.rpm
```
