#!/usr/bin/env python 3.6.3
# -*- coding: utf-8 -*-
'''
Test dataset:
Auditory localizor experiment. Subject listen to 100 trial of 1kHz pure tone with 100ms duration. ITI jitter range from
900ms to 1200ms. EEG recorded with BP actiChamp, 32 sensors, standard 1020 layout, EasyCap 32, PyCoder.
Format: Bp '.vhdr'. Sample rate: 1000Hz. Referenced at Cz. Eog: 'AF3','AF7'.
'''

from rest_ref import *
import matplotlib
matplotlib.use('TkAgg')

event_id= {'AD':1}

raw = mne.io.read_raw_brainvision(f'sample_data/e0044T.vhdr', event_id=event_id, preload=True)

raw = mne.add_reference_channels(raw,'Cz')

raw.drop_channels(['AF3','AF7','STI 014'])

raw_rest = REST_re_reference(raw)

raw_rest.plot(block = True,duration = 1,n_channels=32)

