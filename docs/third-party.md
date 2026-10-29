# Third-Party Source Inventory

Imported on 2026-10-22 from existing local Git objects. No upstream repository was switched, modified, fetched, or copied with its Git metadata. The referenced branches are local snapshots, not evidence of current remote heads.

## Source register

| Import | Original repository and local ref | Commit | Included material |
| --- | --- | --- | --- |
| `tests/upstream/pre-2025/` | `https://github.com/oscomp/testsuits-for-oskernel.git`, `origin/pre-2025` | `8b58dd16d26d30f7c74d48d5832d870d3051b703` | 101 files: full selected `basic/` subtree, `scripts/basic/`, `oscomp_syscalls.md`, and root README. |
| `tests/upstream/final-2026/` | Same repository, `final-2026` | `b5ec6ef8497e1818cbdec3b54bb722f036e57972` | 10 files: `cagent-test/` including cJSON, two guest scripts, two Python judges, and root README. |
| `tools/environment/reference/Dockerfile.upstream` | `https://gitlab.educg.net/wangmingjian/os-contest-2024-image.git`, `master` | `aa2122f118f9d50e6c378000bd2a102915c8b87c` | One original Dockerfile, retained as reference only. |

The 112 files total 410,719 bytes. File-by-file destinations, upstream paths, Git blob hashes/modes, sizes, and SHA-256 hashes are in `tests/upstream/imports.json`. Run `python3 scripts/verify-imports.py` to check them without access to the original repositories.

The import used Git archives with automatic line-ending conversion disabled and compared each file to its original Git blob before copying. Repository attributes preserve imported bytes. Existing source headers, notices, upstream filenames, and original documentation are retained unchanged.

## License notes

- cJSON's MIT permission/copyright notice is embedded in its copied `.c` and `.h` headers and has been preserved.
- No top-level license file was present in the selected test-tree roots. The selected basic/CAgent scripts, judges, and environment Dockerfile must not be assumed to share cJSON's license. Resolve their applicable terms before redistribution or final publication.
- BusyBox and other large packages were not imported. Their licenses are not being assigned to the copied basic tests or the team's future kernel.
- No license has been chosen for team-authored code. Do not add a blanket license covering third-party material without checking its actual terms.

## Deliberate omissions

- Large compiler archives, QEMU sources/binaries, extracted Kendryte toolchains, and old Cargo dependency caches remain in the original workspace `Code/` cache.
- Full `pre-2025` performance/compatibility suites, disk images, and upstream root image-build Makefiles are omitted. The imported `basic/user/` has its own build files.
- `final-2026` BusyBox, iproute2, full image-build files, and the BuildStorm guest rootfs/toolchain are omitted. Its CAgent Makefile builds only its C programs; the guest scripts still require external runtime components.
- No existing third-party kernel has been adopted. Imported C code belongs to tests and supporting tooling, consistent with the Rust-first kernel requirement.

Keep project-specific changes outside the pinned imports. Update this inventory and manifest together when intentionally replacing or expanding a snapshot. Cite borrowed components in the final design document as well as here.
