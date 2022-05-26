
<img src="https://www.python.org/static/community_logos/python-logo-generic.svg" alt="HomePage"/>

# HeadlineEmailerAutomation
> Scripting with Python!
---

### Table of Contents:

- [Description](#description)
- [Code Snippets](#code-snippets)
- [Summary](#summary)
- [Demo](#demo)




---

## Description

This python script will work as a webscrapper for fetching the top 30 stories of HackerNews. Composing and sending an automated email to the recipients from an authenticated account.

We will create a function to extract the page links (title/components) from the passed url. BeautifulSoup will group the content with it's find_all capability. Structure will then be added to the soup to view as a list.

Once the content is extracted we will compose the email by signing into the smtp server with the credentials. Structure the subject line. Initiate connection and quit the server.

Debbging can be viewed by setting the communication 'server.set_debuglevel(0-3)'



Depencies we will be using

- BeautifulSoup
- smtplib 
- requests & datetime


---

## Code Snippets

> Creating the function that will extract news & build soup
```python
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
```

> Composing the email & setting up smtp server
```python
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
```

> Connecting to client & loggin in
```dart
print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
# sever=smtplib.SMTP SSL('smtp.gmail.com', 465)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
#server.ehlo
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')

server.quit()
```


---

## Summary

Fun project to introduce flutter into my workflow. Building the chat feature will prove useful when implementing into another future project. Looking forward to the next lab.

An extra step would be using Google's Flutterfire for backend intergration

We covered:

- How to build a Flutter app from the ground up
- How to use some of the shortcuts provided in Android Studio and IntelliJ
- How to run, hot reload, and debug your Flutter app on an emulator, a simulator, and a device
- How to customize your user interface with widgets and animations
- How to customize your user interface for Android and iOS


For more information refer to the official documentation.

- [Firebase Documentation](https://firebase.google.com/docs)
- [Flutterfire](https://firebase.google.com/docs/flutter/setup?platform=ios)
- [Flutter Documentation](https://docs.flutter.dev/)
- [Google's Flutter Youtube channel, Lots of great content here](https://www.youtube.com/channel/UCwXdFgeE9KYzlDdR7TG9cMw)

---

## Demo
![HomePage Gif](https://github.com/C-Dev66/HeadlineEmailerAutomation/blob/main/screenshots/headlineEmailer.png)


