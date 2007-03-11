Summary:	Audio sub system for multiple applications
Summary(pl.UTF-8):	Dźwiękowy podsystem dla złożonych aplikacji
Name:		FusionSound
Version:	1.0.0
%define	bver	rc1
Release:	0.%{bver}.1
License:	GPL
Group:		Libraries
Source0:	http://www.directfb.org/downloads/Core/%{name}-%{version}-%{bver}.tar.gz
# Source0-md5:	b9a64ec13b57763e53b13ba4bec86f90
Patch0:		%{name}-conf.patch
URL:		http://www.directfb.org/index.php?path=Development/Projects/FusionSound
BuildRequires:	DirectFB-devel >= 1:%{version}
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FusionSound supports multiple applications using Fusion IPC. It
provides streams, static sound buffers and control over any number of
concurrent playbacks. Sample data is always stored in shared memory,
starting a playback simply adds an entry to the playlist of the mixer
thread in the master application.

%description -l pl.UTF-8
FusionSound wspiera złożone aplikacje używające Fusion IPC. Dostarcza
strumieni, statyczny bufor dźwiękowy i kontrolę poprzez każdą ilość
konkurencyjnych odtwarzaczy. Próbkowana dana jest zawsze przechowywana
w pamięci dzielonej. Rozpoczynając odtwarzanie dodaje wejście do listy
odtwarzania miksera w nadrzędnej aplikacji.

%package devel
Summary:	Development files for the FusionSound
Summary(pl.UTF-8):	Pliki rozwojowe dla FusionSound
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	DirectFB-devel >= 1:%{version}

%description devel
Header files required for development using FusionSound.

%description devel -l pl.UTF-8
Pliki nagłówkowe wymagane do tworzenia programów z użyciem
FusionSound.

%package static
Summary:	Static FusionSound library
Summary(pl.UTF-8):	Statyczna biblioteka FusionSound
Group:		Development/Libraries
# base for directory, -devel for headers
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static FusionSound library.

%description static -l pl.UTF-8
Statyczna biblioteka FusionSound.

%prep
%setup -q -n %{name}-%{version}-%{bver}
%patch0 -p1

# temporary hack for 1.0.0-rc*
sed -i -e 's/^DIRECTFB_REQUIRED_VERSION=.*/DIRECTFB_REQUIRED_VERSION=1.0.0/' configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post 	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO docs/html/[!M]*
%attr(755,root,root) %{_bindir}/fsdump
%attr(755,root,root) %{_bindir}/fsmaster
%attr(755,root,root) %{_libdir}/libfusionsound-*.so.*.*.*
%dir %{_libdir}/directfb-*/interfaces/IFusionSound
%attr(755,root,root) %{_libdir}/directfb-*/interfaces/IFusionSound/lib*.so
%dir %{_libdir}/directfb-*/interfaces/IFusionSoundMusicProvider
%attr(755,root,root) %{_libdir}/directfb-*/interfaces/IFusionSoundMusicProvider/lib*.so
%dir %{_libdir}/directfb-*/snddrivers
%attr(755,root,root) %{_libdir}/directfb-*/snddrivers/libfusionsound*.so
%{_mandir}/man5/fusionsoundrc.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfusionsound.so
%{_libdir}/libfusionsound.la
%{_includedir}/fusionsound
%{_includedir}/fusionsound-internal
%{_pkgconfigdir}/*.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libfusionsound.a
# .la makes no sense in -devel (it's module); here for DFB static linking hacks
%{_libdir}/directfb-*/interfaces/IFusionSound/lib*.[la]*
%{_libdir}/directfb-*/interfaces/IFusionSoundMusicProvider/lib*.[la]*
%{_libdir}/directfb-*/snddrivers/libfusionsound*.[la]*
