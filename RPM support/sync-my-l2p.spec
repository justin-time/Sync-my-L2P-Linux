# 
# spec file for package Sync-my-L2P
#
# Copyright (c) 2015 Stefan Ahlers <stef.ahlers@t-online.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes, issues or comments via https://github.com/Sync-my-L2P/Sync-my-L2P
#

Summary:           Sync-my-L²P – Synchronisiere deinen PC mit dem L²P der RWTH Aachen
Name:              sync-my-l2p
Version:           2.2.0
Release:           2%{?dist}
License:           LGPL-3.0

Source0:        sync-my-l2p.tar.gz
Url:            http://www.sync-my-l2p.de
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Group:          Productivity/Networking/Web/Utilities

%if 0%{?fedora_version} || 0%{?rhel_version} >= 6 || 0%{?centos_version} >= 6
BuildRequires:       openssl-devel qt5-qtbase-devel desktop-file-utils
%endif


%if 0%{?suse_version}
BuildRequires:       libopenssl-devel libqt5-qtbase-devel libudev-mini1 libqt5-qttools-devel update-desktop-files hicolor-icon-theme
%endif

%description
Sync-my-L2P synchronsiert dir mit wenigen Klicks deine 
Dokumente aus dem L²P der RWTH Aachen mit deinem Rechner. 
Es ist einfach zu bedienen, läuft auf jedem Rechner 
und ist außerdem noch vollkommen kostenlos.

%prep
%setup -q -n sync-my-l2p

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{?buildroot}/usr
%if 0%{?suse_version}
%suse_update_desktop_file -i %{buildroot}/usr/share/applications/Sync-my-L2P.desktop Network FileTransfer
%else
desktop-file-validate %{buildroot}/usr/share/applications/Sync-my-L2P.desktop
%endif

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%{_bindir}/*
%if 0%{?suse_version}
%dir %{_datarootdir}/icons/hicolor/16x16
%dir %{_datarootdir}/icons/hicolor/16x16/apps
%dir %{_datarootdir}/icons/hicolor/32x32
%dir %{_datarootdir}/icons/hicolor/32x32/apps
%dir %{_datarootdir}/icons/hicolor/48x48
%dir %{_datarootdir}/icons/hicolor/48x48/apps
%dir %{_datarootdir}/icons/hicolor/128x128
%dir %{_datarootdir}/icons/hicolor/128x128/apps
%endif
%{_datarootdir}/applications/Sync-my-L2P.desktop
%{_datarootdir}/icons/hicolor/16x16/apps/sync-my-L2P.png
%{_datarootdir}/icons/hicolor/32x32/apps/sync-my-L2P.png
%{_datarootdir}/icons/hicolor/48x48/apps/sync-my-L2P.png
%{_datarootdir}/icons/hicolor/128x128/apps/sync-my-L2P.png

%post
%if 0%{?suse_version}
%icon_theme_cache_post hicolor
%desktop_database_post
%else
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%postun
%if 0%{?suse_version}
%icon_theme_cache_postun hicolor
%desktop_database_postun
%else
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
%endif

%posttrans
%if 0%{?fedora_version}
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%changelog

