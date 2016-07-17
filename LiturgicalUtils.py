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

import Translation

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
    elif colLetter=='g':
        return Colors.GREEN
    elif colLetter=='W':
        return Colors.WHITE
    elif colLetter=='R':
        return Colors.RED
    elif colLetter=='P':
        return Colors.PURPLE
    elif colLetter=='r':
        return Colors.ROSE
    elif colLetter=='B':
        return Colors.BLACK
    elif colLetter=='G':
        return Colors.GOLD
    elif colLetter=='b':
        return Colors.BLUE
    else:
        return None

def parseRank(rankLetter):
    if rankLetter=='S':
        return Ranks.SOLEMNITY    
    elif rankLetter=='L':
        return Ranks.LORD
    elif rankLetter=='F':
        return Ranks.FEAST
    elif rankLetter=='M':
        return Ranks.MEMORIAL
    elif rankLetter=='O':
        return Ranks.OPTIONAL
    #should never be needed, but heh.
    elif rankLetter=='w':
        return Ranks.WEEKDAY
    elif rankLetter=='c':
        return Ranks.COMMEMORATION
    elif rankLetter=='S':
        return Ranks.SUNDAY
    elif rankLetter=='a':
        return Ranks.ASHWED
    elif rankLetter=='H':
        return Ranks.HOLYWEEK
    elif rankLetter=='T':
        return Ranks.TRIDUUM
    else:
        return None


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
        #the day this celebration was supposed to take place
        self.originalDate=None

    def printAll(self):
        """Prints a csv-formatted string containing all informations pertaining to the day"""
        retStr=""        
            
        #Todo handle saintrank(s)?
        
        retStr+=str(self.date.date())+";"+str(self.season)+";"+str(self.color)+";"+self.printRank()+";"+self.celebration()
        if self.saintrank:
            retStr+=";"+self.printSaint()
        else:
            retStr+=";"
        if(self.ommitted != None):
            retStr+=";"+"[ Omitted: " + self.ommitted.celebration() +" ("+self.ommitted.printRank()+") ]"
        if self.originalDate:
            retStr+=";"+"( Moved from "+str(self.originalDate.date())+")"
        return retStr;

    def printAll_TR(self,locale):
        """Prints a csv-formatted string containing all informations pertaining to the day, translated in given locale"""
        if Translation.getLocale() != locale:
            try:
                Translation.setLocale(locale)
            except Exception as e:
                print e
                Translation.setLocale("en-EN")
            
        retStr=str(self.date.date())+";"+str(self.season)+";"+Translation.translate(self.printColor())+";"+Translation.translate(self.printRank())+";"+self.translateCelebration()
        
        if self.saintrank:
            retStr+=";"+self.printSaint()
        else:
            retStr+=";"
        if(self.ommitted != None):
            retStr+=";"+"[ "+Translation.translate("ommited")+" " + self.ommitted.translateCelebration() +" ("+Translation.translate(self.ommitted.printRank())+") ]"
        if self.originalDate:
            retStr+=";"+"( "+Translation.translate("mov_from")+" "+str(self.originalDate.date())+")"
        return retStr;

    def celebration(self):        
        #handle multiple optionals
        celeb=""
        if isinstance(self.descr, list):
            for i,string in enumerate(self.descr):
                if i!=0:
                    celeb += ": or "
                celeb+=string
                if isinstance(self.saintrank, list) and self.saintrank[i]:
                    celeb+=", " + str(self.saintrank[i])
        else:
            celeb+=self.descr
            if self.saintrank:
                celeb+=", " + str(self.saintrank)
        return celeb

    def translateCelebration(self):        
        #handle multiple optionals
        celeb=""
        if isinstance(self.descr, list):
            for i,string in enumerate(self.descr):
                if i!=0:
                    celeb += Translation.translate('or_other')+" "
                celeb+=Translation.translate(string)
                if isinstance(self.saintrank, list) and self.saintrank[i]:
                    celeb+=", " + Translation.translate(str(self.saintrank[i]))
        else:
            celeb+=Translation.translate(self.descr)
            if self.saintrank:
                celeb+=", " + Translation.translate(str(self.saintrank))
        return celeb

    def printSaint(self):
        st=""
        if isinstance(self.saintrank, list):
            for i,string in enumerate(self.saintrank):
                if i!=0:
                    st += " : "
                st+=string
        else:
            st+=self.saintrank
        return st

    def printColor(self):
        if self.color == Colors.GREEN:
            return "Green"
        elif self.color == Colors.WHITE:
            return "White"
        elif self.color == Colors.RED:
            return "Red"
        elif self.color == Colors.PURPLE:
            return "Purple"
        elif self.color == Colors.ROSE:
            return "Rose"
        elif self.color == Colors.BLACK:
            return "Black"
        elif self.color == Colors.GOLD:
            return "Gold"
        elif self.color == Colors.BLUE:
            return "Blue"
        else:
            return "No_color"

    def printRank(self):
        if self.rank==Ranks.SOLEMNITY:
            return "rk_sol"
        elif self.rank==Ranks.LORD:
            return "rk_ftL"
        elif self.rank==Ranks.FEAST:
            return "rk_fst"
        elif self.rank==Ranks.MEMORIAL:
            return "rk_mem"
        elif self.rank==Ranks.OPTIONAL:
            return "rk_opt"
        elif self.rank==Ranks.WEEKDAY:
            return "rk_wkd"
        elif self.rank==Ranks.COMMEMORATION:
            return "rk_com"
        elif self.rank==Ranks.SUNDAY:
            return "rk_sun"
        elif self.rank==Ranks.ASHWED:
            return "rk_ash"
        elif self.rank==Ranks.HOLYWEEK:
            return "rk_hwk"
        elif self.rank==Ranks.TRIDUUM:
            return "rk_tri"
        else:
            return "rk_none"


class LiturgicalOptions:
    """This struct stores informations regarding the liturgical rules"""
    def __init__(self, epiphany_fixed=false, ascension_thu=true, corpusChristi_thu=false, opt_mem_mary_sat=false):
        self.epiphany_fixed=epiphany_fixed
        self.ascension_thu=ascension_thu
        self.corpusChristi_thu=corpusChristi_thu
        self.opt_mem_mary_sat=opt_mem_mary_sat

        
        


