import psycopg2

class Database:
    def __init__(self):
        """
        Initialization
        """
        self.conn = None
        self.cur = None

    def connect(self):
        """
        connect to the postgreSQL
        """
        self.conn =  psycopg2.connect("dbname=postgres user=postgres password=509624")
        self.cur = self.conn.cursor()

    def insert_initial_data(self):
        """
        It inserts initial data
        """
        self.insert(person_id= 1, person_name='john', person_age= 20)
        self.insert(person_id= 2, person_name='Paul', person_age=22)
        self.insert(person_id= 3, person_name='Ann', person_age=19)

    def print(self):
        """
        It prints all of the table rows
        """
        # Execute a query
        self.cur.execute("SELECT * FROM person")

        # Retrieve query results
        records = self.cur.fetchall()

        print('ID\tName\tAge')
        for record in records:
            print('%d\t%s\t%d' % record)

    def insert(self,person_id: int, person_age: int, person_name: str):
        """
        it inserts a row into the table
        :param person_id: id of a person
        :param person_age: age of a person
        :param person_name: name of a person
        """

        self.cur.execute("insert into person(id,age,name) values(%s,%s,'%s')" % (person_id, person_age, person_name))
        self.conn.commit()

    def delete(self, person_id):
        """
        It deletes a row from the table
        :param person_id: id of a person to table
        """
        self.cur.execute("delete from person where id=%d" % person_id)
        self.conn.commit()

    def delete_all(self):
        """
        it deletes all rows from the table
        """
        self.cur.execute("delete from person")
        self.conn.commit()