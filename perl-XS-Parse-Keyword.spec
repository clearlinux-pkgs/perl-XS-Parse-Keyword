#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XS-Parse-Keyword
Version  : 0.33
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/XS-Parse-Keyword-0.33.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/XS-Parse-Keyword-0.33.tar.gz
Summary  : 'XS functions to assist in parsing keyword syntax'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-XS-Parse-Keyword-license = %{version}-%{release}
Requires: perl-XS-Parse-Keyword-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::CChecker)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
XS::Parse::Keyword - XS functions to assist in parsing keyword syntax
DESCRIPTION

%package dev
Summary: dev components for the perl-XS-Parse-Keyword package.
Group: Development
Provides: perl-XS-Parse-Keyword-devel = %{version}-%{release}
Requires: perl-XS-Parse-Keyword = %{version}-%{release}

%description dev
dev components for the perl-XS-Parse-Keyword package.


%package license
Summary: license components for the perl-XS-Parse-Keyword package.
Group: Default

%description license
license components for the perl-XS-Parse-Keyword package.


%package perl
Summary: perl components for the perl-XS-Parse-Keyword package.
Group: Default
Requires: perl-XS-Parse-Keyword = %{version}-%{release}

%description perl
perl components for the perl-XS-Parse-Keyword package.


%prep
%setup -q -n XS-Parse-Keyword-0.33
cd %{_builddir}/XS-Parse-Keyword-0.33

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XS-Parse-Keyword
cp %{_builddir}/XS-Parse-Keyword-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-XS-Parse-Keyword/df9f2d29a10846c30925e18b0273e53356f88a79 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XS::Parse::Infix.3
/usr/share/man/man3/XS::Parse::Infix::Builder.3
/usr/share/man/man3/XS::Parse::Keyword.3
/usr/share/man/man3/XS::Parse::Keyword::Builder.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XS-Parse-Keyword/df9f2d29a10846c30925e18b0273e53356f88a79

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
