import sqlite3 as sq3
import pandas.io.sql as pds
import pandas as pd

path = 'baseball.db'
con = sq3.Connection(path)

query = '''
	select * from allstarfull
'''

observations = pds.read_query(query, con)
print(observations)