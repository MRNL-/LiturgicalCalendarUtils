# LiturgicalCalendarUtils
DateTime python extensions to help create and consult a liturgical calendar<br/>
(C) Martin Raynal, 2015<br/>
<br/>
## Dependencies
This project references the following python modules:
* <a href="https://pypi.python.org/pypi/enum34">enum34</a>
* <a href="https://pypi.python.org/pypi/python-dateutil">dateutil</a>

## References
* <a href="https://w2.vatican.va/content/paul-vi/en/motu_proprio/documents/hf_p-vi_motu-proprio_19690214_mysterii-paschalis.html">Motu Proprio <i>Mysterii paschalis</i>, Paul VI, 14-02-1969</a>
* <a href="http://www.romcal.net/norms.html">General Norms for the Liturgical Year and the Calendar, 21-03-1969</a>
* Decree <i>Celebratio Baptismatis Domini</i>, 7 October 1977
* <a href="http://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20000630_memoria-immaculati-cordis-mariae-virginis_lt.html">Notificatio: DE OCCURRENTIA MEMORIAE OBLIGATORIAE IMMACULATI CORDIS BEATAE MARIAE VIRGINIS, Per Decretum die 01-01-1996</a>
*  <a href="http://press.vatican.va/content/salastampa/it/bollettino/pubblico/2016/06/10/0422/00974.html">Apostolorum Apostola - Decretum CCDDS 03-06-2016</a>
<br/>

<pre>
== Most functional work is done, still need data feeding and some cleanup. ==
CatholicDateUtils.py :
	* Methods returning the date of various solemnities and feasts for a given year
	* Full-year calendar generation (heavily based on ROMCal implementation)
		- use: cl= computeCalendar(year, continent, country, diocese, verbose) returns an array containing all informations for given year,
		optionally with the addition of continental and national Propers celebrations
		- for printing the French calendar to csv:
			from CatholicDateUtils import *
			cl=computeCalendar(2017,'Europe','France',verbose=False)
			f1=open('./generated_2017.csv','w+')
			for day in cl:
				print >>f1, day.printAll_TR('fr-FR')
				
		TODO: provide a cleaner API to print and use this structure...
		
LiturgicalUtils.py :
	* 'LiturgicalDay'Class and Enums
		- the day class provides several ways of printing a specific day (raw, translated...). This will likely be expanded again.

Translation.py : 
	* Methods used to translate the keys found in the calendar structure.
	* Expects all localised files to be stored in './locale/[localeName]/' directory, except for default ('en-EN') ones that are at root.
	
TODO List
	* Options to generate specific fixed calendars for <s>Continent/Country/</s>Diocese and Orders
	* AP to pretty print the calendars
	
	* Explicits Queries: Fix calculations to ensure correct priorities are always taken into account
		- For now the date of a Feast will always be returned even when it is superseded by another solemnity or sunday (ex. St Matthias 2015)
	
	* The current calendar is the General Roman Calendar for the ordinary Rite (cf. Mysterii Paschalis, 1969). I may also implement the Tridentine calendar someday.
	* Test. Test and test again. This was really not tested enough, which is NOT GOOD(TM)
	* Maybe actually learn Python ? As this is my first project it is likely ridden with noob errors. Oh well...
	
In fine, I hope to use it for several applications - in particular, to feed the <a href="https://twitter.com/Angelus_LT">@Angelus_LT</a> & @Angelus_FRA twitter accounts with daily hashtags,
or provide the results as a web service...
</pre>
<br/>
## Credits
This was inspired by Jan Schreuder's article on CodeProject:<br/>
http://www.codeproject.com/Articles/10860/Calculating-Christian-Holidays<br/>
and the RomCal project:<br/>
http://www.romcal.net/<br/>
It also makes use of the DateUtil python library, especially (obviously?) the easter() function.<br/>
https://labix.org/python-dateutil<br/>

