import pandas as pd
from datetime import date

meta = [
    {"name" : "Dhruv's Birthday", "date": "2013-06-10", "recurrence" : "yearly"},
    {"name" : "Ramya's Birthday", "date": "1986-02-22", "recurrence" : "yearly"},
    {"name" : "Kiran's Birthday", "date": "1980-06-17", "recurrence" : "yearly"},
    # {"name" : "Salary", "date": "2019-01-25", "recurrence" : "monthly"},
    {"name" : "Trip to India", "date": "2022-07-22", "recurrence" : "once"}
]

def GetCountdown() -> dict:
    cd_df = pd.DataFrame(data=meta)
    cd_df['countdown'] = cd_df.apply(lambda row: 1, axis=1 )
    # print(cd_df)
    cd_df['date'] = cd_df.apply(lambda row: pd.to_datetime(row['date']), axis = 1)
    cd_df['next'] = cd_df.apply(lambda row: row['date'].replace(year = pd.to_datetime("today").year), axis = 1)
    cd_df['next'] = cd_df.apply(lambda row: row['next'].replace(year = pd.to_datetime("today").year + 1) if pd.to_datetime("today") > row['next'] else row['next'], axis = 1)
    # cd_df['today'] = cd_df.apply(lambda row: pd.to_datetime("today"), axis = 1)
    cd_df['daystogo'] = cd_df.apply(lambda row: (row['date'] - pd.to_datetime("today")).days + 1
                                                    if row['recurrence'] == 'once' else
                                                (row['next'] - pd.to_datetime("today")).days + 1
                                                    if (row['recurrence'] == 'yearly') else
                                                -100    
                                    ,axis = 1)
    # print(cd_df)
    ret = cd_df[['name', 'next', 'daystogo']].sort_values('daystogo')
    # print(cd_df[['name', 'next', 'daystogo']].sort_values('daystogo'))
    return ret.to_dict("records")