#!/usr/bin/python2.7

# Report 1 - what are the most popular three articles of all time?
# Report 2 - who are the most popular article authors of all time?
# Report 3 - on which days did more than 1% of requests lead to errors?

import psycopg2 as psy

def connectAccessDB(db_query):

    db = psy.connect(database = "news")
    db_cursor = db.cursor()
    db_cursor.execute(db_query)
    query_result = db_cursor.fetchall()
    db_cursor.close()
    db.close()
    return query_result

def getTopThreeArticles():

    db_query = '''
    SELECT articles.title, COUNT(log.method) AS views
    FROM articles, log WHERE '/article/' || articles.slug = log.path
    GROUP BY articles.title
    ORDER BY views DESC LIMIT 3;
    '''

    db_result = connectAccessDB(db_query)
    for result in db_result:
        print(result[0] + " - " + str(result[1]) + " views")

def getPopularAuthors():

    db_query = '''
    SELECT authors.name, COUNT(log.status) AS views
    FROM authors JOIN articles ON authors.id = articles.author
    JOIN log ON '/article/' || articles.slug = log.path
    AND log.status = '200 OK'
    GROUP BY authors.name
    ORDER BY views DESC;
    '''
    print('\n')
    db_result = connectAccessDB(db_query)
    for result in db_result:
        print(result[0] + " - " + str(result[1]) + " views")

def getDaysErrors():

    db_query = '''
    SELECT queries.date, (
        (errors.all_errors = 100.0/queries.all_queries)
    ) AS percent

    FROM (
        SELECT time::date AS date, COUNT(*) AS all_errors
        FROM log WHERE status = '404 NOT FOUND'
        GROUP BY time::date
    ) AS errors

    JOIN (
        SELECT time::date AS date, COUNT(*)
        AS all_queries
        FROM log
        GROUP BY time::date
    ) AS queries

    ON errors.date = queries.date
        WHERE (
        (errors.all_errors * 100.0/queries.all_queries) > 1.0
    )
    ORDER BY percent;
    '''
    print('\n')
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
