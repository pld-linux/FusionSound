Summary:	Audio sub system for multiple applications
Summary(pl):	D¼wiêkowy podsystem dla z³o¿onych aplikacji
Name:		FusionSound
Version:	0.9.19
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.directfb.org/download/FusionSound/%{name}-%{version}.tar.gz
# Source0-md5:	433214d60e7a1147103abf55717f2f80
URL:		http://www.directfb.org/fusionsound.xml
Patch0:		%{name}-conf.patch
BuildRequires:	DirectFB-devel >= 0.9.20
BuildRequires:	autoconf
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FusionSound supports multiple applications using Fusion IPC. It
provides streams, static sound buffers and control over any number of
concurrent playbacks. Sample data is always stored in shared memory,
starting a playback simply adds an entry to the playlist of the mixer
thread in the master application.

%description -l pl
FusionSound wspiera z³o¿one aplikacje u¿ywaj±ce Fusion IPC. Dostarcza
strumieni, statyczny bufor dzwiêkowy i kontrolê poprzez ka¿d± ilo¶æ
konkurencyjnych odtwarzaczy. Próbkowana dana jest zawsze przechowywana
w pamiêci dzielonej. Rozpoczynaj±c odtwarzanie dodaje wej¶cie do listy
odtwarzania miksera w nadrzêdnej aplikacji.

%package devel
Summary:	Development files for the FusionSound
Summary(pl):	Pliki rozwojowe dla FusionSound
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files required for development using FusionSound.

%description devel -l pl
Pliki nag³ówkowe wymagane do tworzenia programów z u¿yciem
FusionSound.

%package static
Summary:	Static FusionSound library
Summary(pl):	Statyczna biblioteka FusionSound
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static FusionSound library.

%description static -l pl
Statyczna biblioteka FusionSound.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
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
%attr(755,root,root) %{_libdir}/directfb-*/interfaces/IFusionSound/lib*.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/directfb-*/interfaces/IFusionSound/lib*.la
%{_includedir}/fusionsound/*.h
%{_pkgconfigdir}/*.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/directfb-*/interfaces/IFusionSound/lib*.a
