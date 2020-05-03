#!/usr/bin/env python2.7

import psycopg2
import bleach
import datetime


DBNAME = "news"
# What are the most popular three articles of all time


def get_topArticles():
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        get_SQL = "select art.title::varchar, views from \
        (select split_part(log.path,'/',3)\
        as top_three_articles, count (*)::int as views\
        from log group by log.path \
        order by views desc Limit 3) as a inner join \
        articles as art on art.slug = top_three_articles order by views desc;"
        c.execute(get_SQL)
        db.close
        return c.fetchall()
    except psycopg2.Error as e:
        print(e.pgerror)

# Who are the most popular article authors of all time?


def get_topAuthors():
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        get_SQL = " select aut.name, author_count from \
          (select art.author as authorid, sum(views)::int as author_count from\
          (select split_part(log.path,'/',3) as top_three_articles,\
          count (*) as views\
          from log group by log.path order by views desc) \
          as a inner join articles as art on art.slug = top_three_articles\
          group by art.author order by author_count desc) as a inner join\
          authors as aut on authorid =  aut.id;"
        c.execute(get_SQL)
        db.close
        return c.fetchall()
    except psycopg2.Error as e:
        print(e.pgerror)

# On which days did more than 1% of requests lead to errors?


def get_topBugs():
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        get_SQL = "select datelog, percent_daily_errors\
                  from (select datelog, \
                  (sum(numerrors)/sum(numhttpreq)*100)::real\
                  as percent_daily_errors from \
                  (select tot_req.datelog::date as datelog,\
                  err_req.numerrors as numerrors, \
                  tot_req.numhttprequests as numhttpreq\
                  from http_requests_per_day\
                  as tot_req, http_errors_per_day as err_req\
                  where tot_req.datelog = err_req.datelog) as subq \
                  group by datelog order by percent_daily_errors desc)\
                  as subq2\
                  where percent_daily_errors >1;"
        c.execute(get_SQL)
        db.close
        return c.fetchall()
    except psycopg2.Error as e:
        print(e.pgerror)

# Variables


articles = get_topArticles()
authors = get_topAuthors()
bugs = get_topBugs()


def _main():
    print("Top three articles of all time. \n")
    for article in articles:
        print("Article: " + article[0] + ", Views: " + str(article[1]))
    print('\n')
    print("Most popular article authors of all time. \n")
    for author in authors:
        print("Author: " + author[0] + ", Views: " + str(author[1]))
    print('\n')
    print("Days where site experienced >1% errors in server requests. \n")
    for bug in bugs:
        print(bug[0].strftime("%b %d %Y") + " " + str(round(bug[1], 2)) + "%")


_main()
