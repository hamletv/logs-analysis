#!/usr/bin/python2.7

# Report 1 - what are the most popular three articles of all time?
# Report 2 - who are the most popular article authors of all time?
# Report 3 - on which days did more than 1% of requests lead to errors?

import psycopg2 as psy


def getTopThreeArticles():

    db_query1 = '''
    SELECT articles.title, COUNT(log.method) AS views
    FROM articles, log WHERE '/article/' || articles.slug = log.path
    GROUP BY articles.title
    ORDER BY views DESC LIMIT 3;
    '''

    db = psy.connect(database = "news")
    db_cursor = db.cursor()
    db_cursor.execute(db_query1)
    query_result = db_cursor.fetchall()
    for result in query_result:
        print(result[0] + " - " + str(result[1]) + " views")

    db_cursor.close()
    db.close()

def getPopularAuthors():

    db_query2 = '''
    SELECT authors.name, COUNT(log.status) AS views
    FROM authors JOIN articles ON authors.id = articles.author
    JOIN log ON '/article/' || articles.slug = log.path
    AND log.status = '200 OK'
    GROUP BY authors.name
    ORDER BY views DESC;
    '''

    db = psy.connect(database = "news")
    db_cursor = db.cursor()
    db_cursor.execute(db_query2)
    query_result = db_cursor.fetchall()
    for result in query_result:
        print(result[0] + " - " + str(result[1]) + " views")

    db_cursor.close()
    db.close()

def getDaysErrors():

    db_query3 = '''
    SELECT authors.name, COUNT(log.status = '200 OK') AS views
    FROM authors JOIN articles ON authors.id = articles.author
    JOIN log ON '/article/' || articles.slug = log.path
    GROUP BY authors.name
    ORDER BY views DESC;
    '''

    db = psy.connect(database = "news")
    db_cursor = db.cursor()
    db_cursor.execute(db_query3)
    query_result = db_cursor.fetchall()
    for result in query_result:
        print(result[0] + " - " + str(result[1]) + " views")

    db_cursor.close()
    db.close()

if __name__ == "__main__":
    getTopThreeArticles()
    getPopularAuthors()
    getDaysErrors()
