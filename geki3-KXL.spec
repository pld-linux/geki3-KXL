Summary:	Geki3, a video-oriented game
Summary(pl):	Geki3 - gra wideo
Name:		geki3-KXL
Version:	1.0.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://kxl.hn.org/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-scorepath.patch
URL:		http://kxl.hn.org/games.php
BuildRequires:	KXL-devel >= 1.1.5
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	KXL >= 1.1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
2D horizon scroll shooting game.

%description -l pl
Poziomo przewijana strzelanka 2D.

%prep
%setup -q
%patch -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(2755,root,games) %{_bindir}/geki3
%dir %{_datadir}/geki3
%{_datadir}/geki3/bmp
%{_datadir}/geki3/wav
%dir %{_datadir}/geki3/data
%{_datadir}/geki3/data/*.dat
%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/geki3.score
