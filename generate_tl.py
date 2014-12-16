#!/usr/bin/env python

import sys
from pprint import pprint

def check_data(data):
  # Do some typechecking here?
  # Else catch in try / except 
  print "\nChecking data"

def generate_single_tl(serving_value, hundred_value, serving_limit, upper_limit, lower_limit):
  
  try:
    if serving_value > serving_limit:
      return 'Red'
    else:
      if hundred_value > serving_limit:
        return 'Red'
      elif hundred_value <= lower_limit:
        return 'Green'
      else:
        return 'Amber'
  except:
    # Insert proper error checking here
    print "Error in calculating"

def generate_tl(tl_data, nt_data):

  tl = tl_data[nt_data['type']]

  colours = {}

  for l in tl:
    colours[l.title()] = generate_single_tl(
      nt_data[l]['serving_g'], 
      nt_data[l]['hundred_g'], 
      tl[l]['serving'], 
      tl[l]['upper'], 
      tl[l]['lower']
      )
    
  print_tl(colours, False)
  return colours

def print_tl(tl_colours, labels=True):
  if labels:
    print "Fat: %s, Sat: %s, Sugar: %s, Salt: %s" % (
      tl_colours['Fat'], 
      tl_colours['Sat'], 
      tl_colours['Sugar'], 
      tl_colours['Salt']
      )
  else:
    print "%s %s %s %s" % (
      tl_colours['Fat'][0][:1],
      tl_colours['Sat'][0][:1],
      tl_colours['Sugar'][0][:1],
      tl_colours['Salt'][0][:1]
      )

def define_limits():

  data = {
    'food': {
      'fat': {
        'serving': 21,
        'upper': 17.5,
        'lower': 3 
      },
      'sat': {
        'serving': 6,
        'upper': 5,
        'lower': 1.5
      },
      'sugar': {
        'serving': 27,
        'upper': 22.5,
        'lower': 5
      },
      'salt': {
        'serving': 1.8,
        'upper': 1.5,
        'lower': 0.3
      }
    },
    'drink': {
      'fat': {
        'serving': 10.5,
        'upper': 8.75,
        'lower': 1.5 
      },
      'sat': {
        'serving': 3,
        'upper': 2.5,
        'lower': 0.75
      },
      'sugar': {
        'serving': 13.5,
        'upper': 11.25,
        'lower': 2.5
      },
      'salt': {
        'serving': 0.9,
        'upper': 0.75,
        'lower': 0.3
      }
    }
  }

  return data
