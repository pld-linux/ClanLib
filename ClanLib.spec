Summary:	ClanLib, the platform independent game SDK.
Summary(pl):	ClanLib, niezależny od platformy SDK do gier
Name:		ClanLib
Version:	0.1.14
Release:	1
Copyright:	LGPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		http://dark.x.dtu.dk/clansoft/clanlib/download/%{name}-%{version}.tgz
URL:		http://clanlib.org
BuildPrereq:	libpng-devel
BuildPrereq:	libz-devel
BuildPrereq:	Hermes-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The ClanLib SDK is designed to provide an platform independent game SDK using
a lot cleaner (and object oriented) interface than the traditional way it is
done in DirectX, SDL and such. The goals is to avoid game developers
constantly reinventing the wheel by providing smarter ways to eg. load
surfaces.

%description -l pl
ClanLib SDK jest projektowany jako niezależny od platformy SDK dla gier.
Stosuje prosty (i zorienrowany obiektowo) interfejs, przejrzystszy niż
DirectX, SDL i inne.

%package devel
Summary:	ClanLib development package
Summary(pl):	pakiet programistyczny dla ClanLib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki

%description devel
This is the development add-on package that includes the header files needed
to compile new ClanLib applications.

%description -l pl devel
Programistyczne dodatki do ClanLib-a, zawierają pliki nagłówkowe potrzebne
do kompilacji programów korzystających z CleanLib.

%package static
Summary:	ClanLib development package
Summary(pl):	pakiet programistyczny dla ClanLib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki

%description static
This is the development add-on package that includes the header files needed
to compile new ClanLib applications.

%description -l pl staic
Programistyczne dodatki do ClanLib-a, zawierają pliki nagłówkowe potrzebne
do kompilacji programów korzystających z CleanLib.

%prep
%setup -q -n ClanLib
%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make 	LIB_PREFIX="$RPM_BUILD_ROOT/usr/lib" \
	BIN_PREFIX="$RPM_BUILD_ROOT/usr/bin" \
	INC_PREFIX="$RPM_BUILD_ROOT/usr/include" \
	install

strip $RPM_BUILD_ROOT/usr/lib/lib*.so*

gzip -9nf README TODO CREDITS

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/lib*.so*

%files devel
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) /usr/bin/datafile_compiler
/usr/include/ClanLib

%file static
%defattr(644,root,root,755)
/usr/lib/lib*.a

%changelog
* Tue Apr 20 1999 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>
  [0.1.14-2]
- added BuildPrereq (libpng-devel, libz-devel, Hermes-devel).
- added -q %setup patameter,
- added static subpackage.

* Mon Apr 19 1999 Konrad Stepień <kornad@interdata.com.pl>
  [0.1.14-1]
- initial version
