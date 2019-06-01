from keras.preprocessing.image import ImageDataGenerator


def gen_test_data():
    test_datagen = ImageDataGenerator(rescale=1. / 255)

    test_set = test_datagen.flow_from_directory('dataset/test_set',
                                                target_size=(64, 64),
                                                batch_size=32,
                                                class_mode='binary')
    return test_set
