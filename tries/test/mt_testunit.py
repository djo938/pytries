#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

import unittest
from multiLevelTries import multiLevelTries
from exception import pathExistsTriesException, triesException

def buildList(minSize, maxSize, charset):
    ret = []
    for l in range(minSize, maxSize+1):
        index = [0] * l
        
        for c in range(len(charset)**l):
            #build string
            s = ""
            divisor = 1
            for i in range(l):
                s = charset[index[i]] + s
        
            ret.append(s)
            #incremente
            index[0] += 1
            for i in range(len(index)):
                if(index[i] == len(charset)):
                    index[i] = 0
                    if i+1 < len(index):
                        index[i+1] += 1

    return ret

def buildMultiList(minSize, maxSize, listOrigin):
    ret = []
    for l in range(minSize, maxSize+1):
        index = [0] * l
        
        for c in range(len(listOrigin)**l):
            #build string
            s = []
            divisor = 1
            for i in range(l):
                s.append(listOrigin[index[i]])
        
            ret.append(s)
            #incremente
            index[0] += 1
            for i in range(len(index)):
                if(index[i] == len(listOrigin)):
                    index[i] = 0
                    if i+1 < len(index):
                        index[i+1] += 1

    return ret
    
class TraversalTest(unittest.TestCase):
    
    def setUp(self):
        self.mlt = multiLevelTries()
        toInsert = buildMultiList(1,3,buildList(1,3,["a","b"]))
        self.keyValue = {}
        
        for v in toInsert:
            tv = tuple(v)
            string = "".join(v)
            self.keyValue[tv] = string
            self.mlt.insert(tv,string)        
    
    #every inserted stringList are in the tree
    def test_everyKeyInTheTree(self):
        for k,v in self.keyValue.iteritems():
            self.assertTrue( self.mlt.search(k) == v) #TODO search need a list, not a string
    
    
    def _inner_test_everyValueCorrespondToAKey(self, path, node, state, level):
        if node.isValueSet():
            local_mltries = node.value
            
            newState = []
            newState.extend(state)
            newState.append(node.getCompleteName())
            
            if local_mltries.isValueSet():
                self.assertTrue( tuple(newState) in self.keyValue and self.keyValue[tuple(newState)] == local_mltries.value )
            
            
            local_mltries.localTries.genericDepthFirstTraversal(self._inner_test_everyValueCorrespondToAKey, newState)
            
        return state
            
    #a path in the tree comme from a stringList
    def test_everyValueCorrespondToAKey(self):
        self.mlt.localTries.genericDepthFirstTraversal(self._inner_test_everyValueCorrespondToAKey, [])
    
    #can't insert an existing path
    def test_insertExistingValue(self):
        self.assertRaises(pathExistsTriesException, self.mlt.insert,["a"],"a")
    
    #search a non existing path
    def test_tryToSearchANonExistingPath(self):
        self.assertRaises(triesException,self.mlt.search,["z"])
    
    def _inner_test_traversal(self, currentPath, value, traversalState, level):
        
        print traversalState, len(self.keyValue.keys())
        self.assertTrue(len(self.keyValue.keys()) > traversalState)
        
        if value != None and value.isValueSet():
            return traversalState+1 
        return traversalState
    
    def test_traversal(self):
        self.mlt.genericDepthFirstTraversal(self._inner_test_traversal,0, True)
    
if __name__ == '__main__':
    unittest.main()