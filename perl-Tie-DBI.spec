%define	modname	Tie-DBI
%define modver 1.06

Summary:	Tie hashes to DBI relational databases 
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	8
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/Tie/Tie-DBI-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(DBD::SQLite)

%description
This module allows you to tie Perl associative arrays (hashes) to SQL databases
using the DBI interface. The tied hash is associated with a table in a local or
networked database. One column becomes the hash key. Each row of the table
becomes an associative array, from which individual fields can be set or
retrieved.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make 

%check
# test require a real database

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Tie
%{_mandir}/man3/*


