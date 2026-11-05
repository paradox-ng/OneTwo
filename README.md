# OneTwo
muOS theme based on Rezolution by Rosabel

### Supported resolutions:
- 640x480
- 720x480
- 720x720
- 1024x768 (TrimUI Brick; part of the main package since the 2606 update)
- 1280x720*

*I made 1280x720 resolution to look nice on HDMI output, so on TrimUI Smart Pro scaling will look too tiny

No support for TUISP yet..

### Color schemes:
- Dark
- Light
- DMG
- SNES
- GC
- BMO (only with face)
- Mustard (only standard)

## MustardOS 2606 (Andromeda)

This branch updates OneTwo for **MustardOS 2606 Andromeda**:

- One `OneTwo.muxthm` now covers every resolution, including 1024x768 (the former OneTwoTUI package).
- Glyphs are drawn at their native size and follow the screens 2606 renamed or merged (Interface options moved into
  Customisation, System Info and Network Info became System Details, and so on).
- Dialogues (such as the save prompt) use each colour scheme's popup colours.
- RGB lighting for DMG, SNES and Mustard uses 2606's per-alternative colour files.

## Installation

1. Head over to the [Releases](https://github.com/paradox-ng/OneTwo/releases) page
2. Find the most recent release
3. Download `OneTwo.muxthm`
4. Copy it to the `ARCHIVE` folder (on the `SD2`, or `SD1` if you use only one card)
5. Open **Applications > Archive Manager** and select `OneTwo.muxthm` to install it
6. Apply the theme from **Configuration > Customisation > Theme Picker**, and pick a colour scheme from
   **Customisation > Alternative Theme**
> [!TIP]
> For best look you should set Overlay Transparency (in Customisation) to 100%, or you can turn it off by setting to 0
> In game sound and brightness bar are designed to be on the right or left side, so you better not to set it in center. I persanally prefer them to be on the top left corner. Battery overlay can be wherever you like.

If you want to change something, you can do it in Figma by copying [project](https://www.figma.com/design/8hm9YQcy0a1kUIxl1T7SKW/OneTwo?node-id=0-1&t=K41jUL3nJoVDzw4Q-1)

## Building from source

The theme is kept unpacked in this repository: `theme/` is the theme root as muOS installs it, and each colour scheme
lives in `alternates/<Name>/`.

```bash
git clone --branch 2606 https://github.com/paradox-ng/OneTwo.git
cd OneTwo
python3 build.py
```

This writes `dist/OneTwo.muxthm` (and the same theme unpacked in `dist/OneTwo`).

## Previews
![Preview 1](https://github.com/bulkh/OneTwo/blob/main/preview/preview1.png)![Preview 2](https://github.com/bulkh/OneTwo/blob/main/preview/preview2.png)
![Preview 3](https://github.com/bulkh/OneTwo/blob/main/preview/preview3.png)
