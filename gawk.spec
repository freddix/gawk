Summary:	The GNU version of the awk text processing utility
Name:		gawk
Version:	4.1.1
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/gawk/%{name}-%{version}.tar.xz
# Source0-md5:	a2a26543ce410eb74bc4a508349ed09a
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	texinfo
Provides:	awk
Requires:	coreutils
Requires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# redefine _includedir to install headers in a subdir
%define         _includedir     %{_prefix}/include/awk

%description
The gawk packages contains the GNU version of awk, a text processing
utility. Awk interprets a special-purpose programming language to do
quick and easy text pattern matching and reformatting jobs. Gawk
should be upwardly compatible with the Bell Labs research version of
awk and is almost completely compliant with the 1993 POSIX 1003.2
standard for awk.

%package devel
Summary:	Header files for gawk
Group:		Development/Libraries

%description devel
This is the package containing the header files for gawk.

%prep
%setup -q

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_includedir}
install *.h $RPM_BUILD_ROOT%{_includedir}

%{__rm} $RPM_BUILD_ROOT%{_bindir}/gawk-%{version}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gawk/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%doc POSIX.STD
%attr(755,root,root) %{_bindir}/awk
%attr(755,root,root) %{_bindir}/gawk
%attr(755,root,root) %{_bindir}/igawk
%dir %{_libdir}/awk
%dir %{_libdir}/gawk
%attr(755,root,root) %{_libdir}/awk/*
%attr(755,root,root) %{_libdir}/gawk/*.so
%{_datadir}/awk
%{_infodir}/*info*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}

