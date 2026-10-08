Name:           oobzip2
Version:        0.2.0
Release:        1%{?dist}
Summary:        Burrows-Wheeler block sorting text compression engine with integrity checks.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oobzip2
Source0:        oobzip2-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oobzip2 is a sovereign, capability-bounded BZIP COMPRESS written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oobzip2
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oobzip2-uninstall

%files
/usr/bin/oobzip2
/usr/bin/oobzip2-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
