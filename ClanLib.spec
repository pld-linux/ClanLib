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
Summary:	ClanLib development paskage
Summary(pl):	pakiet programistyczny dla ClanLib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki

%description devel
This is the development add-on package that includes the header files needed
to compile new ClanLib applications.

%description -l pl devel
Programistyczne dodatki do ClanLib-a, zawieraj± pliki nag³ówkowe potrzebne
do kompilacji programów korzystaj±cych z CleanLib.

%prep
%setup -n ClanLib
%build
CFLAGS="$RPM_OPT_FLAGS" ./configure -prefix=/usr
make
for i in *.so *.a
do
  strip $i
done

%install
make 	LIB_PREFIX="$RPM_BUILD_ROOT/usr/lib" \
	BIN_PREFIX="$RPM_BUILD_ROOT/usr/bin" \
	INC_PREFIX="$RPM_BUILD_ROOT/usr/include" \
	install

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO CREDITS
%attr(755,root,root) /usr/lib/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/datafile_compiler
/usr/include/ClanLib

%changelog

* Mon Apr 19 1999 Konrad Stepieñ <kornad@interdata.com.pl>
- initial version
