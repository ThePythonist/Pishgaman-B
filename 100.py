import psycopg2

HOST = "localhost"
DATABASE = "test"
USER = "postgres"
PASSWORD ="pishgaman123"

connect = psycopg2.connect(dbname=DATABASE, user=USER, password=PASSWORD, host=HOST)
print("Connected")

cur = connect.cursor()

cur.execute("INSERT INTO person (f_name, l_name, gender, birth, country) VALUES ('Anne','Smith','Female',DATE'1988-01-02','USA');")
print("Done")
connect.commit()


cur.close()
connect.close()
