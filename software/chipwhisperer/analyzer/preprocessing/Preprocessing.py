#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2014, Colin O'Flynn <coflynn@newae.com>
# All rights reserved.
#
# Find this and more at newae.com - this file is part of the chipwhisperer
# project, http://www.assembla.com/spaces/chipwhisperer
#
#    This file is part of chipwhisperer.
#
#    chipwhisperer is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    chipwhisperer is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with chipwhisperer.  If not, see <http://www.gnu.org/licenses/>.
#=================================================

from preprocessing.ResyncCrossCorrelation import ResyncCrossCorrelation
from preprocessing.ResyncPeakDetect import ResyncPeakDetect
from preprocessing.ResyncSAD import ResyncSAD
from preprocessing.Filter import Filter

def listAll(parent):
    valid_targets = {"Disabled":0}
    valid_targets["Resync: Cross Correlation"] = ResyncCrossCorrelation(parent)
    valid_targets["Resync: Peak Detect"] = ResyncPeakDetect(parent)
    valid_targets["Resync: Sum-of-Difference"] = ResyncSAD(parent)
    valid_targets["Digital Filter"] = Filter(parent)
    return valid_targets