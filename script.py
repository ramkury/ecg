import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
import wfdb

# https://github.com/MIT-LCP/wfdb-python/blob/master/demo.ipynb

# Demo 1 - Read a wfdb record using the 'rdrecord' function into a wfdb.Record object.
# Plot the signals, and show the data.
record = wfdb.rdrecord('Samples/f1o01')
wfdb.plot_wfdb(record=record, title='Record a103l from Physionet Challenge 2015') 
print(record.__dict__)
