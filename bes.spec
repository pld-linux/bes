Summary:	OPeNDAP Back End Server software framework
Summary(pl.UTF-8):	Szkielet OPeNDAP Back End Server (serwera backendu OPeNDAP)
Name:		bes
Version:	3.12.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.opendap.org/pub/source/%{name}-%{version}.tar.gz
# Source0-md5:	582e9c4fc5ca27b78982ea0a014c7035
Patch0:		%{name}-missing.patch
Patch1:		%{name}-gdal.patch
URL:		http://opendap.org/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.10
BuildRequires:	bison
BuildRequires:	bzip2-devel
%{?with_tests:BuildRequires:	cppunit-devel >= 1.12.0}
BuildRequires:	gdal-devel >= 1.10.0
BuildRequires:	libdap-devel >= 3.12.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libwrap-devel
BuildRequires:	libxml2-devel >= 1:2.6.16
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires:	libxml2 >= 1:2.6.16
Requires:	%{name}-libs = %{version}-%{release}
Provides:	group(bes)
Provides:	user(bes)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BES is a high-performance back-end server software framework for
OPeNDAP that allows data providers more flexibility in providing end 
users views of their data. The current OPeNDAP data objects (DAS, DDS,
and DataDDS) are still supported, but now data providers can add new
data views, provide new functionality, and new features to their end
users through the BES modular design. Providers can add new data
handlers, new data objects/views, the ability to define views with
constraints and aggregation, the ability to add reporting mechanisms,
initialization hooks, and more.

%description -l pl.UTF-8
BES to szkielet wysoko wydajnego serwera backendu dla OPeNDAP,
pozwalający na większą elastyczność dostarczycieli danych (providers)
w udostępnianiu widoków danych dla użytkowników końcowych. Obecne
obiekty danych OPeNDAP (DAS, DDS i DataDDS) są nadal obsługiwane, ale
teraz dostarczyciele danych mogą dodawać nowe widoki danych, zapewniać
nową funkcjonalność oraz nowe możliwości dla użytkowników końcowych
poprzez modularną budowę BES. Dostarczyciele mogą dodawać nowe
procedury obsługujące (handlers), nowe obiekty/widoki danych,
możliwość definiowania widoków z ograniczeniami i agregacją, możliwość
dodawania mechanizmów raportujących, uchwytów inicjujących itd.

%package libs
Summary:	Shared OPeNDAP Back End Server libraries
Summary(pl.UTF-8):	Biblioteki współdzielone serwera backendu OPeNDAP
Group:		Libraries
Requires:	libdap >= 3.12.0

%description libs
Shared OPeNDAP Back End Server libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone serwera backendu OPeNDAP.

%package devel
Summary:	Header files for OPeNDAP Back End Server libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek serwera backendu OPeNDAP
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	bzip2-devel
Requires:	libstdc++-devel
Requires:	openssl-devel
Requires:	zlib-devel

%description devel
Header files for OPeNDAP Back End Server libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek serwera backendu OPeNDAP.

%package static
Summary:	Static OPeNDAP Back End Server libraries
Summary(pl.UTF-8):	Statyczne biblioteki serwera backendu OPeNDAP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OPeNDAP Back End Server libraries.

%description static -l pl.UTF-8
Statyczne biblioteki serwera backendu OPeNDAP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i \
	-e 's:=/tmp:=/var/cache/bes:' \
	-e 's:=.*/bes\.log:=/var/log/bes/bes.log:' \
	-e 's:=.*/lib/bes:=%{_libdir}/bes:' \
	-e 's:=.*/share/bes:=%{_datadir}/bes:' \
	-e 's:=.*/share/hyrax:=%{_datadir}/hyrax:' \
	-e 's:=/full/path/to/serverside/certificate/file.pem:=/etc/pki/bes/cacerts/file.pem:' \
	-e 's:=/full/path/to/serverside/key/file.pem:=/etc/pki/bes/public/file.pem:' \
	-e 's:=/full/path/to/clientside/certificate/file.pem:=/etc/pki/bes/cacerts/file.pem:' \
	-e 's:=/full/path/to/clientside/key/file.pem:=/etc/pki/bes/public/file.pem:' \
	-e 's:=user_name:=bes:' \
	-e 's:=group_name:=bes:' \
	dispatch/bes/bes.conf

%build
%{__libtoolize}
%{__aclocal} -I conf
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-libwrap
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,/etc/pki/bes/{cacerts,public}} \
	$RPM_BUILD_ROOT{/var/cache/bes,/var/log/bes}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_bindir}/besd $RPM_BUILD_ROOT/etc/rc.d/init.d

%{__rm} $RPM_BUILD_ROOT%{_libdir}/bes/*.{la,a}
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libbes*.la

install -d $RPM_BUILD_ROOT%{systemdtmpfilesdir}
cat >$RPM_BUILD_ROOT%{systemdtmpfilesdir}/bes.conf <<EOF
d /var/run/bes 0775 bes bes -
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 307 bes
%useradd -u 307 -d /var/cache/bes -g bes -s /bin/false -c "BES daemon" bes

%postun
if [ "$1" = "0" ]; then
	%userremove bes
	%groupremove bes
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bescmdln
%attr(755,root,root) %{_bindir}/besctl
%attr(755,root,root) %{_bindir}/besdaemon
%attr(755,root,root) %{_bindir}/beslistener
%attr(755,root,root) %{_bindir}/besregtest
%attr(755,root,root) %{_bindir}/besstandalone
%attr(755,root,root) %{_bindir}/hyraxctl
%dir %{_sysconfdir}/bes/modules
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/dap.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/functions.conf
%dir /etc/pki/bes
%dir /etc/pki/bes/cacerts
%dir /etc/pki/bes/public
%attr(754,root,root) /etc/rc.d/init.d/besd
%attr(775,bes,bes) %dir /var/cache/bes
%attr(775,bes,bes) %dir /var/log/bes
%attr(775,bes,bes) %dir /var/run/bes
%{systemdtmpfilesdir}/bes.conf

%files libs
%defattr(644,root,root,755)
%doc NEWS README*
%attr(755,root,root) %{_libdir}/libbes_dispatch.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbes_dispatch.so.8
%attr(755,root,root) %{_libdir}/libbes_ppt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbes_ppt.so.4
%attr(755,root,root) %{_libdir}/libbes_xml_command.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbes_xml_command.so.1
%dir %{_libdir}/bes
%attr(755,root,root) %{_libdir}/bes/libdap_module.so
%attr(755,root,root) %{_libdir}/bes/libdap_xml_module.so
%attr(755,root,root) %{_libdir}/bes/libdapreader_module.so
%attr(755,root,root) %{_libdir}/bes/libfunctions_module.so
%dir %{_sysconfdir}/bes
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/bes.conf
%dir %{_datadir}/bes
%{_datadir}/bes/bes_help.*
%{_datadir}/bes/dap_help.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bes-config
%attr(755,root,root) %{_bindir}/bes-config-pkgconfig
%attr(755,root,root) %{_bindir}/besCreateModule
%attr(755,root,root) %{_libdir}/libbes_dispatch.so
%attr(755,root,root) %{_libdir}/libbes_ppt.so
%attr(755,root,root) %{_libdir}/libbes_xml_command.so
%{_includedir}/bes
%{_pkgconfigdir}/bes_dispatch.pc
%{_pkgconfigdir}/bes_ppt.pc
%{_pkgconfigdir}/bes_xml_command.pc
%{_aclocaldir}/bes.m4
%{_datadir}/bes/templates

%files static
%defattr(644,root,root,755)
%{_libdir}/libbes_dispatch.a
%{_libdir}/libbes_ppt.a
%{_libdir}/libbes_xml_command.a
