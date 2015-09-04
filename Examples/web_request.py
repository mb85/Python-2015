#!/usr/bin/env python3
# coding: utf-8

import urllib.request
import urllib.parse

# Our base URL
url = "http://www.website.com"

# The data we wish to send to the server
data = {
    "firstName": "Mark",
    "lastName": "Blows",
    "occupation": "Teacher",
    "sex": "Male",
    "birthDate": "30/08/1985"
}

# Encode the data in GET url format
parameters = urllib.parse.urlencode(data)

# The full url, now with parameters at the end
full_url = "?".join([url, parameters])
print(full_url)

