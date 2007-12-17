%define	module	Tie-DBI
%define name	perl-%{module}
%define version	1.02
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Tie hashes to DBI relational databases 
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/Tie/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch

%description
This module allows you to tie Perl associative arrays (hashes) to SQL databases
using the DBI interface. The tied hash is associated with a table in a local or
networked database. One column becomes the hash key. Each row of the table
becomes an associative array, from which individual fields can be set or
retrieved.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor CFLAGS="%{optflags}"
%make 

%check
# test require a real database

%install
rm -rf %{buildroot} 
%{makeinstall_std}

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Tie
%{_mandir}/*/*

