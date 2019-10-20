#Imports & Dependencies
# !pip install selenium
# !pip install splinter
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests


# # Step 1 - Scraping.
# * This notebook is used for all scraping and analysis

def mars_rescrape():

    # Choose the executable path to driver 
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)


    # ## NASA Mars News
    # * Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text.
    # * Assign the text to variables that will be referenced later.


    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")



    # article = soup.find("div", class_='list_text')
    news_title = soup.find("div", class_="content_title").text
    news_p = soup.find("div", class_ ="article_teaser_body").text
    print(news_title)
    print(news_p)


    # # JPL Mars Space Images - Featured Image


    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    image = soup.find("img", class_="thumb")["src"]
    featured_image_url = "https://www.jpl.nasa.gov" + image
    print(featured_image_url)


    # ## Mars Weather
    # * Visit the Mars Weather twitter account and scrape the latest Mars weather tweet from the page. 
    # * Save the tweet text for the weather report as a variable called mars_weather.

    # Mars Weather Twitter
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)


    # HTML Object 
    html_weather = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_weather, 'html.parser')

    # Find all elements that contain tweets
    latest_tweets = soup.find_all('div', class_='js-tweet-text-container')

    # Retrieve all elements that contain news title in the specified range
    # Look for entries that display weather related words to exclude non weather related tweets 
    for tweet in latest_tweets: 
        weather_tweet = tweet.find('p').text
        if 'Sol' and 'pressure' in weather_tweet:
            print(weather_tweet)
            break
        else: 
            pass


    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)
    mars_data = pd.read_html(facts_url)
    mars_data_df = mars_data[0]
    mars_data_df.columns = ["Description", "Mars", "Earth"]
    mars_data_df.set_index("Description", inplace = True)
    mars_facts = mars_data_df.to_html()
    print(mars_facts)






    # Visit hemispheres website through splinter module 
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)


    # HTML Object
    html_hemispheres = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_hemispheres, 'html.parser')

    items = soup.find_all('div', class_='item')

    hemisphere_image_urls = []

    hemispheres_main_url = 'https://astrogeology.usgs.gov'

    # Loop through the items previously stored
    for i in items: 
        title = i.find('h3').text
        partial_img_url = i.find('a', class_='itemLink product-item')['href']
        browser.visit(hemispheres_main_url + partial_img_url)
        partial_img_html = browser.html
        soup = BeautifulSoup( partial_img_html, 'html.parser')
        img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
        hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
        

    browser.quit()

        # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "weather_tweet" : weather_tweet,
        "mars_facts" : mars_facts,
        "hiu" : hemisphere_image_urls
    }

    return mars_data

