from selenium import webdriver
import requests

# 1

response_repo = requests.get("https://api.github.com/users/avielb/repos")
print(len(response_repo.json()))  # 30
assert len(response_repo.json()) > 5, "there are less then 5 repos"

# 2


# 3
response_universities = requests.get("http://universities.hipolabs.com/search?country=Israel")
print(len(response_universities.json()))  # 23
assert len(response_universities.json()) > 5, "there are less then 5 universities from Israel"

# 4
my_driver = webdriver.Chrome()
my_driver.get("https://www.ycombinator.com/")
assert my_driver.title == "Y Combinator", "Title is not Y Combinator"
print(my_driver.title)

# 5
my_driver_2 = webdriver.Chrome()
my_driver_2.get("https://hub.docker.com")
assert my_driver_2.title == "Docker Hub Container Image Library | App Containerization", "Title is not as expected"
print(my_driver_2.title)
