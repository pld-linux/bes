# Notes on module subpackages:
# - order comes from source directories / git module names
# - individual module versions (used in Provides/Obsoletes) could be found in $DIR/NEWS files
Summary:	OPeNDAP Back End Server software framework
Summary(pl.UTF-8):	Szkielet OPeNDAP Back End Server (serwera backendu OPeNDAP)
Name:		bes
Version:	3.17.1
Release:	5
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://www.opendap.org/pub/source/%{name}-%{version}.tar.gz
# Source0-md5:	09d5f49ff524d6981d6418643c674d16
Patch0:		%{name}-conf.patch
Patch1:		%{name}-configure.patch
Patch2:		%{name}-link.patch
URL:		https://www.opendap.org/
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

%package module-dapreader
Summary:	OpeNDAP BES dapreader module
Summary(pl.UTF-8):	Moduł dapreader dla serwera OpeNDAP BES
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description module-dapreader
This module can be used by the BES to return DAP2 and DAP4 responses
using simple input files.

%description module-dapreader -l pl.UTF-8
Ten moduł może być używany przez BES do zwracania odpowiedzi DAP2 i
DAP4 przy użyciu prostych plików wejściowych.

%package module-handler-csv
Summary:	CSV module for the OPeNDAP BES server
Summary(pl.UTF-8):	Moduł CSV dla serwera OPeNDAP BES
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	opendap-csv_handler = 1.1.3
Obsoletes:	opendap-csv_handler < 1.1.3
# old name (single v3.5.1 release from 2010)
Obsoletes:	opendap-csv_module

%description module-handler-csv
This is the CSV handler module for the OPeNDAP data server. It serves
data stored in CSV-formatted files.

%description module-handler-csv -l pl.UTF-8
Ten pakiet zawiera moduł obsługi CSV dla serwera danych OPeNDAP.
Serwuje dane zapisane w plikach w formacie CSV.

%package module-dap-server
Summary:	Basic request handling for OPeNDAP servers
Summary(pl.UTF-8):	Podstawowa obsługa żądań dla serwerów OPeNDAP
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	dap-server = 4.2.3
Obsoletes:	dap-server < 4.2.3

%description module-dap-server
This package contains general purpose handlers for use with the new
Hyrax data server. These are the Usage, ASCII and HTML form handlers.
Each takes input from a 'data handler' and returns a HTML or plain
text response - something other than a DAP response object.

%description module-dap-server -l pl.UTF-8
Ten pakiet zawiera kilka procedur obsługi ogólnego przeznaczenia dla
nowego serwera danych Hyrax. Są to procedury obsługi Usage, ASCII oraz
formularzy HTML. Każdy z nich pobiera wejście z procedury obsługi
danych i zwraca odpowiedź w formacie HTML lub czystego tekstu - czegoś
innego, niż obiekt odpowiedzi DAP.

%package module-fileout-gdal
Summary:	OPeNDAP BES server module to return a GeoTiff, JP2k, etc., file for a DAP Data response
Summary(pl.UTF-8):	Moduł serwera OPeNDAP BES zwracający pliki GeoTiff, JP2k itp. jako odpowiedź DAP
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gdal >= 1.10.0
Provides:	opendap-fileout_gdal = 0.9.8
Obsoletes:	opendap-fileout_gdal < 0.9.8

%description module-fileout-gdal
This is the fileout GDAL response handler for Hyrax - the OPeNDAP data
server. With this handler a server can easily be configured to return
data packaged in a GeoTiff, JP2, etc., file.

%description module-fileout-gdal -l pl.UTF-8
Ten pakiet zawiera moduł serwera danych OPeNDAP (Hyrax) obsługujący
odpowiedzi GDAL. Przy jego użyciu można łatwo skonfigurować serwer,
aby zwracał dane spakowane w pliku GeoTiff, JP2 itp.

%package module-fileout-json
Summary:	OPeNDAP BES server module to return JSON responses
Summary(pl.UTF-8):	Moduł serwera OPeNDAP BES zwracający odpowiedzi JSON
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	opendap-fileout_json = 1.0.3

%description module-fileout-json
This is the fileout JSON response handler for Hyrax - the OPeNDAP data
server.

%description module-fileout-json -l pl.UTF-8
Ten pakiet zawiera moduł serwera danych OPeNDAP (Hyrax) obsługujący
odpowiedzi JSON.

%package module-fileout-netcdf
Summary:	OPeNDAP BES server module to return a NetCDF file for a DAP Data response
Summary(pl.UTF-8):	Moduł serwera OPeNDAP BES zwracający pliki NetCDF jako odpowiedź DAP
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	opendap-fileout_netcdf = 1.4.0
Obsoletes:	opendap-fileout_netcdf = 1.4.0

%description module-fileout-netcdf
This is the fileout netCDF response handler for Hyrax - the OPeNDAP
data server. With this handler a server can easily be configured to
return data packaged in a netCDF 3 file.

%description module-fileout-netcdf -l pl.UTF-8
Ten pakiet zawiera moduł serwera danych OPeNDAP (Hyrax) obsługujący
odpowiedzi netCDF. Przy jego użyciu można łatwo skonfigurować serwer,
aby zwracał dane spakowane w pliku netCDF 3.

%package module-handler-fits
Summary:	FITS data handler module for the OPeNDAP BES data server
Summary(pl.UTF-8):	Moduł obsługujący dane FITS dla serwera danych OPeNDAP BES
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	opendap-fits_handler = 1.0.15
Obsoletes:	opendap-fits_handler < 1.0.15

%description module-handler-fits
This is the FITS data handler module for the OPeNDAP data server. It
reads FITS data and returns DAP responses that are compatible with
DAP2 and the dap-server software.

%description module-handler-fits -l pl.UTF-8
Ten pakiet zawiera moduł obsługujący dane FITS dla serwera danych
OPeNDAP. Odczytuje dane FITS i zwraca odpowiedzi DAP zgodne z
oprogramowaniem DAP2 i dap-server.

%package module-handler-freeform
Summary:	FreeForm data handler module for the OPeNDAP BES data server
Summary(pl.UTF-8):	Moduł obsługujący dane FreeForm dla serwera danych OPeNDAP BES
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	opendap-freeform_handler = 3.9.3
Obsoletes:	opendap-freeform_handler < 3.9.3

%description module-handler-freeform
This is the FreeForm data handler module for the OPeNDAP data server.
It reads ASCII, binary and DB4 files which have been described using
FreeForm and returns DAP responses that are compatible with DAP2 and
the dap-server software.

%description module-handler-freeform -l pl.UTF-8
Ten pakiet zawiera moduł obsługujący dane FreeForm dla serwera danych
OPeNDAP. Odczytuje dane z plików ASCII, binarnych i DB4 opisane przy
użyciu FreeForm i zwraca odpowiedzi DAP zgodne z oprogramowaniem DAP2
i dap-server.

%package module-gateway
Summary:	Gateway module for the OPeNDAP BES data server
Summary(pl.UTF-8):	Moduł bramki dla serwera danych OPeNDAP BES
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	opendap-gateway_module = 1.1.6
Obsoletes:	opendap-gateway_module < 1.1.6

%description module-gateway
This is the Gateway module for the OPeNDAP data server. It allows a
remote URL to be passed as a container to the BES, have that remote
URL accessed, and served locally.

%description module-gateway -l pl.UTF-8
Ten pakiet zawiera moduł bramki (Gateway) dla serwera danych OPeNDAP.
Pozwala na przekazanie zdalnego URL-a jako kontenera do BES, który
odwołuje się do tego zdalnego URL-a i serwuje go lokalnie.

%package module-handler-gdal
Summary:	GDAL data handler module for the OPeNDAP BES data server
Summary(pl.UTF-8):	Moduł obsługujący dane GDAL dla serwera danych OPeNDAP BES
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gdal >= 1.10.0
Provides:	opendap-gdal_handler = 1.0.3
Obsoletes:	opendap-gdal_handler < 1.0.3

%description module-handler-gdal
This is the GDAL data handler module for the OPeNDAP data server. It
should be able to serve any file that can be read using the GDAL
library.

%description module-handler-gdal -l pl.UTF-8
Ten pakiet zawiera moduł obsługujący dane GDAL dla serwera danych
OPeNDAP. Powinien być w stanie zaserwować dowolny plik, który można
odczytać przy użyciu biblioteki GDAL.

%package module-handler-hdf4
Summary:	HDF4 data handler module for the OPeNDAP BES data server
Summary(pl.UTF-8):	Moduł obsługujący dane HDF4 dla serwera danych OPeNDAP BES
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	opendap-hdf4_handler = 3.12.0
Obsoletes:	opendap-hdf4_handler < 3.12.0

%description module-handler-hdf4
This is the HDF4 data handler module for the OPeNDAP data server. It
reads HDF4 and HDF-EOS2 files and returns DAP responses that are
compatible with DAP2 and the dap-server software.

%description module-handler-hdf4 -l pl.UTF-8
Ten pakiet zawiera moduł obsługujący dane HDF4 dla serwera danych
OPeNDAP. Odczytuje pliki HDF4 oraz HDF-EOS2 i zwraca odpowiedzi DAP
zgodne z oprogramowaniem DAP2 i dap-server.

%package module-handler-hdf5
Summary:	HDF5 data handler module for the OPeNDAP BES data server
Summary(pl.UTF-8):	Moduł obsługujący dane HDF5 dla serwera danych OPeNDAP BES
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	opendap-hdf5_handler = 2.3.2
Obsoletes:	opendap-hdf5_handler < 2.3.2

%description module-handler-hdf5
This is the HDF5 data handler module for the OPeNDAP data server. It
reads HDF5 files and returns DAP responses that are compatible with
DAP2 and the dap-server software.

%description module-handler-hdf5 -l pl.UTF-8
Ten pakiet zawiera moduł obsługujący dane HDF5 dla serwera danych
OPeNDAP. Odczytuje pliki HDF5 i zwraca odpowiedzi DAP zgodne z
oprogramowaniem DAP2 i dap-server.

%package module-ncml
Summary:	NCML module for the OPeNDAP BES data server
Summary(pl.UTF-8):	Moduł NCML dla serwera danych OPeNDAP BES
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	opendap-ncml_module = 1.4.1
Obsoletes:	opendap-ncml_module < 1.4.1

%description module-ncml
This is the NcML module for the OPeNDAP data server. It parses NcML
files to add metadata to other local datasets on the local Hyrax
server. It also allows authors to create joinNew and union
aggregations of other datasets.

%description module-ncml -l pl.UTF-8
Ten pakiet zawiera moduł NcML dla serwera danych OPeNDAP. Analizuje
pliki NcML w celu dodania metadanych do innych lokalnych zbiorów
danych na lokalnym serwerze Hyrax. Ponadto pozwala autorom na
tworzenie agregatów joinNew i union innych zbiorów danych.

%package module-handler-netcdf
Summary:	NetCDF 3 data handler module for the OPeNDAP BES data server
Summary(pl.UTF-8):	Moduł obsługujący dane NetCDF 3 dla serwera danych OPeNDAP BES
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	opendap-netcdf_handler = 3.11.3
Obsoletes:	opendap-netcdf_handler < 3.11.3

%description module-handler-netcdf
This is the NetCDF data handler module for the OPeNDAP data server. It
reads NetCDF 3 files and returns DAP responses that are compatible
with DAP2 and the dap-server software.

%description module-handler-netcdf -l pl.UTF-8
Ten pakiet zawiera moduł obsługujący dane NetCDF dla serwera danych
OPeNDAP. Odczytuje pliki NetCDF 3 i zwraca odpowiedzi DAP zgodne z
oprogramowaniem DAP2 i dap-server.

%package module-functions-ugrid
Summary:	ugrid functions handler for the OPeNDAP BES data server
Summary(pl.UTF-8):	Moduł obsługi funkcji ugrid dla serwera danych OPeNDAP BES
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gridfields >= 1.0.5
Provides:	opendap-ugrid_functions = 1.0.5
Obsoletes:	opendap-ugrid_functions < 1.0.5

%description module-functions-ugrid
This is the ugrid (Unstructured Grid or irregular mesh) subsetting
function handler for Hyrax. This Hyrax server function will subset a
compliant ugrid mesh and return a mesh that is also compliant. The
subset can be specified using latitude, longitude and time.

%description module-functions-ugrid -l pl.UTF-8
Ten pakiet zawiera moduł ugrid (Unstructured Grid - tablicy bez
struktury lub maski nieregularnej) obsługujący funkcję podzbioru dla
serwera Hyrax. Funkcja serwera wyliczy podzbiór zgodny z siatką ugrid
i zwróci także zgodną siatkę. Podzbiór może być określony przy użyciu
szerokości, długości i czasu.

%package module-handler-w10n
Summary:	w10n data handler module for the OPeNDAP BES data server
Summary(pl.UTF-8):	Moduł obsługujący dane w10n dla serwera danych OPeNDAP BES
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	opendap-w10n_handler = 1.0.3

%description module-handler-w10n
This package provides w10n navigation and data retrieval for Hyrax
data server.

%description module-handler-w10n -l pl.UTF-8
Ten pakiet zapewnia nawigację oraz odtwarzanie danych w10n dla serwera
danych Hyrax.

%package module-handler-xml_data
Summary:	Basic request handling the OPeNDAP BES data server
Summary(pl.UTF-8):	Obsługa podstawowych zapytań dla serwera danych OPeNDAP BES
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	opendap-xml_data_handler = 1.0.9
Obsoletes:	opendap-xml_data_handler < 1.0.9

%description module-handler-xml_data
This package contains a general purpose handler for use with the Hyrax
data server. This handler takes input from a 'data handler' and
returns XML document that encodes both dataset metadata and values. It
is intended to be used for small data requests and web systems that
need data in XML documents.

%description module-handler-xml_data -l pl.UTF-8
Ten pakiet zawiera moduł obsługi ogólnego przeznaczenia przeznaczony
dla serwera danych Hyrax. Moduł ten przyjmuje dane wejściowe z modułu
obsługi danych (data handler) i zwraca dokuemnt XML, zawierający
zakodowane zarówno metadane, jak i wartości zbioru danych. Jest
przeznaczony do użycia dla ządań małych danych oraz systemów WWW
wymagających danych w dokumentach XML.

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
	--with-hdfeos2 \
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

%files module-dapreader
%defattr(644,root,root,755)
%doc dapreader/README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/dapreader.conf
%attr(755,root,root) %{_libdir}/bes/libdapreader_module.so
%dir %{_datadir}/hyrax/data/dapreader
%{_datadir}/hyrax/data/dapreader/fnoc1.das
%{_datadir}/hyrax/data/dapreader/fnoc1.data
%{_datadir}/hyrax/data/dapreader/fnoc1.dds
%dir %{_datadir}/hyrax/data/dapreader/dap4
%{_datadir}/hyrax/data/dapreader/dap4/dap4.html
%{_datadir}/hyrax/data/dapreader/dap4/D4-xml
%{_datadir}/hyrax/data/dapreader/dap4/dmr-testsuite

%files module-handler-csv
%defattr(644,root,root,755)
%doc modules/csv_handler/{COPYRIGHT,ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/csv.conf
%attr(755,root,root) %{_libdir}/bes/libcsv_module.so
%dir %{_datadir}/hyrax/data/csv
%{_datadir}/hyrax/data/csv/temperature.csv

%files module-dap-server
%defattr(644,root,root,755)
%doc modules/dap-server/{COPYRIGHT_*,ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/dap-server.conf
%attr(755,root,root) %{_libdir}/bes/libascii_module.so
%attr(755,root,root) %{_libdir}/bes/libusage_module.so
%attr(755,root,root) %{_libdir}/bes/libwww_module.so
%{_datadir}/bes/dap-server_help.*

%files module-fileout-gdal
%defattr(644,root,root,755)
%doc modules/fileout_gdal/{ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/fong.conf
%attr(755,root,root) %{_libdir}/bes/libfong_module.so

%files module-fileout-json
%defattr(644,root,root,755)
%doc modules/fileout_json/{ChangeLog,NEWS}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/fojson.conf
%attr(755,root,root) %{_libdir}/bes/libfojson_module.so

%files module-fileout-netcdf
%defattr(644,root,root,755)
%doc modules/fileout_netcdf/{COPYRIGHT,ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/fonc.conf
%attr(755,root,root) %{_libdir}/bes/libfonc_module.so

%files module-handler-fits
%defattr(644,root,root,755)
%doc modules/fits_handler/{COPYRIGHT,ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/fits.conf
%attr(755,root,root) %{_libdir}/bes/libfits_module.so
%dir %{_datadir}/hyrax/data/fits
%{_datadir}/hyrax/data/fits/*.fts

%files module-handler-freeform
%defattr(644,root,root,755)
%doc modules/freeform_handler/{COPYRIGHT,ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/ff.conf
%attr(755,root,root) %{_libdir}/bes/libff_module.so
%dir %{_datadir}/hyrax/data/ff
%{_datadir}/hyrax/data/ff/*.dat
%{_datadir}/hyrax/data/ff/*.dat.das
%{_datadir}/hyrax/data/ff/*.fmt

%files module-gateway
%defattr(644,root,root,755)
%doc modules/gateway_module/{COPYRIGHT,ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/gateway.conf
%attr(755,root,root) %{_libdir}/bes/libgateway_module.so

%files module-handler-gdal
%defattr(644,root,root,755)
%doc modules/gdal_handler/{ChangeLog,NEWS,README}
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

%files module-handler-hdf4
%defattr(644,root,root,755)
%doc modules/hdf4_handler/{COPYRIGHT_URI,ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/h4.conf
%attr(755,root,root) %{_libdir}/bes/libhdf4_module.so
%dir %{_datadir}/hyrax/data/hdf4
%{_datadir}/hyrax/data/hdf4/*.HDF.gz
%{_datadir}/hyrax/data/hdf4/*.hdf.gz
%{_datadir}/hyrax/data/hdf4/grid_1_2d.hdf

%files module-handler-hdf5
%defattr(644,root,root,755)
%doc modules/hdf5_handler/{ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/h5.conf
%attr(755,root,root) %{_libdir}/bes/libhdf5_module.so
%dir %{_datadir}/hyrax/data/hdf5
%{_datadir}/hyrax/data/hdf5/grid_1_2d.h5

%files module-ncml
%defattr(644,root,root,755)
%doc modules/ncml_module/{COPYRIGHT,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/bes/libncml_module.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/ncml.conf
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

%files module-handler-netcdf
%defattr(644,root,root,755)
%doc modules/netcdf_handler/{COPYRIGHT,ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/nc.conf
%attr(755,root,root) %{_libdir}/bes/libnc_module.so
%dir %{_datadir}/hyrax/data/nc
%{_datadir}/hyrax/data/nc/bears.nc
%{_datadir}/hyrax/data/nc/bears.nc.das
%{_datadir}/hyrax/data/nc/coads_climatology.nc
%{_datadir}/hyrax/data/nc/fnoc1.das
%{_datadir}/hyrax/data/nc/fnoc1.nc
%{_datadir}/hyrax/data/nc/fnoc1.nc.html
%{_datadir}/hyrax/data/nc/zero_length_array.nc

%files module-functions-ugrid
%defattr(644,root,root,755)
%doc modules/ugrid_functions/{ChangeLog,INSTALL,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/ugrid_functions.conf
%attr(755,root,root) %{_libdir}/bes/libugrid_functions.so
%dir %{_datadir}/hyrax/data/ugrids
%{_datadir}/hyrax/data/ugrids/ugrid_test_*.nc

%files module-handler-w10n
%defattr(644,root,root,755)
%doc modules/w10n_handler/{ChangeLog,NEWS}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/w10n.conf
%attr(755,root,root) %{_libdir}/bes/libw10n_handler.so

%files module-handler-xml_data
%defattr(644,root,root,755)
%doc modules/xml_data_handler/{ChangeLog,NEWS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/xml_data_handler.conf
%attr(755,root,root) %{_libdir}/bes/libxml_data_module.so

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
