import requests

# Getting the count of problems mentions on Reddit
response = requests.get("https://api.pushshift.io/reddit/search/submission/?q=%22leetcode%201234%22&subreddit=leetcode&fields=title&after12m")
if response.status_code == 200:
	res = (response.json())
count = {}
for i in range(3):
	count[len(requests.get(f"https://api.pushshift.io/reddit/search/submission/?q=%22leetcode%20{i}%22&subreddit=leetcode&fields=title&after12m").json()["data"])] = i
for key, value in count.items():
	print(f"Question {value} was mentioned {key} times")


#Getting the LC question title/url
response = requests.get("https://www.google.com/search?q=leetcode+124")

l = (response.text.find("<h3"))
r = (response.text.find("h3>"))
print(response.text[l + 60:r - 8])