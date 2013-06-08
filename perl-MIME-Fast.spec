#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MIME
%define		pnam	Fast
Summary:	MIME::Fast - parsing MIME messages (wrapper for C gmime library)
Summary(pl.UTF-8):	MIME::Fast - przetwarzanie wiadomości MIME (interfejs do biblioteki gmime)
Name:		perl-MIME-Fast
Version:	1.6
Release:	5
# same as perl or GPL v2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MIME/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3c6466c7645bed52ae6bbce9705e3814
Patch0:		%{name}-gmime.patch
URL:		http://search.cpan.org/dist/MIME-Fast/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
# Can't test with earlier versions of gmime-2
BuildRequires:	gmime-devel >= 2.1.0
%if %{with tests}
BuildRequires:	perl(Test::More)
# We don't have this
#BuildRequires:	perl-PerlIO-gzip
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIME::Fast is a perl module for creating, editing and parsing MIME
messages.  This module is based on the very good C library called
gmime (currently in development). MIME::Fast outght to be faster and
should use less memory and CPU resources than standard MIME (perl
module), because MIME::Fast is the wrapper for C functions (calling
C function is much, much less expensive than calling perl function).

%description -l pl.UTF-8
MIME::Fast to moduł Perla do tworzenia, edycji i analizy wiadomości
MIME. Ten moduł jest oparty na bardzo dobrej bibliotece C o nazwie
gmime (aktualnie rozwijanej). MIME::Fast powinien być szybszy i używać
mniej pamięci oraz zasobów procesora niż standardowy moduł Perla MIME,
ponieważ jest interfejsem do funkcji w C (wywołanie funkcji C jest
dużo, dużo mniej kosztowne niż wywołanie funkcji perlowej).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorarch}/MIME/Fast.pm
%dir %{perl_vendorarch}/auto/MIME/Fast
%attr(755,root,root) %{perl_vendorarch}/auto/MIME/Fast/*.so
%{_mandir}/man3/*
