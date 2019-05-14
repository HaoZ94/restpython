"""REST python implementation for EEG data analysis."""
'''
For more see http://www.neuro.uestc.edu.cn/rest/

    Reference: 1. Yao D (2001) A method to standardize a reference of scalp EEG recordings to a point at infinity.
    			  Physiol Meas 22:693?11. doi: 10.1088/0967-3334/22/4/305
    		   2. Dong L, Li F, Liu Q, Wen X, Lai Y, Xu P and Yao D (2017) MATLAB Toolboxes for Reference Electrode Standardization Technique (REST) of Scalp EEG. 
    		   	  Front. Neurosci. 11:601. doi: 10.3389/fnins.2017.00601
'''

__author__    = "Hao Zhu"
__copyright__ = "Copyright 2019"
__date__      = '2019/04/09'
__license__   = "MIT"
__version__   = "1.0.1"
__email__     = "hz808@nyu.edu"

from .rest_ref import REST_re_reference