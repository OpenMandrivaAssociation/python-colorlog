%define module colorlog

Name:		python-colorlog
Summary:	A colored formatter for the python logging module
Version:	6.10.1
Release:	1
License:	MIT License
Group:		Development/Python
URL:		https://pypi.org/project/colorlog/
Source0:	https://files.pythonhosted.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Add colours to the output of Python's logging module.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}-py%{pyver}.*-info
