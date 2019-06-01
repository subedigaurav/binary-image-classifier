# make the necessary imports
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense


# BUILDING THE CNN
def build_model():
    # Initializing the CNN
    classifier = Sequential()

    # Step 1 - Convolution
    classifier.add(Convolution2D(filters=32, kernel_size=(3, 3), input_shape=(64, 64, 3), activation='relu'))

    # Step 2 - Pooling
    classifier.add(MaxPooling2D(pool_size=(2, 2), strides=2))

    # Adding a second convolutional layer for performance improvement
    classifier.add(Convolution2D(filters=32, kernel_size=(3, 3), activation='relu'))
    classifier.add(MaxPooling2D(pool_size=(2, 2), strides=2))

    # Step 3 - Flattening
    classifier.add(Flatten())

    # Step 4 - Full Connection
    classifier.add(Dense(units=128, activation='relu'))
    classifier.add(Dense(units=1, activation='sigmoid'))

    # Compiling the CNN
    classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return classifier
