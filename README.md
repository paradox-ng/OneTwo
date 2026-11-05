# OneTwo

OneTwo is a muOS theme made by bulkh, based on Rezolution by Rosabel. This fork, maintained by Paradox (`paradox-ng`),
updates it for MustardOS 2606 (Andromeda) and keeps bulkh's design.

[bulkh's repository](https://github.com/bulkh/OneTwo) holds the README and previews, and the theme is published as
release packages. This fork unpacks the v4 release (`OneTwo.muxthm`, plus `OneTwoTUI.muxthm` for the TrimUI Brick) into
source folders, merges the two packages and updates the result for 2606. The `2606` branch is the default and holds the
update. The `main` branch still matches bulkh's repository.

## What changed for 2606

- One `OneTwo.muxthm` now covers every resolution, including 1024x768, which used to be the separate OneTwoTUI package.
- Glyphs are drawn at their native size and follow the screens that 2606 renamed or merged. For example, Interface
  options moved into Customisation, and System Info and Network Info became System Details.
- Dialogues, such as the save prompt, use each colour scheme's popup colours.
- RGB lighting for DMG, SNES and Mustard uses 2606's per-alternative colour files.

## Resolutions

- 640x480
- 720x480
- 720x720
- 1024x768 (TrimUI Brick)
- 1280x720

bulkh made the 1280x720 layout to look good on HDMI output. The TrimUI Smart Pro isn't supported yet, and on its screen
the 1280x720 layout scales down and looks too small.

## Colour schemes

Dark, Light, DMG, SNES and GC, each with a GamePal version, plus BMO and Mustard.

## Installation

1. Download `OneTwo.muxthm` from the most recent release on the [Releases page](https://github.com/paradox-ng/OneTwo/releases).
2. Copy it to the `ARCHIVE` folder (on `SD2`, or on `SD1` if you use only one card).
3. Open **Applications > Archive Manager** and select `OneTwo.muxthm` to install it.
4. Apply the theme from **Configuration > Customisation > Theme Picker**, and pick a colour scheme from
   **Customisation > Alternative Theme**.

> [!TIP]
> For the best look, set Overlay Transparency (in Customisation) to 100%, or set it to 0 to turn the overlays off.
> The in-game sound and brightness bars are designed to sit on the left or right side, so avoid putting them in the
> centre. bulkh prefers the top left corner. The battery overlay can go anywhere.

## Changing the design

bulkh's design is a [Figma project](https://www.figma.com/design/8hm9YQcy0a1kUIxl1T7SKW/OneTwo?node-id=0-1&t=K41jUL3nJoVDzw4Q-1).
Make a copy of it to change something.

## Building from source

The theme is kept unpacked in this repository. `theme/` is the theme root as muOS installs it, and each colour scheme
lives in `alternates/<Name>/`. The build script only needs Python 3.

```bash
git clone --branch 2606 https://github.com/paradox-ng/OneTwo.git
cd OneTwo
python3 build.py
```

This writes `dist/OneTwo.muxthm`, and the same theme unpacked in `dist/OneTwo`.

## Previews
![Preview 1](https://github.com/bulkh/OneTwo/blob/main/preview/preview1.png)![Preview 2](https://github.com/bulkh/OneTwo/blob/main/preview/preview2.png)
![Preview 3](https://github.com/bulkh/OneTwo/blob/main/preview/preview3.png)

## Links

- [OneTwo on muOS's community forum](https://community.muos.dev/t/pixie-onetwo/)
- [Aurora for 2606](https://github.com/paradox-ng/Aurora), Rosabel's theme; OneTwo is a remake of its old layout

## Reporting problems

Report problems with this 2606 update in [this fork's issues](https://github.com/paradox-ng/OneTwo/issues).
