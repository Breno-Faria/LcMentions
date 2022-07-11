import requests
import psycopg2
from db import conn

# Getting the count of problems mentions on Reddit
cur = conn.cursor()
for i in range(10):
	response = requests.get(f"https://www.google.com/search?q=leetcode+{i}")
	l = (response.text.find("<h3"))
	r = (response.text.find("h3>"))
	cur.execute("INSERT INTO problems (count, number, title) VALUES (%s, %s, %s)",
	(len(requests.get(f"https://api.pushshift.io/reddit/search/submission/?q=%22leetcode%20{i}%22&subreddit=leetcode&fields=title&after12m").json()["data"])
	, i, response.text[l + 60:r - 19]))

conn.commit()
cur.close()
conn.close()