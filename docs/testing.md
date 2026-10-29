# Testing Plan

## Import integrity

Run `python3 scripts/verify-imports.py` from a clean checkout. It checks the size and SHA-256 of every imported file against `tests/upstream/imports.json`, without requiring the original workspace repositories or network access.

The manifest also records the original Git path, blob object, and executable mode. Windows copies do not set POSIX execute bits; call imported shell scripts with the correct shell (`bash` or `sh`) or restore their recorded modes on Linux. Keep upstream bytes unchanged.

## Host scaffold check

Run `cargo check --workspace --locked --offline`. This checks only the empty `no_std` library using the host target. It does not validate a kernel executable, bare-metal target, linker, or runtime feature.

## Basic syscall tests

`tests/upstream/pre-2025/` includes the complete selected `basic/` subtree, its runner, upstream README, and syscall reference. The build files and user library are preserved verbatim. Start by inspecting `basic/user/Makefile`, `basic/user/CMakeLists.txt`, and `basic/README.md` in the selected container.

The upstream README is RISC-V-oriented and the CMake file has architecture assumptions. Verify cross compilers and LoongArch support before claiming the tests build on both architectures. The full upstream root Makefile and other test groups are not included; do not run a full-suite image build from this subset.

## Advanced reference tests

`tests/upstream/final-2026/` contains CAgent C sources with cJSON, its local Makefile, the guest scripts, reference judges, and README. The C sources are tests, not kernel code.

CAgent additionally needs a working guest userspace, BusyBox and other shell tools, sockets, filesystem support, and timing. BuildStorm additionally needs the upstream guest image with glibc, Rust tools, sources, and offline cache. These runtime dependencies are not included here. Do not run guest test scripts directly on the development host: they mount filesystems, start services, and write guest paths.

The national final README, scripts, and judges contain potentially different example markers and baseline values. Use the actual pinned scripts/judges to understand this snapshot, and confirm regional applicability before making it an acceptance requirement. Judge output from synthetic or host logs is not a contest score.

## Future QEMU regression

1. Record the confirmed image digest, Rust/linker versions, QEMU version, test-image hashes, memory, SMP, and command lines.
2. Verify ELF machine types and entry addresses for both root kernel artifacts.
3. Boot each real kernel with its matching test disk and serial logging.
4. Execute confirmed test groups serially, preserve their official start/end markers, and shut down QEMU after completion.
5. Save raw serial logs under `artifacts/logs/` and parsed results under `artifacts/results/`.
6. Record failures as well as passes; retain platform-run evidence separately from local regression results.

Current kernel/QEMU/platform status: not run; no executable kernel exists.
