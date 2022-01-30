from turtle import heading
import requests
import bs4

email_id = input("Enter the Email ID: ")

index1 = email_id.index('@')

name = email_id[:index1]
name = ''.join([i for i in name if not i.isdigit()])

text = name + " linkedin"
url = 'https://google.com/search?q=' + text

# Fetching the URL data and storing it in a vairable
request_address = requests.get(url)

# Creating soup from the fetched request
soup = bs4.BeautifulSoup(request_address.text, "html.parser")
# print(soup)
heading_object = soup.find_all('a')

for info in heading_object:

        if("https://in.linkedin.com" in info.get('href')):

            indx = info.get('href').index('sa=')
            temp = info.get('href')[7:indx-1]
            # print(temp)

            indx1 = temp.index('in/')
            print("https://www.linkedin.com/in/" + temp[indx1+3:])
