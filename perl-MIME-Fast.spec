
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	MIME
%define	pnam	Fast
Summary:	Parsing MIME messages (wrapper for C gmime library)
Summary(pl):	Parsowanie wiadomo¶ci MIME (interfejs do biblioteki gmime)
Name:		perl-MIME-Fast
Version:	1.4
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
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
