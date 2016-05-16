%global srcname wikipedia
%global sum Wikipedia API for Python

Name:           python-%{srcname}
Version:        1.4.0
Release:        2%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/wikipedia
Source0:        https://pypi.python.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Search Wikipedia, get article summaries, get data like links and images
from a page, and more.

%package -n     python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}
BuildRequires:  python2-devel
BuildRequires:  python-beautifulsoup4
BuildRequires:  python-requests
BuildRequires:  python-setuptools
Requires:       python-beautifulsoup4
Requires:       python-requests

%description -n python2-%{srcname}
Search Wikipedia, get article summaries, get data like links and images
from a page, and more.

%package -n     python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
Requires:       python3-beautifulsoup4
Requires:       python3-requests

%description -n python3-%{srcname}
Search Wikipedia, get article summaries, get data like links and images
from a page, and more.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{srcname}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/*.egg-info

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/*.egg-info

%changelog
* Sun May 15 2016 Maxim Orlov <murmansksity@gmail.com> - 1.4.0-2.R
- Add tests
- Add missing R: python-requests
- Add missing R: python3-requests

* Wed Nov 18 2015 Maxim Orlov <murmansksity@gmail.com> - 1.4.0-1.R
- Initial package.
