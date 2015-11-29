# LiturgicalCalendarUtils
DateTime python extensions to help create and consult a liturgical calendar
(C) Martin Raynal, 2015

<pre>
== This is currently a work heavily in progress. ==
CatholicDateUtils.py :
	* Methods returning the date of various solemnities and feasts for a given year
	* Full-year calendar generation (heavily based on ROMCal implementation)
	
	
TODO List
	* Options to generate specific fixed calendars for Continent/Country/Diocese
	* Pretty print the calendars ?
	* Fix calculations to ensure correct priorities are always taken into account
		- For now the date of a Feast will always be returned even when it is superseded by another solemnity
	* This library should be somewhat Catholic & French centric for now, but I may consider expanding it to include Orthodox and localised options
		* The current calendar is the General Roman Calendar for the ordinary Rite (cf. Mysterii Paschalis, 1969). I may also implement the 'Tridentine' calendar.
	* Test. Test and test again. This was not really tested, which is NOT GOOD(TM)
	* Maybe actually learn Python ? As this is my first project it is likely ridden with noob errors. Oh well...
	
In fine, I hope to use it for several applications - in particular, to feed the @Angelus_LT & @Angelus_FRA twitter accounts with daily hashtags,
or provide the results as a web service...

= Credits =
This was inspired by Jan Schreuder's article on CodeProject:
http://www.codeproject.com/Articles/10860/Calculating-Christian-Holidays
and the RomCal project:
http://www.romcal.net/
It also makes use of the DateUtil python library, especially (obviously?) the easter() function.
https://labix.org/python-dateutil

</pre>
