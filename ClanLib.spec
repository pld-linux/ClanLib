Summary:	ClanLib, the platform independent game SDK.
Summary(pl):	ClanLib, niezale¿ny od platformy SDK do gier
Name:		ClanLib
Version:	0.1.14
Release:	1
Copyright:	LGPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		http://dark.x.dtu.dk/clansoft/clanlib/download/%{name}-%{version}.tgz
URL:		http://clanlib.org
BuildPrereq:	libpng-devel
BuildPrereq:	zlib-devel
BuildPrereq:	Hermes-devel
BuildPrereq:	libstdc++-devel
BuildPrereq:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The ClanLib SDK is designed to provide an platform independent game SDK using
a lot cleaner (and object oriented) interface than the traditional way it is
done in DirectX, SDL and such. The goals is to avoid game developers
constantly reinventing the wheel by providing smarter ways to eg. load
surfaces.

%description -l pl
ClanLib SDK jest projektowany jako niezale¿ny od platformy SDK dla gier.
Stosuje prosty (i zorienrowany obiektowo) interfejs, przejrzystszy ni¿
DirectX, SDL i inne.

%package devel
Summary:	ClanLib development package
Summary(pl):	pakiet programistyczny dla ClanLib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This is the development add-on package that includes the header files needed
to compile new ClanLib applications.

%description -l pl devel
Programistyczne dodatki do ClanLib-a, zawieraj± pliki nag³ówkowe potrzebne
do kompilacji programów korzystaj±cych z CleanLib.

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
%setup -q -n ClanLib
%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make 	LIB_PREFIX="$RPM_BUILD_ROOT%{_libdir}" \
	BIN_PREFIX="$RPM_BUILD_ROOT/usr/bin" \
	INC_PREFIX="$RPM_BUILD_ROOT/usr/include" \
	install

strip $RPM_BUILD_ROOT%{_libdir}/lib*.so*

gzip -9nf README TODO CREDITS

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so*

%files devel
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) /usr/bin/datafile_compiler
/usr/include/ClanLib

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Tue Apr 20 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.1.14-2]
- added BuildPrereq (libpng-devel, libz-devel, Hermes-devel).
- added -q %setup patameter,
- added static subpackage.

* Mon Apr 19 1999 Konrad Stepieñ <kornad@interdata.com.pl>
  [0.1.14-1]
- initial version
