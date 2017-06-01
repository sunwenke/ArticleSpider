import pymysql


conn = pymysql.connect(host='192.168.0.129', port=3306, user='root', password='198813', db='article_spider',charset='utf8', use_unicode=True)
cur = conn.cursor ()


cur.execute("insert into movie(title,url) values ('ab我._2012'),('www.sohu.com')")
conn.commit()
conn.close()

