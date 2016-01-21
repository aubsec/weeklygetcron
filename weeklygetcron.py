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
import time

#getMcAfeeDAT() parses gdeltaavv.ini, finds the current version,
#and downloads the lastest DAT version to the 'dir'.
def getMcAfeeDAT(directory):
    #http://update.nai.com/products/commonupdater/gdeltaavv.ini
    try:
        iniFileName = directory + '/mcafee.ini'
        print('[+] Starting download of McAfee VSE Update')
        url = 'http://update.nai.com/products/commonupdater/gdeltaavv.ini'
        urllib.request.urlretrieve(url, iniFileName)
        with open(iniFileName, 'r') as iniFile:
            for line in iniFile:
                if 'CurrentVersion' in line:
                    ver = str(line[-5:])
        
        ver = str(ver.replace('\n', ''))
        url = 'http://download.nai.com/products/licensed/superdat/english/intel/' + ver + 'xdat.exe'
        fileName = directory + '/'  + ver + 'xdat.exe'
        urllib.request.urlretrieve(url, fileName)
        print('[+] Download of McAfee VSE DAT ' + ver + ' was sucessful')
        iniFile.close()
        os.remove(iniFileName)
        return 0
    except Exception as errorValue:
        function = 'getMcAfeeDAT()'
        exceptionHandler(errorValue, function)
        return 1

#getNSRL() retrieves minimal NSRL from zip and extracts file to pwd
def getNSRL(directory):
    try:
        fileName = directory + '/nsrl.zip' 
        print('[+] Starting download of NSRL')
        url = 'http://www.nsrl.nist.gov/RDS/rds_2.50/rds_250m.zip' #The version number does change.  Modify to parse version number before downloading
        response = urllib.request.urlretrieve(url, fileName)
        print('[+] NSRL downloaded to ' + directory) # + '/\n[+] Beginning unzip to ' + directory + '/')
        #Keeping file compressed for now.  
        #unzip(fileName, directory) 
        #os.remove(fileName)
        print('[+] Download of NSRL was sucessful.')
        return 0
    except Exception as errorValue:
        function = 'getNSRL()'
        exceptionHandler(errorValue, function)
        return 1

#getNSRLEncase() retrieves the Encase version of the NSRL in zip format.
def getNSRLEncase(directory):
    try:
        fileName = directory + '/NRL_Encase_Unified.zip'
        print('[+] Starting download of NSRL Encase')
        url = 'http://www.nsrl.nist.gov/RDS/rds_2.50/Encase_Unified_rds_250.zip'
        response = urllib.request.urlretrieve(url, fileName)
        print('[+] Download of NSRL Encase format is complete')
        return 0
    except Exception as errorValue:
        function = 'getNSRLEncase()'
        exceptionHander(errorValue, function)
        return 1

#getSnort() downloads the community Snort rules.
def getSnort(directory):
    try:
        fileName = directory + '/snortrules-snapshot.2962.tar.gz'
        print('[+] Starting download of Snort community rules')
        url = 'https://snort.org/rules/snortrules-snapshot-2962.tar.gz?oinkcode=ce600e851dbd2f74c3ee671c9f10522d8eab909f'
        response = urllib.request.urlretrieve(url, fileName)
        #In later itteration, have the rules automatically unpacked to appropriate location.  
        print('[+] Download of Snort Community Rules complete')
        return 0
    except Exception as errorValue:
        function = 'getSnort()'
        exceptionHander(errorValue, function)
        return 1

#Creates directory for output
def makeDir():
    now = time.strftime('%Y%m%d')
    cwd = os.getcwd()
    directory = cwd + '/' + now
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

#exceptionHandler() collects error codes and prints to screen
def exceptionHandler(errorValue, function):
    print('[!] An error has occured in function ' + function)
    print('[!] ' + str(errorValue))
    return 0

#Generic unzip function.
def unzip(fileName, directory):
    try:
        readFile = zipfile.ZipFile(fileName, 'r')
        readFile.extractall(directory)
        readFile.close()
        return 0
    except Exception as errorValue:
        function = 'unzip()'
        exceptionHandler(errorValue, function)
        return 1


# Main
def main():
    try:
        returnValue = 0
        try:
            directory = makeDir()
            print('[+] Directory ' + directory + '/ created')
        except Exception as errorValue:
            function = 'makeDir()'
            exceptionHandler(errorValue, function)
            returnValue += 1
        returnValue += getNSRL(directory)
        returnValue += getNSRLEncase(directory)
        returnValue += getMcAfeeDAT(directory)
        returnValue += getSnort(directory)
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
