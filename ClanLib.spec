Summary:	ClanLib, the platform independent game SDK.
Summary(pl):	ClanLib, niezale¿ny od platformy SDK do gier
Name:		ClanLib
Version:	0.4.3
Release:	1
Copyright:	LGPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		http://dark.x.dtu.dk/clansoft/clanlib/download/%{name}-%{version}.tar.gz
URL:		http://clanlib.org
Requires:	Hermes >= 1.3.1
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRequires:	Hermes-devel >= 1.3.1
BuildRequires:	libstdc++-devel
BuildRequires:	XFree86-devel
BuildRequires:	svgalib-devel
BuildRequires:	Mesa-devel
BuildRequires:	ImageMagick-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libpng-devel
BuildRequires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ClanLib SDK is designed to provide an platform independent game SDK using
a lot cleaner (and object oriented) interface than the traditional way it is
done in DirectX, SDL and such. The goals is to avoid game developers
constantly reinventing the wheel by providing smarter ways to eg. load
surfaces.

%description -l pl
ClanLib SDK jest projektowany jako niezale¿ny od platformy SDK dla gier.
Stosuje prosty (i zorientowany obiektowo) interfejs, przejrzystszy ni¿
DirectX, SDL i inne.

%package devel
Summary:	ClanLib development package
Summary(pl):	pakiet programistyczny dla ClanLib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	%{name}-OpenGL = %{version}
Requires:	%{name}-MikMod = %{version}
Requires:	%{name}-Magick = %{version}

%description devel
This is the development add-on package that includes the header files needed
to compile new ClanLib applications.

%description -l pl devel
Programistyczne dodatki do ClanLib-a, zawieraj± pliki nag³ówkowe potrzebne
do kompilacji programów korzystaj±cych z ClanLib.

%package svgalib
Summary:	svgalib target for ClanLib
Summary(pl):	obs³uga svgalib dla ClanLib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description svgalib
This is the svgalib target for ClanLib. 

%description -l pl svgalib
Obs³uga svgalib dla ClanLib-a.

%package OpenGL
Summary:	OpenGL target for ClanLib
Summary(pl):	obs³uga OpenGL dla ClanLib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description OpenGL
This is the OpenGL target for ClanLib. 

%description -l pl OpenGL
Obs³uga OpenGL dla ClanLib-a.

%package X11
Summary:	X11 target for ClanLib
Summary(pl):	obs³uga X11 dla ClanLib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description X11
This is the X11 target for ClanLib. 

%description -l pl X11
Obs³uga X11 dla ClanLib-a.

%package Magick
Summary:	ImageMagick module for ClanLib
Summary(pl):	Modu³ ImageMagick dla ClanLib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description Magick
This is the ImageMagic add-on package for ClanLib. It provides support to most
known graphics file-formats.

%description -l pl Magick
Pozwala na obs³ugê praktycznie dowolnych formatów plików graficznych przez
aplikacje ClanLib poprzez biblioteki ImageMagic-a.

%package MikMod
Summary:	MikMod module for ClanLib
Summary(pl):	Modu³ Mikmod dla ClanLib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description MikMod
MikMod module for ClanLib

%description -l pl MikMod
Modu³ Mikmod dla ClanLib

%package static
Summary:	ClanLib development package
Summary(pl):	pakiet programistyczny dla ClanLib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
This is the development add-on package that includes the header files needed
to compile new ClanLib applications.

%description -l pl static
Programistyczne dodatki do ClanLib-a, zawieraj± pliki nag³ówkowe potrzebne
do kompilacji programów korzystaj±cych z CleanLib.

%prep
%setup -q

%build
./autogen.sh
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-static \
	--enable-shared \
	--enable-x11 \
	--enable-fbdev \
	--disable-ggi \
	--enable-opengl \
	--enable-svgalib \
	--disable-ptc \
	--enable-vidmode \
	--enable-clansound \
	--enable-network \
	--enable-dyn
make
make clanGL
make clanMikMod
make clanMagick
make clanPNG
make clanMPEG
make clanGUI
make docs

%install
rm -rf $RPM_BUILD_ROOT
make 	install \
	LIB_PREFIX="$RPM_BUILD_ROOT%{_libdir}" \
	TARGET_PREFIX="$RPM_BUILD_ROOT%{_libdir}/ClanLib" \
	BIN_PREFIX="$RPM_BUILD_ROOT%{_bindir}" \
	INC_PREFIX="$RPM_BUILD_ROOT%{_includedir}"

make docs_install \
	MAN_PREFIX="$RPM_BUILD_ROOT%{_mandir}" \
	HTML_PREFIX="`pwd`/html"

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so*
strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/ClanLib/lib*.so*

gzip -9nf README CREDITS FAQ $RPM_BUILD_ROOT%{_mandir}/man?/* || : 

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   OpenGL -p /sbin/ldconfig
%postun OpenGL -p /sbin/ldconfig

%post   MikMod -p /sbin/ldconfig
%postun MikMod -p /sbin/ldconfig

%post   Magick -p /sbin/ldconfig
%postun Magick -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanCore.so.*.*
%attr(755,root,root) %{_libdir}/libclanGUI.so.*.*
%attr(755,root,root) %{_libdir}/libclanMPEG.so.*.*
%attr(755,root,root) %{_libdir}/libclanPNG.so.*.*
%dir %{_libdir}/ClanLib
%attr(755,root,root) %{_libdir}/ClanLib/libclan-display-fbdev.so*
%attr(755,root,root) %{_libdir}/ClanLib/libclan-input-tty.so*
%attr(755,root,root) %{_libdir}/ClanLib/libclan-network.so*
%attr(755,root,root) %{_libdir}/ClanLib/libclan-sound.so*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ClanLib/libclan-display-x11.so*

%files OpenGL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanGL.so.*.*
%attr(755,root,root) %{_libdir}/ClanLib/libclan-display-glx.so*

%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ClanLib/libclan-display-svgalib.so*

%files Magick
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanMagick.so.*.*

%files MikMod
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclanMikMod.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *gz
%doc html
%{_mandir}/man?/*
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_bindir}/*
%{_includedir}/ClanLib

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/lib*.a
