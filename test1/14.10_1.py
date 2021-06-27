"""
@IDE: Pycharm
@Environment: TF 2.1.0, python 3.7.7

@citation: 시작하세요! 텐서플로 2.0 프로그래밍
@author: Hwanhee kim

@Rewrite: childult-programmer
@Github: https://github.com/childult-programmer
"""

import tensorflow as tf
import numpy as np

# XOR data
x = np.array([[1,1,1,1],[0,0,0,0], [1,0,1,0],[0,1,0,1],[1,0,0,1],[0,1,1,0],[0,0,1,1],[1,1,0,0]])
y = np.array([[1,0], [1,0], [0,1], [0,1],[0,0],[0,0],[1,1],[1,1]])

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(4,input_dim=4, activation='relu'))

model.add(tf.keras.layers.Dense(units=2, activation='relu'))


model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.1), loss='mse')

history = model.fit(x, y, epochs=3000, batch_size=1)

model.summary()

print(model.predict(x))
