# imageClassifier
**imageClassifier** is a simple Image Classifier. It is built using [Keras](https://keras.io/) on top of [Tensorflow](https://www.tensorflow.org).

## Getting Started
### Prerequisites
To run the model, you will need to install Tensorflow and Keras.
1. **Tensorflow**
    ```bash
    pip install tensorflow
    ```
    Official document for Tensorflow installation can be found [here](https://www.tensorflow.org/install).
    
2. **Keras**
    ```bash
    pip install keras
    ```
    Official document for Keras installation can be found [here](https://keras.io/#installation)

3. **Dataset** <br />
    The dataset folder consists of two sub-folders: *cat* and *dog*. These will be the classes for the classifier. I have included about 4000 images for cats and dogs (2000 each).
    You are free to use the sample classes. <br />
    **OR** <br />
    Create sub-folders inside the **dataset** folder as per your requirements and add the images there.

## Installing
### Training the Model
Use *train.py* to train the classifier model. After training, the model will be saved to [HDF5 Format.](http://www.h5py.org/). In command line, run the following code:
```bash
python main.py
```
## Making Predictions
Use the file *predict.py* to make predictions on an image. Assuming *<path-to-file*> is the location of the image to be predicted, use the following code for prediction:
```angular2
predict.py --path <path-to-file>
```


## License
This project is licensed under the MIT License. Please click [here](https://opensource.org/licenses/MIT) to learn more.

This is my first try. Please exuse the mess.  :grinning:
:thumbsup: Good Luck! Have a nice day ahead!  :smiley: