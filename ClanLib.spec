Summary:	ClanLib, the platform independent game SDK
Summary(pl):	ClanLib, niezale¿ny od platformy SDK do gier
Summary(pt_BR):	SDK Clanlib
Name:		ClanLib
Version:	0.6.5
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.clanlib.org/~sphair/download/%{name}-%{version}-1.tar.gz
# Source0-md5:	7115921953ef6fa45102c28622493650
Patch0:		%{name}-OPT.patch
Patch1:		%{name}-GL.patch
Patch2:		%{name}-assert.patch
Patch3:		%{name}-ft2build_h.patch
URL:		http://www.clanlib.org/
# doesn't build with 0.9.12
#BuildRequires:	DirectFB-devel = 0.9.9
BuildRequires:	Hermes-devel >= 1.3.1
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	libjpeg-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel >= 1:1.0
# If broken - don't require it....
#BuildRequires:	lua-devel
BuildRequires:	perl
Requires:	Hermes >= 1.3.1
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
Requires:	%{name} = %{version}
Requires:	Hermes-devel

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
Summary(pl):	Biblioteki statyczne ClanLib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
ClanLib static libraries.

%description static -l pl
Biblioteki statyczne ClanLib.

%package OpenGL
Summary:	OpenGL ClanLib library
Summary(pl):	Biblioteka OpenGL dla ClanLiba
Group:		Libraries
Requires:	%{name} = %{version}
Requires:	OpenGL

%description OpenGL
OpenGL ClanLib library.

%description OpenGL -l pl
Biblioteka OpenGL dla ClanLiba.

%package OpenGL-devel
Summary:	Headers files for OpenGL ClanLib library
Summary(pl):	Pliki nag³ówkowe biblioteki OpenGL dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-OpenGL = %{version}
Requires:	%{name}-devel = %{version}
Requires:	OpenGL-devel

%description OpenGL-devel
Headers files for OpenGL ClanLib library.

%description OpenGL-devel -l pl
Pliki nag³ówkowe biblioteki OpenGL dla ClanLiba.

%package OpenGL-static
Summary:	Static OpenGL ClanLib library
Summary(pl):	Statyczna biblioteka OpenGL dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-OpenGL-devel = %{version}

%description OpenGL-static
Static OpenGL ClanLib library.

%description OpenGL-static -l pl
Statyczna biblioteka OpenGL dla ClanLiba.

%package MikMod
Summary:	MikMod ClanLib library
Summary(pl):	Biblioteka MikMod dla ClanLiba
Group:		Libraries
Requires:	%{name} = %{version}

%description MikMod
MikMod ClanLib library.

%description MikMod -l pl
Biblioteka MikMod dla ClanLiba.

%package MikMod-devel
Summary:	Headers files for MikMod ClanLib library
Summary(pl):	Pliki nag³ówkowe biblioteki MikMod dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-MikMod = %{version}
Requires:	%{name}-devel = %{version}
Requires:	libmikmod-devel

%description MikMod-devel
Headers files for MikMod ClanLib library.

%description MikMod-devel -l pl
Pliki nag³ówkowe biblioteki MikMod dla ClanLiba.

%package MikMod-static
Summary:	Static MikMod ClanLib library
Summary(pl):	Statyczna biblioteka MikMod dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-MikMod-devel = %{version}

%description MikMod-static
Static MikMod ClanLib library.

%description MikMod-static -l pl
Statyczna biblioteka MikMod dla ClanLiba.

%package Vorbis
Summary:	Vorbis ClanLib library
Summary(pl):	Biblioteka Vorbis dla ClanLiba
Group:		Libraries
Requires:	%{name} = %{version}

%description Vorbis
Vorbis ClanLib library.

%description Vorbis -l pl
Biblioteka Vorbis dla ClanLiba.

%package Vorbis-devel
Summary:	Headers files for Vorbis ClanLib library
Summary(pl):	Pliki nag³ówkowe biblioteki Vorbis dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-Vorbis = %{version}
Requires:	%{name}-devel = %{version}

%description Vorbis-devel
Headers files for Vorbis ClanLib library.

%description Vorbis-devel -l pl
Pliki nag³ówkowe biblioteki Vorbis dla ClanLiba.

%package Vorbis-static
Summary:	Static Vorbis ClanLib library
Summary(pl):	Statyczna biblioteka Vorbis dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-Vorbis-devel = %{version}

%description Vorbis-static
Static Vorbis ClanLib library.

%description Vorbis-static -l pl
Statyczna biblioteka Vorbis dla ClanLiba.

%package TTF
Summary:	TTF ClanLib library
Summary(pl):	Biblioteka TTF dla ClanLiba
Group:		Libraries
Requires:	%{name} = %{version}

%description TTF
TTF ClanLib library.

%description TTF -l pl
Biblioteka TTF dla ClanLiba.

%package TTF-devel
Summary:	Headers files for TTF ClanLib library
Summary(pl):	Pliki nag³ówkowe biblioteki TTF dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-TTF = %{version}
Requires:	%{name}-devel = %{version}

%description TTF-devel
Headers files for TTF ClanLib library.

%description TTF-devel -l pl
Pliki nag³ówkowe biblioteki TTF dla ClanLiba.

%package TTF-static
Summary:	Static TTF ClanLib library
Summary(pl):	Statyczna biblioteka TTF dla ClanLiba
Group:		Development/Libraries
Requires:	%{name}-TTF-devel = %{version}

%description TTF-static
Static TTF ClanLib library.

%description TTF-static -l pl
Statyczna biblioteka TTF dla ClanLiba.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# note: rtti is needed --- ClanLib uses exceptions!
cp /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure \
	--enable-static \
	--enable-shared \
	--%{?debug:en}%{!?debug:dis}able-debug \
%ifarch %{ix86}
	--enable-asm386 \
%endif
	--enable-clansound \
	--enable-dyn \
	--enable-fbdev \
	--enable-gui \
	--enable-jpeg \
	--enable-mikmod \
	--enable-network \
	--enable-opengl \
	--enable-png \
	--enable-smalljpeg \
	--enable-ttf \
	--enable-vidmode \
	--enable-vorbis \
	--enable-x11 \
	--disable-lua \
	--disable-directfb
# lua is broken, DirectFB too fresh?

%{__make}
%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	LIB_PREFIX="$RPM_BUILD_ROOT%{_libdir}" \
	TARGET_PREFIX="$RPM_BUILD_ROOT%{_libdir}/ClanLib" \
	BIN_PREFIX="$RPM_BUILD_ROOT%{_bindir}" \
	INC_PREFIX="$RPM_BUILD_ROOT%{_includedir}"

%{__make} docs_install \
	MAN_PREFIX="$RPM_BUILD_ROOT%{_mandir}" \
	HTML_PREFIX="`pwd`/html"

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   OpenGL -p /sbin/ldconfig
%postun OpenGL -p /sbin/ldconfig

%post   MikMod -p /sbin/ldconfig
%postun MikMod -p /sbin/ldconfig

%post   TTF -p /sbin/ldconfig
%postun TTF -p /sbin/ldconfig

%post   Vorbis -p /sbin/ldconfig
%postun Vorbis -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CREDITS
%attr(755,root,root) %{_libdir}/libclanApp.so.*.*
%attr(755,root,root) %{_libdir}/libclanCore.so.*.*
%attr(755,root,root) %{_libdir}/libclanDisplay.so.*.*
%attr(755,root,root) %{_libdir}/libclanGUI.so.*.*
%attr(755,root,root) %{_libdir}/libclan*JPEG.so.*.*
%attr(755,root,root) %{_libdir}/libclanNetwork.so.*.*
%attr(755,root,root) %{_libdir}/libclanPNG.so.*.*
%attr(755,root,root) %{_libdir}/libclanSound.so.*.*

%files devel
%defattr(644,root,root,755)
%doc README html
%attr(755,root,root) %{_bindir}/clanlib-config
%attr(755,root,root) %{_libdir}/libclanApp.so
%attr(755,root,root) %{_libdir}/libclanCore.so
%attr(755,root,root) %{_libdir}/libclanDisplay.so
%attr(755,root,root) %{_libdir}/libclanGUI.so
%attr(755,root,root) %{_libdir}/libclan*JPEG.so
%attr(755,root,root) %{_libdir}/libclanNetwork.so
%attr(755,root,root) %{_libdir}/libclanPNG.so
%attr(755,root,root) %{_libdir}/libclanSound.so
%dir %{_includedir}/ClanLib
%{_includedir}/ClanLib/Application
%{_includedir}/ClanLib/Core
%{_includedir}/ClanLib/Display
%{_includedir}/ClanLib/GUI
%{_includedir}/ClanLib/*JPEG
%{_includedir}/ClanLib/Network
%{_includedir}/ClanLib/PNG
%{_includedir}/ClanLib/Signals
%{_includedir}/ClanLib/Sound
%{_includedir}/ClanLib/application.h
%{_includedir}/ClanLib/core.h
%{_includedir}/ClanLib/display.h
%{_includedir}/ClanLib/efence.h
%{_includedir}/ClanLib/gui.h
%{_includedir}/ClanLib/jpeg.h
%{_includedir}/ClanLib/network.h
%{_includedir}/ClanLib/png.h
%{_includedir}/ClanLib/signals.h
%{_includedir}/ClanLib/sound.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libclanApp.a
%{_libdir}/libclanCore.a
%{_libdir}/libclanDisplay.a
%{_libdir}/libclanGUI.a
%{_libdir}/libclan*JPEG.a
%{_libdir}/libclanNetwork.a
%{_libdir}/libclanPNG.a
%{_libdir}/libclanSound.a

%files OpenGL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanGL.so.*.*

%files OpenGL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanGL.so
%{_includedir}/ClanLib/GL
%{_includedir}/ClanLib/gl.h

%files OpenGL-static
%defattr(644,root,root,755)
%{_libdir}/libclanGL.a

%files MikMod
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanMikMod.so.*.*

%files MikMod-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanMikMod.so
%{_includedir}/ClanLib/MikMod
%{_includedir}/ClanLib/mikmod.h

%files MikMod-static
%defattr(644,root,root,755)
%{_libdir}/libclanMikMod.a

%files Vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanVorbis.so.*.*

%files Vorbis-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanVorbis.so
%{_includedir}/ClanLib/Vorbis
%{_includedir}/ClanLib/vorbis.h

%files Vorbis-static
%defattr(644,root,root,755)
%{_libdir}/libclanVorbis.a

%files TTF
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanTTF.so.*.*

%files TTF-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanTTF.so
%{_includedir}/ClanLib/TTF
%{_includedir}/ClanLib/ttf.h

%files TTF-static
%defattr(644,root,root,755)
%{_libdir}/libclanTTF.a
