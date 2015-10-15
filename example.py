from facebook_crawler import FacebookCrawler

auth_user = 'olvandgame@gmail.com'
password = open('passwords/'+auth_user).read().strip()
crawler = FacebookCrawler(auth_user,password)

example_user = 'antal.vandenbosch'
user = crawler.get_user(example_user)
print(example_user + ' is '+user.age+' years old')

for post in user.posts[0:10]:

    print(post.date)
    print(post.text)
