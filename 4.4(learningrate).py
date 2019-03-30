#损失函数 loss=(w+1)^2,令w初值为5。反向传播就是求最优的w
import tensorflow as tf
w=tf.Variable(tf.constant(5,dtype=tf.float32))
#定义损失函数
loss=tf.square(w+1)
train_step=tf.train.GradientDescentOptimizer(0.2).minimize(loss)
#生成会话训练40轮
with tf.Session() as sess:
    init_op=tf.global_variables_initializer()
    sess.run(init_op)
    for i in range(40):
        sess.run(train_step)
        w_val=sess.run(w)
        loss_val=sess.run(loss)
        print("after %d step w is : %f loss is %f."%(i,w_val,loss_val))