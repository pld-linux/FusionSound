Summary:	Audio sub system for multiple applications
Summary(pl):	D�wi�kowy podsystem dla z�o�onych aplikacji
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
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FusionSound supports multiple applications using Fusion IPC. It
provides streams, static sound buffers and control over any number of
concurrent playbacks. Sample data is always stored in shared memory,
starting a playback simply adds an entry to the playlist of the mixer
thread in the master application.

%description -l pl
FusionSound wspiera z�o�one aplikacje u�ywaj�ce Fusion IPC. Dostarcza
strumieni, statyczny bufor dzwi�kowy i kontrol� poprzez ka�d� ilo��
konkurencyjnych odtwarzaczy. Pr�bkowana dana jest zawsze przechowywana
w pami�ci dzielonej. Rozpoczynaj�c odtwarzanie dodaje wej�cie do listy
odtwarzania miksera w nadrz�dnej aplikacji.

%package devel
Summary:	Development files for the FusionSound
Summary(pl):	Pliki rozwojowe dla FusionSound
Group:		Development/Libraries
Requires:	DirectFB-devel >= 0.9.20
# doesn't require base

%description devel
Header files required for development using FusionSound.

%description devel -l pl
Pliki nag��wkowe wymagane do tworzenia program�w z u�yciem
FusionSound.

%package static
Summary:	Static FusionSound library
Summary(pl):	Statyczna biblioteka FusionSound
Group:		Development/Libraries
# base for directory, -devel for headers
Requires:	%{name} = %{version}
Requires:	%{name}-devel = %{version}

%description static
Static FusionSound library.

%description static -l pl
Statyczna biblioteka FusionSound.

%prep
%setup -q
%patch0 -p1

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
%dir %{_libdir}/directfb-*/interfaces/IFusionSound
%attr(755,root,root) %{_libdir}/directfb-*/interfaces/IFusionSound/lib*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/fusionsound
%{_pkgconfigdir}/*.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
# .la makes no sense in -devel (it's module); here for DFB static linking hacks
%{_libdir}/directfb-*/interfaces/IFusionSound/lib*.la
%{_libdir}/directfb-*/interfaces/IFusionSound/lib*.a
