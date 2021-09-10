# dmenu-kaomojis

List kaomojis from http://kaomoji.ru/en in dmenu, and copy them to the clipboard

## Requirements

### Dmenu

Requires atleast the [printindex](https://tools.suckless.org/dmenu/patches/printindex/) patch to
work **associated with the `-I` flag** (the patch uses `-ix`). This is because I added this feature manually in my build of
[dmenu](https://github.com/jonathannerat/dmenu) without using that patch, and I have a bunch of
scripts relying on dmenu having a `-I` flag. Either apply the patch and change the flag, or modify
`dmenu-kaomojis` to use the flag you want.

### Python

The script relies on the `requests` and `BeautifulSoup` libraries, which you can install by running:
```sh
pip install -r requirements.txt
```

## Usage

First run `get_kaomojis.py` to generate a `kaomojis.tsv` file, which will be placed by default in either
`$XDG_CACHE_HOME`, `$HOME/.cache`, or in the current directory (the first one that exists). You can
also specify the path for this as the first argument:

```sh
./get_kaomojis.py /path/to/kaomojis.tsv
```

Then run `dmenu-kaomojis` by either typing it in a terminal, or binding it to a key from your DE/WM of choice.
You can optionally specify the path to the `kaomojis.tsv` file if you choose a custom location, and
every argument after that is interpreted as a `dmenu` option:

```sh
./dmenu-kaomojis /path/to/kaomojis.tsv -c -w 500 -l 10

./dmenu-kaomojis -B -l5
```
