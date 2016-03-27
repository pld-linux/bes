Summary:	OPeNDAP Back End Server software framework
Summary(pl.UTF-8):	Szkielet OPeNDAP Back End Server (serwera backendu OPeNDAP)
Name:		bes
Version:	3.17.0
Release:	0.1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.opendap.org/pub/source/%{name}-%{version}.tar.gz
# Source0-md5:	4534a887fe752cb30f20a09bda058fd1
Patch0:		%{name}-conf.patch
Patch1:		%{name}-configure.patch
Patch2:		%{name}-link.patch
URL:		http://opendap.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	bison
BuildRequires:	bzip2-devel
%{?with_tests:BuildRequires:	cppunit-devel >= 1.12.0}
BuildRequires:	cfitsio-devel
BuildRequires:	gdal-devel >= 1.10.0
BuildRequires:	gridfields-devel >= 1.0.5
BuildRequires:	hdf-devel >= 4
BuildRequires:	hdf-eos-devel >= 2
BuildRequires:	hdf5-devel
BuildRequires:	libdap-devel >= 3.17.0
BuildRequires:	libicu-devel >= 3.6
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libwrap-devel
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 1:2.6.16
BuildRequires:	openjpeg2-devel >= 2
BuildRequires:	openssl-devel
BuildRequires:	perl-base
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
Requires:	libdap >= 3.17.0

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
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I conf
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CURL=/usr/bin/curl \
	--with-hdfeos2="" \
	--with-libwrap
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/pki/bes/{cacerts,certs,public} \
	$RPM_BUILD_ROOT{/var/cache/bes,/var/log/bes} \
	$RPM_BUILD_ROOT%{_datadir}/hyrax/data

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_bindir}/besstandalone
%attr(755,root,root) %{_bindir}/hyraxctl
%dir %{_sysconfdir}/bes/modules
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/dap.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/functions.conf
%dir /etc/pki/bes
%dir /etc/pki/bes/cacerts
%dir /etc/pki/bes/certs
%dir /etc/pki/bes/public
%attr(754,root,root) /etc/rc.d/init.d/besd
%dir %{_datadir}/hyrax
%dir %{_datadir}/hyrax/data
%attr(775,bes,bes) %dir /var/cache/bes
%attr(775,bes,bes) %dir /var/log/bes
%attr(775,bes,bes) %dir /var/run/bes
%{systemdtmpfilesdir}/bes.conf

# [opendap-csv_handler]
#%doc modules/csv_handler/{COPYRIGHT,ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/csv.conf
%attr(755,root,root) %{_libdir}/bes/libcsv_module.so
%dir %{_datadir}/hyrax/data/csv
%{_datadir}/hyrax/data/csv/temperature.csv

# [opendap-fileout_gdal]
#%doc modules/fileout_gdal/{ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/fong.conf
%attr(755,root,root) %{_libdir}/bes/libfong_module.so

# [opendap-fileout_netcdf]
#%doc modules/fileout_netcdf/{COPYRIGHT,ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/fonc.conf
%attr(755,root,root) %{_libdir}/bes/libfonc_module.so

# [opendap-fits_handler]
#%doc modules/fits_handler/{COPYRIGHT,ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/fits.conf
%attr(755,root,root) %{_libdir}/bes/libfits_module.so
%dir %{_datadir}/hyrax/data/fits
%{_datadir}/hyrax/data/fits/*.fts

# [opendap-freeform_handler]
#%doc modules/freeform_handler/{COPYRIGHT,ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/ff.conf
%attr(755,root,root) %{_libdir}/bes/libff_module.so
%dir %{_datadir}/hyrax/data/ff
%{_datadir}/hyrax/data/ff/*.dat
%{_datadir}/hyrax/data/ff/*.dat.das
%{_datadir}/hyrax/data/ff/*.fmt

# [opendap-gateway_module]
#%doc modules/gateway_module/{COPYRIGHT,ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/gateway.conf
%attr(755,root,root) %{_libdir}/bes/libgateway_module.so

# [opendap-gdal_handler]
#%doc modules/gdal_handler/{ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/gdal.conf
%attr(755,root,root) %{_libdir}/bes/libgdal_module.so
%dir %{_datadir}/hyrax/data/gdal
%{_datadir}/hyrax/data/gdal/*.wind.grb.bz2
%{_datadir}/hyrax/data/gdal/*.jp2
%{_datadir}/hyrax/data/gdal/*.jpg
%{_datadir}/hyrax/data/gdal/*.lgo
%{_datadir}/hyrax/data/gdal/*.tif
%{_datadir}/hyrax/data/gdal/*.txt
%{_datadir}/hyrax/data/gdal/*.TIF
%doc %{_datadir}/hyrax/data/gdal/README

# [opendap-hdf4_handler]
#%doc modules/hdf4_handler/{COPYRIGHT_URI,ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/h4.conf
%attr(755,root,root) %{_libdir}/bes/libhdf4_module.so
%dir %{_datadir}/hyrax/data/hdf4
%{_datadir}/hyrax/data/hdf4/*.HDF.gz
%{_datadir}/hyrax/data/hdf4/*.hdf.gz
%{_datadir}/hyrax/data/hdf4/grid_1_2d.hdf

# [opendap-hdf5_handler]
#%doc modules/hdf5_handler/{ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/h5.conf
%attr(755,root,root) %{_libdir}/bes/libhdf5_module.so
%dir %{_datadir}/hyrax/data/hdf5
%{_datadir}/hyrax/data/hdf5/grid_1_2d.h5

# [opendap-ncml_module]
#%doc modules/ncml_module/{COPYRIGHT,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/bes/libncml_module.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/ncml.conf
#XXX %dir %{_datadir}/hyrax/data/nc
%{_datadir}/hyrax/data/nc/jan.nc
%{_datadir}/hyrax/data/nc/feb.nc
%dir %{_datadir}/hyrax/data/ncml
%{_datadir}/hyrax/data/ncml/fnoc1.nc
%{_datadir}/hyrax/data/ncml/*.ncml
%dir %{_datadir}/hyrax/data/ncml/agg
%{_datadir}/hyrax/data/ncml/agg/*.ncml
%dir %{_datadir}/hyrax/data/ncml/agg/dated
%{_datadir}/hyrax/data/ncml/agg/dated/*.nc
%dir %{_datadir}/hyrax/data/ncml/agg/grids
%{_datadir}/hyrax/data/ncml/agg/grids/*.hdf

# [opendap-netcdf_handler]
#%doc modules/netcdf_handler/{COPYRIGHT,ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/nc.conf
%attr(755,root,root) %{_libdir}/bes/libnc_module.so
# XXX dir here? (see module_ncml)
%dir %{_datadir}/hyrax/data/nc
%{_datadir}/hyrax/data/nc/bears.nc
%{_datadir}/hyrax/data/nc/bears.nc.das
%{_datadir}/hyrax/data/nc/coads_climatology.nc
%{_datadir}/hyrax/data/nc/fnoc1.das
%{_datadir}/hyrax/data/nc/fnoc1.nc
%{_datadir}/hyrax/data/nc/fnoc1.nc.html
%{_datadir}/hyrax/data/nc/zero_length_array.nc

# [opendap-ugrid_functions]
#%doc modules/ugrid_functions/{ChangeLog,INSTALL,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/ugrid_functions.conf
%attr(755,root,root) %{_libdir}/bes/libugrid_functions.so
%dir %{_datadir}/hyrax/data/ugrids
%{_datadir}/hyrax/data/ugrids/ugrid_test_*.nc

# [opendap-xml_data_handler]
#%doc modules/xml_data_handler/{ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/xml_data_handler.conf
%attr(755,root,root) %{_libdir}/bes/libxml_data_module.so

# [dap-server]
#%doc modules/dap-server/{COPYRIGHT_*,ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/dap-server.conf
%attr(755,root,root) %{_libdir}/bes/libascii_module.so
%attr(755,root,root) %{_libdir}/bes/libusage_module.so
%attr(755,root,root) %{_libdir}/bes/libwww_module.so
%{_datadir}/bes/dap-server_help.*

# (fileout_json - new module)
#%doc modules/fileout_json/{ChangeLog,NEWS}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/fojson.conf
%attr(755,root,root) %{_libdir}/bes/libfojson_module.so

# (w10n_handler - new module)
#%doc modules/w10n_handler/{ChangeLog,NEWS}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/w10n.conf
%attr(755,root,root) %{_libdir}/bes/libw10n_handler.so

#%doc dapreader/README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/dapreader.conf
%dir %{_datadir}/hyrax/data/dapreader
%{_datadir}/hyrax/data/dapreader/fnoc1.das
%{_datadir}/hyrax/data/dapreader/fnoc1.data
%{_datadir}/hyrax/data/dapreader/fnoc1.dds
%dir %{_datadir}/hyrax/data/dapreader/dap4
%{_datadir}/hyrax/data/dapreader/dap4/dap4.html
%{_datadir}/hyrax/data/dapreader/dap4/D4-xml
%{_datadir}/hyrax/data/dapreader/dap4/dmr-testsuite

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
