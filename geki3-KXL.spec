#
# TODO: move score file(s) to /var/games
#
Summary:	Geki3, a video-oriented game
Summary(pl):	Geki3 - gra wideo
Name:		geki3-KXL
Version:	1.0.2
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source:		http://www2.mwnet.or.jp/~fc3srx7/download/%{name}-%{version}.tar.gz
URL:		http://www2.mwnet.or.jp/~fc3srx7/
BuildRequires:	KXL-devel >= 1.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
2D horizon scroll shooting game.

%description -l pl
Przewijana strzelanka 2D.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/geki3
%doc COPYING ChangeLog README
%dir %{_datadir}/geki3
%{_datadir}/geki3/bmp
%{_datadir}/geki3/wav
%dir %{_datadir}/geki3/data
%{_datadir}/geki3/data/*.dat
# MOVE TO /var/games!!!
%config(noreplace) %{_datadir}/geki3/data/.score
