Name: kdeadmin4
Version: 4.0.81
Group: Graphical desktop/KDE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary: K Desktop Environment - Administrative Tools
URL: ftp://ftp.kde.org/pub/kde/stable/%version/src/
Epoch: 2
Release: %mkrel 1
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeadmin-%version.tar.bz2
Source1: kpackage.pamd
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
BuildRequires: kdelibs4-devel >= %version
BuildRequires: kdepimlibs4-devel >= %version
%ifarch %{ix86} x86_64
BuildRequires:	lilo
%endif
Obsoletes: ksysv
Requires: kcron
Requires: kuser
Requires: kpackage
Requires: knetworkconf 

%description
The kdeadmin package contains packages that usually only a system
administrator might need:
	- kcron
    	Editor for the cron command scheduler.
	- kdat
   		Tape backup tool.
	- kfile-plugins
    	Make Konqueror display additional info on about *.dep and *.rpm files.
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

%package -n kuser
Group:      Graphical desktop/KDE
Summary:    Users and groups manager
Provides:   kuser4
Conflicts:  kdeadmin4 < 2:4.0.1
Obsoletes: kde4-kuser < 2:4.0.68
Provides: kde4-kuser = %epoch:%version

%description -n kuser
Kuser is a tool to create, remove and modify user accounts and groups.

%files -n kuser
%defattr(-,root,root)
%_kde_bindir/kuser
%_kde_datadir/applications/kde4/kuser.desktop
%_kde_datadir/apps/kuser
%_kde_datadir/config.kcfg/kuser.kcfg
%_kde_docdir/*/*/kuser
%_kde_iconsdir/*/*/*/kuser*

#------------------------------------------------------------------------	

%package -n kcron
Group:      Graphical desktop/KDE
Summary:    Graphical task scheduler
Provides:   kcron4
Conflicts:  kdeadmin4 < 2:4.0.1
Obsoletes: kde4-kcron < 2:4.0.68
Provides: kde4-kcron = %epoch:%version

%description -n kcron
Kcron is a graphical frontend to the cron system, used to schedule regular 
tasks on a Unix system.

%files -n kcron
%defattr(-,root,root)
%_kde_datadir/kde4/services/kcm_cron.desktop
%_kde_libdir/kde4/kcm_cron.so
%_kde_docdir/*/*/kcron

#------------------------------------------------------------------------

%package -n ksystemlog
Group:      Graphical desktop/KDE
Summary:    System log viewer tool for KDE 4
Provides:   ksystemlog4

%description -n ksystemlog
This program is developed for being used by beginner users,
which don't know how to find information about their Linux system,
and how the log files are in their computer.
But it is also designed for advanced users,
who want to quickly see problems occuring on their server.

KSystemLog has the following features :

- View all the main log of your system, by selecting them
 directly in a menu
 - Auto display new lines logged in bold
 - Tabbed view to allow displaying several logs at the same time
 - Saving in a file and copying to clipboard the selected log
   lines are also implemented (and email to your friends)
   - It can parse the following log files of your system :

   - X.org (or Xfree) logs
   - System logs (using the Syslog parser of KSystemLog)
   - Kernel logs
   - Daemons logs
   - Cron logs
   - Boot logs
   - Authentication logs
   - Cups logs
   - ACPID logs

%files -n ksystemlog
%defattr(-,root,root)
%_kde_bindir/ksystemlog
%_kde_appsdir/ksystemlog
%_kde_iconsdir/hicolor/*/apps/ksystemlog.*
%_kde_datadir/applications/kde4/ksystemlog.desktop
%_kde_docdir/*/*/ksystemlog

#------------------------------------------------------------------------	

%package -n knetworkconf
Group:      Graphical desktop/KDE
Summary:    KDE Control Center module to configure network
Provides:   knetworkconf4
Conflicts:  kdeadmin4 < 2:4.0.1
Obsoletes: kde4-knetworkconf < 2:4.0.68
Provides: kde4-knetworkconf = %epoch:%version

%description -n knetworkconf
KNetworkConf is a KDE Control Center module to configure TCP/IP settings on a 
Linux machine.

%files -n knetworkconf
%defattr(-,root,root)
%_kde_datadir/kde4/services/kcm_knetworkconfmodule.desktop
%_kde_libdir/kde4/kcm_knetworkconfmodule.so
%_kde_appsdir/knetworkconf
%_kde_docdir/*/*/knetworkconf
%_kde_iconsdir/*/*/*/knetworkconf*
%_kde_iconsdir/*/*/*/networ*

#------------------------------------------------------------------------	

%ifarch %{ix86} x86_64
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

%package -n kpackage
Group: Graphical desktop/KDE
Summary:Manager for DEB, RPM
Obsoletes: %name-kpackage
Conflicts:  kdeadmin4 < 2:4.0.1
Obsoletes: kde4-kpackage < 2:4.0.68
Provides: kde4-kpackage = %epoch:%version

%description -n kpackage
Kpackage is a package manager that is integrated into the K Desktop 
Environement. It works with the KDE File Manager to manage DEB, RPM 
and Slackware tgz software packages.

%files -n kpackage
%defattr(-,root,root)
%_kde_bindir/kpackage
%config(noreplace) %_sysconfdir/pam.d/kpackage
%_kde_iconsdir/*/*/*/kpackage*
%_kde_datadir/applications/kde4/kpackage.desktop
%_kde_datadir/config.kcfg/kpackageSettings.kcfg
%_kde_appsdir/kpackage
%_kde_docdir/*/*/kpackage
%exclude %_kde_libdir/pkgconfig/system-tools-backends.pc

#------------------------------------------------------------------------	

%prep
%setup -q -n kdeadmin-%version

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

