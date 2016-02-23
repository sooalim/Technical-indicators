import urllib
import re

#scrapes investor estimates from marketwatch.com site 
#url
htmltext = urllib.urlopen('http://www.marketwatch.com/investing/stock/lnkd/analystestimates').read()

#scan for estimates provided
regex_type = '<td class="first">(.+?)</td>'
pattern_type = re.compile(regex_type)
types = re.findall(pattern_type, htmltext)

#print Mean estimates
regex = '<td class="first">Mean Estimate</td>\r\n\s*<td>(.+?)</td>\r\n\s*<td>(.+?)</td>\r\n\s*<td>(.+?)</td>\r\n\s*<td>(.+?)</td>'
pattern = re.compile(regex)

results = re.findall(pattern, htmltext)

for estimate in results:
	print estimate, '\n'



# http://www.marketwatch.com/charts/barcharts/analysts-ratings.img?data=10,6,4+1,1,2+16,7,8+1,1,0+0,0,0&legend=Buy|Overweight|Hold|Underweight|Sell&title=YHOO+Recommendations