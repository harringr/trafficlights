##README

Usage:

```php

# Get the Flask server running
$ ./flask_api.py
* Running on http://127.0.0.1:5000/
* Restarting with reloader
 
```
Then use curl to make a POST request - returns array with traffic light data 

```php

$ curl http://localhost:5000/ -X POST -d 'type=food' -d 'size_g=100' -d 'fat_100=4.5' -d 'fat_serving=16.9' -d 'sat_100=1.2' -d 'sat_serving=4.5' -d 'sugar_100=3.4' -d 'sugar_serving=12.8'

{
    "tl_data": {
        "Fat": "Amber",
        "Salt": "Green",
        "Sat": "Green",
        "Sugar": "Green"
    }
}

```