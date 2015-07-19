Summary:	K Desktop Environment - Administrative Tools
Name:		kdeadmin4
Version:	4.14.3
Release:	3
Epoch:		2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Suggests:	kcron
Suggests:	ksystemlog
Suggests:	kuser
BuildArch:	noarch

%description
The kdeadmin package contains packages that usually only a system
administrator might need:
- kcron (editor for the cron command scheduler)
- kuser (user manager)
- ksystemlog (system log viewer tool for KDE4)

%files

#------------------------------------------------------------------------

%prep

%build

%install

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.14.3-1
- New version 4.14.3

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.0-1
- New version 4.11.0
- A metapackage from now on

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.5-1
- New version 4.10.5
- Fix files
- Update description

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.0-1
- New version 4.10.0
- Drop system-config-printer-kde which is replaced by print-manager in upstream

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.1-1
- New version 4.9.1

* Wed Aug 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.0
- New version 4.9.0

* Mon Jul 16 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.97
- New version 4.8.97

* Fri Jun 29 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.95
- Update to 4.8.95

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.3-1
- update to 4.8.3

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.1-1
- update to 4.8.1

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.8.0-1
+ Revision: 762512
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.97-1
+ Revision: 758097
- New upstream tarball

* Tue Jan 03 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.95-1
+ Revision: 748792
- New version

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.90-1
+ Revision: 739366
- New upstream tarball

* Tue Nov 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.80-1
+ Revision: 732344
- Add Automoc4 as buildrequires ( to workaround a rpm5/iurt bug)
- New upstream tarball 4.7.80
- New upstream tarball 4.7.80

* Fri Aug 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.41-1
+ Revision: 697177
- New version 4.7.41

* Mon Aug 01 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.40-1
+ Revision: 692642
- New release 4.7.40

* Mon Jun 13 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.4-1
+ Revision: 684400
- New version 4.6.4

* Fri May 13 2011 Funda Wang <fwang@mandriva.org> 2:4.6.3-1
+ Revision: 674018
- new version 4.6.3

* Tue Apr 05 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.2-1
+ Revision: 650765
- Remove mkrel
- New version 4.6.2

* Mon Feb 28 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.1-1
+ Revision: 640722
- New version 4.6.1

* Wed Jan 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.0-1
+ Revision: 632960
- New version KDE 4.6 Final

* Thu Jan 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.95-1mdv2011.0
+ Revision: 629114
- New version KDE 4.6 RC2

* Thu Dec 23 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.90-1mdv2011.0
+ Revision: 624058
- New upstream tarball

* Wed Dec 08 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.85-1mdv2011.0
+ Revision: 616339
- New upstream tarball

* Sat Nov 27 2010 Funda Wang <fwang@mandriva.org> 2:4.5.80-1mdv2011.0
+ Revision: 601634
- new version 4.5.80 (aka 4.6 beta1)

* Sat Nov 20 2010 Funda Wang <fwang@mandriva.org> 2:4.5.77-0.svn1198704.1mdv2011.0
+ Revision: 599222
- new snapshot 4.5.77
- there is no core sub package now

* Fri Oct 29 2010 Funda Wang <fwang@mandriva.org> 2:4.5.74-0.svn1190490.1mdv2011.0
+ Revision: 589884
- new snapshot 4.5.74

* Wed Sep 15 2010 Funda Wang <fwang@mandriva.org> 2:4.5.68-1mdv2011.0
+ Revision: 578417
- new snapshot 4.5.68

* Tue Sep 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.67-1mdv2011.0
+ Revision: 576447
- New version 4.5.67
- Fix file list
- New version 4.5.65
- Do not build system-config-printer-kde
  CCBUG: 60829

* Fri Aug 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.0-1mdv2011.0
+ Revision: 566564
- New upstream tarball
- Update to version 4.5.0

* Wed Jul 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.95-1mdv2011.0
+ Revision: 562632
- kde 4.4.95

* Tue May 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-1mdv2010.1
+ Revision: 542096
- Update to version 4.4.3
- Fix s-c-p-kde package name
- Remove rpm-devel buildrequires ( was needed for kde4-lilo )
  fix s-c-p-kde file list and requires

* Sun Mar 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-1mdv2010.1
+ Revision: 528309
- Update to version 4.4.2

* Thu Mar 11 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.1-1mdv2010.1
+ Revision: 517956
- kde4-lilo does not exist anymore
- Update to version 4.4.1

* Tue Feb 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.0-1mdv2010.1
+ Revision: 502605
- Update to version 4.4.0

* Mon Feb 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.98-1mdv2010.1
+ Revision: 498938
- Update to version 4.3.98 aka "kde 4.4 RC3"
- Update to version 4.3.98 aka "kde 4.4 RC3"

* Mon Jan 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.95-1mdv2010.1
+ Revision: 495974
- Update to version 4.3.95 aka "kde 4.4 RC2"

* Sun Jan 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.90-1mdv2010.1
+ Revision: 488235
- kpackage is not anymore
- Update to kde 4.4 rc1

  + Funda Wang <fwang@mandriva.org>
    - revert last commit (wait for next beta)
    - kpackage is not there any more

* Mon Dec 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.85-1mdv2010.1
+ Revision: 480702
- Update to kde 4.4 beta2

* Fri Dec 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.80-1mdv2010.1
+ Revision: 473202
- Update to kde 4.4 beta1

* Thu Nov 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.77-1mdv2010.1
+ Revision: 470388
- Update to kde 4.3.77
  Add branch switch
- Update to kde 4.3.75

* Mon Nov 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.75-1mdv2010.1
+ Revision: 466600
- Update to kde 4.3.75

* Thu Nov 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.73-2mdv2010.1
+ Revision: 465256
- Rebuild against new Qt

* Sun Nov 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.73-1mdv2010.1
+ Revision: 463207
- Update to kde 4.3.73
  Remove merged patch

* Tue Oct 06 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.2-1mdv2010.0
+ Revision: 454668
- New upstream release 4.3.2.

* Tue Sep 01 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.1-1mdv2010.0
+ Revision: 423220
- New upstream release 4.3.1.

* Sat Aug 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.0-2mdv2010.0
+ Revision: 416469
- Obsolete kde3 packages

* Tue Aug 04 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.0-1mdv2010.0
+ Revision: 409442
- New upstream release 4.3.0.
- Update to KDE 4.3 RC3

* Sat Jul 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.96-1mdv2010.0
+ Revision: 394881
- Update to Rc2

* Fri Jun 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.95-1mdv2010.0
+ Revision: 389371
- Update to kde 4.3Rc1

* Thu Jun 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.90-1mdv2010.0
+ Revision: 382826
- Update to beta2

* Fri May 29 2009 Funda Wang <fwang@mandriva.org> 2:4.2.88-1mdv2010.0
+ Revision: 380797
- New version 4.2.88

* Fri May 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.87-1mdv2010.0
+ Revision: 378795
- Update to kde   4.2.87

* Fri May 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.85-1mdv2010.0
+ Revision: 373531
- Update to kde 4.2.85
- Really remove patch when not needed just not comment them

* Tue May 05 2009 Funda Wang <fwang@mandriva.org> 2:4.2.71-0.svn961800.1mdv2010.0
+ Revision: 372037
- disable pkgconfig

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Update to kde 4.2.71
    - Remove non existing files

* Sat May 02 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.70-0.svn954171.1mdv2010.0
+ Revision: 370552
- Fix file list
- Update to kde 4.2.70
  Remove old macros

  + Helio Chissini de Castro <helio@mandriva.com>
    - Add build conflicts for future reference builds

* Wed Apr 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-2mdv2009.1
+ Revision: 367586
- Do not package system-config-printer-kde

* Fri Mar 27 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.2-1mdv2009.1
+ Revision: 361729
- Update with 4.2.2 try#1 packages

* Mon Mar 02 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.1-1mdv2009.1
+ Revision: 347011
- KDE 4.2.1 try#1 upstream release

* Mon Feb 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-2mdv2009.1
+ Revision: 340860
- Rebuild against qt4.5

* Wed Jan 28 2009 Funda Wang <fwang@mandriva.org> 2:4.2.0-1mdv2009.1
+ Revision: 334736
- New version 4.2.0

* Wed Jan 07 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.96-1mdv2009.1
+ Revision: 326829
- Update with Release Candidate 1 - 4.1.96

* Sat Dec 13 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.85-1mdv2009.1
+ Revision: 314016
- New version KDE 4.2 Beta2

* Thu Dec 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.82-1mdv2009.1
+ Revision: 313356
- Update to kde 4.1.82

* Sun Nov 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.81-1mdv2009.1
+ Revision: 308639
- Update to kde 4.1.81

* Wed Nov 19 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.80-1mdv2009.1
+ Revision: 304562
- Update with Beta 1 - 4.1.80

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add requires on kdebase4-runtime package

* Sat Nov 15 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.73-1mdv2009.1
+ Revision: 303391
- Fix BuildRequire
- Add some python Buildrequires (python-kde4 && python-qt4)
- Update to kde 4.1.73
  New package system-config-printer-kde

* Sat Oct 25 2008 Funda Wang <fwang@mandriva.org> 2:4.1.71-1mdv2009.1
+ Revision: 297029
- New version 4.1.71

* Tue Oct 21 2008 Funda Wang <fwang@mandriva.org> 2:4.1.70-1mdv2009.1
+ Revision: 296143
- New version 4.1.70
- disable kpackage-doc installiing when not building kpackage
- drop unwanted pkgconfig files as fedora does
- fix description
- bump smart as requirement, as it is hardcoded in kpackage

  + Helio Chissini de Castro <helio@mandriva.com>
    - KDE 4.1.2 arriving.
    - Upgrade to forthcoming 4.1.1 packages
    - kpackage removed as smart is almost obsoleted and Mandriva uses different approach to rpm

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add missing requires on ksystemlog

* Fri Jul 25 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.0-1mdv2009.0
+ Revision: 247591
- Update with Release Candidate 1 - 4.1.0

  + Funda Wang <fwang@mandriva.org>
    - suggests instead of requires. It can still use rpm to install packages
    - kpackage requires smart

* Sun Jul 13 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.98-1mdv2009.0
+ Revision: 234234
- Update with Release Candidate 1 - 4.0.98

* Mon Jul 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.85-1mdv2009.0
+ Revision: 232410
- New version kde 4.0.85
- Do not show Kuser and KPackage on the menu (menu cleaning task)

* Fri Jun 27 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.84-1mdv2009.0
+ Revision: 229405
- Update with new snapshot tarballs 4.0.84

* Thu Jun 19 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.83-1mdv2009.0
+ Revision: 226120
- Update with new snapshot tarballs 4.0.83

* Thu Jun 12 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.82-1mdv2009.0
+ Revision: 218301
- Update with new snapshot tarballs 4.0.82

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jun 03 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.81-1mdv2009.0
+ Revision: 214721
- Update with new snapshot tarballs 4.0.81

  + Michael Scherer <misc@mandriva.org>
    - use the same logic as buildrequires to decide if kde4-lilo is compiled ( ie, fix the logic for sparc, or mips )
    - fix typo and missing description

* Sat May 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.80-2mdv2009.0
+ Revision: 210965
- Versionnate buildrequires

* Sat May 24 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.80-1mdv2009.0
+ Revision: 210779
- New upstream kde4 4.1 beta1

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Own %%_kde_appsdir/ksystemlog

* Fri May 16 2008 Funda Wang <fwang@mandriva.org> 2:4.0.74-1mdv2009.0
+ Revision: 208073
- New version 4.0.74

* Tue May 13 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.73-1mdv2009.0
+ Revision: 206790
- Fix file list
- Update to kde 4.0.73

* Thu May 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.72-1mdv2009.0
+ Revision: 199816
- Update to kde 4.0.72
- New snapshot 4.0.70
- Fix epoch
- New snapshot 4.0.69

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 alpha 1
    - New upstream kde4 4.1 alpha 1

* Fri Mar 28 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.3-1mdv2008.1
+ Revision: 191005
- Update for last stable release 4.0.3

* Sat Mar 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.2-2mdv2008.1
+ Revision: 182258
- Rebuild against new qt4 changes

* Sat Mar 01 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.2-1mdv2008.1
+ Revision: 177449
- New upstream bugfix release 4.0.2

* Wed Feb 20 2008 Thierry Vignaud <tv@mandriva.org> 2:4.0.1-2mdv2008.1
+ Revision: 173184
- fix no-buildroot-tag

* Mon Feb 11 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.1-1mdv2008.1
+ Revision: 165293
- Splitted packages
- Fixed file list and duplicates
- Update for 4.0.1

* Wed Jan 23 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.0-1mdv2008.1
+ Revision: 156943
- Update to kde 4.0.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 24 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:3.97.1-0.750650.1mdv2008.1
+ Revision: 137426
- New snapshot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 11 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:3.97.1-0.746368.1mdv2008.1
+ Revision: 117174
- New snapshot
- New snapshot
- New snapshot
- New version 3.91

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot

* Wed May 09 2007 Laurent Montel <lmontel@mandriva.org> 2:3.90.1-0.20070502.1mdv2008.0
+ Revision: 25718
- new snapshot

* Wed May 02 2007 Laurent Montel <lmontel@mandriva.org> 2:3.80.3-0.20070502.5mdv2008.0
+ Revision: 20526
- new snapshot
- new snapshot


* Sun Mar 11 2007 Laurent Montel <lmontel@mandriva.com> 3.80.3-0.20070311.5mdv2007.1
+ Revision: 141315
- new snapshot
- Fix buildrequires
- new snapshot
- Fix spec file
- new snapshot
- 3.80.3

* Fri Feb 16 2007 Laurent Montel <lmontel@mandriva.com> 2:3.80.2-0.20070215.4mdv2007.1
+ Revision: 121693
- new snapshot
- Fix spec file
- new snapshot
- Fix description
- new snapshot
- Fix buildrequires
- update
- Fix buildrequires
- Import kdeadmin4

* Fri Nov 03 2006 Laurent Montel <lmontel@mandriva.com> 3.5.5-3mdv2007.0
- First package

