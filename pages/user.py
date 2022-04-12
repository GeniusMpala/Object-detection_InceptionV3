#%%writefile user.py
import streamlit as st
import tempfile
from Base_app import *
from Model import *
from Video import *

def filter_frame(txt_search):
    files = [f for f in os.listdir("./encoded_images") if os.path.isfile(os.path.join("./encoded_images", f))]
    files.sort(key = lambda x: int(x.split()[1][:-4]))
    indices = [i for i, s in enumerate(files) if txt_search.lower() in s]
    return files[indices[0]]

files = [f for f in os.listdir("./encoded_images") if os.path.isfile(os.path.join("./encoded_images", f))]
fi = [i.split()[0] for i in files] 
detected_obj = list(set(fi))

def app():

    global rez

    rez = "..."


    f = st.file_uploader("Upload video")

    s1, s2, s3 = st.columns([1,4,2])

    with s2:
        search = st.text_input("Search for objects in video")
        if search in detected_obj:
            rez = "Found"
        else:
            rez = "Not Found"
        
    with s3:
        st.write('Search results')
        if f is None:
            status = st.write(f'{search} ...')
        else:
            status = st.write(f'{search} {rez}')


    with st.container():

        col1, col2 = st.columns([2,6])

        with col1:
            st.write("Objects in video")
            for i in range(len(detected_obj)):
                st.write(str(i+1) +  " "+str(detected_obj[i]))
        with col2:
            

            if f is not None:
                tfile = tempfile.NamedTemporaryFile(delete=False) 
                tfile.write(f.read())

                with st.spinner('Initializing Frame Extration...'):
                    extract_frames(tfile.name, "./images")
                st.success('Frame Extraction Complete...')

                with st.spinner('Initializing Frame Encoding...'):
                    label_frames(inputpath="./images", outputpath='./encoded_images/', videoFile=r"./sample_vid/10Second Video Grilled Pizza Quesadillas_480p.mp4")
                st.success('Process Completed...')

                with st.spinner('Initializing Frame Building'):
                    build_video(inputpath='./encoded_images/', outputpath='./videos/video.mp4',fps=5)
                st.success('Process Completed...')

                if search.lower() in detected_obj:
                    rez = "found"
                    img = Image.open('./encoded_images/'+str(filter_frame(search)))
                    st.image(img, caption=search.lower() + " frame found")
                else:
                    play_video('./videos/video.avi')

