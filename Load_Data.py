import mysql.connector
import Db_connection as DB
import pandas as pd

class Load_Date:
    def __init__(self):
        self.db = DB.Db_Connection()
        self.mycursor = self.db.connect_to_db()
    

    def load_data(self):

        try:
            df1 = pd.DataFrame()
            df = pd.ExcelFile('C:\\Users\\praka\\Downloads\\Bird_Monitoring_Data_GRASSLAND.XLSX')
            sheet_names = df.sheet_names            
            for i in sheet_names:
                    dataframe = pd.read_excel('C:\\Users\\praka\\Downloads\\Bird_Monitoring_Data_GRASSLAND.XLSX', sheet_name=i)
                    if len(dataframe) != 0:
                        df1['Distance'].fillna('FlyOver',inplace = True)
                        df1['ID_Method'].fillna('Visualization',inplace = True) # as this is fly over
                        df1 = pd.concat([df1, dataframe], ignore_index=True)
            
            self.InsertRD_fromDF(df1,'Grass')
            
            df1 = pd.DataFrame()
            df = pd.ExcelFile('C:\\Users\\praka\\Downloads\\Bird_Monitoring_Data_FOREST.XLSX')
            sheet_names = df.sheet_names            
            for i in sheet_names:
                    dataframe = pd.read_excel('C:\\Users\\praka\\Downloads\\Bird_Monitoring_Data_FOREST.XLSX', sheet_name=i)
                    if len(dataframe) != 0:
                        df1['Sex'].fillna('Undetermined',inplace = True)
                        df1['Distance'].fillna('FlyOver',inplace = True)
                        df1['ID_Method'].fillna('Visualization',inplace = True) # as this is fly over

                        df1 = pd.concat([df1, dataframe], ignore_index=True)
            
            self.InsertRD_fromDF(df1,'forest')

        except Exception as e:
            print(f"An error occurred: {e}")


    # def Insert_formatted(self,df,excl):
    #     try:
    #         if excl == 'Grass':
    #             for i in df.itertuples():

                    # Interval_slot1 = 0
                    # Interval_slot2 = 0
                    # Interval_slot3 = 0
                    # Interval_slot4 = 0
                    # if i.interval_length == '0-2.5 min':
                    #     Interval_slot1 = 1
                    # elif i.interval_length == '2.5 - 5 min':
                    #     Interval_slot2 = 1
                    # elif i.interval_length == '5 - 7.5 min':
                    #     Interval_slot3 = 1
                    # else:
                    #     Interval_slot4 = 1                  


                    # id_method1 = 0
                    # id_method2 = 0
                    # id_method3 = 0
                    # if i.ID_Method == 'Calling':
                    #     id_method1 = 1
                    # elif i.ID_Method == 'Singing':
                    #     id_method2 = 1
                    # else:
                    #     id_method3 = 1     #blank is also treated as visualization as those date has "flyover observation" as true which means visually observed

                    # Distance1 = 0
                    # Distance2 = 0
                    # Distance3 = 0
                    # if i.Distance == '<= 50 Meters':
                    #     Distance1 = 1
                    # elif i.Distance == '50 - 100 Meters':
                    #     Distance2 = 1
                    # else:
                    #     Distance3 = 1   # blanks are treated as 0 distance as those are fly over. or if resuired it can be termed as <= 50

                    # Sex1 = 0
                    # Sex2 = 0
                    # Sex3 = 0
                    # if len(i.Sex) == 0 or i.Sex == 'Undetermined' :
                    #     Sex3 = 1 # as the sex is not entered it is assumed sex was undetermined by the observer.
                    # elif i.Sex == 'Male':
                    #     Sex1 = 1
                    # else:
                    #     Sex2 = 1

            #         sql = f'''insert into Proj2.BirdWatch_Raw values \
            #             ( NEXTVAL(Proj2.rukid) , "{i.Admin_Unit_Code}" , "{i.Sub_Unit_Code}",null, \
            #                 "{i.Plot_Name}",	"{i.Location_Type}",	{i.Year}, "{i.Date}",\
            #                 "{i.Start_Time}",	"{i.End_Time}",	"{i.Observer}",	{i.Visit},	{Interval_slot},\
            #                 {id_method},	{Distance},	{i.Flyover_Observed},	"{Sex}",	"{i.Common_Name}",\
            #                 "{i.Scientific_Name}",	{i.AcceptedTSN},	{i.TaxonCode},	"{i.AOU_Code}",	{i.PIF_Watchlist_Status},\
            #                 {i.Regional_Stewardship_Status},	{i.Temperature},	{i.Humidity},	"{i.Sky}",	"{i.Wind}",\
            #                 "{i.Disturbance}",	{i.Previously_Obs},	{i.Initial_Three_Min_Cnt} )'''
            #         print(sql)
            #         self.exe(sql)
            # else :
            #     for i in df.itertuples():

                    # if i.interval_length == '0-2.5 min':
                    #     Interval_slot = 1
                    # elif i.interval_length == '2.5 - 5 min':
                    #     Interval_slot = 2
                    # elif i.interval_length == '5 - 7.5 min':
                    #     Interval_slot = 3
                    # else:
                    #     Interval_slot = 4     


                    # if i.ID_Method == 'Calling':
                    #     id_method = 1
                    # elif i.ID_Method == 'Singing':
                    #     id_method = 2
                    # else:
                    #     id_method = 3   


                    # if i.Distance == '<= 50 Meters':
                    #     Distance = 1
                    # elif i.Distance == '50 - 100 Meters':
                    #     Distance = 2
                    # else:
                    #     Distance = 3   # blanks are treated as 0 distance as those are fly over. or if resuired it can be termed as <= 50

                    # if len(i.Sex) == 0:
                    #     Sex = 'Undetermined' # as the sex is not entered it is assumed sex was undetermined by the observer.
                    # else:
                    #     Sex = i.Sex


        #             sql = f'''insert into Proj2.BirdWatch_Raw values \
        #                 ( NEXTVAL(Proj2.rukid) , "{i.Admin_Unit_Code}" , "{i.Sub_Unit_Code}","{i.Site_Name}", \
        #                     "{i.Plot_Name}",	"{i.Location_Type}",	{i.Year}, "{i.Date}",\
        #                     "{i.Start_Time}",	"{i.End_Time}",	"{i.Observer}",	{i.Visit},	{Interval_slot},\
        #                     {id_method},	{Distance},	{i.Flyover_Observed},	"{Sex}",	"{i.Common_Name}",\
        #                     "{i.Scientific_Name}",	{i.AcceptedTSN},	{i.NPSTaxonCode},	"{i.AOU_Code}",	{i.PIF_Watchlist_Status},\
        #                     {i.Regional_Stewardship_Status},	{i.Temperature},	{i.Humidity},	"{i.Sky}",	"{i.Wind}",\
        #                     "{i.Disturbance}",	null,	{i.Initial_Three_Min_Cnt} )'''
        #             print(sql)
        #             self.exe(sql)                

        # except Exception as e:
        #     print(f"An error occurred: {e}")


    def InsertRD_fromDF(self,df,excl):
        try:
            if excl == 'Grass':
                for i in df.itertuples():
                    sql = f'''insert into Proj2.BirdWatch_Raw values \
                        ( NEXTVAL(Proj2.rukid) , "{i.Admin_Unit_Code}" , "{i.Sub_Unit_Code}",null, \
                            "{i.Plot_Name}",	"{i.Location_Type}",	{i.Year}, "{i.Date}",\
                            "{i.Start_Time}",	"{i.End_Time}",	"{i.Observer}",	{i.Visit},	"{i.Interval_Length}",\
                            "{i.ID_Method}",	"{i.Distance}",	{i.Flyover_Observed},	"{i.Sex}",	"{i.Common_Name}",\
                            "{i.Scientific_Name}",	{i.AcceptedTSN},	{i.TaxonCode},	"{i.AOU_Code}",	{i.PIF_Watchlist_Status},\
                            {i.Regional_Stewardship_Status},	{i.Temperature},	{i.Humidity},	"{i.Sky}",	"{i.Wind}",\
                            "{i.Disturbance}",	{i.Previously_Obs},	{i.Initial_Three_Min_Cnt} )'''
                    print(sql)
                    self.exe(sql)
            else :
                for i in df.itertuples():
                    sql = f'''insert into Proj2.BirdWatch_Raw values \
                        ( NEXTVAL(Proj2.rukid) , "{i.Admin_Unit_Code}" , "{i.Sub_Unit_Code}","{i.Site_Name}", \
                            "{i.Plot_Name}",	"{i.Location_Type}",	{i.Year}, "{i.Date}",\
                            "{i.Start_Time}",	"{i.End_Time}",	"{i.Observer}",	{i.Visit},	"{i.Interval_Length}",\
                            "{i.ID_Method}",	"{i.Distance}",	{i.Flyover_Observed},	"{i.Sex}",	"{i.Common_Name}",\
                            "{i.Scientific_Name}",	{i.AcceptedTSN},	{i.NPSTaxonCode},	"{i.AOU_Code}",	{i.PIF_Watchlist_Status},\
                            {i.Regional_Stewardship_Status},	{i.Temperature},	{i.Humidity},	"{i.Sky}",	"{i.Wind}",\
                            "{i.Disturbance}",	null,	{i.Initial_Three_Min_Cnt} )'''
                    print(sql)
                    self.exe(sql)                

        except Exception as e:
            print(f"An error occurred: {e}")


################################################ execute the SQL and commit to database #########################################
    def exe(self,sql):
        try:
            self.mycursor.execute(sql)
            self.db.commit_db()       
        except mysql.connector.Error as err :
            print(f"Error: {err}")   


################################################ Delete all the line in the table #########################################
    def delt(self,table_name):
        sql = f"Delete from {table_name} where 1=1"
        self.exe(sql)


################################################ close the connection ######################################### 
    def close_connection(self):
        self.db.close_connection()




ld = Load_Date()
ld.load_data()
ld.close_connection()

