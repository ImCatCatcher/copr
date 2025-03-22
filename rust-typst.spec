Name:           rust-typst
Version:        0.13.1
Release:        2%{?dist}
Summary:        A new markup-based typesetting system that is powerful and easy to learn.
Provides:       typst
Obsoletes:      typst

License:        Apache-2.0
URL:            https://github.com/typst/typst
Source:	    	https://github.com/typst/typst/archive/refs/tags/v0.13.1.tar.gz#/%{name}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildRequires:  openssl-devel
BuildRequires:	cargo

%global debug_package %{nil}

%description
Typst is a new markup-based typesetting system that is designed to be as powerful as LaTeX while being much easier to learn and use.

%prep
%autosetup -n typst-%{version}

%build
cargo build --release

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 target/release/typst %{buildroot}/%{_bindir}/typst

%files
%{_bindir}/typst
%license LICENSE
%doc README.md

%changelog
* Sat Mar 22 2025 Arseniy Zasypkin <imcatcatcher@internet.ru> 0.13.1-2
 - Add typst obsoletes.

* Sat Mar 22 2025 Arseniy Zasypkin <imcatcatcher@internet.ru> 0.13.1-1
 - Initial package.