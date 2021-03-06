def trainNW1():
  model = models.Sequential()
  model.add(layers.ZeroPadding2D(padding=(1,1), input_shape=(8, 8, 14)))
  model.add(layers.Conv2D(32, (3, 3), strides = (1,1), activation='relu'))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.AveragePooling2D((2, 2)))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(layers.Flatten())
  model.add(layers.Dense(128,activation='softmax'))
  model.add(layers.Reshape((1,128)))

  # model.summary()
  model.compile(optimizer='adam',
                loss = tf.keras.losses.MeanSquaredError(),
                metrics=['accuracy'])
  return model.fit(TrainWX, TrainWY, epochs = 10)

def trainNB1():
  model = models.Sequential()
  model.add(layers.ZeroPadding2D(padding=(1,1), input_shape=(8, 8, 14)))
  model.add(layers.Conv2D(32, (3, 3), strides = (1,1), activation='relu'))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.AveragePooling2D((2, 2)))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(layers.Flatten())
  model.add(layers.Dense(128,activation='softmax'))
  model.add(layers.Reshape((1,128)))

  # model.summary()
  model.compile(optimizer='adam',
                loss = tf.keras.losses.MeanSquaredError(),
                metrics=['accuracy'])
  return model.fit(TrainBX, TrainBY, epochs = 10)

def trainNW2():
  model = models.Sequential()
  model.add(layers.ZeroPadding2D(padding=(1,1), input_shape=(8, 8, 14)))
  model.add(layers.Conv2D(32, (3, 3), strides = (1,1), activation='relu'))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(layers.Flatten())
  model.add(layers.Dense(128,activation='softmax'))
  model.add(layers.Reshape((1,128)))

  # model.summary()
  model.compile(optimizer='Nadam',
                loss = tf.keras.losses.MeanSquaredError(),
                metrics=['accuracy'])
  return model.fit(TrainWX, TrainWY, epochs = 10)

def trainNB2():
  model = models.Sequential()
  model.add(layers.ZeroPadding2D(padding=(1,1), input_shape=(8, 8, 14)))
  model.add(layers.Conv2D(32, (3, 3), strides = (1,1), activation='relu'))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(layers.Flatten())
  model.add(layers.Dense(128,activation='softmax'))
  model.add(layers.Reshape((1,128)))

  # model.summary()
  model.compile(optimizer='Nadam',
                loss = tf.keras.losses.MeanSquaredError(),
                metrics=['accuracy'])
  return model.fit(TrainBX, TrainBY, epochs = 10)

def trainNW3():
  model = models.Sequential()
  model.add(layers.ZeroPadding2D(padding=(1,1), input_shape=(8, 8, 14)))
  model.add(layers.Conv2D(32, (3, 3), strides = (1,1), activation='relu'))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(layers.Flatten())
  model.add(layers.Dense(128,activation='softmax'))
  model.add(layers.Reshape((1,128)))

  # model.summary()
  model.compile(optimizer='Nadam',
                loss = tf.keras.losses.MeanSquaredLogarithmicError(),
                metrics=['accuracy'])
  return model.fit(TrainWX, TrainWY, epochs = 20)

def trainNB3():
  model = models.Sequential()
  model.add(layers.ZeroPadding2D(padding=(1,1), input_shape=(8, 8, 14)))
  model.add(layers.Conv2D(32, (3, 3), strides = (1,1), activation='relu'))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(layers.Flatten())
  model.add(layers.Dense(128,activation='softmax'))
  model.add(layers.Reshape((1,128)))

  # model.summary()
  model.compile(optimizer='Nadam',
                loss = tf.keras.losses.MeanSquaredLogarithmicError(),
                metrics=['accuracy'])
  return model.fit(TrainBX, TrainBY, epochs = 20)

def trainNW4():
  model = models.Sequential()
  model.add(layers.ZeroPadding2D(padding=(1,1), input_shape=(8, 8, 14)))
  model.add(layers.Conv2D(32, (3, 3), strides = (1,1), activation='elu'))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.Conv2D(64, (3, 3), activation='elu'))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.Conv2D(64, (3, 3), activation='elu'))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.Conv2D(64, (3, 3), activation='elu'))
  model.add(layers.Flatten())
  model.add(layers.Dense(128,activation='softmax'))
  model.add(layers.Reshape((1,128)))

  # model.summary()
  model.compile(optimizer='adam',
                loss = tf.keras.losses.MeanSquaredLogarithmicError(),
                metrics=['accuracy'])
  return model.fit(TrainWX, TrainWY, epochs = 10)

history = trainNW4()

def trainNB4():
  model = models.Sequential()
  model.add(layers.ZeroPadding2D(padding=(1,1), input_shape=(8, 8, 14)))
  model.add(layers.Conv2D(32, (3, 3), strides = (1,1), activation='elu'))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.Conv2D(64, (3, 3), activation='elu'))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.Conv2D(64, (3, 3), activation='elu'))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.Conv2D(64, (3, 3), activation='elu'))
  model.add(layers.Flatten())
  model.add(layers.Dense(128,activation='softmax'))
  model.add(layers.Reshape((1,128)))

  # model.summary()
  model.compile(optimizer='adam',
                loss = tf.keras.losses.MeanSquaredLogarithmicError(),
                metrics=['accuracy'])
  return model.fit(TrainBX, TrainBY, epochs = 10)

def trainNW5():
  model = models.Sequential()
  model.add(layers.ZeroPadding2D(padding=(1,1), input_shape=(8, 8, 14)))
  model.add(layers.Conv2D(32, (3, 3), strides = (1,1), activation='relu'))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(layers.Flatten())
  model.add(layers.Dense(128,activation='softmax'))
  model.add(layers.Reshape((1,128)))

  # model.summary()
  model.compile(optimizer='Nadam',
                loss = tf.keras.losses.MeanSquaredLogarithmicError(),
                metrics=['accuracy'])
  return model.fit(TrainWX, TrainWY, epochs = 10)

def trainNB5():
  model = models.Sequential()
  model.add(layers.ZeroPadding2D(padding=(1,1), input_shape=(8, 8, 14)))
  model.add(layers.Conv2D(32, (3, 3), strides = (1,1), activation='relu'))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.ZeroPadding2D(padding=(1,1)))
  model.add(layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(layers.Flatten())
  model.add(layers.Dense(128,activation='softmax'))
  model.add(layers.Reshape((1,128)))

  # model.summary()
  model.compile(optimizer='Nadam',
                loss = tf.keras.losses.MeanSquaredLogarithmicError(),
                metrics=['accuracy'])
  return model.fit(TrainBX, TrainBY, epochs = 10)
