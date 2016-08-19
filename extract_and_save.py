#!/usr/bin/python

import datetime
import json
import sys
import urllib2

from pexif import JpegFile

TIME_FORMAT = '%Y:%m:%d %H:%M:%S'

obj = {}
with open(sys.argv[1]) as f:
    obj = json.loads(f.read())

for photo in obj['response']['photos']['items']:
    date = datetime.datetime.fromtimestamp(photo['createdAt'])
    loc = (photo['venue']['location']['lat'], photo['venue']['location']['lng'])
    print photo['venue']['name']

    url = "%soriginal%s" % (photo['prefix'], photo['suffix'])
    req = urllib2.Request(url)
    handler = urllib2.urlopen(req)

    ef = JpegFile.fromString(handler.read())

    exif = ef.get_exif()
    primary = exif.get_primary()

    ef.set_geo(loc[0], loc[1])
    primary.DateTime = date.strftime(TIME_FORMAT)

    ef.writeFile('photos/%s.jpg' % photo['id'])
