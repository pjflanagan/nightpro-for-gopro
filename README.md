
# NightPro for GoPro

Run `nightpro` to automatically make nightlapse videos from your GoPro's nightlapse images.

## Installation

```
pip3 install nightpro-for-gopro
```

Be sure to install ffmpeg as well.

### Maunal Installation

Clone this repository, then run this from the repository's directory.

```
python3 setup.py install 
```

## Usage

Just run `nightpro` from the folder containing your nightlapse files. Nightpro will find all of the starter photos for the series and run `ffmpeg` on them. There are also several optional arguments that can be passed in.

```
nightpro -i <input_folder> -o <output_name> -s <size> -r <rate>
```

| Argument     | Optional | Description | Default        |
| ------------ | -------- | ----------- | -------------- |
| `input_folder` | yes      | path to folder containing nightlapse photos       | current folder (`.`) |
| `output_name`  | yes      | name of the video file to be created, names will have `-<starting photo number>.mp4` appened        | `nightpro`       |
| `size`         | yes      | size can be specified in `WxH` format | full size
| `rate`         | yes      | framerate  | `32` |

### ffmpeg

NightPro is a wrapper for this `ffmpeg` command, which turns a series of images into a timelapse video. Nightpro defaults much of this command and automatically finds the start numbers for you. That way to run the command below multiple times, you only have to run `nightpro` once.

```
ffmpeg -r 32 -start_number <number> -i ./<folder>/G00%d.JPG -vcodec libx264 -pix_fmt yuv420p <name>.mp4
```

`-vcodec libx264 -pix_fmt yuv420p` ensures compatability with Quicktime
