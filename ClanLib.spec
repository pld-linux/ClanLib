Summary:	ClanLib, the platform independent game SDK
Summary(pl):	ClanLib, niezale¿ny od platformy SDK do gier
Summary(pt_BR):	SDK Clanlib
Name:		ClanLib
Version:	0.6.1
Release:	4
License:	LGPL
Group:		Libraries
Source0:	http://dark.x.dtu.dk/~mbn/clanlib/download/download-japj/%{name}-%{version}/%{name}-%{version}-1.tar.gz
Patch0:		%{name}-OPT.patch
Patch1:		%{name}-config.patch
URL:		http://www.clanlib.org/
BuildRequires:	Hermes-devel >= 1.3.1
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	libmikmod-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
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
Summary(pl):	pakiet programistyczny dla ClanLib
Summary(pt_BR):	Arquivos para desenvolvimento usando a Clanlib
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	%{name}-OpenGL = %{version}
Requires:	%{name}-MikMod = %{version}
Requires:	%{name}-TTF = %{version}
Requires:	%{name}-Vorbis = %{version}
Requires:	Hermes-devel

%description devel
This is the development add-on package that includes the header files
needed to compile new ClanLib applications.

%description devel -l pl
Programistyczne dodatki do ClanLib-a, zawieraj± pliki nag³ówkowe
potrzebne do kompilacji programów korzystaj±cych z ClanLib.

%description devel -l pt_BR
Arquivos que possibilitam o desenvolvimento de aplicativos utilizando
a biblioteca Clanlib.

%package svgalib
Summary:	svgalib target for ClanLib
Summary(pl):	obs³uga svgalib dla ClanLib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description svgalib
This is the svgalib target for ClanLib.

%description svgalib -l pl
Obs³uga svgalib dla ClanLib-a.

%package OpenGL
Summary:	OpenGL target for ClanLib
Summary(pl):	obs³uga OpenGL dla ClanLib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description OpenGL
This is the OpenGL target for ClanLib.

%description OpenGL -l pl
Obs³uga OpenGL dla ClanLib-a.

%package GGI
Summary:	GGI target for ClanLib
Summary(pl):	obs³uga GGI dla ClanLib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description GGI
This is the GGI target for ClanLib.

%description GGI -l pl
Obs³uga GGI dla ClanLib-a.

%package MikMod
Summary:	MikMod module for ClanLib
Summary(pl):	Modu³ Mikmod dla ClanLib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description MikMod
MikMod module for ClanLib.

%description MikMod -l pl
Modu³ Mikmod dla ClanLib-a.

%package Vorbis
Summary:	Vorbis module for ClanLib
Summary(pl):	Modu³ Vorbis dla ClanLib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description Vorbis
Vorbis module for ClanLib.

%description Vorbis -l pl
Modu³ Vorbis dla ClanLib-a.

%package TTF
Summary:	TTF module for ClanLib
Summary(pl):	Modu³ TTF dla ClanLib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description TTF
TTF module for ClanLib.

%description TTF -l pl
Modu³ TTF dla ClanLib-a.

%package static
Summary:	ClanLib development package
Summary(pl):	pakiet programistyczny dla ClanLib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This is the development add-on package that includes the header files
needed to compile new ClanLib applications.

%description static -l pl
Programistyczne dodatki do ClanLib-a, zawieraj± pliki nag³ówkowe
potrzebne do kompilacji programów korzystaj±cych z ClanLib.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1

%build
# note: rtti is needed --- ClanLib uses exceptions!
aclocal
%{__autoconf}
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
	CFLAGS="%{rpmcflags} `pkg-config libpng12 --cflags`"; CXXFLAGS="$CFLAGS"
fi
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
	--disable-lua	# broken

# not functional right now
# in fact - non existenz in actual configure...
#	--enable-mpeg


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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanApp.so.*.*
%attr(755,root,root) %{_libdir}/libclanCore.so.*.*
%attr(755,root,root) %{_libdir}/libclanDisplay.so.*.*
%attr(755,root,root) %{_libdir}/libclanGUI.so.*.*
%attr(755,root,root) %{_libdir}/libclan*JPEG.so.*.*
%attr(755,root,root) %{_libdir}/libclanNetwork.so.*.*
#%attr(755,root,root) %{_libdir}/libclanMPEG.so.*.*
%attr(755,root,root) %{_libdir}/libclanPNG.so.*.*
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

%files TTF
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanTTF.so.*.*

%files devel
%defattr(644,root,root,755)
%doc README CREDITS html
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_bindir}/*
%{_includedir}/ClanLib

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
