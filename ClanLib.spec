#
# Conditional build:
%bcond_with	sse2	# use SSE2 instructions
#
%ifarch pentium4 %{x8664}
%define	with_sse2	1
%endif
#
%define	cvmajor	3.0
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
Patch2:		really-disable-sse2.patch
URL:		http://www.clanlib.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1.6
BuildRequires:	doxygen
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d-3
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
Obsoletes:	ClanLib-Vorbis
Obsoletes:	ClanLib-MikMod
Obsoletes:	ClanLib-TTF
Obsoletes:	ClanLib-OpenGL1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

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
Obsoletes:	ClanLib-Vorbis-devel
Obsoletes:	ClanLib-TTF-devel
Obsoletes:	ClanLib-MikMod-devel
Obsoletes:	ClanLib-OpenGL1-devel

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
Obsoletes:	ClanLib-Vorbis-static
Obsoletes:	ClanLib-TTF-static
Obsoletes:	ClanLib-MikMod-static
Obsoletes:	ClanLib-OpenGL1-static

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
%patch2 -p1

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

%post	SWRender -p /sbin/ldconfig
%postun	SWRender -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING CREDITS README
%attr(755,root,root) %{_libdir}/libclan30App-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan30App-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan30Core-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan30CSSLayout-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan30CSSLayout-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan30Core-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan30Database-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan30Database-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan30Display-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan30Display-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan30GUI-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan30GUI-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan30Network-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan30Network-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan30Sound-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan30Sound-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan30Sqlite-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan30Sqlite-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan30Compute-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan30Compute-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan30GameIDE-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan30GameIDE-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan30Physics2D-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan30Physics2D-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan30Physics3D-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan30Physics3D-%{cvmajor}.so.1
%attr(755,root,root) %{_libdir}/libclan30Scene3D-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan30Scene3D-%{cvmajor}.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan30App.so
%attr(755,root,root) %{_libdir}/libclan30CSSLayout.so
%attr(755,root,root) %{_libdir}/libclan30Core.so
%attr(755,root,root) %{_libdir}/libclan30Database.so
%attr(755,root,root) %{_libdir}/libclan30Display.so
%attr(755,root,root) %{_libdir}/libclan30GUI.so
%attr(755,root,root) %{_libdir}/libclan30Network.so
%attr(755,root,root) %{_libdir}/libclan30Sound.so
%attr(755,root,root) %{_libdir}/libclan30Sqlite.so
%attr(755,root,root) %{_libdir}/libclan30Compute.so
%attr(755,root,root) %{_libdir}/libclan30GameIDE.so
%attr(755,root,root) %{_libdir}/libclan30Physics2D.so
%attr(755,root,root) %{_libdir}/libclan30Physics3D.so
%attr(755,root,root) %{_libdir}/libclan30Scene3D.so
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
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/Sound
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/sound.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/Sqlite
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/sqlite.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/Compute
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/GameIDE
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/Physics2D
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/Physics3D
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/Scene3D
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/compute.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/d3d.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/gameide.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/physics2d.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/physics3d.h
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/scene3d.h
%{_aclocaldir}/clanlib.m4
%{_pkgconfigdir}/clanApp-%{cvmajor}.pc
%{_pkgconfigdir}/clanCSSLayout-%{cvmajor}.pc
%{_pkgconfigdir}/clanCore-%{cvmajor}.pc
%{_pkgconfigdir}/clanDatabase-%{cvmajor}.pc
%{_pkgconfigdir}/clanDisplay-%{cvmajor}.pc
%{_pkgconfigdir}/clanGUI*-%{cvmajor}.pc
%{_pkgconfigdir}/clanNetwork-%{cvmajor}.pc
%{_pkgconfigdir}/clanSound-%{cvmajor}.pc
%{_pkgconfigdir}/clanSqlite-%{cvmajor}.pc
%{_pkgconfigdir}/clanCompute-%{cvmajor}.pc
%{_pkgconfigdir}/clanGameIDE-%{cvmajor}.pc
%{_pkgconfigdir}/clanPhysics2D-%{cvmajor}.pc
%{_pkgconfigdir}/clanPhysics3D-%{cvmajor}.pc
%{_pkgconfigdir}/clanScene3D-%{cvmajor}.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libclan30App.a
%{_libdir}/libclan30CSSLayout.a
%{_libdir}/libclan30Core.a
%{_libdir}/libclan30Database.a
%{_libdir}/libclan30Display.a
%{_libdir}/libclan30GUI.a
%{_libdir}/libclan30Network.a
%{_libdir}/libclan30Sound.a
%{_libdir}/libclan30Sqlite.a
%{_libdir}/libclan30Compute.a
%{_libdir}/libclan30GameIDE.a
%{_libdir}/libclan30Physics2D.a
%{_libdir}/libclan30Physics3D.a
%{_libdir}/libclan30Scene3D.a

%files OpenGL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan30GL-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan30GL-%{cvmajor}.so.1

%files OpenGL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan30GL.so
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/GL
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/gl.h
%{_pkgconfigdir}/clanGL-%{cvmajor}.pc

%files OpenGL-static
%defattr(644,root,root,755)
%{_libdir}/libclan30GL.a

%files SWRender
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan30SWRender-%{cvmajor}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan30SWRender-%{cvmajor}.so.1

%files SWRender-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan30SWRender.so
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/SWRender
%{_includedir}/ClanLib-%{cvmajor}/ClanLib/swrender.h
%{_pkgconfigdir}/clanSWRender-%{cvmajor}.pc

%files SWRender-static
%defattr(644,root,root,755)
%{_libdir}/libclan30SWRender.a

%files doc
%defattr(644,root,root,755)
%{_docdir}/clanlib-%{cvmajor}
