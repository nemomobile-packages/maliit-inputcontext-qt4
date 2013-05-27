# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       maliit-qt4

# >> macros
# << macros

Summary:    Qt4 support for Maliit
Version:    0.99.0+git1.6948f2e52c45c5
Release:    1
Group:      System/Libraries
License:    LGPLv2.1
URL:        http://gitorious.org/maliit/maliit-inputcontext-qt4
Source0:    %{name}-%{version}.tar.bz2
Source100:  maliit-qt4.yaml
Requires:   dbus-x11
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Obsoletes:   maliit-framework < 0.99

%description
Qt4 support for Maliit 1.0, including libmaliit and Qt4 input context


%package devel
Summary:    Maliit Framework Input Method library development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for the additional Maliit API library


%package tests
Summary:    Maliit Qt4 Tests Package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description tests
Tests for Maliit Qt4 integration


%prep
%setup -q -n %{name}-%{version}/maliit-inputcontext-qt4

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/qt4/plugins/inputmethods/libmaliit-qt4.so
%{_libdir}/libmaliit-1.0.so*
%{_libdir}/libmaliit-connection.so*
%{_libdir}/libmaliit-settings.so*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_includedir}/maliit-qt4/
%{_libdir}/pkgconfig/*
# >> files devel
# << files devel

%files tests
%defattr(-,root,root,-)
%{_libdir}/maliit-framework-tests/
# >> files tests
# << files tests
