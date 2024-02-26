# from keras.datasets import mnist
# from keras.models import Sequential
# from keras import layers
# from keras.utils import to_categorical
#
# # Load the mnist data
# (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
# print("Training Data ")
# print(train_images.shape)
# print(len(train_labels))
#
# print("Testing Data ")
# print(test_images.shape)
# print(len(test_labels))
#
# # Model preparation
# network = Sequential()
# network.add(layers.Flatten(input_shape=(28 * 28)))
# network.add(layers.Dense(512, activation="relu"))
# network.add(layers.Dense(10, activation="softmax"))
#
# # Compile the model
# network.compile(
#     optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"]
# )
#
# # Reshape the image data
# train_images = train_images.reshape((60000, 28 * 28))
# train_images = train_images.astype("float32") / 255
#
# test_images = test_images.reshape((10000, 28 * 28))
# test_images = test_images.astype("float32") / 255
#
# # Convert the labels to categorical
# train_labels = to_categorical(train_labels)
# test_labels = to_categorical(test_labels)
#
# # Fitting
# network.fit(train_images, train_labels, epochs=5, batch_size=128)
#
# test_loss, test_acc = network.evaluate(test_images, test_labels)
# print(test_loss, test_acc)
