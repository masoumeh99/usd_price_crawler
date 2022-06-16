import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go


class Plot(object):

    # init method to initialize the database and
    def __init__(self):

        # Creating connection to database
        self.create_connection()


    def create_connection(self):

        self.conn = psycopg2.connect(
            host="localhost",
            database="kilidTest",
            user="postgres",
            password="2050954530")

        #Setting auto commit false
        self.conn.autocommit = True

        #Creating a cursor object using the cursor() method
        self.cursor = self.conn.cursor() 


    def retrieving(self, query):

        #Retrieving data
        self.cursor.execute(query)

        #Fetching all rows from the table
        result = self.cursor.fetchall()

        #Commit the changes in the database
        self.conn.commit()

        #Closing the connection
        self.conn.close()

        return result
    
    def plot(self, header, data):

        df = pd.DataFrame(data, columns=header)

        df.index = df["date"]

        df.sort_index(inplace=True)

        df['close_price'].plot()

        plt.show()

    

    def candlestickChart(self, header, data):

        df = pd.DataFrame(data, columns=header)
        
        fig = go.Figure(data=[go.Candlestick(x=df['date'],
                       open=df['openvalue'], high=df['maxvalue'],
                       low=df['minvalue'], close=df['closevalue'])])

        fig.show()




def __init__():

    plot = Plot()

    # There are 2 types of plots below, uncomment each one you want to see the plots


    # 1- Plot daily close prices
    data = plot.retrieving('''SELECT latindate, closevalue from usd''')
    plot.plot(['date', 'close_price'], data)

    # # 2- Plot daily candlestick chart
    # data = plot.retrieving('''SELECT latindate, openvalue, maxvalue, minvalue, closevalue from usd''')
    # plot.candlestickChart(['date', 'openvalue', 'maxvalue', 'minvalue', 'closevalue'], data)

__init__()