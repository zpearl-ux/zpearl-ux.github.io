"""Run once on your own computer: python download_images.py
Downloads every image used by the site from Squarespace into ./images (do this BEFORE cancelling Squarespace)."""
import json, os, urllib.request
here = os.path.dirname(os.path.abspath(__file__))
for url, name in json.load(open(os.path.join(here, 'images.json'))).items():
    dest = os.path.join(here, 'images', name)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        open(dest, 'wb').write(urllib.request.urlopen(req).read()); print('ok  ', name)
    except Exception as e:
        print('FAIL', name, e)
