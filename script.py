import matplotlib.pyplot as plt
import numpy as np
# https://github.com/MIT-LCP/wfdb-python/blob/master/demo.ipynb
import wfdb
from wfdb import processing
import scipy
import math
record = wfdb.rdrecord('Samples/f1o01')
fs = record.fs
nyq_f = fs/2 
w_high = 100/(math.pi*nyq_f)
w_low = 0.05/(math.pi*nyq_f)
wn = [w_low, w_high]
filt_order = 2
#ecg
ecg = record.p_signal[:,1]
plt.plot(ecg, label='original ecg')
ecg[np.where(np.isnan(ecg))] = ecg[np.where(np.isnan(ecg))[0]-1]
b, a = scipy.signal.butter(2, wn, btype='bandpass')
processed_ecg = scipy.signal.lfilter(b, a, ecg)
plt.plot(processed_ecg, label='filtered ecg')
plt.legend()
plt.show()
qrs_inds = processing.gqrs_detect(sig=ecg, fs=fs)
hrs = processing.compute_hr(sig_len=len(ecg), qrs_inds=qrs_inds, fs=fs)
plt.plot(hrs, label='heart rate')
plt.legend()
plt.show()