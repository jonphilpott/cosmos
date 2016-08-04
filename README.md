# cosmos

Python + OpenCV2 image capture app designed for raspberry pi and video astronomy usage, also includes snippets and scripts for general video astronomy usage.

## Usage

The cosmos app implements a very bare set of features, the philosphy
of the app is to be an image provider to other applications for
further processing (like Mathematica.) A lot of the defaults are
designed around what's "normal" for the Raspberry Pi running Raspbian
(e.g paths)

When the application is running you can:
- press space to bring up the on-screen menus
- use the up and down keys to scroll through the controls
- use the left and right keys to change the controls
- if you turn on SHARE IMAGE it will save a snapshot of the current view to /run/shm/cosmos.png every second. This feature is now on by default.
- Pressing 's' will save a PNG snapshot into $HOME/Pictures.
- Pressing 'c' will draw crosshairs on display

## Command Line Options

```
usage: cosmos [-h] [--headless] [--device DEVICE] [--divider DIVIDER]
              [--filename FILENAME] [--savepath SAVEPATH]

Cosmos - Basic Video Astronomy capture application.

optional arguments:
  -h, --help           show this help message and exit
  --headless           Run in headless mode with no UI window.
  --device DEVICE      set capture device number.
  --divider DIVIDER    set frame divider.
  --filename FILENAME  set capture filename in /run/shm. File will be written
                       to /run/shm/filename.png
  --savepath SAVEPATH  set path where snapshots will be written, default is
                       HOME/Pictures
```


## Requirements
- opencv2 python library (on raspberry pi: apt-get install python-opencv)

## Mathematica Library

Also included is a very basic Mathematica Module to import the image and to detect and hilight stars.

```
Get["/path/to/cosmos/extras/mathematica/VideoAstronomy.m"]

# grab a frame
MyFrame = CosmosImage[]

# highlight detected stars
HighlightStars[MyFrame]

```

## Nginx snippet

also included is a very basic 3 line include for nginx that create an alias for /cosmos.png to /run/shm/cosmos.png

## set_pal.sh

A quick one-liner to set the first image capture device to PAL mode -
designed for usage with the Revolution Imager device which outputs PAL
video by default.
