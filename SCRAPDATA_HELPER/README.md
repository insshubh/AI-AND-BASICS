<h2 align="center">SCRAPED Data Viewer</h1>
<p align="center">Search your querry related With Scrap Data on along with talking to a chatbot</p>
 <ol>
<li>This is a small python project to Srap Data of Multiple pages and Store it to Csv format </li> <li>I created this project for MotionCut  am thinking to turn it to a complete chatbot service for python soon where user No need to Search or find Details on Website they just give title and Chatbot shows all Related Values to it .</li></ol>
 </p>
 
 <h2>Features</h2>
<ul>
    <li>Search your Querry instantly without looking on Webpage.</li>
    <li>Install packages from pip</li>
    <li>A chatbot support we are Working on, which uses NLP techniques for better User Service</li>
</ul>
# Use Proxy For GET request over different IP..

```python
proxy_servers = {
   'http': 'http://proxy.sample.com:8080',
   'https': 'http://secureproxy.sample.com:8080',
}

response = requests.get('sample.abc', proxies=proxy_servers)
import requests
from bs4 import BeautifulSoup
import pandas as pd

# List to store extracted key & values from the webpage
dic = []

# Scraping data from multiple pages
for i in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    response = requests.get(url)
    res = response.content
    soup = BeautifulSoup(res, 'html.parser')
    ol = soup.find('ol')
    articles = ol.find_all('article')
    
    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']
        rating = article.find('p')
        r = rating.attrs['class'][1]
        price = article.find('div', class_='product_price')
        rate = price.find('p').text
        availability = article.find('p', class_='instock availability').text.strip()
        dic.append([title, rate, r, availability])

# Creating a dataframe having Labels as mentions.
df = pd.DataFrame(dic, columns=['Name of Book', 'Price', 'Rating', 'Stock'])
df.to_csv('books.csv')

# Load your CSV data
df = pd.read_csv('/content/books.csv')
df.drop(['Unnamed: 0'], axis=1, inplace=True)

# Function to retrieve book details by title
def get_book_details(title):
    book_details = df[df['Name of Book'].str.lower() == title.lower()]
    return book_details

# Simple chatbot loop
while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        break
    else:
        book_title = user_input.strip()  # Remove leading/trailing spaces
        book_info = get_book_details(book_title)
        if not book_info.empty:
            print("Bot:")
            print(book_info)
        else:
            print("Bot: Book not found.")

```
```
### Output
User: shubham
Bot: Book not found.
User: 22/11/63
Bot: Book not found.
User: 11/22/63
Bot:
    Name of Book   Price Rating     Stock
417     11/22/63  £48.48  Three  In stock
User: The Requiem Red
Bot:
      Name of Book   Price Rating     Stock
5  The Requiem Red  £22.65    One  In stock
User: exit
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

<div align="center">
  
### Show some ❤️ by starring this repository!
  
</div>
