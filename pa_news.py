import requests
from bs4 import BeautifulSoup
import sqlite3
def latest():
    url = 'https://www.prothomalo.com/collection/latest'
    n_paper = "ProthomAlo"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="card-with-image-zoom")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News_data.db')
            c = conn.cursor()

            c.execute("SELECT * FROM news WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="IiRps").text
                n_key = news_soup.find('a', class_="vXi2j").text
                conn = sqlite3.connect('News_data.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO news VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def special_news():
    url = 'https://www.prothomalo.com/collection/special-news'
    n_paper = "ProthomAlo"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="card-with-image-zoom")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News_data.db')
            c = conn.cursor()

            c.execute("SELECT * FROM news WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="IiRps").text
                n_key = news_soup.find('a', class_="vXi2j").text
                conn = sqlite3.connect('News_data.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO news VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def politics():
    url = 'https://www.prothomalo.com/politics'
    n_paper = "ProthomAlo"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="card-with-image-zoom")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News_data.db')
            c = conn.cursor()

            c.execute("SELECT * FROM news WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="IiRps").text
                n_key = news_soup.find('a', class_="vXi2j").text
                conn = sqlite3.connect('News_data.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO news VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def cr_viris():
    url = 'https://www.prothomalo.com/topic/%E0%A6%95%E0%A6%B0%E0%A7%8B%E0%A6%A8%E0%A6%BE%E0%A6%AD%E0%A6%BE%E0%A6%87%E0%A6%B0%E0%A6%BE%E0%A6%B8'
    n_paper = "ProthomAlo"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="card-with-image-zoom")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News_data.db')
            c = conn.cursor()

            c.execute("SELECT * FROM news WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="IiRps").text
                n_key = news_soup.find('a', class_="vXi2j").text
                conn = sqlite3.connect('News_data.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO news VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def bangladesh():
    url = 'https://www.prothomalo.com/bangladesh'
    n_paper = "ProthomAlo"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="card-with-image-zoom")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News_data.db')
            c = conn.cursor()

            c.execute("SELECT * FROM news WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="IiRps").text
                n_key = news_soup.find('a', class_="vXi2j").text
                conn = sqlite3.connect('News_data.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO news VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def world():
    url = 'https://www.prothomalo.com/world'
    n_paper = "ProthomAlo"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="card-with-image-zoom")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News_data.db')
            c = conn.cursor()

            c.execute("SELECT * FROM news WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="IiRps").text
                n_key = news_soup.find('a', class_="vXi2j").text
                conn = sqlite3.connect('News_data.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO news VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def business():
    url = 'https://www.prothomalo.com/business'
    n_paper = "ProthomAlo"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="card-with-image-zoom")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News_data.db')
            c = conn.cursor()

            c.execute("SELECT * FROM news WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="IiRps").text
                n_key = news_soup.find('a', class_="vXi2j").text
                conn = sqlite3.connect('News_data.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO news VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def opinion():
    url = 'https://www.prothomalo.com/opinion'
    n_paper = "ProthomAlo"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="card-with-image-zoom")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News_data.db')
            c = conn.cursor()

            c.execute("SELECT * FROM news WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="IiRps").text
                n_key = news_soup.find('a', class_="vXi2j").text
                conn = sqlite3.connect('News_data.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO news VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def sports():
    url = 'https://www.prothomalo.com/sports'
    n_paper = "ProthomAlo"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="card-with-image-zoom")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News_data.db')
            c = conn.cursor()

            c.execute("SELECT * FROM news WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="IiRps").text
                n_key = news_soup.find('a', class_="vXi2j").text
                conn = sqlite3.connect('News_data.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO news VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def entertainment():
    url = 'https://www.prothomalo.com/entertainment'
    n_paper = "ProthomAlo"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="card-with-image-zoom")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News_data.db')
            c = conn.cursor()

            c.execute("SELECT * FROM news WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="IiRps").text
                n_key = news_soup.find('a', class_="vXi2j").text
                conn = sqlite3.connect('News_data.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO news VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def chakri():
    url = 'https://www.prothomalo.com/chakri'
    n_paper = "ProthomAlo"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="card-with-image-zoom")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News_data.db')
            c = conn.cursor()

            c.execute("SELECT * FROM news WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="IiRps").text
                n_key = news_soup.find('a', class_="vXi2j").text
                conn = sqlite3.connect('News_data.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO news VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")
def lifestyle():
    url = 'https://www.prothomalo.com/lifestyle'
    n_paper = "ProthomAlo"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('a', class_="card-with-image-zoom")

    for link in links:
        n_link = link['href']

        if "video" in n_link:
            continue
        else:
            conn = sqlite3.connect('News_data.db')
            c = conn.cursor()

            c.execute("SELECT * FROM news WHERE n_link=?", (n_link,))
            items = c.fetchall()
            conn.commit()
            conn.close()

            if items == []:
                news = requests.get(n_link)
                news_soup = BeautifulSoup(news.text, 'html.parser')
                scripts = news_soup.find_all('script')
        
                n_title = news_soup.find('h1', class_="IiRps").text
                n_key = news_soup.find('a', class_="vXi2j").text
                conn = sqlite3.connect('News_data.db')
                c = conn.cursor()
                #c.execute("CREATE TABLE newses(n_link text, n_title text, n_key text, n_paper text)")
                c.execute("INSERT INTO news VALUES(?,?,?,?)", (n_link, n_title, n_key, n_paper))
                print("Insert Successfully")

                conn.commit()
                conn.close()
            else:
                continue
            
            print(n_link + "\n" + n_title+ "\n" + n_key+ "\n" + n_paper+ "\n")
            
    print(len(links))
    print("Complete")