import wfdb
from script import *
from GUI import *
import time
import matplotlib.pyplot as plt
import numpy as np
gui = GUI() 
record = wfdb.rdrecord('Samples/f1o01')
ecg = record.p_signal[:,1]
ecg[np.where(np.isnan(ecg))] = 0
fs = record.fs
time_step = 10 # time in seconds
index_step = time_step*fs
for i in range(0, len(ecg), index_step):
	start = i
	if(i+index_step>=len(ecg)):
		end = len(ecg)
	else:
		end = i+index_step
	processed_ecg, hr = filter_ecg(ecg[start:end], fs, get_heart_rate=True)
	t = np.array(list(range(0,len(processed_ecg))))/fs
	avg_hr = round(np.nanmean(hr))
	gui.plot_signal(t, processed_ecg,
					x_label='Time (seconds)', y_label='ECG',
					title='Mean heart rate: {}'.format(avg_hr))
	time.sleep(0.01)
plt.figure()
processed_ecg = filter_ecg(ecg, fs, get_heart_rate=False)
plt.plot(ecg, label='original ecg')
plt.plot(processed_ecg, label='filtered ecg')
plt.legend()
plt.show()