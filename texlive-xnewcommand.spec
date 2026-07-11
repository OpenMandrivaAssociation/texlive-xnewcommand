%global tl_name xnewcommand
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Define \global and \protected commands with \newcommand
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xnewcommand
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xnewcommand.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xnewcommand.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the means of defining \global and (e-TeX)
\protected commands, within the framework of LaTeX's standard
\newcommand.

