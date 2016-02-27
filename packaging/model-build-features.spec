%define release_prefix 1

Name:       model-build-features
Summary:    Model Build Feature configuration file for optimize packages-listing
Version:    0.1
Release:    %{release_prefix}
Group:      Development/System
Source:     %{name}-%{version}.tar.gz
License:    Apache-2.0
URL:        http://www.tizen.org
BuildArch:  noarch

%description
Model Build Feature configuration file for optimize packages-listing

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/rpm/
cp default/macros.modelbuildfeatures.default  default/macros.modelbuildfeatures
%if "%{profile}" == "mobile"
cp default/macros.modelbuildfeatures.tm1  default/macros.modelbuildfeatures
%if "%{_repository}" == "emulator32-wayland"
cp default/macros.modelbuildfeatures.emulatorM  default/macros.modelbuildfeatures
%endif
%else
%if "%{profile}" == "wearable"
cp default/macros.modelbuildfeatures.tw1  default/macros.modelbuildfeatures
%if "%{_repository}" == "emulator-circle"
cp default/macros.modelbuildfeatures.emulatorW  default/macros.modelbuildfeatures
%endif
%endif
%endif

install -m 644 default/macros.modelbuildfeatures %{buildroot}%{_sysconfdir}/rpm

%files
%defattr(-,root,root,-)
%{_sysconfdir}/rpm/macros.modelbuildfeatures

