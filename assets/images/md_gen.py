"""
A quick script to generate markdown for the gallery section of the web site from images (all files) in the assets directory 

Organized files with random dates by folder. Files in folders must be uniquely named. Manual clean up of non image files required.

Saves markdown in _posts directory
"""
from os import walk
import datetime
import random 

def gen_date(
    start_date = datetime.date(2020, 2, 1), 
    end_date = datetime.date(2020, 5, 7) 
    ):
    """Genearte and stringify random date btw range"""
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    random_date_string = random_date.strftime("%Y-%m-%d") 
    return random_date_string

f = []
path = "./"
save_path = "/Users/chriscorrell/Documents/Programming/earring_project_site/barber-jekyll/_posts/"
for (dirpath, dirnames, filenames) in walk(path):
    s_path = dirpath
    date = gen_date()
    print(s_path)
    print(filenames)
    for fn in filenames:
        txt = f"""--- 
layout: post
title: "" 
description:
image: /assets/images{dirpath[1:]}/{fn}
author: Chris Correll
tags: 
--- """
        fn_bare = fn.split(".")[0]
        if fn_bare != "":
            fn = date+"-"+fn_bare+".markdown"
            print(fn)
        text_file = open(save_path+fn, "w")
        n = text_file.write(txt)
        text_file.close()
