# TODO:
# - check what is happening with the documentation - possible cause: just
#   not ready
# - clean-up
# Warning: 0.7.2 is a developement version, but considered as stable as it is:/
# Maybe switch to 0.6.5 ?
#
Summary:	ClanLib, the platform independent game SDK
Summary(pl):	ClanLib, niezale¿ny od platformy SDK do gier
Summary(pt_BR):	SDK Clanlib
Name:		ClanLib
Version:	0.7.2
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://www.clanlib.org/~sphair/download/%{name}-%{version}-1.tar.bz2
Patch0:		%{name}-OPT.patch
#Patch1:		%{name}-config.patch
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
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
The ClanLib SDK is designed to provide an platform independent game
SDK using a lot cleaner (and object oriented) interface than the
traditional way it is done in DirectX, SDL and such. The goals is to
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
Requires:	%{name}-OpenGL = %{version}
Requires:	%{name}-MikMod = %{version}
#Requires:	%{name}-TTF = %{version}
Requires:	%{name}-Vorbis = %{version}
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

%package doc
Summary:	ClanLib reference documentation for programmers
Summary(pl):	Dokumentacja programisty do biblioteki ClanLib
Group:		Documentation

%description doc
ClanLib reference documentation for programmers.

%description doc -l pl
Dokumentacja programisty do biblioteki ClanLib

%package svgalib
Summary:	svgalib target for ClanLib
Summary(pl):	Obs³uga svgalib dla ClanLib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description svgalib
This is the svgalib target for ClanLib.

%description svgalib -l pl
Obs³uga svgalib dla ClanLiba.

%package OpenGL
Summary:	OpenGL target for ClanLib
Summary(pl):	Obs³uga OpenGL dla ClanLib
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	OpenGL

%description OpenGL
This is the OpenGL target for ClanLib.

%description OpenGL -l pl
Obs³uga OpenGL dla ClanLiba.

%package GGI
Summary:	GGI target for ClanLib
Summary(pl):	Obs³uga GGI dla ClanLib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description GGI
This is the GGI target for ClanLib.

%description GGI -l pl
Obs³uga GGI dla ClanLiba.

%package MikMod
Summary:	MikMod module for ClanLib
Summary(pl):	Modu³ Mikmod dla ClanLib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description MikMod
MikMod module for ClanLib.

%description MikMod -l pl
Modu³ Mikmod dla ClanLiba.

%package Vorbis
Summary:	Vorbis module for ClanLib
Summary(pl):	Modu³ Vorbis dla ClanLib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description Vorbis
Vorbis module for ClanLib.

%description Vorbis -l pl
Modu³ Vorbis dla ClanLiba.

#%package TTF
#Summary:	TTF module for ClanLib
#Summary(pl):	Modu³ TTF dla ClanLib
#Group:		Development/Libraries
#Requires:	%{name} = %{version}

#%description TTF
#TTF module for ClanLib.

#%description TTF -l pl
#Modu³ TTF dla ClanLiba.

%package static
Summary:	ClanLib static libraries
Summary(pl):	Statyczne biblioteki ClanLib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static versions of ClanLib libraries.

%description static -l pl
Ten pakiet zawiera statyczne wersje bibliotek ClanLib.

%prep
%setup -q
%patch0 -p1

%build
# note: rtti is needed --- ClanLib uses exceptions!
rm -f missing
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

# not functional right now
# in fact - non existenz in actual configure...
#	--enable-mpeg

%{__make}

#%{__make} docs  doesn't work
cd Documentation
%{__autoconf}
cp -f Makefile Makefile.tmp
%configure
mv -f Makefile.tmp Makefile
Utilities/webbuilder.pl documentation.theme index.xml
Utilities/webbuilder.pl documentation.theme Tutorial/index.xml
# tictactoe.zip contains Win32 executable
rm -f Tutorial/index.xml Tutorial/TicTacToe/{.cvsignore,tictactoe.zip}
%{__make} -C Overview
%{__make} -C Reference

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	

#%{__make} docs_install \
#	MAN_PREFIX="$RPM_BUILD_ROOT%{_mandir}" \
#	HTML_PREFIX="`pwd`/html"
%{__make} install -C Documentation/Overview \
	HTML_PREFIX="`pwd`/html"
%{__make} html_install -C Documentation/Reference \
	HTML_PREFIX="`pwd`/html"
cp -rf Documentation/index.html Documentation/Tutorial html

# missing from make install
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_aclocaldir}}
install Setup/Unix/clanlib-config $RPM_BUILD_ROOT%{_bindir}
install Documentation/clanlib-config.1 $RPM_BUILD_ROOT%{_mandir}/man1
install Setup/Unix/clanlib.m4 $RPM_BUILD_ROOT%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   OpenGL -p /sbin/ldconfig
%postun OpenGL -p /sbin/ldconfig

%post   MikMod -p /sbin/ldconfig
%postun MikMod -p /sbin/ldconfig

#%post   TTF -p /sbin/ldconfig
#%postun TTF -p /sbin/ldconfig

%post   Vorbis -p /sbin/ldconfig
%postun Vorbis -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS CREDITS NEWS README README.gui 
%attr(755,root,root) %{_libdir}/libclanApp.so.*.*
%attr(755,root,root) %{_libdir}/libclanCore.so.*.*
%attr(755,root,root) %{_libdir}/libclanDisplay.so.*.*
%attr(755,root,root) %{_libdir}/libclanGUI.so.*.*
#%attr(755,root,root) %{_libdir}/libclan*JPEG.so.*.*
%attr(755,root,root) %{_libdir}/libclanNetwork.so.*.*
#%attr(755,root,root) %{_libdir}/libclanMPEG.so.*.*
#%attr(755,root,root) %{_libdir}/libclanPNG.so.*.*
%attr(755,root,root) %{_libdir}/libclanGUIStyleBoring.so.*.*
%attr(755,root,root) %{_libdir}/libclanGUIStyleSilver.so.*.*
%attr(755,root,root) %{_libdir}/libclanSignals.so.*.*
%attr(755,root,root) %{_libdir}/libclanSound.so.*.*

%files OpenGL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanGL.so.*.*

%files MikMod
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanMikMod.so.*.*

%files Vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanVorbis.so.*.*

#%files TTF
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libclanTTF.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/clanlib-config
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/ClanLib
%{_aclocaldir}/*.m4
%{_mandir}/man1/clanlib-config.1*

%files doc
%defattr(644,root,root,755)
%doc README.upgrade html

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
