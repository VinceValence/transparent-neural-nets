#!/usr/bin/env python
# coding: utf-8

# In[6]:


from abc import ABC, abstractstaticmethod
import numpy as np


# In[7]:


class CGNode(ABC):
    
    '''
    Computational graph node template
    '''
    
    @abstractstaticmethod
    def prop_forward(x):
        pass
    
    @abstractstaticmethod
    def prop_backward():
        pass


# In[8]:


class CGSum(CGNode):
    
    '''
    Computational graph sum node
    '''
    
    @staticmethod
    def prop_forward(x):
        return np.sum(x)
    
    @staticmethod
    def prop_backward(x):
        return np.ones(np.array(x).size)


# In[9]:


class CGMul(CGNode):
    
    '''
    Computational graph multiplication node
    '''
    
    @staticmethod
    def prop_forward(x):
        return np.prod(x)
    
    @staticmethod
    def prop_backward(x):
        _x = np.array(x)
        repeated = np.ones([_x.size, _x.size])*x
        np.fill_diagonal(repeated, 1)
        return np.prod(repeated, 1)


# In[12]:


CGDot.prop_forward([1,2], [3,4])


# In[ ]:


class CGExp:
    
    @staticmethod
    def prop_forward()

