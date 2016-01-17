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

#error() collects error codes and prints to screen
def error(errorValue, function):
    print('[!] An error has occured in function ' + str(function))
    print('[E] ' + str(errorValue))
    exit(1)

#Generic unzip function.
def unzip(fileName):
    try:
        readFile = zipfile.ZipFile(fileName, 'r')
        zipfile.ZipFile.extractall(readFile)
        readFile.close()
        return
    except Exception as e:
        errorValue = e.value
        function = 'unzip()'
        error(errorValue, function)

#getNSRL() retrieves minimal NSRL from zip and extracts file to cwd
def getNSRL():
    try:
        fileName = '/tmp/nsrl.zip'
        print('[+] Starting download of NSRL')
        url = 'http://www.nsrl.nist.gov/RDS/rds_2.50/rds_250m.zip'
        response = urllib.request.urlretrieve(url, fileName)
        print('[+] NSRL downloaded to /tmp/\n[+] Beginning unzip to cwd')
        unzip(fileName)
        os.remove(fileName)
        sucess = '[+] Download and unzip of NSRL was sucessful.'
        return sucess
    except Exception as e:
        errorValue = e.value
        function = 'getNSRL()'
        error(errorValue, function)

def main():
    try:
        print(getNSRL())
        exit(0)
    except Exception as e:
        errorValue = e.value
        function = 'main()'
        error(errorValue, function)

if __name__=='__main__':
    main()
