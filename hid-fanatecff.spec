%if 0%{?fedora}
%global debug_package %{nil}
%endif

%global forgeurl https://github.com/gotzl/hid-fanatecff
%global commit 124372964d81ab71b4dc54858c746f1fe3621dbe
%forgemeta

Name:       hid-fanatecff
Version:    1.0.1
Release:    1%{?dist}
Summary:    Kernel module for Fanatec devices
Group:      System Environment/Kernel
License:    GPL

URL:        %{forgeurl}
Source:     %{forgesource}

# add linuxconsoletools for evdev-joystick commands
Requires: linuxconsoletools

BuildRequires: pkgconfig(udev)

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}


%description
This package provides a driver for FANATEC driving wheels. 

%prep
%forgeautosetup


%install
install -d %{buildroot}%{_udevrulesdir}
install -m 0644 %{_builddir}/%{topdir}/fanatec.rules %{buildroot}%{_udevrulesdir}/99-fanatec.rules

%files
%{_udevrulesdir}/99-fanatec.rules

%post
# Reload udev rules after installation
/sbin/udevadm control --reload-rules
/sbin/udevadm trigger

%postun
if [ $1 -eq 0 ]; then
    # Reload udev rules after uninstallation
    /sbin/udevadm control --reload-rules
    /sbin/udevadm trigger
fi

%clean
rm -rf %{buildroot}

%changelog
* Wed Jul 10 2024 Sigonze <sigonze@proton.me> 1.0.1
- Update to 1.0.1
* Wed Jul 3 2024 Sigonze <sigonze@proton.me> 1.0
- Initial build.
