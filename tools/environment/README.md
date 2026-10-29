# Development Environment

The local task-page snapshot names `zhouzhouyi/os-contest:20260510` and QEMU 9.2.1. These are recorded snapshot values, not a fresh confirmation of the current evaluator.

The root Dockerfile is a small development wrapper:

```sh
docker build -t oskernel2026-dev .
docker run --rm -it -v "${PWD}:/workspace" oskernel2026-dev
```

Use the commands in a Linux shell, or adjust the volume syntax for your Windows shell. Override the base explicitly with `--build-arg CONTEST_IMAGE=<verified-image-or-digest>` if the organizer confirms a different image. The container is intended to operate on the mounted project; it does not copy sibling workspace files.

The image has not been pulled or built during repository organization. Verify Docker's Linux-container support, image availability/digest, Rust/rustup, both target triples, linkers, Python, Make, and QEMU before claiming a reproducible kernel build. Do not infer daemon availability from the Docker client version.

## Original environment reference

`reference/Dockerfile.upstream` is copied verbatim from local environment commit `aa2122f118f9d50e6c378000bd2a102915c8b87c`. It documents available toolchains, crate caches, and QEMU setup. It references large archives, an extracted Kendryte toolchain, and an old dependency-cache project which remain in `../Code/os-contest-2024-image/` at workspace level. Those files are not vendored into the submission repository.

Do not build that reference Dockerfile from this directory: its build context is intentionally incomplete. Do not copy its old cached Cargo dependency list into the kernel by default. The main repository builds no third-party kernel code at this stage.

The root Makefile and dependency-free Rust library do not require hidden Cargo configuration. If configuration or vendored dependencies become necessary, store required configuration visibly and validate the evaluator's hidden-file filtering before submission.
