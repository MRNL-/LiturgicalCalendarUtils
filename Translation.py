# -*- coding: cp1252 -*-

#----------------------------------------------------------------------------------#
# Translation
# https://github.com/MRNL-/LiturgicalCalendarUtils
# (C) Martin Raynal, 2015
#----------------------------------------------------------------------------------#
# This module provides translation of Celebrations' names and Saints' titles.
#----------------------------------------------------------------------------------#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>. 
#----------------------------------------------------------------------------------#

import os

def getLocale():
    return locale

def setLocale(newlocale):
    global locale, celebrations, saintRanks
    if newlocale==locale:
        return
    
    path="./locale"
    #path="C:\Users\Martin Raynal\Documents\GitHub\LiturgicalCalendarUtils\locale"
    if(newlocale != 'en-EN'):
        path+="/"+newlocale
        
    #TODO : raise exception or just return error code while using default ?
    if os.path.exists(path):
        locale=newlocale
        #Load property files
        celebrations=loadProperties(path+"/celebrations.properties")
        saintRanks=loadProperties(path+"/saints.properties")
    else:
        raise Exception("Locale '"+newlocale+"' was not found.")
        
def loadProperties(path):
    "Loads the given .properties file"
    myprops = dict(line.strip().split('=')
for line in open(path)
    if ("=" in line and not line.startswith("#")))
    
    return myprops

def translate(string):
    if string in celebrations.keys():
        return celebrations[string]
    else:
        if '%' in string:
            #ferial weekday
            allStr=string.split('%')
            size=len(allStr)-1
            retStr=""
            for i,s in enumerate(allStr):
                retStr+=celebrations[s]
                if i<size:
                    retStr+=" "
                
            return retStr
        
        #assume a saint rank
        allStr=string.strip().split('&')
        retStr=""
        size=len(allStr)-1
        for i,s in enumerate(allStr):
            #todo '|'
            if s in saintRanks.keys():
                retStr+=saintRanks[s]
            else:
                retStr+="[ "+s+": KEY_NOT_FOUND ]"
            if i<size:
                retStr+=" & "
        return retStr

#--------------------------------------
# Module-wide variables
#--------------------------------------

locale="en-EN"
celebrations=loadProperties("./locale/celebrations.properties")
saintRanks=loadProperties("./locale/saints.properties")
