Summary:	ClanLib, the platform independent game SDK
Summary(pl):	ClanLib, niezale¿ny od platformy SDK do gier
Summary(pt_BR):	SDK Clanlib
Name:		ClanLib
Version:	0.8.0
Release:	0.RC1.1
License:	LGPL v2
Group:		Libraries
#Source0Download: http://www.clanlib.org/download.html
# http://www.clanlib.org/download/releases-0.8/ClanLib-0.8.0-RC1.tgz
Source0:	http://www.clanlib.org/download/releases-0.8/%{name}-%{version}-RC1.tgz
# Source0-md5:	edda2e3000ec4b02e435982ff44a3841
Patch0:		%{name}-link.patch
Patch1:		%{name}-gcc4.patch
URL:		http://www.clanlib.org/
# doesn't build with 0.9.12
#BuildRequires:	DirectFB-devel = 0.9.9
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_gfx-devel >= 1.2.0
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	libxslt-progs
BuildRequires:	perl-base
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
The ClanLib SDK is designed to provide an platform independent game
SDK using a lot cleaner (and object oriented) interface than the
traditional way it is done in DirectX, SDL and such. The goal is to
avoid game developers constantly reinventing the wheel by providing
smarter ways to eg. load surfaces.

%description -l pl
ClanLib SDK jest projektowany jako niezale¿ny od platformy SDK dla
gier. Stosuje prosty (i zorientowany obiektowo) interfejs,
przejrzystszy ni¿ DirectX, SDL i inne.

%description -l pt_BR
A Clanlib é uma biblioteca de jogos multi-plataforma desenhada para
facilitar o trabalho dos desenvolvedores. A idéia principal é fornecer
uma interface comum para os problemas clássicos dos jogos (carregar
gráficos por exemplo).

%package devel
Summary:	ClanLib development package
Summary(pl):	Pakiet programistyczny dla ClanLib
Summary(pt_BR):	Arquivos para desenvolvimento usando a Clanlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This is the development add-on package that includes the header files
needed to compile new ClanLib applications.

%description devel -l pl
Programistyczne dodatki do ClanLiba, zawieraj± pliki nag³ówkowe
potrzebne do kompilacji programów korzystaj±cych z ClanLib.

%description devel -l pt_BR
Arquivos que possibilitam o desenvolvimento de aplicativos utilizando
a biblioteca Clanlib.

%package static
Summary:	ClanLib static libraries
Summary(pl):	Statyczne biblioteki ClanLib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static versions of ClanLib libraries.

%description static -l pl
Ten pakiet zawiera statyczne wersje bibliotek ClanLib.

%package doc
Summary:	ClanLib reference documentation for programmers
Summary(pl):	Dokumentacja programisty do biblioteki ClanLib
Group:		Documentation

%description doc
ClanLib reference documentation for programmers.

%description doc -l pl
Dokumentacja programisty do biblioteki ClanLib

%package OpenGL
Summary:	OpenGL ClanLib library
Summary(pl):	Biblioteka OpenGL dla ClanLiba
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL

%description OpenGL
OpenGL ClanLib library.

%description OpenGL -l pl
Biblioteka OpenGL dla ClanLiba.

%package OpenGL-devel
Summary:	Header files for OpenGL ClanLib library
Summary(pl):	Pliki nag³ówkowe biblioteki OpenGL dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-OpenGL = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	OpenGL-devel

%description OpenGL-devel
Header files for OpenGL ClanLib library.

%description OpenGL-devel -l pl
Pliki nag³ówkowe biblioteki OpenGL dla ClanLiba.

%package OpenGL-static
Summary:	Static OpenGL ClanLib library
Summary(pl):	Statyczna biblioteka OpenGL dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-OpenGL-devel = %{version}-%{release}

%description OpenGL-static
Static OpenGL ClanLib library.

%description OpenGL-static -l pl
Statyczna biblioteka OpenGL dla ClanLiba.

%package MikMod
Summary:	MikMod ClanLib library
Summary(pl):	Biblioteka MikMod dla ClanLiba
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description MikMod
MikMod ClanLib library.

%description MikMod -l pl
Biblioteka MikMod dla ClanLiba.

%package MikMod-devel
Summary:	Header files for MikMod ClanLib library
Summary(pl):	Pliki nag³ówkowe biblioteki MikMod dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-MikMod = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libmikmod-devel

%description MikMod-devel
Header files for MikMod ClanLib library.

%description MikMod-devel -l pl
Pliki nag³ówkowe biblioteki MikMod dla ClanLiba.

%package MikMod-static
Summary:	Static MikMod ClanLib library
Summary(pl):	Statyczna biblioteka MikMod dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-MikMod-devel = %{version}-%{release}

%description MikMod-static
Static MikMod ClanLib library.

%description MikMod-static -l pl
Statyczna biblioteka MikMod dla ClanLiba.

%package SDL
Summary:	SDL ClanLib library
Summary(pl):	Biblioteka SDL dla ClanLiba
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description SDL
SDL ClanLib library.

%description SDL -l pl
Biblioteka SDL dla ClanLiba.

%package SDL-devel
Summary:	Header files for SDL ClanLib library
Summary(pl):	Pliki nag³ówkowe biblioteki SDL dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-SDL = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	SDL-devel

%description SDL-devel
Header files for SDL ClanLib library.

%description SDL-devel -l pl
Pliki nag³ówkowe biblioteki SDL dla ClanLiba.

%package SDL-static
Summary:	Static SDL ClanLib library
Summary(pl):	Statyczna biblioteka SDL dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-SDL-devel = %{version}-%{release}

%description SDL-static
Static SDL ClanLib library.

%description SDL-static -l pl
Statyczna biblioteka SDL dla ClanLiba.

%package Vorbis
Summary:	Vorbis ClanLib library
Summary(pl):	Biblioteka Vorbis dla ClanLiba
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description Vorbis
Vorbis ClanLib library.

%description Vorbis -l pl
Biblioteka Vorbis dla ClanLiba.

%package Vorbis-devel
Summary:	Header files for Vorbis ClanLib library
Summary(pl):	Pliki nag³ówkowe biblioteki Vorbis dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-Vorbis = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libvorbis-devel

%description Vorbis-devel
Header files for Vorbis ClanLib library.

%description Vorbis-devel -l pl
Pliki nag³ówkowe biblioteki Vorbis dla ClanLiba.

%package Vorbis-static
Summary:	Static Vorbis ClanLib library
Summary(pl):	Statyczna biblioteka Vorbis dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-Vorbis-devel = %{version}-%{release}

%description Vorbis-static
Static Vorbis ClanLib library.

%description Vorbis-static -l pl
Statyczna biblioteka Vorbis dla ClanLiba.

%prep
%setup -q -n %{name}-%{version}-RC1
%patch0 -p1
%patch1 -p1

rm -rf autom4te.cache

%build
# note: rtti is needed --- ClanLib uses exceptions!
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--enable-static \
	--enable-shared \
	--%{?debug:en}%{!?debug:dis}able-debug \
%ifarch %{ix86}
	--enable-asm386 \
%endif
	--enable-dyn
# directfb disabled now

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	

# missing from make install
install -d $RPM_BUILD_ROOT%{_aclocaldir}
install Setup/Unix/clanlib.m4 $RPM_BUILD_ROOT%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   OpenGL -p /sbin/ldconfig
%postun OpenGL -p /sbin/ldconfig

%post   MikMod -p /sbin/ldconfig
%postun MikMod -p /sbin/ldconfig

%post	SDL -p /sbin/ldconfig
%postun	SDL -p /sbin/ldconfig

%post   Vorbis -p /sbin/ldconfig
%postun Vorbis -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CREDITS NEWS README README.sdl TODO-RSN
%attr(755,root,root) %{_libdir}/libclanApp-0.8.so.*.*
%attr(755,root,root) %{_libdir}/libclanCore-0.8.so.*.*
%attr(755,root,root) %{_libdir}/libclanDisplay-0.8.so.*.*
%attr(755,root,root) %{_libdir}/libclanGUI-0.8.so.*.*
%attr(755,root,root) %{_libdir}/libclanGUIStyleSilver-0.8.so.*.*
%attr(755,root,root) %{_libdir}/libclanNetwork-0.8.so.*.*
%attr(755,root,root) %{_libdir}/libclanSignals-0.8.so.*.*
%attr(755,root,root) %{_libdir}/libclanSound-0.8.so.*.*

%files devel
%defattr(644,root,root,755)
%doc README.kdevelop README.upgrade
%attr(755,root,root) %{_libdir}/libclanApp.so
%attr(755,root,root) %{_libdir}/libclanCore.so
%attr(755,root,root) %{_libdir}/libclanDisplay.so
%attr(755,root,root) %{_libdir}/libclanGUI.so
%attr(755,root,root) %{_libdir}/libclanGUIStyleSilver.so
%attr(755,root,root) %{_libdir}/libclanNetwork.so
%attr(755,root,root) %{_libdir}/libclanSignals.so
%attr(755,root,root) %{_libdir}/libclanSound.so
%{_libdir}/libclanApp.la
%{_libdir}/libclanCore.la
%{_libdir}/libclanDisplay.la
%{_libdir}/libclanGUI.la
%{_libdir}/libclanGUIStyleSilver.la
%{_libdir}/libclanNetwork.la
%{_libdir}/libclanSignals.la
%{_libdir}/libclanSound.la
%dir %{_includedir}/ClanLib-0.8
%dir %{_includedir}/ClanLib-0.8/ClanLib
%{_includedir}/ClanLib-0.8/ClanLib/Application
%{_includedir}/ClanLib-0.8/ClanLib/application.h
%{_includedir}/ClanLib-0.8/ClanLib/Core
%{_includedir}/ClanLib-0.8/ClanLib/core.h
%{_includedir}/ClanLib-0.8/ClanLib/Display
%{_includedir}/ClanLib-0.8/ClanLib/display.h
%{_includedir}/ClanLib-0.8/ClanLib/GUI*
%{_includedir}/ClanLib-0.8/ClanLib/gui*.h
%{_includedir}/ClanLib-0.8/ClanLib/Network
%{_includedir}/ClanLib-0.8/ClanLib/network.h
%{_includedir}/ClanLib-0.8/ClanLib/Signals
%{_includedir}/ClanLib-0.8/ClanLib/signals.h
%{_includedir}/ClanLib-0.8/ClanLib/Sound
%{_includedir}/ClanLib-0.8/ClanLib/sound.h
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/clanApp-0.8.pc
%{_pkgconfigdir}/clanCore-0.8.pc
%{_pkgconfigdir}/clanDisplay-0.8.pc
%{_pkgconfigdir}/clanGUI*-0.8.pc
%{_pkgconfigdir}/clanNetwork-0.8.pc
%{_pkgconfigdir}/clanSignals-0.8.pc
%{_pkgconfigdir}/clanSound-0.8.pc

%files doc
%defattr(644,root,root,755)
%{_docdir}/clanlib

%files static
%defattr(644,root,root,755)
%{_libdir}/libclanApp.a
%{_libdir}/libclanCore.a
%{_libdir}/libclanDisplay.a
%{_libdir}/libclanGUI.a
%{_libdir}/libclanGUIStyleSilver.a
%{_libdir}/libclanNetwork.a
%{_libdir}/libclanSignals.a
%{_libdir}/libclanSound.a

%files OpenGL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanGL-0.8.so.*.*

%files OpenGL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanGL.so
%{_libdir}/libclanGL.la
%{_includedir}/ClanLib-0.8/ClanLib/GL
%{_includedir}/ClanLib-0.8/ClanLib/gl.h
%{_pkgconfigdir}/clanGL-0.8.pc

%files OpenGL-static
%defattr(644,root,root,755)
%{_libdir}/libclanGL.a

%files MikMod
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanMikMod-0.8.so.*.*

%files MikMod-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanMikMod.so
%{_libdir}/libclanMikMod.la
%{_includedir}/ClanLib-0.8/ClanLib/MikMod
%{_includedir}/ClanLib-0.8/ClanLib/mikmod.h
%{_pkgconfigdir}/clanMikMod-0.8.pc

%files MikMod-static
%defattr(644,root,root,755)
%{_libdir}/libclanMikMod.a

%files SDL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanSDL-0.8.so.*.*

%files SDL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanSDL.so
%{_libdir}/libclanSDL.la
%{_includedir}/ClanLib-0.8/ClanLib/SDL
%{_includedir}/ClanLib-0.8/ClanLib/sdl.h
%{_pkgconfigdir}/clanSDL-0.8.pc

%files SDL-static
%defattr(644,root,root,755)
%{_libdir}/libclanSDL.a

%files Vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanVorbis-0.8.so.*.*

%files Vorbis-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanVorbis.so
%{_libdir}/libclanVorbis.la
%{_includedir}/ClanLib-0.8/ClanLib/Vorbis
%{_includedir}/ClanLib-0.8/ClanLib/vorbis.h
%{_pkgconfigdir}/clanVorbis-0.8.pc

%files Vorbis-static
%defattr(644,root,root,755)
%{_libdir}/libclanVorbis.a
