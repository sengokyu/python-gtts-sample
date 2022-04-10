# [gtts](https://gtts.readthedocs.io/en/latest/index.html) output directly sample

## Pre requirements

- lame 3.100
- openal-soft 1.21.1
- python 3.10
- poetry

## Getting Started

```console
poetry install
DYLD_LIBRARY_PATH=/usr/local/opt/openal-soft/lib poetry run python3 ex_gtts ja 'こんにちは。'
```
