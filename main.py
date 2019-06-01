from keras.models import Sequential

from gen_model import build_model
import gen_training_data
import gen_test_data

import argparse


def build_and_train():
    model = build_model()

    # generate training and test dataset
    training_set = gen_training_data.gen_training_data()
    test_set = gen_test_data.gen_test_data()

    # TRAINING THE CLASSIFIER
    model.fit_generator(training_set,
                        steps_per_epoch=4000,
                        epochs=15,
                        validation_data=test_set,
                        validation_steps=1000)

    model.save('classifier.hd5')


if __name__ == "__main__":
    build_and_train()
