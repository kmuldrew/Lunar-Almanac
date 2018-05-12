# Lunar-Almanac
Nautical almanac pages similar in style to those ca. 1800

The program creates a pdf file for a particular month giving the lunar distances that are convenient for each day of the month as well as a few other useful tables for working lunars as a navigator might have done around the year 1800. Time is Greenwich apparent time and the day starts at noon.

You will need to install Skyfield, math, pandas, calendar, reportlab and time.

The code currently uses the de421 ephemeris but if you want to generate tables for historical purposes, you may need to change it to de422 to go back further than about 200 years.
