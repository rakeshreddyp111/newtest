
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route('/')
def home_endpoint():
    return 'Hello World'


# In[ ]:


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)

