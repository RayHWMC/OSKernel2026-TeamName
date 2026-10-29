# Architecture Plan

## Current implementation

Only a dependency-free Rust `no_std` library exists. No startup assembly, executable target, linker script, allocator, driver, or syscall implementation has been added. The directories below reserve responsibilities and are not compiled modules yet.

## Proposed boundaries

| Directory | Responsibility |
| --- | --- |
| `kernel/src/arch/riscv64/` | Entry code, linker layout, SBI/serial/shutdown integration, registers, trap frames, page tables, and context switching for RISC-V. |
| `kernel/src/arch/loongarch64/` | Entry code, linker layout, serial/shutdown integration, registers, trap frames, page tables, and context switching for LoongArch. |
| `kernel/src/mm/` | Physical frames, virtual address spaces, heap, user mappings, and fault handling. |
| `kernel/src/trap/` | Common exception/interrupt dispatch with architecture-specific entry code behind the architecture boundary. |
| `kernel/src/task/` | Task/process lifecycle, saved execution contexts, scheduler, exec, and wait semantics. |
| `kernel/src/syscall/` | Linux-compatible syscall dispatch, argument validation, return values, and errno handling. |
| `kernel/src/fs/` | VFS, descriptors, paths, and Ext4 support for the evaluator's test disks. |
| `kernel/src/drivers/` | Serial, VirtIO block, and later networking, using each architecture's actual device topology. |
| `crates/` | Shared libraries extracted only when an implemented subsystem needs them. |

Begin with RISC-V serial boot, then bring up LoongArch before expanding architecture-dependent interfaces. Keep the two ELF output names stable: `kernel-rv` and `kernel-la`. Confirm entry addresses, firmware behavior, target triples, linker commands, and QEMU device layout before implementing each platform.

Do not import the environment repository's old Cargo dependency cache as the kernel's dependency list: it is not a kernel implementation. Select and attribute dependencies deliberately, then retain source for offline evaluator builds where required.

## Build constraints

- The root `make all` will build both kernels once boot targets exist. The current failure is intentional and must not be replaced by dummy files.
- The evaluator may remove hidden directories. Any future Cargo configuration needed at build time must be stored visibly (for example `cargo/config.toml`) and explicitly supplied/restored by the build.
- Pin a Rust toolchain only after confirming both target libraries and linkers in the contest container.
- Record third-party kernel bases and their licenses before adoption. No kernel base has been chosen or copied.
