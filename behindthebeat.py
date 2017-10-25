
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
from SearchRequest import SearchRequest
from SongRequest import SongRequest
from AlbumRequest import AlbumRequest
import os

def main():
    access_token = 'VCjn8DtNP_UbXRNr08zsJATjBMxH41_yjAoZXnAtQjek6VdUGXc6MY4OaH8TWL5A'
    arguments = docopt(__doc__, version="behindthebeat 1.0")

    if (arguments['--artist'] and arguments['--song']):
        print "behindthebeat --artist=<artist> --song=<song>"

        query = arguments['--artist'] + " " + arguments['--song']

        search_request = SearchRequest(query, access_token)
        response = search_request.execute();

    elif (arguments['--artist'] and arguments['--album']):
        print "behindthebeat --artist=<artist> --album=<album>"

if __name__ == '__main__':
    main()
