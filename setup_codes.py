#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Green World

Created on Wed Mar  9 13:56:48 2022

@author: shiqimeng
"""
# Run in command line
# Install Pelican
# pip install "pelican[markdown]"

# Change directory
cd /Users/shiqimeng/Desktop/GreenWorld

# Skeleton project
# pelican-quickstart

# Save file as markdown

# Generate site
pelican -s pelicanconf.py content -t themes/pelican-fh5co-marble/

# Preview site
cd /Users/shiqimeng/Desktop/GreenWorld/output
python -m pelican.server

# http://localhost:8000/ 

