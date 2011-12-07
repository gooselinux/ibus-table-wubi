Name:       ibus-table-wubi
Version:    1.2.0.20090715
Release:    8%{?dist}

Summary:        Wubi input methods for ibus-table
Summary(zh_CN): IBus-Table 五笔码表
Summary(zh_HK): IBus-Table 五筆碼表
Summary(zh_TW): IBus-Table 五筆碼表

License:    GPLv3+
Group:      System Environment/Libraries
URL:        http://code.google.com/p/ibus/
Source0:    http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

Requires:         ibus-table >= 1.2
Requires(post):   ibus-table >= 1.2
BuildRequires:    ibus-table-devel >= 1.2

%description
The package contains Wubi input methods for Table engine of IBus platform. 

%description -l zh_CN
本包含有 IBus-Table 五笔码表。

%description -l zh_HK
呢個包有 IBus-Table 五筆碼表。

%description -l zh_TW
此套件包含 IBus-Table 五筆碼表。

%prep
%setup -q

%build
export IBUS_TABLE_CREATEDB="%{_bindir}/ibus-table-createdb -o"
%configure --prefix=%{_prefix} --enable-wubi86
%__make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} NO_INDEX=true INSTALL="install -p" install

%clean
%__rm -rf %{buildroot}

%post
cd %{_datadir}/ibus-table/tables/
%{_bindir}/ibus-table-createdb -i -n wubi86.db

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_datadir}/ibus-table/tables/wubi86.db
%{_datadir}/ibus-table/icons/wubi86.svg

%changelog
* Thu Feb 25 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20090715-8.el6
- Resolves: rhbz#567750
- Fixes build error with BuildRequires from ibus-table to ibus-table-devel.
- Removes ibus from Requires as ibus-table should have request that.

* Thu Jan 14 2010 Caius 'kaio' Chance - 1.2.0.20090715-7
- Resolves: rhbz#556335
- Fixes to spec bugs.

* Thu Jan 14 2010 Caius 'kaio' Chance - 1.2.0.20090715-6.el6
- Resolves: rhbz#555211
- Rebuilt due to own package resolution errors of brew.

* Thu Jan 14 2010 Caius 'kaio' Chance - 1.2.0.20090715-5.el6
- Resolves: rhbz#555211
- Fixes to rpmlint warnings.

* Wed Jan 13 2010 Caius 'kaio' Chance - 1.2.0.20090715-4.el6
- Resolves: rhbz#554946
- Add translations for supported non-English languages to summary and descriptions.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.2.0.20090715-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20090715-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090715-2.fc12
- Removed unneccessary BuildRequires.
- Removed unneccessary owned directories.
- Changed autogen.sh into configure.

* Wed Jul 15 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090715-1.fc12
- Rebuilt with IBus version 1.2.

* Fri Jul 03 2009 Caius 'kaio' Chance <k at kaio.me> - 1.1.0.20090316-9.fc12
- Rebuilt.

* Wed Jul 01 2009 Caius 'kaio' Chance <k at kaio.me> - 1.1.0.20090316-8.fc12
- Corrected by change into installed table directory for index creation.
- Further specify package dependencies.
- Added owned directories that supposed to belong to this package.
- Move hard coded commands to macros.

* Mon May 17 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090316-7.fc12
- Rebuilt with indexing during post-install.

* Mon May 17 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090316-6.fc12
- Resolves: rhbz#500973 (Missing .txt during post.)

* Thu Apr 23 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090316-5.fc12
- Refined file properties and updated description.

* Wed Apr 01 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090316-4.fc11
- Correct license to GPLv3+ and preserve timestamp during make install.

* Mon Mar 27 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090316-3.fc11
- Resolves: rhbz#488168
- Rebuilt with latest upstream.

* Mon Mar 27 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090316-2.fc11
- Resolves: rhbz#488168
- Removed wubi98.

* Mon Mar 16 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090316-1.fc11
- Resolves: rhbz#488168
- Splited from ibus-table.
- Added contents of AUTHORS.
