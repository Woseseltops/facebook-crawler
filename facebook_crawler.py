import mechanize
from bs4 import BeautifulSoup
from datetime import date

class FacebookCrawler():

    def __init__(self,username,password):

        #Create browser
        self.browser = mechanize.Browser()
        self.browser.set_handle_robots(False)
        cookies = mechanize.CookieJar()
        self.browser.set_cookiejar(cookies)
        self.browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
        self.browser.set_handle_refresh(False)

        #Log in
        self.browser.open('http://m.facebook.com/')
        self.browser.select_form(nr = 0)

        self.browser.form['email'] = username
        self.browser.form['pass'] = password
        self.browser.submit()

    def get_user(self,username):

        raw_page = self.browser.open('http://m.facebook.com/'+username+'/year/'+str(date.today().year))
        posts = self.html_to_posts(raw_page.read())

        user = FacebookUser(username,posts,None)
        return user

    def html_to_posts(self,html):

        parsed_page = BeautifulSoup(html)

        posts = []
        dates = []

        for abbr in parsed_page.find_all('abbr'):
            dates.append(abbr.get_text())

        index = 0

        for div in parsed_page.find_all('div'):

            if 'class' in div.attrs and 'by' in div['class']:
                posts.append(FacebookPost(dates[index],div.get_text()))

                index += 1

        return posts

class FacebookUser():

    def __init__(self,username,posts,age):

        self.posts = posts
        self.age = age

class FacebookPost():

    def __init__(self,date,text):

        self.date = date
        self.text = text

if __name__ == '__main__':

    auth_user = 'olvandgame@gmail.com'
    password = open('passwords/'+auth_user).read().strip()
    crawler = FacebookCrawler(auth_user,password)

    user = crawler.get_user('antal.vandenbosch')
    print(user.posts[0].date)

#TODO
# Alleen recente posts