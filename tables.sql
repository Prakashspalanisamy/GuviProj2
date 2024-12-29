CREATE SEQUENCE Proj2.rukid

******************************************************************
CREATE TABLE Proj2.BirdWatch_Raw(
  ukid BIGINT ,
  Admin_Unit_Code VARCHAR(10) NOT NULL,
  Sub_Unit_Code VARCHAR(10),
  Site_Name VARCHAR(15),
  Plot_Name VARCHAR(15),	
  Location_Type VARCHAR(15) NOT NULL,	
  Year_watch SMALLINT,
  Date_watch DATETIME ,
  Start_Time TIME,
  End_Time TIME,
  Observer VARCHAR(25),
  Visit SMALLINT,
  Interval_Length VARCHAR(30),
  ID_Method	VARCHAR(20),
  Distance VARCHAR(20),	
  Flyover_Observed	BOOLEAN, 
  Sex VARCHAR(15) ,	
  Common_Name VARCHAR(60),	
  Scientific_Name VARCHAR(60) NOT NULL,	
  AcceptedTSN MEDIUMINT,
  TaxonCode	MEDIUMINT, 
  AOU_Code VARCHAR(10),	
  PIF_Watchlist_Status BOOLEAN,
  Regional_Stewardship_Status BOOLEAN,
  Temperature decimal(20,15),
  Humidity decimal(20,15),
  Sky VARCHAR(25),	
  Wind VARCHAR(60),	
  Disturbance VARCHAR(30),	
  Previously_Obs BOOLEAN,
  Initial_Three_Min_Cnt BOOLEAN, 
  PRIMARY KEY (ukid)
);

/*  UNIQUE INDEX c1 (Admin_Unit_Code, Location_Type, Date_watch, Start_Time, Scientific_Name, sex , Interval_Length)*/
  
  *****************************************************************************************************
  
  
  CREATE SEQUENCE Proj2.ukid
  
  
  CREATE TABLE Proj2.BirdWatch(
  ukid BIGINT ,
  Admin_Unit_Code VARCHAR(10) NOT NULL,
  Sub_Unit_Code VARCHAR(10),
  Plot_Name VARCHAR(15),	
  Location_Type VARCHAR(15) NOT NULL,	
  Year_watch SMALLINT,
  Date_watch DATETIME ,
  Start_Time TIME,
  End_Time TIME,
  Observer VARCHAR(25),
  Visit SMALLINT,
  Interval_Slot1 SMALLINT,
  Interval_Slot2 SMALLINT,
  Interval_Slot3 SMALLINT,
  Interval_Slot4 SMALLINT,
  ID_Method1	SMALLINT,
  ID_Method2	SMALLINT,
  ID_Method3	SMALLINT,  
  Distance1 SMALLINT,	
  Distance2 SMALLINT,	
  Distance3 SMALLINT,	
  Flyover_Observed	BOOLEAN, 
  Sex VARCHAR(15) ,	
  Scientific_Name VARCHAR(60) NOT NULL,	
  AOU_Code VARCHAR(10),	
  PIF_Watchlist_Status BOOLEAN,
  Regional_Stewardship_Status BOOLEAN,
  Temperature decimal(20,15),
  Humidity decimal(20,15),
  Sky SMALLINT,	
  Wind SMALLINT,	
  Disturbance SMALLINT,	
  Previously_Obs BOOLEAN,
  Initial_Three_Min_Cnt BOOLEAN, 
  PRIMARY KEY (ukid)
  );
  
  /*UNIQUE INDEX c1 (Admin_Unit_Code, Location_Type, Date_watch, Start_Time, Scientific_Name, sex , Interval_Slot )*/
  
 /* NEXTVAL(Proj2.ukid); */
 
 