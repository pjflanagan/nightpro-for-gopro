
import os
import sys
import getopt
import re

USAGE_PROMPT = 'usage: nightpro -i <input_folder> -o <output_name> -s <size> -r <rate>'

DEFAULT_IN = '.'
DEFAULT_OUT = 'nightpro'
DEFAULT_RATE = '32'
DEFAULT_SIZE = 'default'


def _checkInputFolderArg(inputfolder):
    if not os.path.isdir(inputfolder):
        print('folder ({folder}) was not found'.format(folder=inputfolder))
        sys.exit(2)
    return inputfolder


def _checkSizeArg(size):
    # TODO: if size not formatted properly then DEFAULT_SIZE
    if size == 'small':
        return '640x480'
    return size


def _checkRateArg(rate):
    try:
        int(rate)
    except:
        return DEFAULT_RATE
    return rate


def _readopt(argv):
    inputfolder = DEFAULT_IN
    outputfile = DEFAULT_OUT
    size = DEFAULT_SIZE
    rate = DEFAULT_RATE

    try:
        opts, args = getopt.getopt(
            argv, 'hi:o:s:r:', ['help', 'folder=', 'out=', 'size=', 'rate='])
    except getopt.GetoptError:
        print(USAGE_PROMPT)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(USAGE_PROMPT)
            sys.exit()
        elif opt in ('-i', '--in'):
            inputfolder = _checkInputFolderArg(arg)
        elif opt in ('-o', '--out'):
            outputfile = arg
        elif opt in ('-s', '--size'):
            size = _checkSizeArg(arg)
        elif opt in ('-r', '--rate'):
            rate = _checkRateArg(arg)

    print('folder: ' + inputfolder)
    print('out: ' + outputfile)
    print('rate: ' + rate)
    print('size: ' + size)

    return inputfolder, outputfile, size, rate


def _determineStarts(inputfolder):
    last = 0
    starts = []

    for filename in sorted(os.listdir(inputfolder)):
        if filename.endswith('.JPG') or filename.endswith('.jpg'):
            fileNameNumeric = re.sub('[^0-9]', '', filename)
            fileNumber = int(fileNameNumeric)
            if fileNumber != last + 1:
                starts.append(fileNumber)
            last = fileNumber
        else:
            continue

    print('found {count} nightlapse(s)'.format(count=str(len(starts))))

    return starts


def _process(inputfolder, starts, outputfile, size, rate):
    sizeArg = '-s ' + size
    if size == DEFAULT_SIZE:
        sizeArg = ''

    CMD = 'ffmpeg {rateArg} {sizeArg} {startArg} {inputfolderArg} -vcodec libx264 -pix_fmt yuv420p {outputfileArg}'

    for start in starts:
        cmd = CMD.format(
            rateArg='-r ' + rate,
            startArg='-start_number ' + str(start),
            inputfolderArg='-i {inputfolder}/G00%d.JPG'.format(
                inputfolder=inputfolder),
            outputfileArg='{outputfile}-{start}.mp4'.format(
                outputfile=outputfile, start=start),
            sizeArg=sizeArg
        )
        print(cmd)
        os.system(cmd)


def main():
    argv = sys.argv[1:]
    inputfolder, outputfile, size, rate = _readopt(argv)
    starts = _determineStarts(inputfolder)
    _process(inputfolder, starts, outputfile, size, rate)
