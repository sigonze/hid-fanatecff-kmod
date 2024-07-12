%if 0%{?fedora}
%global debug_package %{nil}
%endif

%define kmodname hid-fanatecff

%global forgeurl https://github.com/gotzl/%{kmodname}
%global tag 0.1.1
%forgemeta

Name:       %{kmodname}
Version:    %{tag}
Release:    1%{?dist}
Summary:    udev rules for Fanatec devices
Group:      System Environment/Kernel
License:    GPL

URL:        %{forgeurl}
Source:     %{forgesource}

# add linuxconsoletools for evdev-joystick commands
Requires: linuxconsoletools

BuildRequires: pkgconfig(udev)

Requires: %{name}-kmod >= %{version}


%description
This package provides udev rules for FANATEC devices 

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
* Fri Jul 12 2024 Sigonze <sigonze@proton.me> 0.1.1-1
- Align version with source repo
* Wed Jul 10 2024 Sigonze <sigonze@proton.me> 1.0.1
- Update to 1.0.1
* Wed Jul 3 2024 Sigonze <sigonze@proton.me> 1.0
- Initial build.