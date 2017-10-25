"""behindthebeat

Usage:
    behindthebeat.py <artist>
    behindthebeat.py <artist> (--track=<track> | --album=<album>)
    behindthebeat.py (-h | --help)
    behindthebeat.py (-v | --version)

Options:
    -h --help               Show this screen.
    -v --version            Show version.
    -t --track=<track>      The song title (for use with --artist)
    -b --album=<album>      The album title (for use with --artist)
"""

from docopt import docopt
import os

def main():
    access_token = 'VCjn8DtNP_UbXRNr08zsJATjBMxH41_yjAoZXnAtQjek6VdUGXc6MY4OaH8TWL5A'
    arguments = docopt(__doc__, version="behindthebeat 1.0")

    if (arguments['<artist>'] and arguments['--track']):
        query = arguments['<artist>'] + " " + arguments['--track']
        print query
        
    elif (arguments['<artist>'] and arguments['--album']):
        query = arguments['<artist>'] + " " + arguments['--album']
        print query

if __name__ == '__main__':
    main()
