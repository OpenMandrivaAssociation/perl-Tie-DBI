%define	modname	Tie-DBI
%define modver 1.08

Summary:	Tie hashes to DBI relational databases 
Name:		perl-%{modname}
Version:	%{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://wiki.github.com/toddr/Tie-DBI
Source0:	https://cpan.metacpan.org/authors/id/T/TO/TODDR/Tie-DBI-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
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
%doc Changes
%{perl_vendorlib}/Tie
%{_mandir}/man3/*


