Name:		texlive-umtypewriter
Version:	64443
Release:	1
Summary:	Fonts to typeset with the xgreek package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/umtypewriter
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umtypewriter.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The UMTypewriter font family is a monospaced font family that
was built from glyphs from the CB Greek fonts, the CyrTUG
Cyrillic alphabet fonts ("LH"), and the standard Computer
Modern font family. It contains four OpenType fonts which are
required for use of the xgreek package for XeLaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/opentype/public/umtypewriter/UMTypewriter-Bold.otf
%{_texmfdistdir}/fonts/opentype/public/umtypewriter/UMTypewriter-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/public/umtypewriter/UMTypewriter-Italic.otf
%{_texmfdistdir}/fonts/opentype/public/umtypewriter/UMTypewriter-Oblique.otf
%{_texmfdistdir}/fonts/opentype/public/umtypewriter/UMTypewriter-Regular.otf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}
