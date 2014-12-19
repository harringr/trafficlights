##README

generate_tl.py is a short Python script to calculate nutrition traffic light data for fat, saturated fat, sugar and salt, as can be seen on the front of packs of many foods (especially pre-packaged foods in the UK/Ireland).  See [p14 of this Department of Health document](https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/300886/2902158_FoP_Nutrition_2014.pdf) for more details.
 
Usage of standalone script:

```python

import generate_tl as tl

def generate_food_data():

  data = {
    'type': 'food',
    'size_g': 400,
    'serving_size': '1/2 pizza',
    'fat': {
      'serving_g': 16.9,
      'hundred_g': 4.5,
    },
    'sat': {
      'serving_g': 4.5,
      'hundred_g': 1.2,
    },
    'sugar': {
      'serving_g': 12.8,
      'hundred_g': 3.4,
    },
    'salt': {
      'serving_g': 1.6,
      'hundred_g': 0.4,
    }
  }

  return data

def main():

  # Define data for the food you want to analyse / convert to traffic lights
  food_data = generate_food_data()

  # Get the traffic light limits
  nutrition_data = tl.define_limits()

  # Generate the traffic light data
  tl.generate_tl(nutrition_data, food_data)

if __name__ == '__main__':
  main()
```

Alternatively, you can use a REST API

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