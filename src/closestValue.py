# -*- coding: utf-8 -*-
"""
closestValue, based on .m file

function v = cslosestValue (x, XV)

Given a value X and an array of values XV return the value in XV
that is closest to X.  If two values are equally close, it is not
defined which of the two will be returned. XV need not be sorted
and repeated values are allowed.

"""

import numpy as np

def closestValue (x, XV):

    r = np.sort ([np.transpose(np.abs(XV - x)), np.transpose(list(range(np.size(XV,2))))], axis=0);
    v = XV (r[0,1]);
    return v
