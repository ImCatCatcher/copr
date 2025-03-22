Name:           rust-tytanic
Version:        0.2.2
Release:        2%{?dist}
Summary:        A test runner for typst projects.
Provides:       tytanic
Provides:	    tt

License:        MIT
URL:            https://github.com/tingerrr/tytanic
Source:		https://github.com/tingerrr/tytanic/archive/refs/tags/v0.2.2.tar.gz#/%{name}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildRequires:  openssl-devel
BuildRequires:	cargo

Requires: rust-typst >= 0.13.1

%global debug_package %{nil}

%description
Tytanic is a test runner for Typst projects. It helps you worry less about regressions and speeds up your development.

%prep
%autosetup -n tytanic-%{version}

%build
cargo build --release

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 target/release/tt %{buildroot}/%{_bindir}/tt

%files
%{_bindir}/tt
%license LICENSE
%doc README.md

%changelog
* Sat Mar 22 2025 Arseniy Zasypkin <imcatcatcher@internet.ru> 0.2.2-2
 - Add rust-typst v0.13.1 dependency.

* Sat Mar 22 2025 Arseniy Zasypkin <imcatcatcher@internet.ru> 0.2.2-1
 - Initial package.