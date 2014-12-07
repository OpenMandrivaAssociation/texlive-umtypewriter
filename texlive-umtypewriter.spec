# revision 18651
# category Package
# catalog-ctan /fonts/umtypewriter
# catalog-date 2009-07-23 15:45:58 +0200
# catalog-license ofl
# catalog-version 001.002
Name:		texlive-umtypewriter
Version:	001.002
Release:	9
Summary:	Fonts to typeset with the xgreek package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/umtypewriter
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umtypewriter.tar.xz
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
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 001.002-2
+ Revision: 757281
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 001.002-1
+ Revision: 719844
- texlive-umtypewriter
- texlive-umtypewriter
- texlive-umtypewriter

