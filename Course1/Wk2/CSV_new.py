
import csv

path = "C:\\Users\\gonza\Documents\\GitHub\\Coursera_Python Data Products for Predictive Analysis\\Course1\Wk2\\amazon_reviews_us_Gift_Card_v1_00.tsv"


# In[51]:


f = open(path,encoding="utf8")


# In[52]:


reader = csv.reader(f,  delimiter = '\t')


# In[53]:


header = next (reader)


# In[54]:


dataset = []
for line in reader:
    d = dict(zip(header,line))
    for field in ['helpful_votes', 'star_rating', 'total_votes']:
        d[field]= int(d[field])
    for field in ['verified_purchase', 'vine']:
        if d[field] == 'Y':
            d[field] = True
        else:
            d[field] = False        
    dataset.append(d)


# In[55]:


ratings = [d['star_rating'] for d in dataset]


# In[56]:


sum(ratings)/len(ratings)


# In[57]:


ratingCounts= {1:0,2:0,3:0,4:0,5:0}


# In[58]:


for d in dataset:
    ratingCounts [d['star_rating']] +=1


# In[59]:


ratingCounts


# In[60]:


from collections import defaultdict


# In[61]:


ratingc=  defaultdict(int)


# In[62]:


for d in dataset: 
    ratingc [d['star_rating']] += 1


# In[63]:


ratingc


# In[64]:


verifiedCounts =  defaultdict(int)


# In[65]:


for d in dataset:
    verifiedCounts[d['verified_purchase']]+=1


# In[66]:


verifiedCounts


# In[67]:


productCount =  defaultdict(int)


# In[68]:


for d in dataset:
    productCount[d['product_id']] +=1


# In[69]:


counts = [(productCount[p],p) for p in productCount]


# In[70]:


counts.sort()


# In[71]:


counts[-10:]


# In[72]:


productCount


# In[73]:


RatingsPerProd = defaultdict(list)


# In[74]:


for d in dataset:
    RatingsPerProd[d['product_id']].append(d['star_rating'])


# In[75]:


averageratingpe = {}
for p in RatingsPerProd:
    averageratingpe[p] = sum(RatingsPerProd[p])/len(RatingsPerProd[p])


# In[76]:


averageratingpe


# In[77]:


RatingsPerProd


# In[78]:


topRated = [(averageratingpe[p],p) for p in averageratingpe if len(RatingsPerProd[p])>50]


# In[79]:


topRated.sort()


# In[80]:


topRated[-10:]


# In[84]:


customer = defaultdict(int)


# In[85]:


for d in dataset:
    customer [d['customer_id']]+=1


# In[87]:


customer


# In[94]:


top_customer = [(customer[p],p) for p in customer if (customer[p]>= 3)]


# In[96]:


top_customer.sort()


# In[98]:


top_customer[-10:]


# In[103]:


review = defaultdict(list)


# In[105]:


for d in dataset:
    review[d['helpful_votes']].append(d['review_headline'])


# In[121]:


best_reviews = [(p,review[p]) for p in review if (p>=50)]


# In[122]:


best_reviews.sort()


# In[124]:


best_reviews[-100:]


# In[133]:


rating_verified =  defaultdict(list)


# In[134]:


rating_unverified = defaultdict(int)


# In[149]:


for d in dataset:
    rating_verified[d['verified_purchase']].append(d['star_rating'])


# In[150]:


sum(rating_verified[True])/len(rating_verified[True])


# In[151]:


sum(rating_verified[False])/len(rating_verified[False])


# In[152]:


len(rating_verified[True])


# In[ ]:




