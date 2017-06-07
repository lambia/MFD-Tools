#!/usr/bin/env python3
# -*- coding: utf-8 -*-
########################################################################
# Written in Sept. 2016 by Luca Lambia
# Distributed under GNU/GPL -> http://www.gnu.org/licenses/
# Credits to Gerhard Klostermeier
########################################################################

from sys import exit, argv
from binascii import unhexlify
import os

def main():
  """ Convert MifareClassicTool to MiFareDump. """
  # Are there enouth arguments?
  if len(argv) is 4:
    if(argv[1].lower() == 'file'):
      convert_one(argv[2],argv[3])
    elif(argv[1].lower() == 'dir'):
      convert_all()
  else:
    usage()
	
def convert_all():
  for thisfile in os.listdir(argv[2]):
    # There is no "KO", but if there are troubles will be printed out just after the name of the file
    print("[OK] - "+thisfile)
    convert_one(argv[2]+"/"+thisfile,argv[3]+"/"+thisfile+".mfd")

def convert_one(fFrom,fTo):
  # TODO: Check if the dump has all sectors and no unknown data
  # and if not, create the missing data.
  # (0x00 for data, 0xFF for keys and 0x078069)

  # Convert the file line by line.
  with open(fFrom, 'r') as mctFile, open(fTo, 'wb') as mfdFile:
    for line in mctFile:
      if line[:8] == '+Sector:':
        continue
      mfdFile.write( unhexlify(line.lower().rstrip()) )

def usage():
  """ Print the usage. """
  print('\r\nUsage: '+ argv[0] + ' file <dump.mct> <output.mfd>')
  print('Or:    ' + argv[0] + ' dir <mct-folder> <mfd-folder>')
  print('\r\nUsing "dir" argument will automatically:\r\n- add the trailing slash at the end of directory names\r\n- Put *.mfd extension to files')
  print('\r\nPath can include spaces if \\backslahed.\r\nDumps needs all sectors and no unknown data.')
  exit(1);


if __name__ == '__main__':
    main()

