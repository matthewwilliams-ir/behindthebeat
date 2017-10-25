
"""behindthebeat allows to find out the producers behind a song

Usage:
    behindthebeat [--artist=<artist>] [--album=<album>]
                  [--artist=<artist>] [--song=<song>]
                  (-h | --help)
                  (-v | --version)

Options:
    -h --help               Show this screen.
    -v --version            Show version.
    --artist                The artist name (--song or --album is required)
    --song=<song>           The song title (for use with --artist)
    --album=<album>         The album title (for use with --artist)
    --debug                 Verbose logging.
"""

""" Author:

Matthew Williams
    http://twitter.com/mattxwill
    http://github.com/matthewwilliams-ir

"""

from docopt import docopt
import os

def main():
    arguments = docopt(__doc__, version="behindthebeat 1.0")

    if (arguments['--artist'] and arguments['--song']):
        print "behindthebeat --artist=<artist> --song=<song>"
    elif (arguments['--artist'] and arguments['--album']):
        print "behindthebeat --artist=<artist> --album=<album>"

if __name__ == '__main__':
    main()
