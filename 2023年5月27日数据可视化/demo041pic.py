import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

db_filename = 'dinofunworld-1.db'

conn = sqlite3.connect(db_filename)

c = conn.cursor()
data = np.random.randint(140, 180, 200)

c.execute(
    "select attraction, count(*) as count from checkin where attraction in (select AttractionID from attraction where category LIKE '%Food%')  and visitorID in (select distinct visitorID from checkin where attraction in (select AttractionID from attraction where category LIKE '%Food%') group by visitorID having count(*) >= 2) group by attraction order by count desc")

tableResult2 = c.fetchall()
tableResult2Frame = pd.DataFrame.from_records(tableResult2, columns=['attraction', 'count'])

tableResult2Data = list(tableResult2Frame['count'])
tableResult2Label = list(tableResult2Frame['attraction'])
plt.hist(tableResult2Label, bins=12)

plt.show()
