import warnings
warnings.filterwarnings("ignore", message=r"Passing", category=FutureWarning)
import os
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import decode_predictions
from tensorflow.keras.applications.inception_v3 import preprocess_input
import numpy as np



#from tensorflow.keras.applications.vgg16 import decode_predictions
#from tensorflow.keras.applications.vgg16 import preprocess_input
#from tensorflow.keras.applications.vgg16 import VGG16
#model = VGG16(weights='imagenet', include_top='True')



model =InceptionV3(weights='imagenet', include_top=True)

print("Done...")


def identify(): 
    
    

  #img = image.load_img(r"C:/Users/Genius/Pictures/MEmu Photo/KAVHU.png") 
  filename = "C:/Users/Genius/Desktop/ML_Models/UCF-101-Dataset/UCF-101/YoYo/train_2/FB_IMG_16484399013100809.JPG"

  if not os.path.exists(filename):
      os.makedirs(filename)
      
  img = image.load_img(filename, color_mode='rgb', target_size=(224,224))
  


  # Resizing to fit into VGGNET
  x = image.img_to_array(img)
  x.shape
  x = np.expand_dims(x, axis=0)

  # Using Pre-Trained model for prediction
  x = preprocess_input(x)
  features = model.predict(x)
  p = decode_predictions(features)
  return p

label = identify()[0][0][1]
print(f"A {label} was identified in the image...")

identify()


        