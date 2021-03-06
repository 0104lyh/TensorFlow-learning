#两层简单神经网络（全连接）
import tensorflow as tf

#定义输入和参数
#用placeholder定义输入（sess.run()喂多组数据）
x = tf.placeholder(tf.float32,shape=(None,2))
#这里的shape后面写None的原因是，在后面不知道要输入多少组数据，但是第二个2是因为我们知道要输入的是两个'条件'
w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

#定义前项传播过程

a = tf.matmul(x,w1)
y = tf.matmul(a,w2)

#调用会话计算结果
with tf.Session() as sess:
	init_op=tf.global_variables_initializer()
	#这里提一个自己经常犯的错误:variables经常忘记了s.然后就会报错。。。
	sess.run(init_op)
	print("the result of this is:\n",sess.run(y,feed_dict={x:[[0.7,0.5],[0.2,0.3],[0.3,0.4],[0.4,0.5]]}))
	print("w1:\n",sess.run(w1))
	print("w2:\n",sess.run(w2))

