%global srcname wikipedia
%global sum Wikipedia API for Python

Name:           python-%{srcname}
Version:        1.4.5
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/barrust/Wikipedia
Source0:        %{url}/archive/v%{version}.tar.gz

BuildArch:      noarch

%description
Search Wikipedia, get article summaries, get data like links and images
from a page, and more.

%package -n     python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}
BuildRequires:  python2-devel
BuildRequires:  python-beautifulsoup4
BuildRequires:  python-nose
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
BuildRequires:  python3-nose
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
Requires:       python3-beautifulsoup4
Requires:       python3-requests

%description -n python3-%{srcname}
Search Wikipedia, get article summaries, get data like links and images
from a page, and more.

%prep
%autosetup -n Wikipedia-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
nosetests -v tests
nosetests-%{python2_version}
nosetests-%{python3_version}

%files -n python2-%{srcname}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-*.egg-info

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-*.egg-info

%changelog
* Fri Sep 02 2016 Maxim Orlov <murmansksity@gmail.com> - 1.4.5-1.R
- Update to 1.4.5

* Thu Sep 01 2016 Maxim Orlov <murmansksity@gmail.com> - 1.4.4-1.R
- Update to 1.4.4

* Fri Aug 05 2016 Maxim Orlov <murmansksity@gmail.com> - 1.4.3-1.R
- Update to 1.4.3
- Drop all patches

* Thu May 19 2016 Maxim Orlov <murmansksity@gmail.com> - 1.4.2-1.R
- Update to 1.4.2
- Add 0002-__version__-fix.patch

* Mon May 16 2016 Maxim Orlov <murmansksity@gmail.com> - 1.4.1-1.R
- Update to 1.4.1
- Use a new Source0/URL
- Add BR: python-nose
- Add BR: python3-nose
- Add 0001-Fix-tests.patch

* Sun May 15 2016 Maxim Orlov <murmansksity@gmail.com> - 1.4.0-2.R
- Add tests
- Add missing R: python-requests
- Add missing R: python3-requests

* Wed Nov 18 2015 Maxim Orlov <murmansksity@gmail.com> - 1.4.0-1.R
- Initial package.
