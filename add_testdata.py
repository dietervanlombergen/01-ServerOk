from data import add_server

websites = [
    {"name": "Google", "hostname": "www.google.com"},
    {"name": "YouTube", "hostname": "www.youtube.com"},
    {"name": "Facebook", "hostname": "www.facebook.com"},
    {"name": "Amazon", "hostname": "www.amazon.com"},
    {"name": "Twitter", "hostname": "www.twitter.com"},
    {"name": "Instagram", "hostname": "www.instagram.com"},
    {"name": "LinkedIn", "hostname": "www.linkedin.com"},
    {"name": "Reddit", "hostname": "www.reddit.com"},
    {"name": "Netflix", "hostname": "www.netflix.com"},
    {"name": "eBay", "hostname": "www.ebay.com"},
    {"name": "Microsoft", "hostname": "www.microsoft.com"},
    {"name": "Wikipedia", "hostname": "en.wikipedia.org"},
    {"name": "Yahoo", "hostname": "www.yahoo.com"},
    {"name": "Apple", "hostname": "www.apple.com"},
    {"name": "WhatsApp", "hostname": "www.whatsapp.com"},
    {"name": "Pinterest", "hostname": "www.pinterest.com"},
    {"name": "Spotify", "hostname": "www.spotify.com"},
    {"name": "Airbnb", "hostname": "www.airbnb.com"},
    {"name": "Adobe", "hostname": "www.adobe.com"},
    {"name": "IMDb", "hostname": "www.imdb.com"}
]



for server in websites:
    add_server(server["name"], server["hostname"])