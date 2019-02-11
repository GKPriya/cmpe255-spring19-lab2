
# coding: utf-8

# In[1]:


def mean_num_friends(x):

    # TOD0
    sum=0
    for i in num_friends:
        sum = sum + i 
    return sum/len(x)

def median_num_friends(x):

    # TODO
    x.sort()
    size=len(x)
    
    if size<1:
        return None
    if size%2 == 1:
        return x[size//2]
    else:
        return sum(x[size//2-1:size//2+1])/2.0
    
    
        
num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]


# In[2]:


print("mean ={} ".format(median_num_friends(num_friends)))



# In[3]:


print("mean ={} ".format(mean_num_friends(num_friends)))

