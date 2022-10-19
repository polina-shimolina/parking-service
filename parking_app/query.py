import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="password",
    db="parking"
)

c=db.cursor()
c.execute("INSERT INTO users (name, car) VALUES (%s, %s);", ('Дима', 'Е107КХ'))
db.commit()
c.close()
db.close()