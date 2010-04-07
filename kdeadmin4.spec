%define with_printer_applet 0
%{?_with_printer_applet: %{expand: %%global with_printer_applet 1}}

%define branch 0
%{?_branch: %{expand: %%global branch 1}}


%if %branch
%define kde_snapshot svn1053190
%endif

Name: kdeadmin4
Version: 4.4.2
Release: %mkrel 1
Epoch: 2
Summary: K Desktop Environment - Administrative Tools
Group: Graphical desktop/KDE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://www.kde.org
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeadmin-%version%kde_snapshot.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeadmin-%version.tar.bz2
%endif
Patch0:   kdeadmin-4.0.84-fix-menu-entries.patch
License: GPL
Requires: pciutils
BuildRequires: X11-devel 
BuildRequires: freetype2-devel 
BuildRequires: bzip2-devel 
BuildRequires: jpeg-devel 
BuildRequires: lcms-devel 
BuildRequires: mng-devel
BuildRequires: png-devel 
BuildRequires: libz-devel
BuildRequires: pam-devel
BuildRequires: libxml2-utils
BuildRequires: kdelibs4-devel >= 2:4.2.98
BuildRequires: kdelibs4-experimental-devel >= 2:4.2.98
BuildRequires: kdepimlibs4-devel >= 4.2.98
BuildRequires: python-kde4
BuildRequires: python-qt4
BuildRequires: python-devel
BuildRequires: python-cups
%if %with_printer_applet
BuildRequires: system-config-printer-libs
%else
BuildConflicts: system-config-printer-libs
%endif
Obsoletes: ksysv
Suggests: kcron
Suggests: kuser
Suggests: knetworkconf 
Suggests: ksystemlog

%if %mdkversion >= 201000
Obsoletes:    kdeadmin < 2:3.5.10-2
Obsoletes:    kdeadmin-kpackage < 2:3.5.10-2
Obsoletes:    kdeadmin-ksysv < 2:3.5.10-2
%endif

%description
The kdeadmin package contains packages that usually only a system
administrator might need:
	- kcron
    		Editor for the cron command scheduler.
	- kuser
   		An user manager.

%files
%defattr(-,root,root)
%doc README

#------------------------------------------------------------------------	

%package -n kuser
Group: Graphical desktop/KDE
Summary:  Users and groups manager
Provides: kuser4
Conflicts: kdeadmin4 < 2:4.0.1
Obsoletes: kde4-kuser < 2:4.0.68
Provides: kde4-kuser = %epoch:%version
Requires: kdebase4-runtime >= 1:%version 

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
Requires: kdebase4-runtime >= 1:%version

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
Requires: kdebase4-runtime >= 1:%version

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
%_kde_datadir/applications/kde4/ksystemlog.desktop
%_kde_docdir/*/*/ksystemlog

#------------------------------------------------------------------------	

%package -n knetworkconf
Group: Graphical desktop/KDE
Summary: KDE Control Center module to configure network
Provides: knetworkconf4
Conflicts: kdeadmin4 < 2:4.0.1
Obsoletes: kde4-knetworkconf < 2:4.0.68
Provides: kde4-knetworkconf = %epoch:%version
Requires: kdebase4-runtime >= 1:%version

%description -n knetworkconf
KNetworkConf is a KDE Control Center module to configure TCP/IP settings on a 
Linux machine.

%files -n knetworkconf
%defattr(-,root,root)
%_kde_datadir/kde4/services/kcm_knetworkconfmodule.desktop
%_kde_libdir/kde4/kcm_knetworkconfmodule.so
%_kde_appsdir/knetworkconf
%_kde_docdir/*/*/kcontrol/knetworkconf
%_kde_iconsdir/*/*/*/knetworkconf*
%_kde_iconsdir/*/*/*/networ*

#------------------------------------------------------------------------
%if %with_printer_applet
%package system-config-printer-kde
Summary: View current print jobs and configure new printers
Group: Graphical desktop/KDE
URL: http://utils.kde.org/projects/printer-applet
Requires: %name-core = %version
Requires: python-kde4 >= 1:4.1.0
Requires: python-cups
Requires: python-qt4
Requires: python-dbus
Requires: printer-applet
Requires: kdebase4-runtime >= 1:%version

%description system-config-printer-kde
Printer Applet is a system tray utility that shows current print jobs,
shows printer warnings and errors and shows when printers that have
been plugged in for the first time are being auto-configured by
hal-cups-utils.

%files system-config-printer-kde
%defattr(-,root,root)
%_kde_datadir/kde4/services/system-config-printer-kde.desktop
%_kde_appsdir/system-config-printer-kde
%endif
#------------------------------------------------------------------------

%prep
%if %branch
%setup -q -n kdeadmin-%version%kde_snapshot
%else
%setup -q -n kdeadmin-%version
%endif
%patch0 -p0

%build
%cmake_kde4 
%make

%install
rm -fr %buildroot
%makeinstall_std -C build

%clean
rm -fr %buildroot

