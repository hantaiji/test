#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tensorflow.compat.v1 as tf 
tf.disable_eager_execution()
#定义输入和参数
x=tf.constant([[0.7,0.5]])
w1=tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2=tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))
#定以前向传播过程
a=tf.matmul(x,w1)
y=tf.matmul(a,w2)
#使用会话计算结果
with tf.Session() as sess:
    init_op=tf.global_variables_initializer()
    sess.run(init_op)
    print ("y in tf3_3.py is:\n",sess.run(y))

