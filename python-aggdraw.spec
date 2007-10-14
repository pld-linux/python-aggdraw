#
# NOTE: The source code of aggdraw contain needed files from AGG library
#       source tree and the module itself isn't dynamically linked with
#       AGG, so there's no need for 'BR: agg-devel' and 'R: agg'. This
#       however may change in the future versions of aggdraw.
%define		package		aggdraw
%define		buildver	20051010
#
%bcond_without	freetype2	# Build without freetype support
#
Summary:	An add-on to the PIL library that supports anti-aliased drawing
Summary(pl.UTF-8):	Dodatek do biblioteki PIL z obsługą rysowania z wygładzaniem
Name:		python-aggdraw
Version:	1.1
Release:	0.%{buildver}.1
License:	Python (MIT style)
Group:		Libraries/Python
Source0:	http://effbot.org/media/downloads/%{package}-%{version}-%{buildver}.zip
# Source0-md5:	9dd2dc67f079592d87970aed0bc5d519
%{?with_freetype2:Patch0:	%{name}-freetype-enable.patch}
URL:		http://effbot.org/zone/aggdraw-index.htm
%{?with_freetype2:BuildRequires:	freetype-devel}
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The aggdraw module implements the basic WCK 2D Drawing Interface on
top of the AGG library. This library provides high-quality drawing,
with anti-aliasing and alpha compositing, while being fully compatible
with the WCK renderer.

%description -l pl.UTF-8
Moduł aggdraw implementuje podstawowy interfejs WCK 2D Drawing
Interface ponad biblioteką AGG. Biblioteka ta pozwala na wykonywanie
wysokiej jakości rysunków z obsługą wygładzania krawędzi i kanałem
alpha będąc jednocześnie w pełni kompatybilną z silnikiem renderującym
WCK.

%prep
%setup -q -n %{package}-%{version}-%{buildver}
%if %{with freetype2}
%patch0 -p1
%endif

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT

%{__python} ./setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{py_sitedir}/*.so
