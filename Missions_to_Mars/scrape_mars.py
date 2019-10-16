# Jadd Cheng
# October 15, 2019
# Import dependencies
import pandas as pd # to extract HTML table.
from bs4 import BeautifulSoup as bs # bs --> parse and extract data
from splinter import Browser # splinter --> to navigate pages.
import requests
from urllib.parse import urlparse
import time # for sleep statement

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():

    # initialize browser instance.
    browser = init_browser()

    # dict to hold extracted data.
    mars_data = {}

## 1. NASA Mars News - Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
    url_news = 'https://mars.nasa.gov/news/'
    browser.visit(url_news)
    time.sleep(1)

    html_news = browser.html
    soup_news = bs(html_news, 'lxml')
    news_item = soup_news.find_all('li', class_='slide')[0]
    
    mars_data['news_title'] = news_item.h3.get_text()
    mars_data['news_p'] = news_item.get_text()

# 2. JPL Mars Space Images - Featured Image
# * Visit the url for JPL Featured Space Image here.
# * https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
# * Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
# * Make sure to find the image url to the full size .jpg image.
# * Make sure to save a complete url string for this image.

    url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_image)
    time.sleep(2)

    browser.click_link_by_id("full_image")
    time.sleep(2)

    browser.click_link_by_partial_text("more info")
    time.sleep(2)

    # create soup object to parse DOM.
    soup_image = bs(browser.html, 'lxml')

    # scrape image link url for hires featured image of the day.
    url_image_path = soup_image.article.figure.a['href']

    mars_data["featured_image_url"] = 'https://www.jpl.nasa.gov' + url_image_path

# 3. Mars Weather - Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.
#  `mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'`

    url_weather = 'https://twitter.com/marswxreport?lang=en'
    requests.get(url_weather)
    html_weather = requests.get(url_weather).text
    soup_weather = bs(html_weather, 'lxml')
    
    mars_data["mars_weather"] = soup_weather.find('div', class_="content").p.get_text()


# 4. Mars Facts - Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# * Use Pandas to convert the data to a HTML table string.
# * https://space-facts.com/mars/
# * Scraping strategy: No need to soupify.
# * Just pass HTML string directly to Pandas `read_html` method.
# * Pandas will automatically detect all tables and return a list of them.
# * Can reference individual tables with bracket notation, e.g. `[0]`
    url_facts = 'https://space-facts.com/mars/'
    html_facts = requests.get(url_facts).text
    
    pd.read_html(html_facts)

    df_facts = pd.read_html(html_facts)[1]
    facts_html_table = df_facts.to_html(header=False, index=False)

    mars_data["facts_html_table"] = facts_html_table.replace('\n', '')

# 5. Mars Hemispheres
# * Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
# * You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# * Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
# * Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
# 
# ### Example:
# >`hemisphere_image_urls = [
#     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
#     {"title": "Cerberus Hemisphere", "img_url": "..."},
#     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
#     {"title": "Syrtis Major Hemisphere", "img_url": "..."},
# ]`
    url_hemispheres = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_hemispheres)
    time.sleep(1)

    html_hemispheres = browser.html
    soup_hemispheres = bs(html_hemispheres, 'lxml')
    urlparse(url_hemispheres)

    hemisphere_items = soup_hemispheres.find('div', class_="collapsible results").find_all("div", "item")
    
    links = []
    for hemisphere in hemisphere_items:
        link = 'https://' + urlparse(url_hemispheres).netloc + hemisphere.a['href']
        links.append(link)

    hemisphere_image_urls = [] # {"title": "Valles Marineris Hemisphere", "img_url": "..."}

    for link in links:
        browser.visit(link)
        time.sleep(1)
        link_soup = bs(browser.html, 'lxml')
        title = link_soup.h2.text.replace(" Enhanced", "")
        img_url =  link_soup.find('div', class_="downloads").find('li').a['href']    
        hemisphere_image_urls.append({"title": title, "img_url": img_url})

    mars_data['hemisphere_image_urls'] = hemisphere_image_urls

    # QUIT BROWSER! avoid multiple chromedriver windows open.
    browser.quit()

    return mars_data

if __name__ == "__main__":
    # scrape()
    mars_data = scrape()
    print(mars_data)
    # import the scrape script in app.py