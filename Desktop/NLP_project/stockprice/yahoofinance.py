import urllib

# Downloading and stores bollinger upper and bottom range for stock quote stored in file "nasdaq100" from yahoo finance to "BBand" 
# Also retrieves list of stocks that are below or above the bollinger range

list = open('nasdaq100', 'r')
x = 0
stocks = []

for i in list:
	x+=1
 	stocks.append(i.strip('\n'))

y = 0
understring = []
overstring = []
BBand = open('BBand', 'w+')
BBand.write("\n == current, lower, upper ==\n ")	
for stock in stocks:
	y = y+1
	htmltext = urllib.urlopen('https://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=bollinger;ys=2014;yz=2;ts=1234567890/csv?period=20&nstddev=2').read()
	pricedata = urllib.urlopen('https://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1d/csv').read()
	pricevalues = pricedata.split()
	current_price = float(pricevalues[-1].split(",")[1])
	values=str(htmltext).split()

	bollinger_lower = float(values[-1].split(",")[2])
	bollinger_upper = float(values[-1].split(",")[3])

	absolute_top = current_price - bollinger_upper
	percent_top = absolute_top / current_price

	absolute_bottom = current_price - bollinger_lower
	percent_bottom = absolute_bottom / current_price
	
	string  = stock +" "+str(current_price)+" "+str(bollinger_lower)+" "+str(bollinger_upper)+"\n"
	BBand.write(string)

	if percent_bottom <0:
		text = str(y) + '(under): ' + stock + ' ' +  str(percent_bottom * 100) + '%\n'
		understring.append(text)

	if percent_top > 0:
		text = str(y) + '(over):' + stock + ' ' +  str(percent_top * 100) + '%\n'
		overstring.append(text)

BBand.write("\n ===============below bollinger lower support================\n ")	
	
for i in understring:
	BBand.write(i)

BBand.write("\n ===============above bollinger upper resistnance============\n ")	
for j in overstring:
	BBand.write(j)

