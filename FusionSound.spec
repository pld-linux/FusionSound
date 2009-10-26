Summary:	Audio sub system for multiple applications
Summary(pl.UTF-8):	Dźwiękowy podsystem dla złożonych aplikacji
Name:		FusionSound
Version:	1.1.1
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/downloads/Core/%{name}-%{version}.tar.gz
# Source0-md5:	f29b0e6bb693e59b7303c163c737a39b
Patch0:		%{name}-conf.patch
Patch1:		%{name}-git.patch
Patch2:		%{name}-leck.patch
Patch3:		compile.patch
URL:		http://www.directfb.org/index.php?path=Platform/FusionSound
BuildRequires:	DirectFB-devel >= 1:1.2.0
# for examples
BuildRequires:	LiTE-devel >= 0.8.9
BuildRequires:	alsa-lib-devel >= 0.9
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	ffmpeg-devel >= 0.4.9-4.20080822
BuildRequires:	libcddb-devel >= 1.0.0
BuildRequires:	libmad-devel
BuildRequires:	libtimidity-devel >= 0.1.0
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1:1.0.0
BuildRequires:	pkgconfig >= 1:0.9
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
Requires:	DirectFB-devel >= 1:1.2.0

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

%package musicprovider-cdda
Summary:	CD-DA music provider module for FusionSound
Summary(pl.UTF-8):	Moduł FusionSound dostarczający muzykę CD-DA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description musicprovider-cdda
CD-DA music provider module for FusionSound.

%description musicprovider-cdda -l pl.UTF-8
Moduł FusionSound dostarczający muzykę CD-DA.

%package musicprovider-ffmpeg
Summary:	ffmpeg music provider module for FusionSound
Summary(pl.UTF-8):	Moduł FusionSound dostarczający muzykę przez ffmpeg
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description musicprovider-ffmpeg
ffmpeg music provider module for FusionSound.

%description musicprovider-ffmpeg -l pl.UTF-8
Moduł FusionSound dostarczający muzykę przez ffmpeg.

%package musicprovider-mad
Summary:	MP3 libmad music provider module for FusionSound
Summary(pl.UTF-8):	Moduł FusionSound dostarczający muzykę MP3 przez libmad
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description musicprovider-mad
MP3 music provider module for FusionSound.

%description musicprovider-mad -l pl.UTF-8
Moduł FusionSound dostarczający muzykę MP3 przez libmad.

%package musicprovider-timidity
Summary:	MIDI libtimidity music provider module for FusionSound
Summary(pl.UTF-8):	Moduł FusionSound dostarczający muzykę MIDI przez libtimidity
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description musicprovider-timidity
MIDI libtimidity music provider module for FusionSound.

%description musicprovider-timidity -l pl.UTF-8
Moduł FusionSound dostarczający muzykę MIDI przez libtimidity.

%package musicprovider-vorbis
Summary:	Ogg Vorbis music provider module for FusionSound
Summary(pl.UTF-8):	Moduł FusionSound dostarczający muzykę Ogg Vorbis
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description musicprovider-vorbis
Ogg Vorbis music provider module for FusionSound.

%description musicprovider-vorbis -l pl.UTF-8
Moduł FusionSound dostarczający muzykę Ogg Vorbis.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static
%{__make} \
	FFMPEG_CFLAGS="-I/usr/include/libavcodec -I/usr/include/libavformat"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post 	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO docs/html/[!M]*
%attr(755,root,root) %{_bindir}/fsdump
%attr(755,root,root) %{_bindir}/fsmaster
%attr(755,root,root) %{_bindir}/fsplay
%attr(755,root,root) %{_bindir}/fsproxy
%attr(755,root,root) %{_bindir}/fsvolume
%attr(755,root,root) %{_libdir}/libfusionsound-1.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfusionsound-1.1.so.1
%dir %{_libdir}/directfb-1.2-0/interfaces/IFusionSound
%attr(755,root,root) %{_libdir}/directfb-1.2-0/interfaces/IFusionSound/libifusionsound.so
%attr(755,root,root) %{_libdir}/directfb-1.2-0/interfaces/IFusionSound/libifusionsound_dispatcher.so
%attr(755,root,root) %{_libdir}/directfb-1.2-0/interfaces/IFusionSound/libifusionsound_requestor.so
%dir %{_libdir}/directfb-1.2-0/interfaces/IFusionSoundBuffer
%attr(755,root,root) %{_libdir}/directfb-1.2-0/interfaces/IFusionSoundBuffer/libifusionsoundbuffer_dispatcher.so
%attr(755,root,root) %{_libdir}/directfb-1.2-0/interfaces/IFusionSoundBuffer/libifusionsoundbuffer_requestor.so
%dir %{_libdir}/directfb-1.2-0/interfaces/IFusionSoundMusicProvider
%attr(755,root,root) %{_libdir}/directfb-1.2-0/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_playlist.so
%attr(755,root,root) %{_libdir}/directfb-1.2-0/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_wave.so
%dir %{_libdir}/directfb-1.2-0/interfaces/IFusionSoundPlayback
%attr(755,root,root) %{_libdir}/directfb-1.2-0/interfaces/IFusionSoundPlayback/libifusionsoundplayback_dispatcher.so
%attr(755,root,root) %{_libdir}/directfb-1.2-0/interfaces/IFusionSoundPlayback/libifusionsoundplayback_requestor.so
%dir %{_libdir}/directfb-1.2-0/interfaces/IFusionSoundStream
%attr(755,root,root) %{_libdir}/directfb-1.2-0/interfaces/IFusionSoundStream/libifusionsoundstream_dispatcher.so
%attr(755,root,root) %{_libdir}/directfb-1.2-0/interfaces/IFusionSoundStream/libifusionsoundstream_requestor.so
%dir %{_libdir}/directfb-1.2-0/snddrivers
%attr(755,root,root) %{_libdir}/directfb-1.2-0/snddrivers/libfusionsound_alsa.so
%attr(755,root,root) %{_libdir}/directfb-1.2-0/snddrivers/libfusionsound_oss.so
%attr(755,root,root) %{_libdir}/directfb-1.2-0/snddrivers/libfusionsound_wave.so
%{_mandir}/man5/fusionsoundrc.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfusionsound.so
%{_libdir}/libfusionsound.la
%{_includedir}/fusionsound
%{_includedir}/fusionsound-internal
%{_pkgconfigdir}/fusionsound.pc
%{_pkgconfigdir}/fusionsound-internal.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libfusionsound.a
# .la makes no sense in -devel (it's module); here for DFB static linking hacks
%{_libdir}/directfb-1.2-0/interfaces/IFusionSound/lib*.[la]*
%{_libdir}/directfb-1.2-0/interfaces/IFusionSoundBuffer/lib*.[la]*
%{_libdir}/directfb-1.2-0/interfaces/IFusionSoundMusicProvider/lib*.[la]*
%{_libdir}/directfb-1.2-0/interfaces/IFusionSoundPlayback/lib*.[la]*
%{_libdir}/directfb-1.2-0/interfaces/IFusionSoundStream/lib*.[la]*
%{_libdir}/directfb-1.2-0/snddrivers/libfusionsound*.[la]*

%files musicprovider-cdda
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/directfb-1.2-0/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_cdda.so

%files musicprovider-ffmpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/directfb-1.2-0/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_ffmpeg.so

%files musicprovider-mad
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/directfb-1.2-0/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_mad.so

%files musicprovider-timidity
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/directfb-1.2-0/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_timidity.so

%files musicprovider-vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/directfb-1.2-0/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_vorbis.so
