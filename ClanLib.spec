%define	cvmajor	2.0
Summary:	ClanLib, the platform independent game SDK
Summary(pl.UTF-8):	ClanLib, niezależny od platformy SDK do gier
Summary(pt_BR.UTF-8):	SDK Clanlib
Name:		ClanLib
Version:	2.0.2
Release:	1
License:	BSD-like (see COPYING)
Group:		Libraries
#Source0Download: http://www.clanlib.org/download.html
Source0:	http://www.clanlib.org/download/releases-2.0/%{name}-%{version}.tgz
# Source0-md5:	81a9e30e035fbb73a698813f67289505
Patch0:		%{name}-build.patch
URL:		http://www.clanlib.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL >= 1.2.0
BuildRequires:	SDL_gfx-devel >= 1.2.0
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1.6
BuildRequires:	libjpeg-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libpng-devel >= 1.%{cvmajor}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	libxslt-progs
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
Obsoletes:	ClanLib-TTF
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
The ClanLib SDK is designed to provide an platform independent game
SDK using a lot cleaner (and object oriented) interface than the
traditional way it is done in DirectX, SDL and such. The goal is to
avoid game developers constantly reinventing the wheel by providing
smarter ways to eg. load surfaces.

%description -l pl.UTF-8
ClanLib SDK jest projektowany jako niezależny od platformy SDK dla
gier. Stosuje prosty (i zorientowany obiektowo) interfejs,
przejrzystszy niż DirectX, SDL i inne.

%description -l pt_BR.UTF-8
A Clanlib é uma biblioteca de jogos multi-plataforma desenhada para
facilitar o trabalho dos desenvolvedores. A idéia principal é fornecer
uma interface comum para os problemas clássicos dos jogos (carregar
gráficos por exemplo).

%package devel
Summary:	ClanLib development package
Summary(pl.UTF-8):	Pakiet programistyczny dla ClanLib
Summary(pt_BR.UTF-8):	Arquivos para desenvolvimento usando a Clanlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
# for libclanDisplay
Requires:	xorg-lib-libXxf86vm-devel
Obsoletes:	ClanLib-TTF-devel

%description devel
This is the development add-on package that includes the header files
needed to compile new ClanLib applications.

%description devel -l pl.UTF-8
Programistyczne dodatki do ClanLiba, zawierają pliki nagłówkowe
potrzebne do kompilacji programów korzystających z ClanLib.

%description devel -l pt_BR.UTF-8
Arquivos que possibilitam o desenvolvimento de aplicativos utilizando
a biblioteca Clanlib.

%package static
Summary:	ClanLib static libraries
Summary(pl.UTF-8):	Statyczne biblioteki ClanLib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	ClanLib-TTF-static

%description static
This package contains static versions of ClanLib libraries.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczne wersje bibliotek ClanLib.

%package doc
Summary:	ClanLib reference documentation for programmers
Summary(pl.UTF-8):	Dokumentacja programisty do biblioteki ClanLib
Group:		Documentation

%description doc
ClanLib reference documentation for programmers.

%description doc -l pl.UTF-8
Dokumentacja programisty do biblioteki ClanLib

%package OpenGL
Summary:	OpenGL ClanLib library
Summary(pl.UTF-8):	Biblioteka OpenGL dla ClanLiba
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description OpenGL
OpenGL ClanLib library.

%description OpenGL -l pl.UTF-8
Biblioteka OpenGL dla ClanLiba.

%package OpenGL-devel
Summary:	Header files for OpenGL ClanLib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OpenGL dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-OpenGL = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	xorg-lib-libXi-devel
Requires:	xorg-lib-libXxf86vm-devel

%description OpenGL-devel
Header files for OpenGL ClanLib library.

%description OpenGL-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OpenGL dla ClanLiba.

%package OpenGL-static
Summary:	Static OpenGL ClanLib library
Summary(pl.UTF-8):	Statyczna biblioteka OpenGL dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-OpenGL-devel = %{version}-%{release}

%description OpenGL-static
Static OpenGL ClanLib library.

%description OpenGL-static -l pl.UTF-8
Statyczna biblioteka OpenGL dla ClanLiba.

%package MikMod
Summary:	MikMod ClanLib library
Summary(pl.UTF-8):	Biblioteka MikMod dla ClanLiba
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description MikMod
MikMod ClanLib library.

%description MikMod -l pl.UTF-8
Biblioteka MikMod dla ClanLiba.

%package MikMod-devel
Summary:	Header files for MikMod ClanLib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki MikMod dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-MikMod = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libmikmod-devel

%description MikMod-devel
Header files for MikMod ClanLib library.

%description MikMod-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki MikMod dla ClanLiba.

%package MikMod-static
Summary:	Static MikMod ClanLib library
Summary(pl.UTF-8):	Statyczna biblioteka MikMod dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-MikMod-devel = %{version}-%{release}

%description MikMod-static
Static MikMod ClanLib library.

%description MikMod-static -l pl.UTF-8
Statyczna biblioteka MikMod dla ClanLiba.

%package SDL
Summary:	SDL ClanLib library
Summary(pl.UTF-8):	Biblioteka SDL dla ClanLiba
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description SDL
SDL ClanLib library.

%description SDL -l pl.UTF-8
Biblioteka SDL dla ClanLiba.

%package SDL-devel
Summary:	Header files for SDL ClanLib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SDL dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-SDL = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	SDL-devel >= 1.2.0
Requires:	SDL_gfx-devel >= 1.2.0

%description SDL-devel
Header files for SDL ClanLib library.

%description SDL-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SDL dla ClanLiba.

%package SDL-static
Summary:	Static SDL ClanLib library
Summary(pl.UTF-8):	Statyczna biblioteka SDL dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-SDL-devel = %{version}-%{release}

%description SDL-static
Static SDL ClanLib library.

%description SDL-static -l pl.UTF-8
Statyczna biblioteka SDL dla ClanLiba.

%package Vorbis
Summary:	Vorbis ClanLib library
Summary(pl.UTF-8):	Biblioteka Vorbis dla ClanLiba
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description Vorbis
Vorbis ClanLib library.

%description Vorbis -l pl.UTF-8
Biblioteka Vorbis dla ClanLiba.

%package Vorbis-devel
Summary:	Header files for Vorbis ClanLib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Vorbis dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-Vorbis = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libvorbis-devel

%description Vorbis-devel
Header files for Vorbis ClanLib library.

%description Vorbis-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Vorbis dla ClanLiba.

%package Vorbis-static
Summary:	Static Vorbis ClanLib library
Summary(pl.UTF-8):	Statyczna biblioteka Vorbis dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-Vorbis-devel = %{version}-%{release}

%description Vorbis-static
Static Vorbis ClanLib library.

%description Vorbis-static -l pl.UTF-8
Statyczna biblioteka Vorbis dla ClanLiba.

%prep
%setup -q
%patch0 -p1

rm -rf autom4te.cache
echo "dnl" >> acinclude.m4

%build
# note: rtti is needed --- ClanLib uses exceptions!
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--enable-static \
	--enable-shared \
	--enable-docs \
%ifarch %{ix86}
	--enable-asm386 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug
# directfb disabled now

%{__make}

(cd Documentation/Utilities/ReferenceDocs; ln -s ../../../Sources/API ClanLib)
export PKG_CONFIG_PATH=$(pwd)/Setup/pkgconfig
%{__make} html

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-html \
	DESTDIR=$RPM_BUILD_ROOT

# missing from make install
install -d $RPM_BUILD_ROOT%{_aclocaldir}
install Setup/Unix/clanlib.m4 $RPM_BUILD_ROOT%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	OpenGL -p /sbin/ldconfig
%postun	OpenGL -p /sbin/ldconfig

%post	MikMod -p /sbin/ldconfig
%postun	MikMod -p /sbin/ldconfig

%post	SDL -p /sbin/ldconfig
%postun	SDL -p /sbin/ldconfig

%post	Vorbis -p /sbin/ldconfig
%postun	Vorbis -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING CREDITS README
%attr(755,root,root) %{_libdir}/libclanApp-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclanApp-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclanCore-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclanCore-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclanDatabase-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclanDatabase-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclanDisplay-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclanDisplay-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclanGDI-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclanGDI-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclanGUI-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclanGUI-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclanNetwork-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclanNetwork-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclanRegExp-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclanRegExp-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclanSound-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclanSound-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclanSqlite-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclanSqlite-%{cvmajor}.so.1

%files devel
%defattr(644,root,root,755)
%doc README.kdevelop UPGRADE.txt
%attr(755,root,root) %{_libdir}/libclanApp.so
%attr(755,root,root) %{_libdir}/libclanCore.so
%attr(755,root,root) %{_libdir}/libclanDatabase.so
%attr(755,root,root) %{_libdir}/libclanDisplay.so
%attr(755,root,root) %{_libdir}/libclanGDI.so
%attr(755,root,root) %{_libdir}/libclanGUI.so
%attr(755,root,root) %{_libdir}/libclanNetwork.so
%attr(755,root,root) %{_libdir}/libclanRegExp.so
%attr(755,root,root) %{_libdir}/libclanSound.so
%attr(755,root,root) %{_libdir}/libclanSqlite.so
%{_libdir}/libclanApp.la
%{_libdir}/libclanCore.la
%{_libdir}/libclanDatabase.la
%{_libdir}/libclanDisplay.la
%{_libdir}/libclanGDI.la
%{_libdir}/libclanGUI.la
%{_libdir}/libclanNetwork.la
%{_libdir}/libclanRegExp.la
%{_libdir}/libclanSound.la
%{_libdir}/libclanSqlite.la
%dir %{_includedir}/ClanLib-%{cvmajor}
%dir %{_includedir}/ClanLib-%{cvmajor}/ClanLib
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/App
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/application.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/Core
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/core.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/Database
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/database.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/Display
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/display.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/GDI
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/gdi.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/GUI*
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/gui*.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/Network
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/network.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/RegExp
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/regexp.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/Sound
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/sound.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/Sqlite
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/sqlite.h
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/clanApp-%{cvmajor}.pc
%{_pkgconfigdir}/clanCore-%{cvmajor}.pc
%{_pkgconfigdir}/clanDatabase-%{cvmajor}.pc
%{_pkgconfigdir}/clanDisplay-%{cvmajor}.pc
%{_pkgconfigdir}/clanGDI-%{cvmajor}.pc
%{_pkgconfigdir}/clanGUI*-%{cvmajor}.pc
%{_pkgconfigdir}/clanNetwork-%{cvmajor}.pc
%{_pkgconfigdir}/clanRegExp-%{cvmajor}.pc
%{_pkgconfigdir}/clanSound-%{cvmajor}.pc
%{_pkgconfigdir}/clanSqlite-%{cvmajor}.pc

%files doc
%defattr(644,root,root,755)
%{_docdir}/clanlib-*

%files static
%defattr(644,root,root,755)
%{_libdir}/libclanApp.a
%{_libdir}/libclanCore.a
%{_libdir}/libclanDatabase.a
%{_libdir}/libclanDisplay.a
%{_libdir}/libclanGDI.a
%{_libdir}/libclanGUI.a
%{_libdir}/libclanNetwork.a
%{_libdir}/libclanRegExp.a
%{_libdir}/libclanSound.a
%{_libdir}/libclanSqlite.a

%files OpenGL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanGL-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclanGL-%{cvmajor}.so.1

%files OpenGL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanGL.so
%{_libdir}/libclanGL.la
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/GL
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/gl.h
%{_pkgconfigdir}/clanGL-%{cvmajor}.pc

%files OpenGL-static
%defattr(644,root,root,755)
%{_libdir}/libclanGL.a

%files MikMod
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanMikMod-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclanMikMod-%{cvmajor}.so.1

%files MikMod-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanMikMod.so
%{_libdir}/libclanMikMod.la
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/MikMod
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/mikmod.h
%{_pkgconfigdir}/clanMikMod-%{cvmajor}.pc

%files MikMod-static
%defattr(644,root,root,755)
%{_libdir}/libclanMikMod.a

%files SDL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanSDL-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclanSDL-%{cvmajor}.so.1

%files SDL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanSDL.so
%{_libdir}/libclanSDL.la
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/SDL
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/sdl.h
%{_pkgconfigdir}/clanSDL-%{cvmajor}.pc

%files SDL-static
%defattr(644,root,root,755)
%{_libdir}/libclanSDL.a

%files Vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanVorbis-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclanVorbis-%{cvmajor}.so.1

%files Vorbis-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanVorbis.so
%{_libdir}/libclanVorbis.la
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/Vorbis
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/vorbis.h
%{_pkgconfigdir}/clanVorbis-%{cvmajor}.pc

%files Vorbis-static
%defattr(644,root,root,755)
%{_libdir}/libclanVorbis.a
