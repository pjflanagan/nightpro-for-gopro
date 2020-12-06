
# NightPro for GoPro

Run nightpro to automatically make nightlapse videos from your GoPro's nightlapse images.

```
$ nightpro -i <input_folder> -o <output_name> -s <size> -r <rate>
```

- input_folder: optional, default to current folder
- output_name: optional, default nightpro, do not include .mp4 in the name
- size: optional, default full size
- rate: optional, default 32

## Installation

```
pip3 install nightpro-for-gopro
```

### Maunal Installation

Clone this repository, then run this from the repository's directory.

```
python3 setup.py install 
```

## ffmpeg

NightPro is a wrapper for this `ffmpeg` command, which turns a series of images into a timelapse video. Nightpro defaults much of this command and automatically finds the start numbers for you. That way to run the command below multiple times, you only have to run `nightpro` once.

```
$ ffmpeg -r 32 -start_number <number> -i ./<folder>/G00%d.JPG -vcodec libx264 -pix_fmt yuv420p <name>.mp4
```

- Replace `32` with any framerate you'd like
- Replace `<number>` with the number of the first photo, this is prefaced with `G00` in `-i`, add or remove zeros if your numbers are lower or higher
- Replace `<folder>` with the name of the folder the photos are in
- Replace `<name>` with the name of the output file
- `-vcodec libx264 -pix_fmt yuv420p` ensures compatability with Quicktime
- When testing add `-s 640x480` before the output name to make a smaller file size and process faster