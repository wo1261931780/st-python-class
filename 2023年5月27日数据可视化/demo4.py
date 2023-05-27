# 折线图修改：
import sqlite3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

db_filename = 'dinofunworld-1.db'

conn = sqlite3.connect(db_filename)
c = conn.cursor()
