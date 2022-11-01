import psycopg2
from psycopg2 import Error
from flask import Flask, render_template
import util

app = Flask(__name__)

username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

@app.route('/api/update_basket_a')
# this is how you define a function in Python
def update():
    
    cursor, connection = util.connect_to_db(username,password,host,port,database)

    try:
        cursor.execute("INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry');")
        util.disconnect_from_db(connection,cursor)
        return "sucess!"
    except (Exception, Error) as error:
        return error
        util.disconnect_from_db(connection,cursor)


@app.route('/api/unique')    
def table():

    cursor, connection = util.connect_to_db(username,password,host,port,database)

    record = util.run_and_fetch_sql(cursor, "SELECT fruit_a FROM basket_a UNION SELECT fruit_b FROM basket_b")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        col_names = [desc[0] for desc in cursor.description]
    
    


    return render_template('index.html', sql_table = record, table_title=col_names)


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
