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

class LiturgicalDay:
    """This class holds all informations regarding a specific calendar day."""

    def __init__(self, daydate, color, rank, season, descr):
        self.date=daydate
        self.color=color
        self.rank=rank
        self.season=season
        self.descr=descr

        
        


