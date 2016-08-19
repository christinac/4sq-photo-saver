# Saving 4sq photos with timestamps and geocodes

Ever think to yourself, "hm, I'd really like to get my photos out of Foursquare – preferably with the correct geocodes and timestamps?"

(Yeah, I might be the only one. But on the off chance I'm not ..)

This simple script:

1. Downloads photos from your Foursquare checkins
2. Puts their created date as the date at which you checked in
3. Places their geocode (lat/long) at the venue at which you checked in

It doesn't attempt to preserve or set any other exif data, though pull requests that do so are welcome!

## Libraries
You'll need to install [pexif](https://github.com/bennoleslie/pexif) in order to use this script. `pip install -r requirements.txt` will do.

## Data
I pulled my Foursquare photo checkin data from [Apigee](https://apigee.com/console/foursquare) and the `/users/{USER_ID}/photos` [endpoint]( https://developer.foursquare.com/docs/users/photos). If you've got more than 200 photo checkins, the `offset` and `limit` query params can help. The result limit on the photos endpoint is 200.

I then copy-pasted the json blobs into a text editor and saved them. (Yeah, I know, I know – though this didn't take more than 2 minutes and saved me an OAuth token dance.)

Beware: Foursquare doesn't escape double quotes in checkin shouts, if you happened to use them, which makes the json invalid. A [JSON linter](http://jsonlint.com/) can identify what you need to escape.

### Running the script
`python extract_and_save.py [filename]` (e.g `python extract_and_save.py photos.json`)
