#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v13
# autospec commit: 2659038
#
Name     : perl-XS-Parse-Keyword
Version  : 0.43
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/XS-Parse-Keyword-0.43.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/XS-Parse-Keyword-0.43.tar.gz
Summary  : 'XS functions to assist in parsing keyword syntax'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-XS-Parse-Keyword-license = %{version}-%{release}
Requires: perl-XS-Parse-Keyword-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::CChecker)
BuildRequires : perl(File::ShareDir)
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
%setup -q -n XS-Parse-Keyword-0.43
cd %{_builddir}/XS-Parse-Keyword-0.43
pushd ..
cp -a XS-Parse-Keyword-0.43 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XS-Parse-Keyword
cp %{_builddir}/XS-Parse-Keyword-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-XS-Parse-Keyword/ff3cb0dfd45f53bab83fc8e6480335b7afdc4bbe || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.40.0/x86_64-linux-thread-multi/auto/share/dist/XS-Parse-Keyword/include/XSParseInfix.h
/usr/lib/perl5/vendor_perl/5.40.0/x86_64-linux-thread-multi/auto/share/dist/XS-Parse-Keyword/include/XSParseKeyword.h
/usr/share/man/man3/XS::Parse::Infix.3
/usr/share/man/man3/XS::Parse::Infix::Builder.3
/usr/share/man/man3/XS::Parse::Keyword.3
/usr/share/man/man3/XS::Parse::Keyword::Builder.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XS-Parse-Keyword/ff3cb0dfd45f53bab83fc8e6480335b7afdc4bbe

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
