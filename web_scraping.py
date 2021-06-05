from bs4 import BeautifulSoup
import requests
import csv

#headlines and summary
with open('HTML_FILE_PATH') as html_file:
	soup = BeautifulSoup(html_file, 'lxml') # lxml is a parser
print(soup) # no indentation
print(soup.prettify()) #with indentation

#-------------------------------------------------------------------------------------------------------------------------------
match1 = soup.title  #print title of html with title tag
match2 = soup.title.text #print only title 
print(match1)
print(match2)
#-------------------------------------------------------------------------------------------------------------------------------
match3 = soup.div #gives first div tag

article = soup.find('div', class_='class_name') #to target specific class
#note there is a underscore after class attribute on previous line because 'class' is a keyword inn python

headline = article.h2.a.text #print text from anchor tag of h2 of variable article
print(headline)

summary = article.p.text  # print text of the para of variable article
print(summary)

#-------------------------------------------------------------------------------------------------------------------------------

#print all para from all div tags
for all_article in soup.find_all('div', class_='article'):
	headline = all_article.h2.a.text #print text from anchor tag of h2 of variable article
	print(headline)

	summary = all_article.p.text  # print text of the para of variable article
	print(summary)

	print() #new line

#-------------------------------------------------------------------------------------------------------------------------------

# print source code of the htlm file from url with indentation
source = requests.get('url_of_the_site').text
soup = BeautifulSoup(source, 'lxml')
print(soup.pretiffy())


article = soup.find('article') #print article tag
print(article.pretiffy())


headline = article.h2.a.text #print headline of the page
print(headline)


summary = article.find('div', class_= 'class_name').p.text #print the text of para of div
print(summary)



vid_src = article.find('div_name', class_= 'class_name')['attribute_name'] #print the content of the attribute of the tag
print(vid_src)

vid_id = vid_src.split('/') #print splitted text, split by '/'
print(vid_id)

vid_id = vid_src.split('/')[4] #print 4th element of the splitted text, split by '/'
print(vid_id)

vid_id = vid_src.split('?')[0] #print 0th element of the splitted text, split by '?'
print(vid_id)


yt_link= f'https://www.youtube.com/watch?v={vid_id}' #for python 3.6 & above else use format()
print(yt_link) #print youtube link

#-------------------------------------------------------------------------------------------------------------------------------
#to print all headlines under the div tag
for article in soup.find_all('div')
	headline = article.h2.a.text

"""note:- if in the previous cmd, any post will have no header then it will throw an error
to cover that up we will use an alternative to the upper cmd in the next line-->"""


for article in soup.find_all('div'):
	try:
		headline = article.h2.a.text
	except Exception as e:
		#raise e (to print the error)
		#pass (to continue)
		yt_link = None #print none in place of yt_link
#-------------------------------------------------------------------------------------------------------------------------------
#now to save the content to csv file

csv_file = open('NAME_OF_THE_FILE.csv','w')# opening pointer, w for write mode
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline1','headline2','headline3']) #write headers for the csv file 
csv_writer.writerow([headline,summary,yt_link]) #passing values

csv_file.close()
