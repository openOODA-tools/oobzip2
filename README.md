# oobzip2: Sovereign BZIP COMPRESS

<div align="center">

```
================================================================================
                                oobzip2
               Sovereign openOODA BZIP COMPRESS
================================================================================
```

**Sovereign BZIP COMPRESS**  
*Burrows-Wheeler block sorting text compression engine with integrity checks.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oobzip2/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oobzip2-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oobzip2/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oobzip2/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oobzip2-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oobzip2/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oobzip2 [options] [INPUT]

Burrows-Wheeler block sorting text compression engine with integrity checks.

Options:
  -c, --compress       compress input text [default]
  -d, --decompress     decompress bzip2 payload
  -t, --test           test payload and verify CRC-32 integrity
  -i, --inspect        inspect container header and block size
      --bwt            execute raw Burrows-Wheeler Transform
  -1 .. -9             compression block level (100k to 900k) [default: -9]
  -s, --string <TEXT>  explicit input text string
      --json           output formatted as structured JSON
      --mcp            run as Model Context Protocol stdio server
  -h, --help           display this help and exit
  -v, --version        output version information and exit
```

---

## 3. Theming Integration (`oote`)

`oobzip2` synchronizes visual styles and status colors with [oote](https://github.com/openOODA-tools/oote):
* **Configuration:** Reads active palette from `~/.openooda/theme.oot`.
* **Environment Overrides:** Respects `$OODA_THEME` and `$NO_COLOR`.

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oobzip2` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

* `bzip2_compress`: Compress text using BWT, MTF, RLE, and CRC32.
* `bzip2_decompress`: Decompress bzip2 payload back to original text with integrity check.
* `bzip2_inspect`: Inspect container header, block size, and CRC-32 checksum.
* `bzip2_bwt`: Perform forward or inverse Burrows-Wheeler Transform.
* `bzip2_stats`: Evaluate compression ratio, size metrics, and CRC checksum.

```bash
oobzip2 --mcp
```

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (&FsReadCap, &FsWriteCap, &McpCap). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict input validation and operational limits.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
