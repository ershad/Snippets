#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       crypto.py
#       
#       Copyright 2011 Ershad K <ershad92@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.


from Crypto.Cipher import AES
import hashlib
import sys
import getpass

def encrypt(inputFile, key, outFile=None):
    """ Encrypt file """
    try:
        f = open(inputFile)
    except:
        print "Cannot open file: " + inputFile
        sys.exit(1)
        
    lines = f.readlines()
    plaintext = ''

    for line in lines:
        plaintext += line

    length = len(plaintext)
    toBeAdded = (16-length%16)
    if toBeAdded is not 0:
        for a in range(toBeAdded-2):
            plaintext += 'X'
        if toBeAdded < 10:
            plaintext+= '0' + str(toBeAdded)
        else:
            plaintext+= str(toBeAdded)

    aes = AES.new(key, AES.MODE_ECB)
    ciphertext = aes.encrypt(plaintext)

    if outFile is None:
        f = open(inputFile+'.encrypted', 'w')
    else:
        f = open(outFile, "w")
        
    f.write(ciphertext)
    f.close()
    
def decrypt(inputFile, key, outFile=None):
    """Decrypt File"""
    try:
        f = open(inputFile)
    except:
        print "Cannot open file: " + inputFile
        sys.exit(1)
        
    lines = f.readlines()
    ciphertext = ''
    for line in lines:
        ciphertext += line
    aes = AES.new(key, AES.MODE_ECB)
    plaintext = aes.decrypt(ciphertext)
    try:
        numberOfX = int(plaintext[-2:])
    except:
        print "Incorrect Password"
        sys.exit(1)
        
    if numberOfX is not 0:
        plaintext = plaintext[:len(plaintext)-numberOfX]
        
    if outFile is None:
        f = open(inputFile[:-10], 'w')
    else:
        f = open(outFile, "w")

    f.write(plaintext)
    f.close()
    
if __name__ == '__main__':

    argRange = [3, 4, '-e', '-d']
    if len(sys.argv) not in argRange or sys.argv[1] not in argRange:
        print "Usage [Encrypt]: crypt -e INFLILE {OUTFILE}"
        print "Usage [Decrypt]: crypt -d INFLILE {OUTFILE}"
        sys.exit(1)

    key = hashlib.md5(getpass.getpass("Enter password: ")).hexdigest()    
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    if arg1 == '-e':
        if len(sys.argv) == 4:
            encrypt(arg2, key, sys.argv[3])
        else:
            encrypt(arg2, key)

    if arg1 == '-d':
        if len(sys.argv) == 4:
            decrypt(arg2, key, sys.argv[3])
        else:
            decrypt(arg2, key)
