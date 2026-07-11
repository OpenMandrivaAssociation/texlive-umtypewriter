%global tl_name umtypewriter
%global tl_revision 64443

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Fonts to typeset with the xgreek package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/umtypewriter
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/umtypewriter.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/umtypewriter.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The UMTypewriter font family is a monospaced font family that was built
from glyphs from the CB Greek fonts, the CyrTUG Cyrillic alphabet fonts
("LH"), and the standard Computer Modern font family. It contains four
OpenType fonts which are required for use of the xgreek package for
XeLaTeX.

