import requests
response_repo = requests.get("https://api.github.com/users/avielb/repos")
print(len(response_repo.json()))  # 30
assert len(response_repo.json()) > 5, "there are less then 5 repos"

response_universities = requests.get("http://universities.hipolabs.com/search?country=Israel")
print(len(response_universities.json()))  # 23
assert len(response_universities.json()) > 5, "there are less then 5 universities from Israel"