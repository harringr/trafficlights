#!/usr/bin/env python
# -*- coding: utf-8 -*-


import generate_tl as tl


"""Test type of data structures"""
def test_limit_datatypes():
        
    limit_data = tl.define_limits()

    assert isinstance(limit_data, dict)
    assert isinstance(limit_data['food'], dict)


"""Test num items in dictionary"""
def test_limit_datasizes():

    limit_data = tl.define_limits()

    assert len(limit_data['food']) == 4


"""Test some contents"""
def test_limit_data_content():

    limit_data = tl.define_limits()

    assert limit_data['food']['fat']['serving'] == 21
    assert limit_data['food']['sugar']['lower'] == 5
    assert limit_data['food']['salt']['upper'] == 1.5
    assert limit_data['drink']['fat']['serving'] == 10.5
    assert limit_data['drink']['fat']['upper'] == 8.75
    assert limit_data['drink']['fat']['lower'] == 1.5

# Function to calculate a single traffic light is defined as... 
# generate_single_tl(serving_value, hundred_value, serving_limit, upper_limit, lower_limit)


"""Fat - Red according to serving"""
def test_single_tl_fat_red_by_serving():
    
    tl_colour = tl.generate_single_tl(21.1, 3, 21, 17.5, 3.0)
    assert tl_colour == 'Red'


"""Fat - Red according to per_100"""
def test_single_tl_fat_red():

    tl_colour = tl.generate_single_tl(21, 17.6, 21, 17.5, 3.0)
    assert tl_colour == 'Red'


"""Fat - Amber according to per_100"""
def test_single_tl_fat_amber():

    tl_colour = tl.generate_single_tl(21, 17.5, 21, 17.5, 3.0)
    assert tl_colour == 'Amber'


"""Fat - Green according to per_100"""
def test_single_tl_fat_green():

    tl_colour = tl.generate_single_tl(21, 3.0, 21, 17.5, 3.0)
    assert tl_colour == 'Green'


"""Sat - Red according to serving"""
def test_single_tl_sat_red_by_serving():
    
    tl_colour = tl.generate_single_tl(6.1, 5, 6, 5, 1.5)
    assert tl_colour == 'Red'


"""Sat - Red according to per_100"""
def test_single_tl_sat_red():

    tl_colour = tl.generate_single_tl(6, 5.1, 6, 5, 1.5)
    assert tl_colour == 'Red'


"""Sat - Amber according to per_100"""
def test_single_tl_sat_amber():

    tl_colour = tl.generate_single_tl(6, 5, 6, 5, 1.5)
    assert tl_colour == 'Amber'


"""Sat - Green according to per_100"""
def test_single_tl_sat_green():

    tl_colour = tl.generate_single_tl(6, 1.5, 6, 5, 1.5)
    assert tl_colour == 'Green'


"""Sugar - Red according to serving"""
def test_single_tl_sug_red_by_serving():
    
    tl_colour = tl.generate_single_tl(27.1, 22, 27, 5, 22.5)
    assert tl_colour == 'Red'


"""Sugar - Red according to per_100"""
def test_single_tl_sug_red():

    tl_colour = tl.generate_single_tl(27, 22.51, 27, 22.5, 5)
    assert tl_colour == 'Red'


"""Sugar - Amber according to per_100"""
def test_single_tl_sug_amber():

    tl_colour = tl.generate_single_tl(27, 5.1, 27, 22.5, 5)
    assert tl_colour == 'Amber'


"""Sugar - Green according to per_100"""
def test_single_tl_sug_green():

    tl_colour = tl.generate_single_tl(25, 5, 27, 22.5, 5)
    assert tl_colour == 'Green'


"""Salt - Red according to serving"""
def test_single_tl_salt_red_by_serving():
    
    tl_colour = tl.generate_single_tl(1.81, 1.4, 1.8, 1.5, 0.3)
    assert tl_colour == 'Red'


"""Salt - Red according to per_100"""
def test_single_tl_salt_red():

    tl_colour = tl.generate_single_tl(1.8, 1.51, 1.8, 1.5, 0.3)
    assert tl_colour == 'Red'


"""Salt - Amber according to per_100"""
def test_single_tl_salt_amber():

    tl_colour = tl.generate_single_tl(1.8, 1.5, 1.8, 1.5, 0.3)
    assert tl_colour == 'Amber'


"""Salt - Green according to per_100"""
def test_single_tl_salt_green():

    tl_colour = tl.generate_single_tl(1.8, 0.3, 1.8, 1.5, 0.3)
    assert tl_colour == 'Green'
