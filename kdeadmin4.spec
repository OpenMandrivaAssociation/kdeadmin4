%define with_printer_applet 1
%{?_with_printer_applet: %{expand: %%global with_printer_applet 1}}

Name:		kdeadmin4
Version: 4.9.2
Release: 1
Epoch:		2
Summary:	K Desktop Environment - Administrative Tools
Group:		Graphical desktop/KDE
URL:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdeadmin-%{version}.tar.xz
License:	GPL
Requires:	pciutils
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	python-kde4-devel
BuildRequires:	python-qt4
BuildRequires:	python-devel
BuildRequires:	python-cups
%if %{with_printer_applet}
BuildRequires:	system-config-printer-libs
%else
BuildConflicts:	system-config-printer-libs
%endif
BuildRequires:	automoc4
Suggests:	kcron
Suggests:	kuser
Suggests:	ksystemlog

%description
The kdeadmin package contains packages that usually only a system
administrator might need:
	- kcron
		Editor for the cron command scheduler.
	- kuser
		An user manager.

%files
%doc README

#------------------------------------------------------------------------

%package -n kuser
Group:		Graphical desktop/KDE
Summary:	Users and groups manager
Provides:	kuser4
Provides:	kde4-kuser = %{EVRD}

%description -n kuser
Kuser is a tool to create, remove and modify user accounts and groups.

%files -n kuser
%{_kde_bindir}/kuser
%{_kde_applicationsdir}/kuser.desktop
%{_kde_appsdir}/kuser
%{_kde_datadir}/config.kcfg/kuser.kcfg
%{_kde_docdir}/*/*/kuser
%{_kde_iconsdir}/*/*/*/kuser*

#------------------------------------------------------------------------

%package -n kcron
Group:		Graphical desktop/KDE
Summary:	Graphical task scheduler
Provides:	kcron4
Provides:	kde4-kcron = %{EVRD}

%description -n kcron
Kcron is a graphical frontend to the cron system, used to schedule regular 
tasks on a Unix system.

%files -n kcron
%{_kde_services}/kcm_cron.desktop
%{_kde_libdir}/kde4/kcm_cron.so
%{_kde_docdir}/*/*/kcron

#------------------------------------------------------------------------

%package -n ksystemlog
Group:		Graphical desktop/KDE
Summary:	System log viewer tool for KDE 4
Provides:	ksystemlog4

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
%{_kde_bindir}/ksystemlog
%{_kde_appsdir}/ksystemlog
%{_kde_applicationsdir}/ksystemlog.desktop
%{_kde_docdir}/*/*/ksystemlog

#------------------------------------------------------------------------

%if %{with_printer_applet}
%package -n system-config-printer-kde
Summary:	View current print jobs and configure new printers
Group:		Graphical desktop/KDE
URL:		http://utils.kde.org/projects/printer-applet
Requires:	python-kde4
Requires:	python-cups
Requires:	python-dbus
Requires:	kdeutils4-printer-applet

%description -n system-config-printer-kde
Printer Applet is a system tray utility that shows current print jobs,
shows printer warnings and errors and shows when printers that have
been plugged in for the first time are being auto-configured by
hal-cups-utils.

%files -n system-config-printer-kde
%{_kde_services}/system-config-printer-kde.desktop
%{_kde_appsdir}/system-config-printer-kde
%{_kde_docdir}/*/*/system-config-printer-kde
%endif
#------------------------------------------------------------------------

%prep
%setup -q -n kdeadmin-%{version}

%build
%cmake_kde4
%make

%install
rm -fr %{buildroot}
%makeinstall_std -C build

