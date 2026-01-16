# Fork of [BoRe-Depth](https://github.com/liangxiansheng093/BoRe-Depth)

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