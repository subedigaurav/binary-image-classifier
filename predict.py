def predict():
    import numpy as np
    from keras.preprocessing import image
    from keras.models import load_model

    predict_img_path = 'predictset/cat_or_dog.jpg'
    test_image = image.load_img(predict_img_path, target_size=(64, 64))

    test_image = image.img_to_array(test_image)
    model = load_model('classifier.hd5')

    test_image = np.expand_dims(test_image, axis=0)

    result = model.predict(test_image)
    if result[0][0] == 1:
        prediction = 'dog'
    else:
        prediction = 'cat'
    print(prediction)


if __name__ == "__main__":
    predict()
