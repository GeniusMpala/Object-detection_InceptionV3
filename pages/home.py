#%%writefile home.py
import streamlit as st
from Base_app import *

files = [f for f in os.listdir("./en_images") if os.path.isfile(os.path.join("./en_images", f))]
fi = [i.split()[0] for i in files] 
detected_obj = list(set(fi))

def filter_frame(txt_search):
    files = [f for f in os.listdir("./en_images ") if os.path.isfile(os.path.join("./en_images ", f))]
    files.sort(key = lambda x: int(x.split()[1][:-4]))
    indices = [i for i, s in enumerate(files) if txt_search.lower() in s]
    return files[indices[0]]

def app():
    global h_rez

    h_rez = "..."

    st.title('Object Detection using InceptionV3 Model')

    hs1, hs2, hs3 = st.columns([1,4,2])

    #with hs2:
       # h_search = st.text_input("Search for objects in video")
        #if h_search.lower() in detected_obj:
         #   h_rez = "found"
        #else:
         #   h_rez = "not found"
        
   # with hs3:
    #    st.write('Search results')
     #   if h_search.lower() is None:
      #      status = st.write(f'{h_search} ...')
       # else:
        #    status = st.write(f'{h_search} {h_rez}')


    if len(detected_obj) > 6:
        col1, col2, col3 = st.columns([2,2,6])
        with col1:
            #st.subheader("Objects in video")
            for i in range(0,7):
                st.write(str(i+1) +  " "+str(detected_obj[i]))
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            for i in range(7,len(detected_obj)-1):
                st.write(str(i+1) +  " "+str(detected_obj[i]))
        with col3:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
           # if h_search.lower() in detected_obj:
            #    h_rez = "found"
             #   img = Image.open('./en_images/'+str(filter_frame(h_search)))
              #  st.image(img, caption=h_search.lower() + " frame found")
            #else:
             #   play_video("video.mp4")
    else:
        col1, col2 = st.columns([2,6])
        with col1:  
            #st.write("Objects in video")
            for i in range(len(detected_obj)):
                st.write(str(i+1) +  " "+str(detected_obj[i]))
        with col2:
            play_video("video.avi")