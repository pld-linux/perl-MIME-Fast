#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MIME
%define	pnam	Fast
Summary:	MIME::Fast - parsing MIME messages (wrapper for C gmime library)
Summary(pl):	MIME::Fast - przetwarzanie wiadomo¶ci MIME (interfejs do biblioteki gmime)
Name:		perl-MIME-Fast
Version:	1.4
Release:	1
# same as perl or GPL v2
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ae477eeeb5d6c198d221ae9205a3be22
BuildRequires:	perl-devel >= 5.8.0
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

%description -l pl
MIME::Fast to modu³ Perla do tworzenia, edycji i analizy wiadomo¶ci
MIME. Ten modu³ jest oparty na bardzo dobrej bibliotece C o nazwie
gmime (aktualnie rozwijanej). MIME::Fast powinien byæ szybszy i u¿ywaæ
mniej pamiêci oraz zasobów procesora ni¿ standardowy modu³ Perla MIME,
poniewa¿ jest interfejsem do funkcji w C (wywo³anie funkcji C jest
du¿o, du¿o mniej kosztowne ni¿ wywo³anie funkcji perlowej).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
