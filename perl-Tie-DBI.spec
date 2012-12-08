%define	upstream_name	 Tie-DBI
%define upstream_version 1.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Tie hashes to DBI relational databases 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Tie/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(DBD::SQLite)
BuildArch:	noarch

%description
This module allows you to tie Perl associative arrays (hashes) to SQL databases
using the DBI interface. The tied hash is associated with a table in a local or
networked database. One column becomes the hash key. Each row of the table
becomes an associative array, from which individual fields can be set or
retrieved.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.50.0-4mdv2012.0
+ Revision: 765764
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Thu May 05 2011 Funda Wang <fwang@mandriva.org> 1.50.0-2
+ Revision: 669255
- cleanup spec

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Wed Apr 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.50.0-1mdv2011.0
+ Revision: 534935
- new version

* Thu Apr 01 2010 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-1mdv2010.1
+ Revision: 530666
- update to 1.04

* Tue Mar 30 2010 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2010.1
+ Revision: 529784
- update to 1.03

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2010.0
+ Revision: 405719
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.02-4mdv2009.0
+ Revision: 224400
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.02-3mdv2008.1
+ Revision: 180611
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-2mdv2008.0
+ Revision: 47043
- rebuild


* Wed May 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2007.0
- New release 1.02

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-2mdk
- %%mkrel
- spec cleanup
- rpmbuildupdate aware
- fix directory ownership
- better summary and description

* Tue Mar 08 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.01-1mdk
- 1.01

* Mon Nov 29 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.94-1mdk
- 0.94

* Thu Jun 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.93-1mdk
- 0.93
- drop redundant buildrequires and requires
- cosmetics

