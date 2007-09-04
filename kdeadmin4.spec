%define revision 681364

%define use_enable_final 1
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 0
%{?_branch: %{expand: %%global branch 1}}

%if %unstable
%define dont_strip 1
%endif

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%define lib_name_orig %mklibname kdeadmin4
%define lib_major 1
%define lib_name %lib_name_orig%lib_major

Name:		kdeadmin4
Version: 3.93.0
Release: %mkrel 1
Group:		Graphical desktop/KDE
Summary:	K Desktop Environment - Adminstrative Tools
URL:		ftp://ftp.kde.org/pub/kde/stable/%version/src/
Epoch:		2
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeadmin-%version-%revision.tar.bz2
%else
Source:  ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeadmin-%version.tar.bz2
%endif
Source1:	kpackage.pamd
Patch1:		kdeadmin-3.5.5-knetworkconf-add-20071-support.patch
BuildRoot:	%_tmppath/%name-%version-%release-root
License:	GPL
Requires:	pciutils
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
%define mini_release %mkrel 0.%revision.1
BuildRequires: kdelibs4-devel
BuildRequires: kdepimlibs4-devel
%ifarch %{ix86} x86_64
BuildRequires:	lilo
%endif

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

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%_kde_datadir/applications/kde4/kcron.desktop
%_kde_datadir/applications/kde4/kuser.desktop
%_kde_bindir/kcron
%_kde_bindir/kuser
%_kde_bindir/secpolicy
%dir %_kde_datadir/apps/kcron
%_kde_datadir/apps/kcron/*
%dir %_kde_datadir/apps/kuser/
%_kde_datadir/apps/kuser/*
%dir %_kde_datadir/apps/knetworkconf/
%_kde_datadir/apps/knetworkconf/*
%_kde_datadir/config.kcfg/kuser.kcfg
%_kde_datadir/kde4/services/*.desktop
%_kde_libdir/kde4/kcm_knetworkconfmodule.so
%_kde_libdir/pkgconfig/system-tools-backends.pc
%_kde_iconsdir/*/*/*/*
%dir %_kde_docdir/HTML/en/kuser/
%doc %_kde_docdir/HTML/en/kuser/*.bz2
%doc %_kde_docdir/HTML/en/kuser/*.docbook
%doc %_kde_docdir/HTML/en/kuser/*.png

%dir %_kde_docdir/HTML/en/knetworkconf/
%doc %_kde_docdir/HTML/en/knetworkconf/*.png
%doc %_kde_docdir/HTML/en/knetworkconf/*.bz2
%doc %_kde_docdir/HTML/en/knetworkconf/*.docbook

%dir %_kde_docdir/HTML/en/kcron/
%doc %_kde_docdir/HTML/en/kcron/*.bz2
%doc %_kde_docdir/HTML/en/kcron/*.docbook
%doc %_kde_docdir/HTML/en/kcron/*.png

#------------------------------------------------------------------------	

%package -n kde4-kpackage
Group:      Graphical desktop/KDE
Summary:    Manager for DEB, RPM.
Requires:   %name = %epoch:%version-%release
Provides:   kpackage4 = %epoch:%version
Obsoletes:  %name-kpackage

%description -n kde4-kpackage
Kpackage is a package manager that is integrated into the K Desktop 
Environemnt.  It works with the KDE File Manager to manage DEB, RPM 
and Slackware tgz software packages.

%files -n kde4-kpackage
%defattr(-,root,root)
%_kde_bindir/kpackage
%dir %_sysconfdir/pam.d/
%config(noreplace) %_sysconfdir/pam.d/kpackage
%_kde_iconsdir/*/*/*/kpackage.png
%_kde_datadir/applications/kde4/kpackage.desktop
%dir %_kde_datadir/apps/kpackage
%_kde_datadir/apps/kpackage/*
%dir %_kde_docdir/HTML/en/kpackage/
%doc %_kde_docdir/HTML/en/kpackage/*.bz2
%doc %_kde_docdir/HTML/en/kpackage/*.docbook
%doc %_kde_docdir/HTML/en/kpackage/*.png

#------------------------------------------------------------------------	

%package -n kde4-ksysv
Group:      Graphical desktop/KDE
Summary:    Edit your SysV-style init configuration
Provides:   ksysv4
Obsoletes:  %name-ksysv 

%description -n kde4-ksysv
SysV-Init Editor lets you edit your SysV-style init configuration
using drag'n'drop.

%files -n kde4-ksysv
%defattr(-,root,root)


#------------------------------------------------------------------------	

%ifnarch ppc
%package -n kde4-lilo
Group:      Graphical desktop/KDE
Summary:    Configure lilo.
Requires:   %name = %epoch:%version-%release
Obsoletes:  %name-lilo

%description -n kde4-lilo
lilo-config is a kcontrol plugin for configuring LILO, the most commonly
used Linux boot loader.

%post -n kde4-lilo -p /sbin/ldconfig

%postun -n kde4-lilo -p /sbin/ldconfig

%files -n kde4-lilo
%defattr(-,root,root)
%_kde_libdir/kde4/kcm_lilo.so
%dir %_kde_docdir/HTML/en/lilo-config/
%doc %_kde_docdir/HTML/en/lilo-config/*.bz2
%doc %_kde_docdir/HTML/en/lilo-config/*.docbook

%endif

#------------------------------------------------------------------------	

%prep
%setup -q -n kdeadmin-%version

%build
%cmake_kde4 


%make

%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install


# Install kdebase pam configuration file
install -d %buildroot/%_sysconfdir/pam.d
install -m644 %SOURCE1 %buildroot/%_sysconfdir/pam.d/kpackage

rm -rf %buildroot/%_kde_datadir/applnk/Settings/Peripherals/

%ifarch ppc
rm -rf %buildroot/%_kde_docdir/HTML/en/lilo-config
%endif

%clean
rm -fr %buildroot

