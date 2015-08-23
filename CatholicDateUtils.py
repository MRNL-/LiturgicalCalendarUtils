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

from dateutil.easter import *
from datetime import date
from datetime import timedelta

def IsPascalTime(date):
    "Returns TRUE if provided date is during Pascal Time."
    return (date >= easter(date.year) and date <= Trinity(date.year))

def IsHolyWeek(date):
    ""
    return (date > PalmsSunday(date.year) and date < easter(date.year))

def IsInEasterOctave(date):
    ""
    d=timedelta(weeks=1)
    return (date >= easter(date.year) and date <= easter(year)+d)

def IsTriduum(date):
    ""
    return (date >= HolyThursday(date.year) and date < easter(date.year))

def IsLentTime(date):
    "Returns TRUE if provided date is during Lent. NOTE: this includes Sundays for now."
    #TODO? : check if not sunday ?
    return (date >= AshWednesday(date.year) and date < easter(date.year))

def IsAdventTime(date):
    "Returns TRUE if provided date is during Advent."
    return (date >= FirstSundayOfAdvent(date.year) and date < Christmas(date.year))

#======== LENT & PASCAL TIME ==================
def AshWednesday(year):
    "Ash Wednesday for given year. / Mercredi des Cendres de l'année year"
    d=timedelta(days=-46)
    return easter(year)+d

def PalmsSunday(year):
    "Palms Sunday for given year. / Dimanche des Rameaux de l'année year"
    d=timedelta(weeks=-1)
    return easter(year)+d

def HolyThursday(year):
    ""
    d=timedelta(days=-3)
    return easter(year)+d

def GoodFriday(year):
    ""
    d=timedelta(days=-2)
    return easter(year)+d

def EasterVigil(year):
    ""
    d=timedelta(days=-1)
    return easter(year)+d

def Easter(year):
    "Easter of given year. / Paques pour l'année [year]"
    # Redefined to provide a consistent API
    return easter(year)

def Ascension(year):
    ""
    d=timedelta(days=39)
    return easter(year)+d

def Pentecost(year):
    "Whit Sunday of given year. / Pentecote"
    d=timedelta(weeks=7)
    return easter(year)+d

def Trinity(year):
    ""
    d=timedelta(days=56)
    return easter(year)+d

def CorpusChristi(year):
    ""
    # Saint-Sacrement (Fete-Dieu)
    d=timedelta(days=63)
    return easter(year)+d

def SacredHearth(year):
    ""
    d=timedelta(days=19)
    return Pentecost(year)+d

#======== ADVENT & CHRISTMAS ==================
def ChristKing(year):
    ""
    d=timedelta(weeks=-1)
    return FirstSundayOfAdvent(year)+d

def FirstSundayOfAdvent(year):
    ""
    weeks = 4;
    correction = 0;
    christmas = date(year, 12, 25);
    if (christmas.weekday() != 6) :
        # 6 is Sunday
        weeks-= 1
        correction = (christmas.isoweekday());
    d=timedelta(days=(-1*((weeks*7)+correction)))
    return christmas+d

def SecondSundayOfAdvent(year):
    ""
    d=timedelta(weeks=1)
    return FirstSundayOfAdvent(year)+d

def ThirdSundayOfAdvent(year):
    ""
    d=timedelta(weeks=2)
    return FirstSundayOfAdvent(year)+d

def FourthSundayOfAdvent(year):
    ""
    d=timedelta(weeks=3)
    return FirstSundayOfAdvent(year)+d

def Christmas(year):
    "...OK, this one was soooo hard."
    return date(year, 12, 25)

#======== SOLEMNITIES ========================
def Sol_MaryMotherOfGod(year):
    return date(year, 1, 1)

def Epiphany(year):
    ""
    #TODO fixed:  return date(year, 1, 6)
    #Sunday following Jan, 1st
    s = date(year, 1, 2)
    e = date(year, 1, 8)
    delta = timedelta(days=1)
    while s <= e:
        if(s.weekday()==6):
            return s
        s+=delta
    return e

def StJoseph(year):
    ""
    # TODO: Confirm rules
    joseph = date(year, 3, 19)
    # Anticipated to saturday 18 if 19 is palms sunday & observed as a holy
    # day of obligation
    if(joseph == PalmsSunday(year)):
        d = timedelta(days=-1)
        return joseph+d
    return joseph

def Annunciation(year):
    ""
    annonciation = date(year, 3, 25)
    easter_ = easter(year)
    
    # the second monday after easter if 25 is during holy week or Pascal week
    if(easter_<=date(year,4,2)):
        d = timedelta(weeks=1, days=1)
        return easter_+d
    
    # the following monday if 25/03 is a sunday
    if(annonciation.weekday()==6):
        d = timedelta(days=1)
        return annonciation+d
        
    return annonciation

def Sol_NativityOfJohnTheBaptist(year):
    return date(year, 6, 24)

def StsPeterAndPaul(year):
    return date(year, 6, 29)

def Assumption(year):
    return date(year, 8, 15)

def AllSaints(year):
    return date(year, 11, 1)

def ImmaculateConception(year):
    return date(year, 12, 8)

#======== FEASTS ========================
# Feast are superseded by sundays except for Feasts of the Lord & All Souls

def ConversionOfPaul(year):
    paul_cv = date(year, 1, 25)
    if(paul_cv.weekday() == 6):
        return
    return paul_cv

def PresentationOfTheLord(year):
    "Présentation de Jésus au Temple"
    return date(year, 2, 2)

def ChairOfPeter(year):
    chair = date(year, 2, 22)
    if(chair.weekday() == 6):
        return
    return chair

def StMarkEvangelist(year):
    mark = date(year, 4, 25)
    if(mark.weekday() == 6):
        return
    return mark

def StsPhilipAndJames(year):
    "Saints Jacques et Philippe, apotres"
    pAj = date(year, 5, 3)
    if(pAj.weekday() == 6):
        return
    return pAj

# TODO check if any solemnity falls the same day
# i.e. 14/05/2015 was Ascension Thursday...
def StMatthias(year):
    "Saint Matthias, apotre"
    pAj = date(year, 5, 14)
    if(pAj.weekday() == 6):
        return
    return pAj

def Visitation(year):
    visitation = date(year, 5, 31)
    if(visitation.weekday() == 6):
        return
    return visitation

def StThomas(year):
    thomas = date(year, 7, 3)
    if(thomas.weekday() == 6):
        return
    return thomas

def StJames(year):
    "Saint Jacques le Majeur"
    james = date(year, 7, 3)
    if(james.weekday() == 6):
        return
    return james

def Transfiguration(year):
    return date(year, 8, 6)   

def StLawrence(year):
    "Saint Laurent"
    lt = date(year, 8, 10)
    if(lt.weekday() == 6):
        return
    return lt

def StBartholomew(year):
    "Saint Barthelemy"
    bt = date(year, 8, 24)
    if(bt.weekday() == 6):
        return
    return bt

def BirthOfMary(year):
    "Nativite de la Vierge Marie"
    bm = date(year, 9, 8)
    if(bm.weekday() == 6):
        return
    return bm

def Transfiguration(year):
    return date(year, 9, 14)

def StMatthew(year):
    "Saint Matthieu Evangeliste"
    mt = date(year, 9, 21)
    if(mt.weekday() == 6):
        return
    return mt

def Archangels(year):
    "Saints Archanges Michel, Gabriel & Raphael"
    a = date(year, 9, 29)
    if(a.weekday() == 6):
        return
    return a

def StLuke(year):
    "Saint Luc evangeliste"
    luke = date(year, 10, 18)
    if(luke.weekday() == 6):
        return
    return luke

def StsSimonAndJude(year):
    "Saints Simon & Jude, apotres"
    sj = date(year, 10, 28)
    if(sj.weekday() == 6):
        return
    return sj

def AllSouls(year):
    "Défunts"
    return date(year, 11, 2)

def DedicationOfStJohnLateran(year):
    "Dedicace de la basilique St-Jean-de-Latran"
    return date(year, 11, 9)

def StAndrew(year):
    "Saint Andre, apotre"
    a = date(year, 11, 30)
    if(a.weekday() == 6):
        return
    return a

def StStephen(year):
    "Saint Etienne, martyr"
    s = date(year, 12, 26)
    if(s.weekday() == 6):
        return
    return s

def StJohn(year):
    "Saint Jean, evangeliste"
    j = date(year, 11, 27)
    if(j.weekday() == 6):
        return
    return j

def StsInnocents(year):
    "Saints Innocents, martyrs"
    i = date(year, 11, 28)
    if(i.weekday() == 6):
        return
    return i

#----- Mobile feasts --------------

def HolyFamily(year):
    "Fete de la Sainte-Famille"
    if(Christmas.weekday() == 6):
        return date(year, 12, 30)
    day = (Christmas.isoweekday());
    d=timedelta(days=(7 - day)))
    return christmas+d

# Todo: if epiphany is fixed to 6/1
def BaptismOfTheLord(year):
    d=timedelta(weeks=1)
    return Epiphany+d

#=====================================

def StMartin(year):
    "St Martin de Tours"
    return date(year, 11, 11)

