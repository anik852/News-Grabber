import requests
from bs4 import BeautifulSoup
import sqlite3

def latest_news():
    url = 'https://www.ittefaq.com.bd/latest-news'
    n_paper = "Ittefaq"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="link-overlay")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News.db')
            c = conn.cursor()

            c.execute("SELECT * FROM newses WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="title mb10").text
                n_key = news_soup.find('h2', class_="secondary_logo").text

                conn = sqlite3.connect('News.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(Date text, n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO newses VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def special_news():
    url = 'https://www.ittefaq.com.bd/topic/%E0%A6%AC%E0%A6%BF%E0%A6%B6%E0%A7%87%E0%A6%B7-%E0%A6%B8%E0%A6%82%E0%A6%AC%E0%A6%BE%E0%A6%A6'
    n_paper = "Ittefaq"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="link-overlay")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News.db')
            c = conn.cursor()

            c.execute("SELECT * FROM newses WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="title mb10").text
                n_key = news_soup.find('h2', class_="secondary_logo").text

                conn = sqlite3.connect('News.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(Date text, n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO newses VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def national():
    url = 'https://www.ittefaq.com.bd/national'
    n_paper = "Ittefaq"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="link-overlay")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News.db')
            c = conn.cursor()

            c.execute("SELECT * FROM newses WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="title mb10").text
                n_key = news_soup.find('h2', class_="secondary_logo").text

                conn = sqlite3.connect('News.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(Date text, n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO newses VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def country():
    url = 'https://www.ittefaq.com.bd/country'
    n_paper = "Ittefaq"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="link-overlay")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News.db')
            c = conn.cursor()

            c.execute("SELECT * FROM newses WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="title mb10").text
                n_key = news_soup.find('h2', class_="secondary_logo").text

                conn = sqlite3.connect('News.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(Date text, n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO newses VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def politics():
    url = 'https://www.ittefaq.com.bd/politics'
    n_paper = "Ittefaq"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="link-overlay")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News.db')
            c = conn.cursor()

            c.execute("SELECT * FROM newses WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="title mb10").text
                n_key = news_soup.find('h2', class_="secondary_logo").text

                conn = sqlite3.connect('News.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(Date text, n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO newses VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def world_news():
    url = 'https://www.ittefaq.com.bd/world-news'
    n_paper = "Ittefaq"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="link-overlay")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News.db')
            c = conn.cursor()

            c.execute("SELECT * FROM newses WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="title mb10").text
                n_key = news_soup.find('h2', class_="secondary_logo").text

                conn = sqlite3.connect('News.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(Date text, n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO newses VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def sports():
    url = 'https://www.ittefaq.com.bd/sports'
    n_paper = "Ittefaq"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="link-overlay")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News.db')
            c = conn.cursor()

            c.execute("SELECT * FROM newses WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="title mb10").text
                n_key = news_soup.find('h2', class_="secondary_logo").text

                conn = sqlite3.connect('News.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(Date text, n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO newses VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def entertainment():
    url = 'https://www.ittefaq.com.bd/entertainment'
    n_paper = "Ittefaq"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="link-overlay")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News.db')
            c = conn.cursor()

            c.execute("SELECT * FROM newses WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="title mb10").text
                n_key = news_soup.find('h2', class_="secondary_logo").text

                conn = sqlite3.connect('News.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(Date text, n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO newses VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def business():
    url = 'https://www.ittefaq.com.bd/business'
    n_paper = "Ittefaq"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="link-overlay")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News.db')
            c = conn.cursor()

            c.execute("SELECT * FROM newses WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="title mb10").text
                n_key = news_soup.find('h2', class_="secondary_logo").text

                conn = sqlite3.connect('News.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(Date text, n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO newses VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def lifestyle():
    url = 'https://www.ittefaq.com.bd/lifestyle'
    n_paper = "Ittefaq"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="link-overlay")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News.db')
            c = conn.cursor()

            c.execute("SELECT * FROM newses WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="title mb10").text
                n_key = news_soup.find('h2', class_="secondary_logo").text

                conn = sqlite3.connect('News.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(Date text, n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO newses VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def tech():
    url = 'https://www.ittefaq.com.bd/tech'
    n_paper = "Ittefaq"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="link-overlay")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News.db')
            c = conn.cursor()

            c.execute("SELECT * FROM newses WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="title mb10").text
                n_key = news_soup.find('h2', class_="secondary_logo").text

                conn = sqlite3.connect('News.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(Date text, n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO newses VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def opinion():
    url = 'https://www.ittefaq.com.bd/opinion'
    n_paper = "Ittefaq"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="link-overlay")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News.db')
            c = conn.cursor()

            c.execute("SELECT * FROM newses WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="title mb10").text
                n_key = news_soup.find('h2', class_="secondary_logo").text

                conn = sqlite3.connect('News.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(Date text, n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO newses VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def news():
    url = 'https://www.ittefaq.com.bd/news'
    n_paper = "Ittefaq"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="link-overlay")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News.db')
            c = conn.cursor()

            c.execute("SELECT * FROM newses WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="title mb10").text
                n_key = news_soup.find('h2', class_="secondary_logo").text

                conn = sqlite3.connect('News.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(Date text, n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO newses VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
