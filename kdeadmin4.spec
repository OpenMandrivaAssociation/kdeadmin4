%define branch_date 20070418


%define _prefix /opt/kde4/
%define _libdir %_prefix/%_lib
%define _datadir %_prefix/share/
%define _bindir %_prefix/bin
%define _includedir %_prefix/include/
%define _iconsdir %_datadir/icons/
%define _sysconfdir %_prefix/etc/
%define _docdir %_datadir/doc/

%define use_enable_final 1
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %unstable
%define dont_strip 1
%endif

%define lib_name_orig %mklibname kdeadmin4
%define lib_major 1
%define lib_name %lib_name_orig%lib_major

Name:		kdeadmin4
Version:    3.80.3
Release:        %mkrel 0.%branch_date.5
Group:		Graphical desktop/KDE
Summary:	K Desktop Environment - Adminstrative Tools
URL:		ftp://ftp.kde.org/pub/kde/stable/%version/src/
Epoch:		2
Packager:	Mandriva Linux KDE Team <kde@mandriva.com>
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeadmin-%version-%branch_date.tar.bz2
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
BuildRequires: rpm-devel libz-devel
BuildRequires: pam-devel
%define mini_release %mkrel 0.%branch_date.1
BuildRequires: kdelibs4-devel >= %version-%mini_release
BuildRequires: kdepimlibs4-devel >= %version-%mini_release
# createmdkmenu
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
%_datadir/applications/kde4/kcron.desktop
%_datadir/applications/kde4/kuser.desktop
%_bindir/kcron
%_bindir/kuser
%_bindir/secpolicy
%dir %_datadir/apps/kcron
%_datadir/apps/kcron/*
%dir %_datadir/apps/kuser/
%_datadir/apps/kuser/*
%dir %_datadir/apps/knetworkconf/
%_datadir/apps/knetworkconf/*
%_datadir/config.kcfg/kuser.kcfg
%_datadir/kde4/services/*.desktop
%_libdir/kde4/kcm_knetworkconfmodule.so
%_libdir/pkgconfig/system-tools-backends.pc
%_iconsdir/*/*/*/*
%dir %_docdir/HTML/en/kuser/
%doc %_docdir/HTML/en/kuser/*.bz2
%doc %_docdir/HTML/en/kuser/*.docbook
%doc %_docdir/HTML/en/kuser/*.png

%dir %_docdir/HTML/en/knetworkconf/
%doc %_docdir/HTML/en/knetworkconf/*.png
%doc %_docdir/HTML/en/knetworkconf/*.bz2
%doc %_docdir/HTML/en/knetworkconf/*.docbook

%dir %_docdir/HTML/en/kcron/
%doc %_docdir/HTML/en/kcron/*.bz2
%doc %_docdir/HTML/en/kcron/*.docbook
%doc %_docdir/HTML/en/kcron/*.png
#------------------------------------------------------------------------	

%package -n %name-kpackage
Group:      Graphical desktop/KDE
Summary:    Manager for DEB, RPM.
Requires:   %name = %epoch:%version-%release
Provides:   kpackage4 = %epoch:%version

%description -n %name-kpackage
Kpackage is a package manager that is integrated into the K Desktop 
Environemnt.  It works with the KDE File Manager to manage DEB, RPM 
and Slackware tgz software packages.

#%post -n %name-kpackage -p /sbin/ldconfig

#%postun -n %name-kpackage -p /sbin/ldconfig

%files -n %name-kpackage
%defattr(-,root,root)
%_bindir/kpackage
%dir %_sysconfdir/pam.d/
%config(noreplace) %_sysconfdir/pam.d/kpackage
%_iconsdir/*/*/*/kpackage.png
%_datadir/applications/kde4/kpackage.desktop
%dir %_datadir/apps/kpackage
%_datadir/apps/kpackage/*
%dir %_docdir/HTML/en/kpackage/
%doc %_docdir/HTML/en/kpackage/*.bz2
%doc %_docdir/HTML/en/kpackage/*.docbook
%doc %_docdir/HTML/en/kpackage/*.png
#------------------------------------------------------------------------	

%package -n %name-ksysv
Group:      Graphical desktop/KDE
Summary:    Edit your SysV-style init configuration
Provides:	ksysv4

%description -n %name-ksysv
SysV-Init Editor lets you edit your SysV-style init configuration
using drag'n'drop.

%files -n %name-ksysv
%defattr(-,root,root)

#------------------------------------------------------------------------	

%ifnarch ppc
%package -n %name-lilo
Group:      Graphical desktop/KDE
Summary:    Configure lilo.
Requires:   %name = %epoch:%version-%release

%description -n %name-lilo
lilo-config is a kcontrol plugin for configuring LILO, the most commonly
used Linux boot loader.

%post -n %name-lilo -p /sbin/ldconfig

%postun -n %name-lilo -p /sbin/ldconfig

%files -n %name-lilo
%defattr(-,root,root)
%_libdir/kde4/kcm_lilo.so
%dir %_docdir/HTML/en/lilo-config/
%doc %_docdir/HTML/en/lilo-config/*.bz2
%doc %_docdir/HTML/en/lilo-config/*.docbook

%endif

#------------------------------------------------------------------------	

%prep
%setup -q -nkdeadmin-%version-%branch_date

%build
cd $RPM_BUILD_DIR/kdeadmin-%version-%branch_date
mkdir build
cd build
export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=Debug \
%endif
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
        ../

%make


%install
rm -fr %buildroot
cd $RPM_BUILD_DIR/kdeadmin-%version-%branch_date
cd build

make DESTDIR=%buildroot install


#TODO readd it

#kdedesktop2mdkmenu.pl kdeadmin System/Configuration/Other  %buildroot/%_datadir/applications/kde4/kcron.desktop %buildroot/%_menudir/kdeadmin-kcron
#kdedesktop2mdkmenu.pl kdeadmin-kpackage System/Configuration/Packaging  %buildroot/%_datadir/applications/kde4/kpackage.desktop %buildroot/%_menudir/kdeadmin-kpackage
#kdedesktop2mdkmenu.pl kdeadmin "System/Configuration/Boot and Init"  %buildroot/%_datadir/applications/kde4/ksysv.desktop %buildroot/%_menudir/kdeadmin-ksysv
#kdedesktop2mdkmenu.pl kdeadmin System/Configuration/Other  %buildroot/%_datadir/applications/kde4/kuser.desktop %buildroot/%_menudir/kdeadmin-kuser
#kdedesktop2mdkmenu.pl kdeadmin System/Configuration/Other  %buildroot/%_datadir/applications/kde4/kdat.desktop %buildroot/%_menudir/kdeadmin-kdat
#kdedesktop2mdkmenu.pl kdeadmin System/Configuration/KDE/System  %buildroot/%_datadir/applications/kde4/kcm_knetworkconfmodule.desktop %buildroot/%_menudir/kdeadmin-knetworkconfmodule


# Install kdebase pam configuration file
install -d %buildroot/%_sysconfdir/pam.d
install -m644 %SOURCE1 %buildroot/%_sysconfdir/pam.d/kpackage

rm -rf %buildroot/%_datadir/applnk/Settings/Peripherals/

%ifarch ppc
rm -rf %buildroot/%_docdir/HTML/en/lilo-config
%endif

%clean
rm -fr %buildroot

