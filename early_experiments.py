import mechanize
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)

page = browser.open('http://m.facebook.com/')
browser.select_form(nr = 0)
browser.form['email'] = 'olvandgame@gmail.com'
browser.form['pass'] = ''
response = browser.submit()
print(response)

page = browser.open('http://m.facebook.com/antal.vandenbosch/year/2015')
print(page.read())

