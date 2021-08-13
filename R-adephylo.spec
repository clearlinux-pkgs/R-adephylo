#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-adephylo
Version  : 1.1.11
Release  : 33
URL      : https://cran.r-project.org/src/contrib/adephylo_1.1-11.tar.gz
Source0  : https://cran.r-project.org/src/contrib/adephylo_1.1-11.tar.gz
Summary  : Exploratory Analyses for the Phylogenetic Comparative Method
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-adephylo-lib = %{version}-%{release}
Requires: R-ade4
Requires: R-adegenet
Requires: R-ape
Requires: R-phylobase
BuildRequires : R-ade4
BuildRequires : R-adegenet
BuildRequires : R-ape
BuildRequires : R-phylobase
BuildRequires : buildreq-R

%description
and some traits measured for each taxa.

%package lib
Summary: lib components for the R-adephylo package.
Group: Libraries

%description lib
lib components for the R-adephylo package.


%prep
%setup -q -c -n adephylo
cd %{_builddir}/adephylo

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589787937

%install
export SOURCE_DATE_EPOCH=1589787937
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library adephylo
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library adephylo
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library adephylo
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc adephylo || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/adephylo/CITATION
/usr/lib64/R/library/adephylo/DESCRIPTION
/usr/lib64/R/library/adephylo/INDEX
/usr/lib64/R/library/adephylo/Meta/Rd.rds
/usr/lib64/R/library/adephylo/Meta/data.rds
/usr/lib64/R/library/adephylo/Meta/features.rds
/usr/lib64/R/library/adephylo/Meta/hsearch.rds
/usr/lib64/R/library/adephylo/Meta/links.rds
/usr/lib64/R/library/adephylo/Meta/nsInfo.rds
/usr/lib64/R/library/adephylo/Meta/package.rds
/usr/lib64/R/library/adephylo/Meta/vignette.rds
/usr/lib64/R/library/adephylo/NAMESPACE
/usr/lib64/R/library/adephylo/R/adephylo
/usr/lib64/R/library/adephylo/R/adephylo.rdb
/usr/lib64/R/library/adephylo/R/adephylo.rdx
/usr/lib64/R/library/adephylo/data/carni19.RData
/usr/lib64/R/library/adephylo/data/carni70.RData
/usr/lib64/R/library/adephylo/data/lizards.RData
/usr/lib64/R/library/adephylo/data/maples.RData
/usr/lib64/R/library/adephylo/data/mjrochet.RData
/usr/lib64/R/library/adephylo/data/palm.RData
/usr/lib64/R/library/adephylo/data/procella.RData
/usr/lib64/R/library/adephylo/data/tithonia.RData
/usr/lib64/R/library/adephylo/data/ungulates.RData
/usr/lib64/R/library/adephylo/doc/adephylo.R
/usr/lib64/R/library/adephylo/doc/adephylo.Rnw
/usr/lib64/R/library/adephylo/doc/adephylo.pdf
/usr/lib64/R/library/adephylo/doc/index.html
/usr/lib64/R/library/adephylo/help/AnIndex
/usr/lib64/R/library/adephylo/help/adephylo.rdb
/usr/lib64/R/library/adephylo/help/adephylo.rdx
/usr/lib64/R/library/adephylo/help/aliases.rds
/usr/lib64/R/library/adephylo/help/paths.rds
/usr/lib64/R/library/adephylo/html/00Index.html
/usr/lib64/R/library/adephylo/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/adephylo/libs/adephylo.so
/usr/lib64/R/library/adephylo/libs/adephylo.so.avx2
/usr/lib64/R/library/adephylo/libs/adephylo.so.avx512
