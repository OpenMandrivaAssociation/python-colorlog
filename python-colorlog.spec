Summary:	A colored formatter for the python logging module 
Name:		python-colorlog
Version:	6.8.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/c/colorlog/colorlog-%{version}.tar.gz
URL:		https://pypi.org/project/colorlog/
License:	MIT License
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Add colours to the output of Python's logging module.

%prep
%autosetup -p1 -n colorlog-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/colorlog
%{py_sitedir}/colorlog-*.*-info
