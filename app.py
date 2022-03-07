#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def xyz():
     return render_template('app.html')
app.route('/info',methods=['POST'])
def obj():
     if(request.method=='POST'):
          num1=request.form['a']
          num2=request.form['b']
          total=int(num1)+int(num2)
          return render_template('app.html',total1=total)
if __name__ == '__main__':
    app.run()    


# In[ ]:




