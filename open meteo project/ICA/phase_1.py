# Author: <Your name here>
# Student ID: <Your Student ID>

import sqlite3

# Phase 1 - Starter
# 
# Note: Display all real/float numbers to 2 decimal places.

'''
Satisfactory
'''


def select_all_countries(connection):
    # Queries the database and selects all the countries 
    # stored in the countries table of the database.
    # The returned results are then printed to the 
    # console.
    try:
        # Define the query
        query = "SELECT * from [countries]"

        # Get a cursor object from the database connection
        # that will be used to execute database query.
        cursor = connection.cursor()

        # Execute the query via the cursor object.
        results = cursor.execute(query)

        # Iterate over the results and display the results.
        for row in results:
            print(f"Country Id: {row['id']} -- Country Name: {row['name']} -- Country Timezone: {row['timezone']}")

    except sqlite3.OperationalError as ex:
        print(ex)


def select_all_cities(connection):
    try:
        # Define the query
        query = "SELECT * from [cities]"

        # Get a cursor object from the database connection
        # that will be used to execute database query.
        cursor = connection.cursor()

        # Execute the query via the cursor object.
        results = cursor.execute(query)

        # Iterate over the results and display the results.
        for row in results:
            print(f"City Id: {row['id']} -- City Name: {row['name']} -- Longitude: {row['longitude']} -- Latitude: {row['latitude']} -- Country Id: {row['country_id']}")

    except sqlite3.OperationalError as ex:
        print(ex)


'''
Good
'''


def average_annual_temperature(connection, city_id, year):
    try:
        # Define the query
        query = f"SELECT AVG(mean_temp) AS average_annual_temperature FROM [daily_weather_entries] WHERE city_id = {city_id} AND SUBSTR(date, 1, 4) = '{year}'"

        # Get a cursor object from the database connection
        # that will be used to execute database query.
        cursor = connection.cursor()

        # Execute the query via the cursor object.
        results = cursor.execute(query)

        # Iterate over the results and display the results.
        for row in results:
            print(f"Average Annual Temperature: {float('%.2f' % row['average_annual_temperature'])}")

    except sqlite3.OperationalError as ex:
        print(ex)


def average_seven_day_precipitation(connection, city_id, start_date):
    try:
        # Define the query
        query = f"SELECT * FROM [daily_weather_entries] WHERE city_id = {city_id} AND date >= '{start_date}' AND date <  DATE('{start_date}', '+7 days') ORDER BY date ASC"

        # Get a cursor object from the database connection
        # that will be used to execute database query.
        cursor = connection.cursor()

        # Execute the query via the cursor object.
        results = cursor.execute(query)

        # Iterate over the results and display the results.
        for row in results:
            print(f"Date: {row['date']} -- City Id: {row['city_id']} -- Precipitation: {row['precipitation']}")

    except sqlite3.OperationalError as ex:
        print(ex)

'''
Very good
'''


def average_mean_temp_by_city(connection, date_from, date_to):
    try:
        # Define the query
        query = f"SELECT city_id, avg(mean_temp) AS average_mean_temp FROM [daily_weather_entries] WHERE date >= '{date_from}' AND date < '{date_to}' GROUP BY city_id"

        # Get a cursor object from the database connection
        # that will be used to execute database query.
        cursor = connection.cursor()

        # Execute the query via the cursor object.
        results = cursor.execute(query)

        # Iterate over the results and display the results.
        for row in results:
            print(f"City Id: {row['city_id']} -- Average Mean Temp : {float('%.2f' % row['average_mean_temp'])}")

    except sqlite3.OperationalError as ex:
        print(ex)


def average_annual_precipitation_by_country(connection, year):
    try:
        # Define the query
        query = f"SELECT c.country_id, co.name, avg(precipitation)  as average_annual_precipitation FROM [daily_weather_entries] e JOIN [cities] c ON c.id = e.city_id JOIN [countries] co ON co.id = c.country_id WHERE SUBSTR(date, 1, 4) = '{year}' GROUP BY c.country_id, co.name"

        # Get a cursor object from the database connection
        # that will be used to execute database query.
        cursor = connection.cursor()

        # Execute the query via the cursor object.
        results = cursor.execute(query)

        # Iterate over the results and display the results.
        for row in results:
            print(f"Year: {year} -- Country Id: {row['country_id']} -- Country Name: {row['name']} -- Average Annual Precipitation: {float('%.2f' % row['average_annual_precipitation'])}")

    except sqlite3.OperationalError as ex:
        print(ex)


'''
Excellent

You have gone beyond the basic requirements for this aspect.

'''

if __name__ == "__main__":
    # Create a SQLite3 connection and call the various functions
    # above, printing the results to the terminal.
    connection = sqlite3.connect('CIS4044-N-SDI-OPENMETEO-PARTIAL.db')
    connection.row_factory = sqlite3.Row

    print("\n\n------ select_all_countries -------")
    select_all_countries(connection)

    print("\n\n------ select_all_cities -------")
    select_all_cities(connection)

    print("\n\n------ average_annual_temperature(city_id = 1, year = 2000) -------")
    average_annual_temperature(connection, 1, "2000")

    print("\n\n------ average_seven_day_precipitation(city_id = 1, start_date = 2000-01-01) -------")
    average_seven_day_precipitation(connection, 1, "2000-01-01")

    print("\n\n------ average_mean_temp_by_city(date_from = 2000-01-01, date_to = 2000-01-10) -------")
    average_mean_temp_by_city(connection, "2000-01-01", "2000-01-10")

    print("\n\n------ average_annual_precipitation_by_country(year = 2000) -------")
    average_annual_precipitation_by_country(connection, "2000")
