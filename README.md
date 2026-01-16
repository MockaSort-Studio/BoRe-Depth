# Fork of [BoRe-Depth](https://github.com/liangxiansheng093/BoRe-Depth)

## Prerequisite

Nvidia container toolkit installed and configured on host, follow guide [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

or run script:

```
./<path-to-repo-root>/install_nvcr.sh
```

## Getting Started

Open folder as devcontainer in vscode, it contains everything you need.

It makes use of [UV](https://docs.astral.sh/uv/), it will automatically manage the venv and tools.

### Cheatsheet

Run Ruff Checks

```
uvx ruff check (using --fix some violated checks can be fixed)
```

Run Ruff Format

```
uvx ruff format --fix
```

Adding new dependency to project

```
uv add (--dev if dev dep) <pkg_name>
```
