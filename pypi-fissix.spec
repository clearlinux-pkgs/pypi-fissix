#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-fissix
Version  : 21.11.13
Release  : 16
URL      : https://files.pythonhosted.org/packages/94/cb/fe0df0273fd88dbaa4b0c6ed6b7e3e1dc5348f9595622b81da32499197bb/fissix-21.11.13.tar.gz
Source0  : https://files.pythonhosted.org/packages/94/cb/fe0df0273fd88dbaa4b0c6ed6b7e3e1dc5348f9595622b81da32499197bb/fissix-21.11.13.tar.gz
Summary  : Monkeypatches to override default behavior of lib2to3.
Group    : Development/Tools
License  : Python-2.0
Requires: pypi-fissix-license = %{version}-%{release}
Requires: pypi-fissix-python = %{version}-%{release}
Requires: pypi-fissix-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(appdirs)
BuildRequires : pypi(flit_core)

%description
fissix
======
Backport of latest lib2to3, with enhancements.
[![build status](https://travis-ci.org/jreese/fissix.svg?branch=master)](https://travis-ci.org/jreese/fissix)
[![version](https://img.shields.io/pypi/v/fissix.svg)](https://pypi.org/project/fissix)
[![license](https://img.shields.io/pypi/l/fissix.svg)](https://github.com/jreese/fissix/blob/master/LICENSE)
[![code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

%package license
Summary: license components for the pypi-fissix package.
Group: Default

%description license
license components for the pypi-fissix package.


%package python
Summary: python components for the pypi-fissix package.
Group: Default
Requires: pypi-fissix-python3 = %{version}-%{release}

%description python
python components for the pypi-fissix package.


%package python3
Summary: python3 components for the pypi-fissix package.
Group: Default
Requires: python3-core
Provides: pypi(fissix)
Requires: pypi(appdirs)

%description python3
python3 components for the pypi-fissix package.


%prep
%setup -q -n fissix-21.11.13
cd %{_builddir}/fissix-21.11.13
pushd ..
cp -a fissix-21.11.13 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656405195
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-fissix
cp %{_builddir}/fissix-21.11.13/LICENSE %{buildroot}/usr/share/package-licenses/pypi-fissix/d9e4c07df8805b7ff5a20663e7b154c8dd1ddc8b
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-fissix/d9e4c07df8805b7ff5a20663e7b154c8dd1ddc8b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
