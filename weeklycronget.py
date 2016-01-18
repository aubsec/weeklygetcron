#!/usr/bin/env python3

#    weeklycronget.py Used for automated download of DFIR relevent files. 
#    Copyright (C) 2016 Matthew Aubert
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#imports
import urllib.request
import zipfile
import os

#exceptionHandler() collects error codes and prints to screen
def exceptionHandler(errorValue, function):
    print('[!] An error has occured in function ' + str(function))
    print('[!] ' + str(errorValue))
    return 0

#Generic unzip function.
def unzip(fileName):
    try:
        readFile = zipfile.ZipFile(fileName, 'r')
        zipfile.ZipFile.extractall(readFile)
        readFile.close()
        return 0
    except Exception as errorValue:
        function = 'unzip()'
        exceptionHandler(errorValue, function)
        return 1

#getNSRL() retrieves minimal NSRL from zip and extracts file to pwd
def getNSRL():
    try:
        fileName = '/tmp/nsrl.zip' #Work on fixing this so it is OS agnostic
        print('[+] Starting download of NSRL')
        url = 'http://www.nsrl.nist.gov/RDS/rds_2.50/rds_250m.zip' #Verify that the URL remains static.
        response = urllib.request.urlretrieve(url, fileName)
        print('[+] NSRL downloaded to /tmp/\n[+] Beginning unzip to pwd')
        unzip(fileName)
        os.remove(fileName)
        print('[+] Download and unzip of NSRL was sucessful.')
        return 0
    except Exception as errorValue:
        function = 'getNSRL()'
        exceptionHandler(errorValue, function)
        return 1

#WIP getMcAfeeDAT() parses gdeltaavv.ini, finds the current version,
#and downloads the lastest DAT version to the pwd.
def getMcAfeeDAT():
    #http://update.nai.com/products/commonupdater/gdeltaavv.ini
    return 0

def main():
    try:
        returnValue = 0
        returnValue += getNSRL()
        returnValue += getMcAfeeDAT()
        if returnValue != 0:
            print('[!] Program completed with errors')
            exit(1)
        else:
            print('[+] Program completed sucessfully')
            exit(0)
    except Exception as errorValue:
        function = 'main()'
        exceptionHandler(errorValue, function)
        print('[!] Program completed with errors')
        exit(1)

if __name__=='__main__':
    main()

