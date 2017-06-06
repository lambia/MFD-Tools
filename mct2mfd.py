#!/usr/bin/env python3
# -*- coding: utf-8 -*-
########################################################################
# Written in Sept. 2016 by Luca Lambia
# Distributed under GNU/GPL -> http://www.gnu.org/licenses/
# Credits to Gerhard Klostermeier
########################################################################

from sys import exit, argv
from binascii import unhexlify

def main():
  """ Convert MifareClassicTool to MiFareDump. """
  # Are there enouth arguments?
  if len(argv) is not 3:
    usage()

  # TODO: Check if the dump is comple (has all sectors and no unknown data)
  # and if not, create the missing data.
  # (0x00 for data, 0xFF for keys and 0x078069)

  # Convert the file line by line.
  with open(argv[1], 'r') as mctFile, open(argv[2], 'wb') as mfdFile:
    for line in mctFile:
      if line[:8] == '+Sector:':
        continue
      mfdFile.write( unhexlify(line.lower().rstrip()) )


def usage():
  """ Print the usage. """
  print('Usage: ' + argv[0] + ' <mct-dump> <output-file-(mfd)>')
  print('INFO: MCT dump has to be complete ' +
      '(all sectors and no unknown data).')
  exit(1);


if __name__ == '__main__':
    main()

