# OSKernel2026-TeamName

A Rust-first operating-system project for the 2026 Central-Western and South China regional OS kernel implementation contest.

**Status: repository scaffold only.** There is no bootable kernel, syscall implementation, QEMU test result, or platform score yet. The Cargo workspace currently contains one dependency-free `no_std` library.

## Layout

```text
.
|-- Cargo.toml / Cargo.lock     Rust workspace and dependency lock
|-- Makefile                   Host checks and reserved evaluator entry point
|-- Dockerfile                 Development wrapper for the snapshot contest image
|-- kernel/src/
|   |-- arch/riscv64/          Planned RISC-V boot and architecture support
|   |-- arch/loongarch64/      Planned LoongArch boot and architecture support
|   |-- mm/                   Planned memory management
|   |-- trap/                 Planned exceptions and interrupts
|   |-- task/                 Planned processes and scheduling
|   |-- syscall/              Planned user/kernel ABI
|   |-- fs/                   Planned VFS and Ext4 support
|   `-- drivers/              Planned serial and VirtIO devices
|-- crates/                    Reserved shared no_std crates
|-- scripts/                   Host-side maintenance and validation
|-- tests/
|   |-- upstream/pre-2025/    Imported basic syscall tests and reference material
|   |-- upstream/final-2026/  Optional advanced test sources, scripts, and judges
|   `-- integration/          Reserved project-owned integration tests
|-- tools/environment/         Environment notes and original Dockerfile reference
|-- docs/                      Design, testing, attribution, and AI usage
`-- artifacts/                 Ignored local serial logs and result files
```

The workspace-level plan is maintained in `../Doc/tasks.md`. The original workspace documents and `../Code/` repositories remain outside this submission repository. This repository's validation does not require those sibling directories.

## Checks

From this repository root, with Rust/Cargo and Python 3 installed:

```sh
cargo check --workspace --locked --offline
python3 scripts/verify-imports.py
```

With GNU Make, the equivalent commands are `make check` and `make verify-imports`. On Windows, use the installed Cargo/Python executable paths if they are not on PATH. Linux or the contest container is the intended future kernel-build environment.

The evaluator will run `make all`. This target deliberately exits with an error until actual architecture entry points and linking are implemented. It must eventually produce ELF kernels named `kernel-rv` and `kernel-la` at the repository root. An auxiliary `disk.img` is optional. Host library checks do not validate either architecture.

See [environment setup](tools/environment/README.md), [architecture plan](docs/architecture.md), and [testing plan](docs/testing.md).

## Imported tests

The local task-page snapshot points to `pre-2025`; the locally checked-out test repository is `final-2026`. Both imports are pinned to local Git commits, in separate directories. Only selected source files are included; this is not a complete upstream test suite or a runnable guest image.

[Third-party inventory](docs/third-party.md) explains scope, licenses, omitted dependencies, and the [machine-readable file manifest](tests/upstream/imports.json). Preserve imported files unchanged and put project-specific adapters outside `tests/upstream/`.

## Submission preparation

Before submission: verify the current official task details; implement and validate both kernels; pin the working container/toolchain; record a complete platform functional/performance run and valid score; finish design, attribution, and AI-use records; add the demo video share link; check repository visibility and actual platform submission.

Team metadata, project license, and demo video link are pending. No submission or publication has been performed by this repository setup.
