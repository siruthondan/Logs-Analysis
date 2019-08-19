import psycopg2

try:  
    conn = psycopg2.connect("dbname='news'")
    curr = conn.cursor()

    print(" ")
    print('Top 3 Popular Articles:')
    curr.execute('SELECT title, count(log.id) as views FROM articles, log WHERE log.path = CONCAT(\'/article/\', articles.slug) GROUP BY articles.title ORDER BY views desc Limit 3;')
    rows = curr.fetchall()
    for row in rows:
        print('\t' + row[0] + ' - ' + str(row[1]) + ' views')

    print(" ")
    print('Most popular authors of all time:')
    curr.execute('SELECT authors.name,count(authors.id) as Views FROM articles, authors, log WHERE log.path = CONCAT(\'/article/\', articles.slug) and articles.author = authors.id Group By authors.name,authors.id Order By Views Desc;')
    rows = curr.fetchall()
    for row in rows:
        print('\t' + row[0] + ' - ' + str(row[1]) +' views')

    
        
    print(" ")
    print("Total error requests count on a day")
    curr.execute('SELECT to_char(time,\'DD-MON-YYYY\'),COUNT(to_char(time,\'DD-MON-YYYY\')) as count FROM log GROUP BY to_char(time,\'DD-MON-YYYY\') ORDER BY count desc')
    logcount = curr.fetchall()
    curr.execute('SELECT to_char(time,\'DD-MON-YYYY\'),COUNT(to_char(time,\'DD-MON-YYYY\')) as count FROM log WHERE Status = \'404 NOT FOUND\' GROUP BY to_char(time,\'DD-MON-YYYY\') ORDER BY count desc;')
    rows = curr.fetchall()
    for row in rows:
        for logg in logcount:
            if(row[0] == logg[0]):
               percen = round(100.0*row[1]/logg[1],2)
               if(percen > 1):
                    print('\t' + row[0] + ' - ' + str(row[1]) +' Bad Requests' + ' - ' + str(percen) + ' Percentage')
    print(" ")


except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

finally:
    if(conn):
        curr.close()
        conn.close()