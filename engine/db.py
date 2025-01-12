import sqlite3

conn = sqlite3.connect("jarvis.db")

cursor = conn.cursor()
'''
query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)
# query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"

queries = [
    "INSERT INTO web_command VALUES (null, 'youtube', 'https://www.youtube.com/')",
    "INSERT INTO web_command VALUES (null, 'google', 'https://www.google.com/') ",
    "INSERT INTO web_command VALUES (null, 'facebook', 'https://www.facebook.com/') ",
    "INSERT INTO web_command VALUES (null, 'twitter', 'https://www.twitter.com/') ",
    "INSERT INTO web_command VALUES (null, 'instagram', 'https://www.instagram.com/') ",
    "INSERT INTO web_command VALUES (null, 'linkedin', 'https://www.linkedin.com/') ",
    "INSERT INTO web_command VALUES (null, 'reddit', 'https://www.reddit.com/') ",
    "INSERT INTO web_command VALUES (null, 'wikipedia', 'https://www.wikipedia.org/') ",
    "INSERT INTO web_command VALUES (null, 'amazon', 'https://www.amazon.com/') ",
    "INSERT INTO web_command VALUES (null, 'netflix', 'https://www.netflix.com/') ",
    "INSERT INTO web_command VALUES (null, 'github', 'https://www.github.com/') ",
    "INSERT INTO web_command VALUES (null, 'stackoverflow', 'https://stackoverflow.com/') ",
    "INSERT INTO web_command VALUES (null, 'medium', 'https://medium.com/') ",
    "INSERT INTO web_command VALUES (null, 'quora', 'https://www.quora.com/') ",
    "INSERT INTO web_command VALUES (null, 'pinterest', 'https://www.pinterest.com/') ",
    "INSERT INTO web_command VALUES (null, 'bing', 'https://www.bing.com/') ",
    "INSERT INTO web_command VALUES (null, 'yahoo', 'https://www.yahoo.com/') ",
    "INSERT INTO web_command VALUES (null, 'ebay', 'https://www.ebay.com/') ",
    "INSERT INTO web_command VALUES (null, 'nytimes', 'https://www.nytimes.com/') ",
    "INSERT INTO web_command VALUES (null, 'cnn', 'https://www.cnn.com/') ",
    "INSERT INTO web_command VALUES (null, 'bbc', 'https://www.bbc.com/') ",
    "INSERT INTO web_command VALUES (null, 'huffpost', 'https://www.huffpost.com/') ",
    "INSERT INTO web_command VALUES (null, 'espn', 'https://www.espn.com/') ",
    "INSERT INTO web_command VALUES (null, 'imdb', 'https://www.imdb.com/') ",
    "INSERT INTO web_command VALUES (null, 'flickr', 'https://www.flickr.com/') ",
    "INSERT INTO web_command VALUES (null, 'tumblr', 'https://www.tumblr.com/') ",
    "INSERT INTO web_command VALUES (null, 'dropbox', 'https://www.dropbox.com/') ",
    "INSERT INTO web_command VALUES (null, 'spotify', 'https://www.spotify.com/') ",
    "INSERT INTO web_command VALUES (null, 'soundcloud', 'https://www.soundcloud.com/') ",
    "INSERT INTO web_command VALUES (null, 'twitch', 'https://www.twitch.tv/') ",
    "INSERT INTO web_command VALUES (null, 'discord', 'https://www.discord.com/') ",
    "INSERT INTO web_command VALUES (null, 'skype', 'https://www.skype.com/') ",
    "INSERT INTO web_command VALUES (null, 'zoom', 'https://www.zoom.us/') ",
    "INSERT INTO web_command VALUES (null, 'whatsapp', 'https://www.whatsapp.com/') ",
    "INSERT INTO web_command VALUES (null, 'telegram', 'https://www.telegram.org/') ",
    "INSERT INTO web_command VALUES (null, 'slack', 'https://www.slack.com/') ",
    "INSERT INTO web_command VALUES (null, 'asana', 'https://www.asana.com/') ",
    "INSERT INTO web_command VALUES (null, 'trello', 'https://www.trello.com/') ",
    "INSERT INTO web_command VALUES (null, 'airbnb', 'https://www.airbnb.com/') ",
    "INSERT INTO web_command VALUES (null, 'booking', 'https://www.booking.com/') ",
    "INSERT INTO web_command VALUES (null, 'tripadvisor', 'https://www.tripadvisor.com/') ",
    "INSERT INTO web_command VALUES (null, 'expedia', 'https://www.expedia.com/') ",
    "INSERT INTO web_command VALUES (null, 'uber', 'https://www.uber.com/') ",
    "INSERT INTO web_command VALUES (null, 'lyft', 'https://www.lyft.com/') ",
    "INSERT INTO web_command VALUES (null, 'microsoft', 'https://www.microsoft.com/') ",
    "INSERT INTO web_command VALUES (null, 'apple', 'https://www.apple.com/') ",
    "INSERT INTO web_command VALUES (null, 'samsung', 'https://www.samsung.com/') ",
    "INSERT INTO web_command VALUES (null, 'adobe', 'https://www.adobe.com/') ",
    "INSERT INTO web_command VALUES (null, 'intel', 'https://www.intel.com/') ",
    "INSERT INTO web_command VALUES (null, 'amd', 'https://www.amd.com/') ",
    "INSERT INTO web_command VALUES (null, 'nvidia', 'https://www.nvidia.com/') ",
    "INSERT INTO web_command VALUES (null, 'oracle', 'https://www.oracle.com/') ",
    "INSERT INTO web_command VALUES (null, 'ibm', 'https://www.ibm.com/') ",
    "INSERT INTO web_command VALUES (null, 'salesforce', 'https://www.salesforce.com/') ",
    "INSERT INTO web_command VALUES (null, 'shopify', 'https://www.shopify.com/') ",
    "INSERT INTO web_command VALUES (null, 'aliexpress', 'https://www.aliexpress.com/') ",
    "INSERT INTO web_command VALUES (null, 'etsy', 'https://www.etsy.com/') ",
    "INSERT INTO web_command VALUES (null, 'walmart', 'https://www.walmart.com/') ",
    "INSERT INTO web_command VALUES (null, 'target', 'https://www.target.com/') ",
    "INSERT INTO web_command VALUES (null, 'bestbuy', 'https://www.bestbuy.com/') ",
    "INSERT INTO web_command VALUES (null, 'homedepot', 'https://www.homedepot.com/') ",
    "INSERT INTO web_command VALUES (null, 'lowes', 'https://www.lowes.com/') ",
    "INSERT INTO web_command VALUES (null, 'costco', 'https://www.costco.com/') ",
    "INSERT INTO web_command VALUES (null, 'ikea', 'https://www.ikea.com/') ",
    "INSERT INTO web_command VALUES (null, 'alibaba', 'https://www.alibaba.com/') ",
    "INSERT INTO web_command VALUES (null, 'booking', 'https://www.booking.com/') "
]
for query in queries:
    cursor.execute(query)
    print(query)
conn.commit()
'''



query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO sys_command VALUES (null,'pro soccer', 'C:\\Users\\yass3\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\KONAMI\\Pro Evolution Soccer 6 DEMO\\Pro Evolution Soccer 6 DEMO.lnk')"
cursor.execute(query)
conn.commit()

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
#cursor.execute(query)
'''
query = "INSERT INTO sys_command VALUES (null,'youtube', 'https://www.youtube.com/')"
cursor.execute(query)
conn.commit()'''
