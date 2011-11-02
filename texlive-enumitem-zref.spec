Name:		texlive-enumitem-zref
Version:	1.8
Release:	1
Summary:	Extended references to items for enumitem package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/enumitem-zref
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enumitem-zref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enumitem-zref.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enumitem-zref.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package is a companion for the enumitem package; it makes
it possible to reference any item in lists formatted by
enumitem lists, viz., enumerated, itemize and description
lists, and any list defined (or customised) with \newlist or
\setlist. References may be typeset differently with
options/properties and even arbitrary text. With hyperref,
anchors are added for each item to enable hyperlinks within the
document or even to external documents. Three schemes are
provided to make reference names (including the standard \label
command).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/enumitem-zref/enumitem-zref.sty
%doc %{_texmfdistdir}/doc/latex/enumitem-zref/README
%doc %{_texmfdistdir}/doc/latex/enumitem-zref/enumitem-zexample.tex
%doc %{_texmfdistdir}/doc/latex/enumitem-zref/enumitem-zref.pdf
#- source
%doc %{_texmfdistdir}/source/latex/enumitem-zref/enumitem-zref.drv
%doc %{_texmfdistdir}/source/latex/enumitem-zref/enumitem-zref.dtx
%doc %{_texmfdistdir}/source/latex/enumitem-zref/enumitem-zref.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
