#!/usr/bin/env python3

# Log Creator
# By: David Rosinski

import psycopg2

# The global variable for the main program loop
run = True


# Function to connect to the database and run query
def run_query(sql_query):
    try:
        db = psycopg2.connect("dbname=news")
        cursor = db.cursor()
        # Execute the query sent into the function
        cursor.execute(sql_query)
        data = cursor.fetchall()
        db.close()
        return data
    except Exception:
        print("There was an error connecting to the database, now exiting.")
        run = False


def selection_1():
    # Send query - What are 3 most popular articles?
    results = run_query('''select articles.title,
                            concat(count(*), ' Views')
                            from log
                            join articles
                            on replace(path, '/article/', '') = articles.slug
                            where path like '/article/%'
                            group by articles.title
                            order by count(*) desc
                            limit 3''')
    print("\n{0:^40} | {1:^15}".format("Title", "Views"))
    print("----------------------------------------------------------")
    for row in results:
        print(("{0:<40} | {1:>15}".format(*row)))


def selection_2():
    # Send query - Who are the most popular authors?
    results = run_query('''with tots as
                            (select replace(path, '/article/', '') as title,
                            count(*) as views
                            from log
                            where path like '/article/%'
                            group by path
                            order by count(*) desc)
                            select authors.name,
                            concat(sum(tots.views), ' Views')
                            from articles join tots
                            on articles.slug = tots.title
                            join authors on articles.author = authors.id
                            group by authors.name
                            order by sum(tots.views) desc
                            ''')

    print("\n{0:^30} | {1:^15}".format("Author", "Views"))
    print("------------------------------------------------")
    for row in results:
        print(("{0:<30} | {1:>15}".format(*row)))


def selection_3():
    # Send query - Wich day(s) did more than 1% requests lead to errors?
    results = run_query('''with error as
                            (select left(cast(time as text), 10) as date,
                            count(status) as total from log
                            where status like '4%'
                            group by date),
                            total as
                            (select left(cast(time as text), 10) as date,
                            count(status) as total from log group by date)
                            select error.date,
                            concat(cast((error.total * 100.0 / total.total)
                            as numeric(3,2)), '%')
                            from error join total on error.date = total.date
                            where (error.total * 100.0 / total.total) > 1
                            group by error.total, error.date, total.total
                            ''')
    print("\n{0:^15} | {1:^10}".format("Date", "Errors"))
    print("----------------------------")
    for row in results:
        print(("{0:<15} | {1:>10}".format(*row)))


def selection_4():
    global run
    print("Thank you for using the Log Creator")
    run = False    # Stops the main program loop.


# Define the dictionary for the menu selections
selections = {
    1: selection_1,
    2: selection_2,
    3: selection_3,
    4: selection_4,
    }


def main():
    while run:
        print("\nWelcome to the Log Creator!\n")
        print("Please select the log from the below options:")
        print("1. What are the most popular three articles of all time?")
        print("2. Who are the most popular article authors of all time?")
        print("3. On which days did more than 1% of requests lead to errors?")
        print("4. Exit the Log Creator.\n")

        # Get the menu selection from the user
        try:
            user_input = int(input("Log Selection: "))
            if (user_input > 0 and user_input < 5):
                selections[user_input]()
            else:
                raise    # Raise an exception to display error message
        except Exception:
            print("\n Please make your selection with 1-4.\n")


main()
