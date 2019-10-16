# web-scraping-challenge
* October 13, 2019
* See below for most of the links I read to finish the assignment.
* [Instructions](https://github.com/the-Coding-Boot-Camp-at-UT/UT-MCB-DATA-PT-07-2019-U-C/tree/master/homework-instructions/12-Web-Scraping-and-Document-Databases/Instructions)

## Splinter ##
* [Splinter Tutorial](https://splinter.readthedocs.io/en/latest/tutorial.html)

## PyMongo ##
* https://api.mongodb.com/python/current/tutorial.html
* https://www.w3schools.com/python/python_mongodb_getstarted.asp

## Setting Windows path variables ##
* https://www.addictivetips.com/windows-tips/set-path-environment-variables-in-windows-10/

## Web Scraping ##
* [Tutorial: Python Web Scraping Using BeautifulSoup - Dataquest.io](https://www.dataquest.io/blog/web-scraping-tutorial-python/)
* [A Guide to Web Scraping in Python using BeautifulSoup](https://dev.to/ayushsharma/a-guide-to-web-scraping-in-python-using-beautifulsoup-1kgo)
* [Extract text from a webpage using BeautifulSoup and Python - February 12, 2019](https://matix.io/extract-text-from-webpage-using-beautifulsoup-and-python/)
* [Python Script 7: Scraping tweets using BeautifulSoup](https://www.pythoncircle.com/post/522/python-script-7-scraping-tweets-using-beautifulsoup/)
* [Twitter scraper tutorial with Python: Requests, BeautifulSoup, and Selenium — Part 1 - Daw-Ran Liou - Mar 26, 2016 · 4 min read](https://medium.com/@dawranliou/twitter-scraper-tutorial-with-python-requests-beautifulsoup-and-selenium-part-1-8e76d62ffd68)
* [Twitter scraper tutorial with Python: Requests, BeautifulSoup, and Selenium — Part 2 - Daw-Ran Liou - Apr 9, 2016 · 3 min](https://medium.com/@dawranliou/twitter-scraper-tutorial-with-python-requests-beautifulsoup-and-selenium-part-2-b38d849b07fe)
* [What is the difference between 'content' and 'text'](https://stackoverflow.com/questions/17011357/what-is-the-difference-between-content-and-text)
    > > `r.text` is the content of the response in Unicode, and `r.content` is the content of the response in bytes.
* [Make Your Python Web Scraper Smarter - Hannah Huang - Jun 19 · 6 min read](https://levelup.gitconnected.com/make-your-python-web-scraper-smarter-6233f2d10c3f) - How to deal with multiple pages.

### Scraping HTML tables with Pandas
* [Web Scraping with Pandas and Beautifulsoup](https://pythonprogramminglanguage.com/web-scraping-with-pandas-and-beautifulsoup/) - Especially useful for purposes of assignment.
* [Web Scraping HTML Tables with Python - Syed Sadat Nazrul - Jul 25, 2018 · 3 min read](https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059)
* [Parsing HTML Tables in Python with pandas - Benjamin Bertrand 2018-03-27 22:31](https://beenje.github.io/blog/posts/parsing-html-tables-in-python-with-pandas/) - Also very helpful.
* [Styling Pandas Dataframe Tables - SUN 18 NOVEMBER 2018
](https://blog.hedaro.com/styling-dataframe-tables.html) - See use of `from IPython.display import HTML`.
* [Parsing HTML Tables in Python with pandas - Benjamin Bertrand - 2018-03-27 22:31](https://beenje.github.io/blog/posts/parsing-html-tables-in-python-with-pandas/)
* [pandas.DataFrame.to_html](https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.DataFrame.to_html.html)

## Python sleep module
* [Python’s time.sleep() – Pause, Stop, Wait or Sleep your Python Code](https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/)
* [Python: Need to wait before BeautifulSoup and Urllib can parse a website - Stack Overflow](https://stackoverflow.com/questions/21445845/python-need-to-wait-before-beautifulsoup-and-urllib-can-parse-a-website)
* [Tutorial: Web Scraping and BeautifulSoup - Dataquest.io](https://www.dataquest.io/blog/web-scraping-beautifulsoup/)

## Flask-Pymongo 
* [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)

## Challenges and Questions
* `lxml` library does not do https?
* When to use Splinter quit browser `browser.quit()`?

## Urllib.parse
* https://docs.python.org/3/library/urllib.parse.html

## Bootstrap
* [Bootstrap cards](https://coreui.io/docs/components/cards/)
>> Bootstrap cards component provide a flexible and extensible container for displaying content. Bootstrap cards are delivered with a bunch of variants and options.
* [Bootstrap documentation - Cards](https://getbootstrap.com/docs/4.3/components/card/)
>> Bootstrap’s cards provide a flexible and extensible content container with multiple variants and options.

## Jinja
* [Jinja Templates](http://jinja.palletsprojects.com/en/2.10.x/templates/)
* NB Jinja doesn't play nice with HTML comments.
* [Primer on Jinja Templating by Real Python](https://realpython.com/primer-on-jinja-templating/)
* [Passing HTML to template using Flask/Jinja2](https://stackoverflow.com/questions/3206344/passing-html-to-template-using-flask-jinja2)
>> When automatic escaping is enabled everything is escaped by default except for values explicitly marked as safe. Those can either be marked by the application or in the template by using the |safe filter.
>> Example:
>> 
>>>> <div class="info">
>>>>>> {{data.email_content|safe}}
>>>> </div>

## TABLE
<table border="1" class="dataframe">  <tbody>    <tr>      <td>Equatorial Diameter:</td>      <td>6,792 km</td>    </tr>    <tr>      <td>Polar Diameter:</td>      <td>6,752 km</td>    </tr>    <tr>      <td>Mass:</td>      <td>6.39 × 10^23 kg (0.11 Earths)</td>    </tr>    <tr>      <td>Moons:</td>      <td>2 (Phobos &amp; Deimos)</td>    </tr>    <tr>      <td>Orbit Distance:</td>      <td>227,943,824 km (1.38 AU)</td>    </tr>    <tr>      <td>Orbit Period:</td>      <td>687 days (1.9 years)</td>    </tr>    <tr>      <td>Surface Temperature:</td>      <td>-87 to -5 °C</td>    </tr>    <tr>      <td>First Record:</td>      <td>2nd millennium BC</td>    </tr>    <tr>      <td>Recorded By:</td>      <td>Egyptian astronomers</td>    </tr>  </tbody></table>


<!-- soup.find_all("a")
soup("a") -->
<!-- 
# manny code
# scraping = True
# data = []
# while scraping==True:
#     soup = BeautifulSoup(browser.html, "lxml")
#     books = soup.find_all("article", class_="product_pod")
#     for book in books:
#         link = book.find("h3").find("a")["href"]
#         title = book.find("h3").find("a")["title"]
#         data.append({"link": link, "title": title})
#     try:
#         browser.click_link_by_partial_text('next')
#     except:
#         scraping = False -->


<table border="1" class="dataframe">\n  <tbody>\n    <tr>\n      <td>Equatorial Diameter:</td>\n      <td>6,792 km</td>\n    </tr>\n    <tr>\n      <td>Polar Diameter:</td>\n      <td>6,752 km</td>\n    </tr>\n    <tr>\n      <td>Mass:</td>\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n    </tr>\n    <tr>\n      <td>Moons:</td>\n      <td>2 (Phobos &amp; Deimos)</td>\n    </tr>\n    <tr>\n      <td>Orbit Distance:</td>\n      <td>227,943,824 km (1.38 AU)</td>\n    </tr>\n    <tr>\n      <td>Orbit Period:</td>\n      <td>687 days (1.9 years)</td>\n    </tr>\n    <tr>\n      <td>Surface Temperature:</td>\n      <td>-87 to -5 °C</td>\n    </tr>\n    <tr>\n      <td>First Record:</td>\n      <td>2nd millennium BC</td>\n    </tr>\n    <tr>\n      <td>Recorded By:</td>\n      <td>Egyptian astronomers</td>\n    </tr>\n  </tbody>\n</table>'


<table border="1" class="dataframe">  <tbody>    <tr>      <td>Equatorial Diameter:</td>      <td>6,792 km</td>    </tr>    <tr>      <td>Polar Diameter:</td>      <td>6,752 km</td>    </tr>    <tr>      <td>Mass:</td>      <td>6.39 × 10^23 kg (0.11 Earths)</td>    </tr>    <tr>      <td>Moons:</td>      <td>2 (Phobos &amp; Deimos)</td>    </tr>    <tr>      <td>Orbit Distance:</td>      <td>227,943,824 km (1.38 AU)</td>    </tr>    <tr>      <td>Orbit Period:</td>      <td>687 days (1.9 years)</td>    </tr>    <tr>      <td>Surface Temperature:</td>      <td>-87 to -5 °C</td>    </tr>    <tr>      <td>First Record:</td>      <td>2nd millennium BC</td>    </tr>    <tr>      <td>Recorded By:</td>      <td>Egyptian astronomers</td>    </tr>  </tbody></table>