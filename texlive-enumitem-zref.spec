%global tl_name enumitem-zref
%global tl_revision 75712

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.8
Release:	%{tl_revision}.1
Summary:	Extended references to items for enumitem package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/enumitem-zref
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/enumitem-zref.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/enumitem-zref.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/enumitem-zref.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is a companion for the enumitem package; it makes it
possible to reference any item in lists formatted by enumitem lists,
viz., enumerated, itemize and description lists, and any list defined
(or customised) with \newlist or \setlist. References may be typeset
differently with options/properties and even arbitrary text. With
hyperref, anchors are added for each item to enable hyperlinks within
the document or even to external documents. Three schemes are provided
to make reference names (including the standard \label command). The
package is currently broken, cf.
https://tex.stackexchange.com/q/664886/1090

