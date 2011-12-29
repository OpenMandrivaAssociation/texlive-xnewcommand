# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/xnewcommand
# catalog-date 2008-08-24 14:46:50 +0200
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-xnewcommand
Version:	1.2
Release:	1
Summary:	Define \global and \protected commands with \newcommand
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xnewcommand
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xnewcommand.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xnewcommand.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means of defining \global and (e-TeX)
\protected commands, within the framework of LaTeX's standard
\newcommand.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xnewcommand/xnewcommand.sty
%doc %{_texmfdistdir}/doc/latex/xnewcommand/README
%doc %{_texmfdistdir}/doc/latex/xnewcommand/xnewcommand.pdf
%doc %{_texmfdistdir}/doc/latex/xnewcommand/xnewcommand.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
