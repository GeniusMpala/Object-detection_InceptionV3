import warnings
warnings.filterwarnings("ignore", message=r"Passing", category=FutureWarning)




import keras
from keras.layers import Dense, InputLayer, Dropout, Flatten

from keras.applications import InceptionV3

from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications.inception_v3 import decode_predictions
from tensorflow.keras.applications.inception_v3 import preprocess_input
import numpy as np


model =InceptionV3(weights='imagenet', include_top=True)

def identify_frames(img_path):    
  img = image.load_img(img_path, color_mode='rgb', target_size=(224, 224))
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  x = preprocess_input(x)
  features = model.predict(x)
  return features