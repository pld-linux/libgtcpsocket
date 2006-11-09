Summary:	Glib/GObject Networking Library
Summary(pl):	Biblioteka sieciowa oparta o Glib/GObject
Name:		libgtcpsocket
Version:	0.2.0
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgtcpsocket/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	39b811a4049b737d5c068f0e113f3431
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	intltool >= 0.25
BuildRequires:	libtool
Requires(post):	/sbin/ldconfig
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTcpSocket is an object-based multi-threaded TCP/IP networking
wrapper. It provides application-transparent support for proxies and
basic SSL encryption.

%description -l pl
GTcpSocket to obiektowy, wielow±tkowy interfejs do funkcji sieciowych
TCP/IP. Daje przezroczyst± dla aplikacji obs³ugê proxy i podstawowego
szyfrowania SSL.

%package devel
Summary:	Headers for libgtcpsocket
Summary(pl):	Pliki nag³ówkowe libgtcpsocket
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Headers for libgtcpsocket.

%description devel -l pl
Pliki nag³ówkowe libgtcpsocket.

%package static
Summary:	Static libgtcpsocket libraries
Summary(pl):	Statyczne biblioteki libgtcpsocket
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libgtcpsocket libraries.

%description static -l pl
Statyczna wersja bibliotek libgtcpsocket.

%prep
%setup -q

%build
rm -f missing acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-ssl=openssl \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir} \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install

%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/*
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
