#!/usr/bin/python3
"""Lists all cities of a specific state from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset='utf8'
    )

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    try:
        # Prepare SQL query to select cities of the given state
        sql_query = "SELECT GROUP_CONCAT(name SEPARATOR ', ') FROM cities \
                     INNER JOIN states ON cities.state_id = states.id \
                     WHERE states.name = %s ORDER BY cities.id ASC"
        
        # Execute the SQL command with the state name as parameter
        cursor.execute(sql_query, (state_name,))

        # Fetch the result
        result = cursor.fetchone()

        # Print the result
        if result[0]:
            print(result[0])

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the database connection
        db.close()
