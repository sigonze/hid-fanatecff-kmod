%if 0%{?fedora}
%global debug_package %{nil}
%endif

# Build only the akmod package and no kernel module packages:
%define buildforkernels akmod

%define kmodname hid-fanatecff

%global forgeurl https://github.com/gotzl/%{kmodname}
%global tag 0.1.1
%forgemeta

Name:       %{kmodname}-kmod
Version:    %{tag}
Release:    1%{?dist}
Summary:    Kernel module for Fanatec devices
Group:      System Environment/Kernel
License:    GPL

URL:        %{forgeurl}
Source:     %{forgesource}

BuildRequires: kernel-devel
BuildRequires: kmodtool

# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }


%description
This package provides a kernel module for FANATEC driving wheels. 

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}
# Print kmodtool output for debugging purposes
kmodtool  --target %{_target_cpu}  --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%forgesetup

for kernel_version in %{?kernel_versions}; do
    mkdir -p %{_builddir}/_kmod_build_${kernel_version%%___*}
    cp * %{_builddir}/_kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions}; do
    pushd %{_builddir}/_kmod_build_${kernel_version%%___*}
    make %{?_smp_mflags} KVERSION=$(basename ${kernel_version##*___})
    popd
done

%install
for kernel_version in %{?kernel_versions}; do
    mkdir -p %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    install -p -m 0755 %{_builddir}/_kmod_build_${kernel_version%%___*}/*.ko \
        %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
done

%{?akmod_install}

%post
akmod_install


%postun
akmod_remove

%clean
rm -rf %{buildroot}

%changelog
* Fri Jul 12 2024 Sigonze <sigonze@proton.me> 0.1.1-1
- Align version with source repo
* Wed Jul 10 2024 Sigonze <sigonze@proton.me> 1.0.1
- Update to 1.0.1
* Wed Jul 3 2024 Sigonze <sigonze@proton.me> 1.0
- Initial build.
