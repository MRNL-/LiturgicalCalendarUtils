# -*- coding: cp1252 -*-

#----------------------------------------------------------------------------------#
# Catholic DateUtils
# https://github.com/MRNL-/LiturgicalCalendarUtils
# (C) Martin Raynal, 2015
#----------------------------------------------------------------------------------#
#	 This program is free software: you can redistribute it and/or modify
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
# LiturgicalCalendarEnums.py
#   This file contains all enums and classes used for generating the calendar
#----------------------------------------------------------------------------------#

from enum import Enum

class Colors(Enum):
    NONE = 0
    GREEN = 1
    WHITE = 2
    RED = 3
    PURPLE = 4
    ROSE = 5
    BLACK = 6
    GOLD = 7
    BLUE = 8

class Ranks(Enum):
    WEEKDAY = 0
    COMMEMORATION = 1
    OPTIONAL = 2
    MEMORIAL = 3
    FEAST = 4
    SUNDAY = 5
    LORD = 6
    ASHWED = 7
    HOLYWEEK = 8
    TRIDUUM = 9
    SOLEMNITY =10

class Seasons(Enum):
    ORDINARY = 0
    ADVENT = 1
    CHRISTMAS = 2
    LENT = 3
    EASTER = 4
    PASCHAL = 5
    PASSION = 6

def parseColor(colLetter):
    if colLetter=='-':
        return Colors.NONE
    if colLetter=='g':
        return Colors.GREEN
    if colLetter=='W':
        return Colors.WHITE
    if colLetter=='R':
        return Colors.RED
    if colLetter=='P':
        return Colors.PURPLE
    if colLetter=='r':
        return Colors.ROSE
    if colLetter=='B':
        return Colors.BLACK
    if colLetter=='G':
        return Colors.GOLD
    if colLetter=='b':
        return Colors.BLUE

def parseRank(rankLetter):
    if rankLetter=='S':
        return Ranks.SOLEMNITY    
    if rankLetter=='L':
        return Ranks.LORD
    if rankLetter=='F':
        return Ranks.FEAST
    if rankLetter=='M':
        return Ranks.MEMORIAL
    if rankLetter=='O':
        return Ranks.OPTIONAL
    #should never be needed, but heh.
    if rankLetter=='w':
        return Ranks.WEEKDAY
    if rankLetter=='c':
        return Ranks.COMMEMORATION
    if rankLetter=='S':
        return Ranks.SUNDAY
    if rankLetter=='a':
        return Ranks.ASHWED
    if rankLetter=='H':
        return Ranks.HOLYWEEK
    if rankLetter=='T':
        return Ranks.TRIDUUM


class LiturgicalDay:
    """This class holds all informations regarding a specific calendar day."""

    def __init__(self, daydate, color, rank, season, descr, strank=None):
        self.date=daydate
        self.color=color
        #TODO:
        #self.optColor=None
        self.rank=rank
        self.season=season
        self.descr=descr
        self.saintrank=strank
        #ommited celebrations for the day
        self.ommitted=None

    def printAll(self):
        """Prints a csv-formatted string containing all informations pertaining to the day"""
        retStr=""
        #TODO multiple optionals
        retStr+=str(self.date.date())+";"+str(self.season)+";"+str(self.color)+";"+str(self.rank)+";"+self.descr
        if self.saintrank:
            retStr+=";"+self.saintrank
        else:
            retStr+=";"
        if(self.ommitted != None):
            retStr+=";"+"[ Omitted: " + self.ommitted.descr +" ("+str(self.ommitted.rank)+") ]"
        return retStr;
        

        
        


