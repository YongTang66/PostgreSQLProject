import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=postgres user=postgres password=509624")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM person")

# Retrieve query results
records = cur.fetchall()

print('ID\tName\tAge')
for record in records:
    print('%d\t%s\t%d' % record)

age = input("Enter an age: ")
cur.execute("SELECT * FROM person where age=%s" % age)
records = cur.fetchall()
print('ID\tName\tAge')
for record in records:
    print('%d\t%s\t%d' % record)

# insert data
person_id = input("Enter an id to insert: ")
person_age = input("Enter an age to insert: ")
person_name = input("Enter an name to insert: ")

cur.execute("insert into person(id,age,name) values(%s,%s,'%s')" % (person_id, person_age, person_name))
conn.commit()

cur.execute("SELECT * FROM person")
records = cur.fetchall()
print('ID\tName\tAge')
for record in records:
    print('%d\t%s\t%d' % record)