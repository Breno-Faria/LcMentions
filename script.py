import requests
import psycopg2
from db import conn

# Getting the count of every LC problem mention on Reddit, and adding it to a PSQL db, with their title
cur = conn.cursor()
for i in range(100, 300):
	response = requests.get(f"https://www.google.com/search?q=leetcode+{i}")
	l = (response.text.find("<h3"))
	r = (response.text.find("h3>"))
	title = response.text[l + 60:r - 19]
	count = len(requests.get(f"https://api.pushshift.io/reddit/search/submission/?q=%22leetcode%20{i}%22&subreddit=leetcode&fields=title").json()["data"])
	count += len(requests.get(f"https://api.pushshift.io/reddit/search/submission/?q=%22leetcode%20{title}%22&subreddit=leetcode&fields=title").json()["data"])

	cur.execute("INSERT INTO problems (count, number, title) VALUES (%s, %s, %s)",
        (count, i, title))

#Query to db is:
#select title, count from problems ORDER BY count desc;


conn.commit()
cur.close()
conn.close()