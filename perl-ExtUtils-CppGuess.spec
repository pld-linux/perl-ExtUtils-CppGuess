#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	ExtUtils
%define		pnam	CppGuess
Summary:	ExtUtils::CppGuess - guess C++ compiler and flags
Name:		perl-ExtUtils-CppGuess
Version:	0.09
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f8ada38ee4ad86a4f1e20d8525ce0c99
URL:		http://search.cpan.org/dist/ExtUtils-CppGuess/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Capture-Tiny
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::CppGuess attempts to guess the system's C++ compiler
that is compatible with the C compiler that your perl was built with.

It can generate the necessary options to the Module::Build
constructor or to ExtUtils::MakeMaker's WriteMakefile
function.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/ExtUtils/CppGuess.pm
%{_mandir}/man3/*
