%define		packname	geneplotter

Summary:	Graphics related functions for Bioconductor
Name:		R-%{packname}
Version:	1.40.0
Release:	1
License:	Artistic 2.0
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	6c8bead575f194a4331303b6d3a21bf4
URL:		http://bioconductor.org/packages/release/bioc/html/geneplotter.html
BuildRequires:	R
BuildRequires:	R-annotate
BuildRequires:	R-AnnotationDbi
BuildRequires:	R-Biobase
BuildRequires:	R-cran-RColorBrewer
BuildRequires:	R-Biobase
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-annotate
Requires:	R-AnnotationDbi
Requires:	R-Biobase
Requires:	R-cran-RColorBrewer
Requires:	R-Biobase
Suggests:	R-Rgraphviz
Suggests:	R-fibroEset
Suggests:	R-hgu95av2.db
Suggests:	R-hu6800.db
Suggests:	R-hgu133a.db
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Some basic functions for plotting genetic data.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS.Rd
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/data
