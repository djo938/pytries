#!/usr/bin/python2.6
# -*- coding: utf-8 -*- 

#Copyright (C) 2012  Jonathan Delvaux <pytries@djoproject.net>

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

class triesException(Exception):
    def __init__(self,value):
        self.value = value
        
    def __str__(self):
        return repr(self.value)

class valueNotFoundTriesException(triesException):
    def __init__(self,value):
        triesException.__init__(self, value)

class pathNotExistsTriesException(triesException):
    def __init__(self,value):
        triesException.__init__(self, value)

class pathExistsTriesException(triesException):
    def __init__(self,value):
        triesException.__init__(self, value)
        
class noValueSetTriesException(triesException):
    def __init__(self,value):
        triesException.__init__(self, value)
        
class ambiguousPathException(triesException):
    def __init__(self,value):
        triesException.__init__(self, value)
        
class ambiguousPathExceptionWithLevel(ambiguousPathException):
    def __init__(self,value, level,searchStack):
        triesException.__init__(self, value)
        self.level       = level
        self.searchStack = searchStack
