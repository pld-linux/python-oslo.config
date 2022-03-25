#
# Conditional build:
%bcond_with	doc	# do build doc (missing deps)
%bcond_with	tests	# do perform "make test" (missing deps)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Oslo Configuration API
Name:		python-oslo.config
Version:	4.11.0
Release:	5
License:	Apache
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/o/oslo.config/oslo.config-%{version}.tar.gz
# Source0-md5:	144c11b78b24c3d7393e23c5eaf2fedf
URL:		https://pypi.python.org/pypi/oslo.config
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%endif
Requires:	python-PyYAML >= 3.10.0
Requires:	python-debtcollector >= 1.2.0
Requires:	python-netaddr >= 0.7.13
Requires:	python-oslo.i18n >= 2.1.0
Requires:	python-rfc3986 >= 0.3.1
Requires:	python-six >= 1.9.0
Requires:	python-stevedore >= 1.20.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Oslo configuration API supports parsing command line arguments and
.ini style configuration files.

%package -n python3-oslo.config
Summary:	Oslo Configuration API
Group:		Libraries/Python
Requires:	python3-PyYAML >= 3.10.0
Requires:	python3-debtcollector >= 1.2.0
Requires:	python3-netaddr >= 0.7.13
Requires:	python3-oslo.i18n >= 2.1.0
Requires:	python3-rfc3986 >= 0.3.1
Requires:	python3-six >= 1.9.0
Requires:	python3-stevedore >= 1.20.0

%description -n python3-oslo.config
The Oslo configuration API supports parsing command line arguments and
.ini style configuration files.

%package apidocs
Summary:	API documentation for Python oslo.config module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona oslo.config
Group:		Documentation

%description apidocs
API documentation for Pythona oslo.config module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona oslo.config.

%prep
%setup -q -n oslo.config-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd doc
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/oslo_config
%{py_sitescriptdir}/oslo.config-%{version}-py*.egg-info
%if %{without python3}
%attr(755,root,root) %{_bindir}/oslo-config-generator
%endif
%endif

%if %{with python3}
%files -n python3-oslo.config
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%attr(755,root,root) %{_bindir}/oslo-config-generator
%{py3_sitescriptdir}/oslo_config
%{py3_sitescriptdir}/oslo.config-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/*
%endif
