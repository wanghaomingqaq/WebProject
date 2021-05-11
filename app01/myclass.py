import feedparser
from urlextract import URLExtract
import requests
from lxml import html
import tweepy

etree = html.etree


class Weibo():
    def parse(self, url):
        d = feedparser.parse(url)
        wei = []
        for entry in d.entries:
            weibo = {}
            extractor = URLExtract()
            text = entry.description
            urls = extractor.find_urls(text)
            weibo['title'] = entry.title
            weibo['content'] = entry.description
            href = []
            for url in urls:
                flag = ".jpg" in url
                if flag is True:
                    href.append(url)
            weibo['href'] = href
            weibo['url'] = entry.link
            wei.append(weibo)
        return wei


class Hupu:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'

    }

    def hupu(self, url):
        page_text = requests.get(url, headers=self.headers).text
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//*[@id="ajaxtable"]/div[1]/ul/li')
        print(type(li_list))
        print(li_list)
        hupu_list = []
        for li in li_list:
            hupu = {}
            content = li.xpath('./div/a/text()')

            href = 'https://bbs.hupu.com' + li.xpath('./div/a/@href')[0]
            hupu['title'] = content[0]
            hupu['href'] = href
            hupu['day']= content[2]
            hupu['time'] = content[3]
            hupu_list.append(hupu)
        return hupu_list


class Twitter():
    consumer_key = 'TVkCxZC3oHK0hguoguqJB1xmd'
    consumer_secret = '6PsMTfcJSZPvQFy9wYoRNJHDsRuJ44Tkesh5jMrzCa8sAAfdZL'
    access_token = '767361443675017216-R0YmR2a6Q1qepakf8Kmdp6RI74DfQzS'
    access_token_secret = 'prdouOQWqMfSsOTRSj5gm6dUsTJAPv8jfcJs4A0Kt8LmJ'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    def twitter(self,username):
        api = tweepy.API(self.auth)
        public_tweets = api.user_timeline(username)
        a = []
        for tweet in public_tweets:
            content = tweet.text
            a.append(content)
        return a
