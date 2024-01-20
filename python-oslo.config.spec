#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (incomplete dependencies)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Oslo Configuration API
Summary(pl.UTF-8):	API do konfiguracji Oslo
Name:		python-oslo.config
# keep 7.x here for python2 support
Version:	7.0.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/o/oslo.config/oslo.config-%{version}.tar.gz
# Source0-md5:	b065afbe51bac25fa8981d9da1ca782c
URL:		https://pypi.org/project/oslo.config/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-PyYAML >= 3.12
BuildRequires:	python-debtcollector >= 1.2.0
BuildRequires:	python-enum34 >= 1.0.4
BuildRequires:	python-fixtures >= 3.0.0
BuildRequires:	python-mock >= 3.0.0
BuildRequires:	python-netaddr >= 0.7.18
BuildRequires:	python-oslo.i18n >= 3.15.3
BuildRequires:	python-oslo.log >= 3.36.0
BuildRequires:	python-oslotest >= 3.2.0
BuildRequires:	python-requests >= 2.18.0
BuildRequires:	python-requests-mock >= 1.5.0
BuildRequires:	python-rfc3986 >= 1.2.0
BuildRequires:	python-six >= 1.10.0
BuildRequires:	python-stestr >= 2.1.0
BuildRequires:	python-stevedore >= 1.20.0
BuildRequires:	python-testscenarios >= 0.4
BuildRequires:	python-testtools >= 2.2.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-PyYAML >= 3.12
BuildRequires:	python3-debtcollector >= 1.2.0
BuildRequires:	python3-fixtures >= 3.0.0
BuildRequires:	python3-mock >= 3.0.0
BuildRequires:	python3-netaddr >= 0.7.18
BuildRequires:	python3-oslo.i18n >= 3.15.3
BuildRequires:	python3-oslo.log >= 3.36.0
BuildRequires:	python3-oslotest >= 3.2.0
BuildRequires:	python3-requests >= 2.18.0
BuildRequires:	python3-requests-mock >= 1.5.0
BuildRequires:	python3-rfc3986 >= 1.2.0
BuildRequires:	python3-six >= 1.10.0
BuildRequires:	python3-stestr >= 2.1.0
BuildRequires:	python3-stevedore >= 1.20.0
BuildRequires:	python3-testscenarios >= 0.4
BuildRequires:	python3-testtools >= 2.2.0
%endif
%endif
%if %{with doc}
BuildRequires:	python-debtcollector >= 1.2.0
BuildRequires:	python-netaddr >= 0.7.18
BuildRequires:	python-openstackdocstheme >= 1.20.0
BuildRequires:	python-oslo.i18n >= 3.15.3
BuildRequires:	python-reno >= 2.5.0
BuildRequires:	python-rfc3986 >= 1.2.0
BuildRequires:	python-sphinxcontrib-apidoc >= 0.2.0
BuildRequires:	sphinx-pdg-2 >= 1.8.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Oslo configuration API supports parsing command line arguments and
.ini style configuration files.

%description -l pl.UTF-8
API konfiguracyjne Oslo obsługuje analizę argumentów linii poleceń
oraz plików konfiguracyjnych w stylu .ini.

%package -n python3-oslo.config
Summary:	Oslo Configuration API
Summary(pl.UTF-8):	API do konfiguracji Oslo
Group:		Libraries/Python

%description -n python3-oslo.config
The Oslo configuration API supports parsing command line arguments and
.ini style configuration files.

%description -n python3-oslo.config -l pl.UTF-8
API konfiguracyjne Oslo obsługuje analizę argumentów linii poleceń
oraz plików konfiguracyjnych w stylu .ini.

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
PYTHONPATH=$(pwd) \
sphinx-build-2 -b html doc/source doc/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__mv} $RPM_BUILD_ROOT%{_bindir}/oslo-config-generator{,-2}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/oslo-config-validator{,-2}

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/oslo_config/tests
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/oslo-config-generator{,-3}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/oslo-config-validator{,-3}
ln -sf /oslo-config-validator-3 $RPM_BUILD_ROOT%{_bindir}/oslo-config-generator
ln -sf /oslo-config-validator-3 $RPM_BUILD_ROOT%{_bindir}/oslo-config-validator

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/oslo_config/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%attr(755,root,root) %{_bindir}/oslo-config-generator-2
%attr(755,root,root) %{_bindir}/oslo-config-validator-2
%{py_sitescriptdir}/oslo_config
%{py_sitescriptdir}/oslo.config-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-oslo.config
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%attr(755,root,root) %{_bindir}/oslo-config-generator
%attr(755,root,root) %{_bindir}/oslo-config-generator-3
%attr(755,root,root) %{_bindir}/oslo-config-validator
%attr(755,root,root) %{_bindir}/oslo-config-validator-3
%{py3_sitescriptdir}/oslo_config
%{py3_sitescriptdir}/oslo.config-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,cli,configuration,contributor,reference,*.html,*.js}
%endif
