#!/usr/bin/env python
# coding: utf-8

# ### Listas

# In[ ]:


produtos = ["iphone", "ipad", "airpod"]
produtos_novos = ["apple watch", "macbook"]


# In[ ]:





# ### Dicionários

# In[ ]:


produtos_dic = {"iphone": 7000, "ipad": 11000, "airpod": 2500}
novos_produtos_dic = {"apple watch": 3500, "macbook": 15000}


# In[ ]:





# ### Tabelas

# In[ ]:


import pandas as pd

produtos_df = pd.read_csv("produtos.csv")
novos_produtos_df = pd.read_csv("novosprodutos.csv")
display(produtos_df)
display(novos_produtos_df)


# In[ ]:





# In[ ]:




