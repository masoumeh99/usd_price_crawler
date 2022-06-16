# from itemadapter import ItemAdapter
import psycopg2


class UsdtoirtPipeline(object):

    # init method to initialize the database
    def __init__(self):

        # Creating connection to database
        self.create_connection()
          
        # calling method to create table
        self.create_table()


    def create_connection(self):

        self.conn = psycopg2.connect(
            host="localhost",
            database="kilidTest",
            user="postgres",
            password="2050954530")

        self.cure = self.conn.cursor()

    # Create table method using SQL commands to create table
    def create_table(self):

        self.cure.execute("""DROP TABLE IF EXISTS usd""")

        self.cure.execute("""create table usd(persionDate VARCHAR ( 255 ),
                                              latinDate date,
                                              changePercent float,
                                              changeAmount float,
                                              closeValue float,
                                              maxValue float,
                                              minValue float,
                                              openValue float)""") 


    def process_item(self, item, spider):

        self.store_in_db(item)

        #we need to return the item below as scrapy expects us to!
        return item

    def store_in_db(self, item):

        #store data in database table
        for i in range(len(item["persionDate"])):

            self.cure.execute(""" insert into usd values (%s,%s,%s,%s,%s,%s,%s,%s)""", (
                item["persionDate"][i],
                item["latinDate"][i],
                item["changePercent"][i],
                item["changeAmount"][i],
                item["closeValue"][i],
                item["maxValue"][i],
                item["minValue"][i],
                item["openValue"][i]
        ))

        #Commit the changes in the database
        self.conn.commit()

        #Closing the connection
        self.conn.close()
