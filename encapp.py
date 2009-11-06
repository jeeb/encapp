#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Easy encoding script for the PSP

Copyright (c) 2009, Jan Ekström <jeebjp@gmail.com>

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

'''

# Pythonscript

import sys, os, random, PyQt4


if __name__ == "__main__":
    if ( os.name != 'nt' ) :
        print ''' We are extremely sorry, but this script currently doesn't work on *nix. '''
        sys.exit(0)
    else :
        filename = str(sys.argv[1])
        setting = int(sys.argv[2])
        mode = "crf"
        

        '''

            Deciding the ratecontrol mode from input.

        '''

        if ( setting > 0 and setting < 52 ):
            mode = "crf"
        elif ( setting == 0 ):
            sys.exit("You are setting your ratecontrol to 0!\n This will give you lossless which will not work on your hardware!")
        elif ( setting > 51 ):
            mode = "bitrate"
        
        print ''' :::::::::::::::::::::::::::::::::: '''
        print ''' ::::: JEEB's encoding script ::::: '''
        print ''' :::::::::::::::::::::::::::::::::: '''

        '''
            Check if the source file exists.
        '''

        if ( os.path.isfile( filename ) == false ):
             sys.exit("The original file is not there or isn't a file.")

        '''
            Write the video avs file.
            <filename>.video.avs

        '''

        content = 'LoadPlugin(' + <%AppPath%>\avs\ffms2\FFMS2.dll")'
        
