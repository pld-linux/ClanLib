#
# TODO: include GL1 stuff
#
%define	cvmajor	2.1
Summary:	ClanLib, the platform independent game SDK
Summary(pl.UTF-8):	ClanLib, niezależny od platformy SDK do gier
Summary(pt_BR.UTF-8):	SDK Clanlib
Name:		ClanLib
Version:	2.1.0
Release:	1
License:	BSD-like (see COPYING)
Group:		Libraries
#Source0Download: http://www.clanlib.org/download.html
Source0:	http://www.clanlib.org/download/releases-2.0/%{name}-%{version}.tgz
# Source0-md5:	099da97cd0051cc46f2a1c46cb498f6e
Patch0:		%{name}-build.patch
URL:		http://www.clanlib.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL >= 1.2.0
BuildRequires:	SDL_gfx-devel >= 1.2.0
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1.6
BuildRequires:	doxygen
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
%attr(755,root,root) %{_libdir}/libclan21App-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan21App-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan21Core-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan21Core-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan21Database-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan21Database-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan21Display-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan21Display-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan21GDI-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan21GDI-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan21GUI-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan21GUI-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan21Network-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan21Network-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan21RegExp-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan21RegExp-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan21Sound-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan21Sound-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan21Sqlite-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan21Sqlite-%{cvmajor}.so.1

%files devel
%defattr(644,root,root,755)
%doc README.kdevelop UPGRADE.txt
%attr(755,root,root) %{_libdir}/libclan21App.so
%attr(755,root,root) %{_libdir}/libclan21Core.so
%attr(755,root,root) %{_libdir}/libclan21Database.so
%attr(755,root,root) %{_libdir}/libclan21Display.so
%attr(755,root,root) %{_libdir}/libclan21GDI.so
%attr(755,root,root) %{_libdir}/libclan21GUI.so
%attr(755,root,root) %{_libdir}/libclan21Network.so
%attr(755,root,root) %{_libdir}/libclan21RegExp.so
%attr(755,root,root) %{_libdir}/libclan21Sound.so
%attr(755,root,root) %{_libdir}/libclan21Sqlite.so
%{_libdir}/libclan21App.la
%{_libdir}/libclan21Core.la
%{_libdir}/libclan21Database.la
%{_libdir}/libclan21Display.la
%{_libdir}/libclan21GDI.la
%{_libdir}/libclan21GUI.la
%{_libdir}/libclan21Network.la
%{_libdir}/libclan21RegExp.la
%{_libdir}/libclan21Sound.la
%{_libdir}/libclan21Sqlite.la
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
%{_libdir}/libclan21App.a
%{_libdir}/libclan21Core.a
%{_libdir}/libclan21Database.a
%{_libdir}/libclan21Display.a
%{_libdir}/libclan21GDI.a
%{_libdir}/libclan21GUI.a
%{_libdir}/libclan21Network.a
%{_libdir}/libclan21RegExp.a
%{_libdir}/libclan21Sound.a
%{_libdir}/libclan21Sqlite.a

%files OpenGL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan21GL-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan21GL-%{cvmajor}.so.1

%files OpenGL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan21GL.so
%{_libdir}/libclan21GL.la
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/GL
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/gl.h
%{_pkgconfigdir}/clanGL-%{cvmajor}.pc

%files OpenGL-static
%defattr(644,root,root,755)
%{_libdir}/libclan21GL.a

%files MikMod
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan21MikMod-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan21MikMod-%{cvmajor}.so.1

%files MikMod-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan21MikMod.so
%{_libdir}/libclan21MikMod.la
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/MikMod
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/mikmod.h
%{_pkgconfigdir}/clanMikMod-%{cvmajor}.pc

%files MikMod-static
%defattr(644,root,root,755)
%{_libdir}/libclan21MikMod.a

%files Vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan21Vorbis-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan21Vorbis-%{cvmajor}.so.1

%files Vorbis-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan21Vorbis.so
%{_libdir}/libclan21Vorbis.la
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/Vorbis
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/vorbis.h
%{_pkgconfigdir}/clanVorbis-%{cvmajor}.pc

%files Vorbis-static
%defattr(644,root,root,755)
%{_libdir}/libclan21Vorbis.a
