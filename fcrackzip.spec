Name:		fcrackzip
Version:	1.0
Release:	2
Summary:	A zip password cracker
License:	GPLv2
Group:		File tools
URL:		http://oldhome.schmorp.de/marc/fcrackzip.html
Source:		http://oldhome.schmorp.de/marc/data/%{name}-%{version}.tar.gz
Requires:	unzip

%description
A zip password cracker.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std
%__rm -f %{buildroot}%{_bindir}/zipinfo

%clean
%__rm -rf %{buildroot}

%files
%doc COPYING README NEWS AUTHORS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*



%changelog
* Thu Feb 23 2012 Andrey Bondrov <abondrov@mandriva.org> 1.0-1
+ Revision: 779345
- imported package fcrackzip

