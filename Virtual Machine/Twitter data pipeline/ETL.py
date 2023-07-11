# Import the snscrape library for accessing Twitter data
import snscrape.modules.twitter as sntwitter

# Import the pandas library for data manipulation and analysis
import pandas as pd

# Import the json library for working with JSON data
import json

# Import the datetime library for working with dates and times
from datetime import datetime

# Import the s3fs library for accessing data stored in Amazon S3
import s3fs

def  ETL_Datapipeline():
    # Creating list to append tweet data to
    attributes_container = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid since:2021-07-05 until:2022-07-06').get_items()):
        if i>150:
            break
        attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
        
    # Creating a dataframe to load the list
    tweets_df = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])
    
    #exports the  contents  of   tweets_df  to a CSV file
    df = tweets_df.to_csv('covid_data.csv')