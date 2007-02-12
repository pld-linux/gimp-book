# $Revision: 1.5 $
# ToDo:
#  - Fix descriptions.
#  - Is package name ok? Or maybe, it should be changed to something else,
#    like 'gimp-grokking-the-gimp' or 'Grokking-The-Gimp' ?
#  - Like above, shouldn't it be installed under /usr/share/doc/Grokking-the-Gimp ?

Summary:	The HTML version of "Grokking the GIMP" book
Summary(pl.UTF-8):   Wersja HTML książki "Grokking the GIMP"
Name:		gimp-book
Version:	1.0
Release:	1
License:	OpenContent
Group:		Documentation
Source0:	http://gimp-savvy.com/BOOK/TarDist/Grokking-the-GIMP-v%{version}.tar.gz
# Source0-md5:	ad8a6f4fac66d496d32ec2ac48d5a3ed
URL:		http://gimp-savvy.com/BOOK/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
The gimp-book package contains the HTML version of "Grokking the GIMP"
book. It is great source of knowledge for all who would like to get
familiar with GIMP (GNU Image Manipulation Program).

%description -l pl.UTF-8
Pakiet gimp-book zawiera wersję HTML książki "Grokking the GIMP".

%prep
%setup -q -n Grokking-the-GIMP-v%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *
