#!/usr/bin/env python 3.6.3
# -*- coding: utf-8 -*-

"""
Main function of Reference Electrode Standardization Technique

	Parameters: 
		eeg_raw_data:
			MNE-Python io.Raw instance in FIF format 
			The original reference can be either average reference 
			or selected reference sensor like "Cz". Recommended to use
			average reference.
		montage: 
			Electrode montage
			Can be either 'Standard_1020'(97 electrodes) or 
			'Standard_1005' (343 electrodes)
			default: 'Standard_1020'
		mode:
			'average': The original reference is average reference
			'electrode': The original reference is selected reference electrode
			default: 'average'
		reference_ch:
			The original reference electrode
			default : 'Cz'
	
	Returns:
        raw_rest:
        	The raw instance after re-referencd with REST.

    Transferring original reference to average reference then to REST is suggested.

    For more see http://www.neuro.uestc.edu.cn/rest/

    Reference: 1. Yao D (2001) A method to standardize a reference of scalp EEG recordings to a point at infinity.
    			  Physiol Meas 22:693?11. doi: 10.1088/0967-3334/22/4/305
    		   2. Dong L, Li F, Liu Q, Wen X, Lai Y, Xu P and Yao D (2017) MATLAB Toolboxes for Reference Electrode Standardization Technique (REST) of Scalp EEG. 
    		   	  Front. Neurosci. 11:601. doi: 10.3389/fnins.2017.00601

 	Thanks to Li Dong's help.
"""

__author__    = "Hao Zhu"
__copyright__ = "Copyright 2019"
__date__      = '2019/04/09'
__license__   = "MIT"
__version__   = "1.0.1"
__email__     = "hz808@nyu.edu"

# Import Needed Modules
import numpy as np 
import mne
import pickle

#Main function of Reference Electrode Standardization Technique
def REST_re_reference(eeg_raw_data,montage='standard_1005',mode="average",reference_ch='Cz'):

	print('WARNING: Only MNE-Python "io.Raw" Object Is Accepted')

	if montage not in ['standard_1005','standard_1020']:
		print('Montage Need To Be standard_1005/standard_1020')
		return
	else:
		pass

	G_dic = pickle.load(open(f'Lead_Field/{montage}_LeadField.p','rb')) #load leadfiled dictionary

	G = np.array([G_dic[ch] for ch in eeg_raw_data.info['ch_names']]) #get corresponding Lead Field Matirx 

	if mode == 'average':
		raw = eeg_raw_data.set_eeg_reference(ref_channels='average', projection=True)
		raw.apply_proj()

		l = np.ones((G.shape[0],1))
		gar = G.mean(axis=0).reshape(1,3000)
		Gar = G - np.dot(l,gar) #get leadfiled matrix at averaged reference
		Gar_plus = np.linalg.pinv(Gar,rcond=0.05) #Moore-Penrose generalized inverses
		Rar = np.dot(G,Gar_plus)

		REST_data = np.dot(Rar,raw.get_data()) #re-reference

	else:
		raw = eeg_raw_data

		l = np.ones((G.shape[0],1))
		ge = G[raw.info['ch_names'].index(reference_ch)].reshape(1,3000)
		Ge = G - np.dot(l,ge) #get leadfiled matrix at a point reference
		Ge_plus = np.linalg.pinv(Ge,rcond=0.05) #Moore-Penrose generalized inverses
		Re = np.dot(G,Ge_plus)

		REST_data = np.dot(Re,raw.get_data()) #re-reference

	raw_rest = mne.io.RawArray(REST_data, raw.info, first_samp=0, verbose=None) #reconstruct raw instance after REST 

	return raw_rest 
    
