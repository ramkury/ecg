# https://github.com/MIT-LCP/wfdb-python/blob/master/demo.ipynb
from wfdb import processing
import scipy
import math
#cutoff_frequencies in heartz ([low, high])
def filter_ecg(	ecg, fs,
				get_heart_rate=False,cutoff_frequencies=[0.5, 100.0]):
	nyq_f = fs/2 
	w_low = cutoff_frequencies[0]/(math.pi*nyq_f)
	w_high = cutoff_frequencies[1]/(math.pi*nyq_f)	
	filt_order = 4
	b, a = scipy.signal.butter(filt_order, [w_low, w_high], btype='bandpass')
	processed_ecg = scipy.signal.filtfilt(b, a, ecg)
	if get_heart_rate:
		qrs_inds = processing.gqrs_detect(sig=ecg, fs=fs)
		hr = processing.compute_hr(sig_len=len(ecg), qrs_inds=qrs_inds, fs=fs)
		return (processed_ecg, hr) 
	else:
		return (processed_ecg)
	