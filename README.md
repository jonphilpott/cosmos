# cosmos
Python + OpenCV2 image capture app designed for raspberry pi and video astronomy usage

## Usage

It's pretty basic right now and only captures from the first available video capture device which for Video Astronomy usage should probably a USB easycap device

When the application is running you can:
- press space to bring up the on-screen menus
- use the up and down keys to scroll through the controls
- use the left and right keys to change the controls
- if you turn on SHARE IMAGE it will save a snapshot of the current view to /run/shm/cosmos.png every second


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


