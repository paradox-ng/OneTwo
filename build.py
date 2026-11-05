"""Build OneTwo.muxthm.

The theme lives unpacked in this repository so changes can be reviewed:

    theme/                 the theme root, as muOS installs it
    alternates/<Name>/     each alternative, laid out from the theme root

Running ``python3 build.py`` assembles the theme in ``dist/OneTwo/``, packs
every alternative as ``alternate/<Name>.muxalt`` and zips the result into
``dist/OneTwo.muxthm``. Only the Python standard library is needed.
"""

import shutil
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parent
THEME = ROOT / "theme"
ALTERNATES = ROOT / "alternates"
DIST = ROOT / "dist"
BUILD = DIST / "OneTwo"


def files_in(folder: Path):
	return sorted(
		path
		for path in folder.rglob("*")
		if path.is_file()
		and not any(part.startswith(".") for part in path.relative_to(folder).parts)
	)


def pack(folder: Path, archive: Path):
	"""Zip a folder's contents with paths relative to it, as muOS expects."""
	archive.parent.mkdir(parents=True, exist_ok=True)
	with ZipFile(archive, "w", ZIP_DEFLATED) as zipped:
		for path in files_in(folder):
			zipped.write(path, path.relative_to(folder).as_posix())


def main():
	if BUILD.exists():
		shutil.rmtree(BUILD)
	shutil.copytree(THEME, BUILD, ignore=shutil.ignore_patterns(".*"))

	alternates = sorted(path for path in ALTERNATES.iterdir() if path.is_dir())
	for alternate in alternates:
		pack(alternate, BUILD / "alternate" / f"{alternate.name}.muxalt")
		print(f"packed alternate/{alternate.name}.muxalt")

	pack(BUILD, DIST / "OneTwo.muxthm")
	print(f"built {DIST / 'OneTwo.muxthm'} ({len(alternates)} alternatives)")


if __name__ == "__main__":
	main()
