#!/usr/bin/env python

from pprint import pprint
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

  nutrition_data = tl.define_limits()
  food_data = generate_food_data()
  tl.generate_tl(nutrition_data, food_data)

  print "\nFinished\n"

if __name__ == '__main__':
  main()