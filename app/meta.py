import pandas as pd

meta = [
    {"name" : "Birthday", "date": "2020-01-01", "recurrence" : "yearly"},
    {"name" : "Vacation", "date": "2022-12-25", "recurrence" : "once"},
]

def GetCountdown() -> dict:
    cd_df = pd.DataFrame(data=meta)
    cd_df['countdown'] = cd_df.apply(lambda row: 1, axis=1 )
    cd_df['date'] = cd_df.apply(lambda row: pd.to_datetime(row['date']), axis = 1)
    cd_df['next'] = cd_df.apply(lambda row: row['date'].replace(year = pd.to_datetime("today").year), axis = 1)
    cd_df['next'] = cd_df.apply(lambda row: row['next'].replace(year = pd.to_datetime("today").year + 1) if pd.to_datetime("today") > row['next'] else row['next'], axis = 1)
    cd_df['daystogo'] = cd_df.apply(lambda row: (row['date'] - pd.to_datetime("today")).days + 1
                                                    if row['recurrence'] == 'once' else
                                                (row['next'] - pd.to_datetime("today")).days + 1
                                                    if (row['recurrence'] == 'yearly') else
                                                -100    
                                    ,axis = 1)
    ret = cd_df[['name', 'next', 'daystogo']].sort_values('daystogo')
    return ret.to_dict("records")