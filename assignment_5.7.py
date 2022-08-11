from selenium import webdriver

my_driver = webdriver.Chrome()
my_driver.get("https://www.ycombinator.com/")
assert my_driver.title == "Y Combinator", "Title is not Y Combinator"
print(my_driver.title)

my_driver_2 = webdriver.Chrome()
my_driver_2.get("https://hub.docker.com")
assert my_driver_2.title == "Docker Hub Container Image Library | App Containerization", "Title is not as expected"
print(my_driver_2.title)