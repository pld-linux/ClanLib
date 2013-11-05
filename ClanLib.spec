#
# Conditional build:
%bcond_with	sse2	# use SSE2 instructions
#
%ifarch pentium4 %{x8664}
%define	with_sse2	1
%endif
#
%define	cvmajor	2.3
Summary:	ClanLib, the platform independent game SDK
Summary(pl.UTF-8):	ClanLib, niezależny od platformy SDK do gier
Summary(pt_BR.UTF-8):	SDK Clanlib
Name:		ClanLib
Version:	3.0.0
Release:	1
License:	BSD-like (see COPYING)
Group:		Libraries
#Source0Download: http://www.clanlib.org/download.html
Source0:	http://www.clanlib.org/download/releases-3.0/%{name}-%{version}.tgz
# Source0-md5:	ebde34b9452a3b1d26cf81563f6ea62f
Patch0:		%{name}-build.patch
Patch1:		%{name}-link.patch
URL:		http://www.clanlib.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1.6
BuildRequires:	doxygen
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	libjpeg-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libpng-devel >= 1.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	libxslt-progs
BuildRequires:	pcre-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	zlib-devel
%{?with_sse2:Requires:	cpuinfo(sse2)}
Obsoletes:	ClanLib-SDL
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
Obsoletes:	ClanLib-SDL-devel
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
Obsoletes:	ClanLib-SDL-static
Obsoletes:	ClanLib-TTF-static

%description static
This package contains static versions of ClanLib libraries.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczne wersje bibliotek ClanLib.

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

%package OpenGL1
Summary:	OpenGL1 ClanLib library
Summary(pl.UTF-8):	Biblioteka OpenGL1 dla ClanLiba
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description OpenGL1
OpenGL1 ClanLib library.

%description OpenGL1 -l pl.UTF-8
Biblioteka OpenGL1 dla ClanLiba.

%package OpenGL1-devel
Summary:	Header files for OpenGL1 ClanLib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OpenGL1 dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-OpenGL1 = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	xorg-lib-libXi-devel
Requires:	xorg-lib-libXxf86vm-devel

%description OpenGL1-devel
Header files for OpenGL1 ClanLib library.

%description OpenGL1-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OpenGL1 dla ClanLiba.

%package OpenGL1-static
Summary:	Static OpenGL1 ClanLib library
Summary(pl.UTF-8):	Statyczna biblioteka OpenGL1 dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-OpenGL1-devel = %{version}-%{release}

%description OpenGL1-static
Static OpenGL1 ClanLib library.

%description OpenGL1-static -l pl.UTF-8
Statyczna biblioteka OpenGL1 dla ClanLiba.

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

%package SWRender
Summary:	ClanLib SWRender (Software Rendering) library
Summary(pl.UTF-8):	Biblioteka ClanLib SWRender (Software Rendering)
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description SWRender
ClanLib SWRender software rendering library, utilizing SSE2
instructions of x86 processors.
%if %{without sse2}

Note: this package is only stub; ClanLib needs to be recompiled with
SSE2 instructions for it to work.
%endif

%description SWRender -l pl.UTF-8
Biblioteka programowego renderowania ClanLib SWRender, wykorzystująca
instrukcje SSE2 procesorów x86.
%if %{without sse2}

Uwaga: ten pakiet zawiera tylko zaślepki; żeby działał, trzeba
przekompilować ClanLiba z użyciem instrukcji SSE2.
%endif

%package SWRender-devel
Summary:	Header files for ClanLib SWRender library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ClanLib SWRender
Group:		Development/Libraries
Requires:	%{name}-SWRender = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description SWRender-devel
Header files for ClanLib SWRender software rendering library.

%description SWRender-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki programowego renderowania ClanLib
SWRender.

%package SWRender-static
Summary:	Static ClanLib SWRender library
Summary(pl.UTF-8):	Statyczna biblioteka ClanLib SWRender
Group:		Development/Libraries
Requires:	%{name}-SWRender-devel = %{version}-%{release}

%description SWRender-static
Static ClanLib SWRender library.

%description SWRender-static -l pl.UTF-8
Statyczna biblioteka ClanLib SWRender.

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

%package doc
Summary:	ClanLib reference documentation for programmers
Summary(pl.UTF-8):	Dokumentacja programisty do biblioteki ClanLib
Group:		Documentation

%description doc
ClanLib reference documentation for programmers.

%description doc -l pl.UTF-8
Dokumentacja programisty do biblioteki ClanLib

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__rm} -r autom4te.cache

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	%{!?with_sse2:--disable-sse2} \
	--enable-docs \
	--%{?debug:en}%{!?debug:dis}able-debug

export PKG_CONFIG_PATH=$(pwd)/Setup/pkgconfig
%{__make}

%{__make} html \
	PKG_CONFIG_PATH=$(pwd)/Setup/pkgconfig

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

%post   OpenGL1 -p /sbin/ldconfig
%postun OpenGL1 -p /sbin/ldconfig

%post	MikMod -p /sbin/ldconfig
%postun	MikMod -p /sbin/ldconfig

%post	SWRender -p /sbin/ldconfig
%postun	SWRender -p /sbin/ldconfig

%post	Vorbis -p /sbin/ldconfig
%postun	Vorbis -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING CREDITS README
%attr(755,root,root) %{_libdir}/libclan23App-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan23App-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan23Core-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan23CSSLayout-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan23CSSLayout-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan23Core-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan23Database-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan23Database-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan23Display-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan23Display-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan23GUI-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan23GUI-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan23Network-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan23Network-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan23RegExp-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan23RegExp-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan23Sound-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan23Sound-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan23Sqlite-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan23Sqlite-%{cvmajor}.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan23App.so
%attr(755,root,root) %{_libdir}/libclan23CSSLayout.so
%attr(755,root,root) %{_libdir}/libclan23Core.so
%attr(755,root,root) %{_libdir}/libclan23Database.so
%attr(755,root,root) %{_libdir}/libclan23Display.so
%attr(755,root,root) %{_libdir}/libclan23GUI.so
%attr(755,root,root) %{_libdir}/libclan23Network.so
%attr(755,root,root) %{_libdir}/libclan23RegExp.so
%attr(755,root,root) %{_libdir}/libclan23Sound.so
%attr(755,root,root) %{_libdir}/libclan23Sqlite.so
%{_libdir}/libclan23App.la
%{_libdir}/libclan23CSSLayout.la
%{_libdir}/libclan23Core.la
%{_libdir}/libclan23Database.la
%{_libdir}/libclan23Display.la
%{_libdir}/libclan23GUI.la
%{_libdir}/libclan23Network.la
%{_libdir}/libclan23RegExp.la
%{_libdir}/libclan23Sound.la
%{_libdir}/libclan23Sqlite.la
%dir %{_includedir}/ClanLib-%{cvmajor}
%dir %{_includedir}/ClanLib-%{cvmajor}/ClanLib
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/App
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/application.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/CSSLayout
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/csslayout.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/Core
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/core.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/Database
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/database.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/Display
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/display.h
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
%{_aclocaldir}/clanlib.m4
%{_pkgconfigdir}/clanApp-%{cvmajor}.pc
%{_pkgconfigdir}/clanCSSLayout-%{cvmajor}.pc
%{_pkgconfigdir}/clanCore-%{cvmajor}.pc
%{_pkgconfigdir}/clanDatabase-%{cvmajor}.pc
%{_pkgconfigdir}/clanDisplay-%{cvmajor}.pc
%{_pkgconfigdir}/clanGUI*-%{cvmajor}.pc
%{_pkgconfigdir}/clanNetwork-%{cvmajor}.pc
%{_pkgconfigdir}/clanRegExp-%{cvmajor}.pc
%{_pkgconfigdir}/clanSound-%{cvmajor}.pc
%{_pkgconfigdir}/clanSqlite-%{cvmajor}.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libclan23App.a
%{_libdir}/libclan23CSSLayout.a
%{_libdir}/libclan23Core.a
%{_libdir}/libclan23Database.a
%{_libdir}/libclan23Display.a
%{_libdir}/libclan23GUI.a
%{_libdir}/libclan23Network.a
%{_libdir}/libclan23RegExp.a
%{_libdir}/libclan23Sound.a
%{_libdir}/libclan23Sqlite.a

%files OpenGL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan23GL-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan23GL-%{cvmajor}.so.1

%files OpenGL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan23GL.so
%{_libdir}/libclan23GL.la
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/GL
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/gl.h
%{_pkgconfigdir}/clanGL-%{cvmajor}.pc

%files OpenGL-static
%defattr(644,root,root,755)
%{_libdir}/libclan23GL.a

%files OpenGL1
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan23GL1-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan23GL1-%{cvmajor}.so.1

%files OpenGL1-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan23GL1.so
%{_libdir}/libclan23GL1.la
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/GL1
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/gl1.h
%{_pkgconfigdir}/clanGL1-%{cvmajor}.pc

%files OpenGL1-static
%defattr(644,root,root,755)
%{_libdir}/libclan23GL1.a

%files MikMod
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan23MikMod-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan23MikMod-%{cvmajor}.so.1

%files MikMod-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan23MikMod.so
%{_libdir}/libclan23MikMod.la
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/MikMod
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/mikmod.h
%{_pkgconfigdir}/clanMikMod-%{cvmajor}.pc

%files MikMod-static
%defattr(644,root,root,755)
%{_libdir}/libclan23MikMod.a

%files SWRender
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan23SWRender-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan23SWRender-%{cvmajor}.so.1

%files SWRender-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan23SWRender.so
%{_libdir}/libclan23SWRender.la
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/SWRender
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/swrender.h
%{_pkgconfigdir}/clanSWRender-%{cvmajor}.pc

%files SWRender-static
%defattr(644,root,root,755)
%{_libdir}/libclan23SWRender.a

%files Vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan23Vorbis-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan23Vorbis-%{cvmajor}.so.1

%files Vorbis-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan23Vorbis.so
%{_libdir}/libclan23Vorbis.la
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/Vorbis
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/vorbis.h
%{_pkgconfigdir}/clanVorbis-%{cvmajor}.pc

%files Vorbis-static
%defattr(644,root,root,755)
%{_libdir}/libclan23Vorbis.a

%files doc
%defattr(644,root,root,755)
%{_docdir}/clanlib-%{cvmajor}
