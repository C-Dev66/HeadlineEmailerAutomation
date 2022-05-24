import requests #http requests

from bs4 import BeautifulSoup # web scraping

# Send email
import smtplib
# Email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system date and time manipulation
import datetime
now = datetime.datetime.now()


# email content placeholder

content = ''



# Extracting Hacker News Stories


def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt += ('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    responce = requests.get(url)
    content = responce.content
    soup = BeautifulSoup(content, 'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+' :: '+tag.text + "\n" + '<br>') if tag.text!='More' else '')
        #print(tag.prettify) #find_all('span',attrs={'class':'sitestr'})
    return(cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>-------<br>')
content +=('<br><br>End Of Message')

# This function is to extract the front page links or titile/components that we want
# function extract_news is passed the url where we are extracting then we are creating
# is a nice title that says HN Top stories & then extracting the content
# We are using BeautifulSoup to make a soup of the content
# Then we are using soup.find_all to find all the td tags with attributes:
# (class, title, valigh). Then we are creating rows 
# Then we notice that there is one final row that has a value of MORE
# so we are exluding that. Then we are returing the function with cnt



# Let send the email

print('Comosing Email...')

SERVER = 'smtp.gmail.com' # "Your smtp SERVER"
PORT = 587 # your port number
FROM = '' # your from email id **Be Careful pusing this to repo**
TO = '' # your to email id  **Becareful pushing this to repo**
PASS = '' # your email id's password **Becareful pushing this to repo**

# fp = open(file_name, 'rb')
# Create a text/plain message
# msg = MIMEText('')
msg = MIMEMultipart()

# msg.add_header('Content-Disposition', 'attachment', filename='empty.txt')
msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))
# fp.close()


