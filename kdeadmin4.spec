Name: kdeadmin4
Version: 4.0.1
Group: Graphical desktop/KDE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary: K Desktop Environment - Adminstrative Tools
URL: ftp://ftp.kde.org/pub/kde/stable/%version/src/
Epoch: 2
Release: %mkrel 2
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeadmin-%version.tar.bz2
Source1: kpackage.pamd
Patch0: kdeadmin-post-4.0.1-knetworkconf-mandriva.patch
License: GPL
Requires: pciutils
BuildRequires: X11-devel 
BuildRequires: freetype2-devel 
BuildRequires: bzip2-devel 
BuildRequires: jpeg-devel 
BuildRequires: lcms-devel 
BuildRequires: mng-devel
BuildRequires: png-devel 
BuildRequires: rpm-devel 
BuildRequires: libz-devel
BuildRequires: pam-devel
BuildRequires: libxml2-utils
BuildRequires: kdelibs4-devel
BuildRequires: kdepimlibs4-devel
%ifarch %{ix86} x86_64
BuildRequires:	lilo
%endif
Obsoletes: kde4-ksysv
Requires: kde4-kcron
Requires: kde4-kuser
Requires: kde4-kpackage
Requires: kde4-knetworkconf 

%description
The kdeadmin package contains packages that usually only a system
administrator might need:
	- kcron
    	Editor for the cron command scheduler.
	- kdat
   		Tape backup tool.
	- kfile-plugins
    	Make Konquerer display additional info on about *.dep and *.rpm files.
	- ksysv
    	An editor for System V startup schemes.
	- kuser
   		An user manager.
	- lilo-config
    	A plugin for KControl to manage the Linux boot loader LILO.
	- secpolicy
    	A program to display PAM security policies.

%files
%defattr(-,root,root)
%doc README

#------------------------------------------------------------------------	

%package -n kde4-kuser
Group:      Graphical desktop/KDE
Summary:    kde4 kuser
Provides:   kuser4
Conflicts:  kdeadmin4 < 2:4.0.1

%description -n kde4-kuser
Kde4 kuser.

%files -n kde4-kuser
%defattr(-,root,root)
%_kde_bindir/kuser
%_kde_datadir/applications/kde4/kuser.desktop
%_kde_datadir/apps/kuser
%_kde_datadir/config.kcfg/kuser.kcfg
%_kde_docdir/*/*/kuser
%_kde_iconsdir/*/*/*/kuser*

#------------------------------------------------------------------------	

%package -n kde4-kcron
Group:      Graphical desktop/KDE
Summary:    kde4 kcron
Provides:   kcron4
Conflicts:  kdeadmin4 < 2:4.0.1

%description -n kde4-kcron
Kde4 kcron.

%files -n kde4-kcron
%defattr(-,root,root)
%_kde_datadir/applications/kde4/kcron.desktop
%_kde_bindir/kcron
%_kde_bindir/secpolicy
%_kde_datadir/apps/kcron
%_kde_docdir/*/*/kcron
%_kde_iconsdir/*/*/*/kcron*

#------------------------------------------------------------------------	

%package -n kde4-knetworkconf
Group:      Graphical desktop/KDE
Summary:    kde4 knetworkconf
Provides:   knetworkconf4
Conflicts:  kdeadmin4 < 2:4.0.1

%description -n kde4-knetworkconf
Kde4 knetworkconf.

%files -n kde4-knetworkconf
%defattr(-,root,root)
%_kde_datadir/kde4/services/kcm_knetworkconfmodule.desktop
%_kde_libdir/kde4/kcm_knetworkconfmodule.so
%_kde_datadir/apps/knetworkconf
%_kde_docdir/*/*/knetworkconf
%_kde_iconsdir/*/*/*/knetworkconf*
%_kde_iconsdir/*/*/*/networ*

#------------------------------------------------------------------------	

%ifnarch ppc
%package -n kde4-lilo
Group:      Graphical desktop/KDE
Summary:    Configure lilo
Obsoletes:  %name-lilo
Conflicts:  kdeadmin4 < 2:4.0.1

%description -n kde4-lilo
lilo-config is a kcontrol plugin for configuring LILO, the most commonly
used Linux boot loader.

%post -n kde4-lilo -p /sbin/ldconfig

%postun -n kde4-lilo -p /sbin/ldconfig

%files -n kde4-lilo
%defattr(-,root,root)
%_kde_libdir/kde4/kcm_lilo.so
%_kde_docdir/*/*/lilo-config
%_kde_datadir/kde4/services/lilo.desktop

%endif

#------------------------------------------------------------------------	

%package -n kde4-kpackage
Group: Graphical desktop/KDE
Summary:Manager for DEB, RPM
Obsoletes: %name-kpackage
Conflicts:  kdeadmin4 < 2:4.0.1

%description -n kde4-kpackage
Kpackage is a package manager that is integrated into the K Desktop 
Environemnt.  It works with the KDE File Manager to manage DEB, RPM 
and Slackware tgz software packages.

%files -n kde4-kpackage
%defattr(-,root,root)
%_kde_bindir/kpackage
%config(noreplace) %_sysconfdir/pam.d/kpackage
%_kde_iconsdir/*/*/*/kpackage*
%_kde_datadir/applications/kde4/kpackage.desktop
%_kde_datadir/config.kcfg/kpackageSettings.kcfg
%_kde_datadir/apps/kpackage
%_kde_docdir/*/*/kpackage
%exclude %_kde_libdir/pkgconfig/system-tools-backends.pc

#------------------------------------------------------------------------	

%prep
%setup -q -n kdeadmin-%version
%patch0 -p0

%build
%cmake_kde4 

%make

%install
rm -fr %buildroot

make -C build DESTDIR=%buildroot install

# Install kdebase pam configuration file
install -d %buildroot/%_sysconfdir/pam.d
install -m644 %SOURCE1 %buildroot/%_sysconfdir/pam.d/kpackage

%clean
rm -fr %buildroot

