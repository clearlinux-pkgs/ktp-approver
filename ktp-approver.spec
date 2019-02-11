#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : ktp-approver
Version  : 18.12.2
Release  : 3
URL      : https://download.kde.org/stable/applications/18.12.2/src/ktp-approver-18.12.2.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.2/src/ktp-approver-18.12.2.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.2/src/ktp-approver-18.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1
Requires: ktp-approver-data = %{version}-%{release}
Requires: ktp-approver-lib = %{version}-%{release}
Requires: ktp-approver-license = %{version}-%{release}
Requires: ktp-approver-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : telepathy-qt-dev

%description
No detailed description available

%package data
Summary: data components for the ktp-approver package.
Group: Data

%description data
data components for the ktp-approver package.


%package lib
Summary: lib components for the ktp-approver package.
Group: Libraries
Requires: ktp-approver-data = %{version}-%{release}
Requires: ktp-approver-license = %{version}-%{release}

%description lib
lib components for the ktp-approver package.


%package license
Summary: license components for the ktp-approver package.
Group: Default

%description license
license components for the ktp-approver package.


%package locales
Summary: locales components for the ktp-approver package.
Group: Default

%description locales
locales components for the ktp-approver package.


%prep
%setup -q -n ktp-approver-18.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549906401
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549906401
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ktp-approver
cp COPYING %{buildroot}/usr/share/package-licenses/ktp-approver/COPYING
cp cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/ktp-approver/cmake_modules_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd
%find_lang kded_ktp_approver

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.Approver.service
/usr/share/kservices5/kded/ktp_approver.desktop
/usr/share/kservicetypes5/ktp-approver.desktop
/usr/share/xdg/ktp_approverrc

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kded_ktp_approver.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ktp-approver/COPYING
/usr/share/package-licenses/ktp-approver/cmake_modules_COPYING-CMAKE-SCRIPTS

%files locales -f kded_ktp_approver.lang
%defattr(-,root,root,-)

