# hid-fanatecff-kmod
Spec files for the kernel module hid-fanatecff [gotzl/hid-fanatecff](https://github.com/gotzl/hid-fanatecff). 

| :exclamation: | Still work-in-progress  |
|---------------|:------------------------|


## Copr Build status

Package | Build Status
------- | ------------
hid-fanatecff | [![badge](https://copr.fedorainfracloud.org/coprs/sigonze/hid-fanatecff-kmod/package/hid-fanatecff/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/sigonze/hid-fanatecff-kmod/package/hid-fanatecff/)
hid-fanatecff-kmod | [![badge](https://copr.fedorainfracloud.org/coprs/sigonze/hid-fanatecff-kmod/package/hid-fanatecff-kmod/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/sigonze/hid-fanatecff-kmod/package/hid-fanatecff-kmod/)


### Useful commands

To test rpm generation:
```
rpmbuild --undefine '_disable_source_fetch' --define "kernels $(uname -r)" -ba *.spec
```

An output example:
```
$ ls ~/rpmbuild/RPMS/x86_64/
hid-fanatecff-1.0-1.20240704git1243729.fc40.x86_64.rpm
kmod-hid-fanatecff-6.9.7-200.fc40.x86_64-1.0-1.20240704git1243729.fc40.x86_64.rpm
```

The content of the RPM files should be something like:
```
$ rpm -qpl ~/rpmbuild/RPMS/x86_64/*.rpm
/usr/lib/udev/rules.d/99-fanatec.rules
/lib/modules/6.9.7-200.fc40.x86_64/extra
/lib/modules/6.9.7-200.fc40.x86_64/extra/hid-fanatecff
/lib/modules/6.9.7-200.fc40.x86_64/extra/hid-fanatecff/hid-fanatec.ko.xz
```

Verify generated RPM dependencies:
```
$ rpm -qp --requires ~/rpmbuild/RPMS/x86_64/*.rpm

$ rpm -qp --provides ~/rpmbuild/RPMS/x86_64/*.rpm
```

Manual installation:
```
sudo dnf install ~/rpmbuild/RPMS/x86_64/*.rpm
```
