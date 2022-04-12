import streamlit as st
import tempfile
import warnings
import os
from PIL import Image
from Video import *

warnings.filterwarnings("ignore", message=r"Passing", category=FutureWarning)


# hide hamburger menu
# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# hide footer
hide_footer_style = """
<style>
.reportview-container .main footer {visibility: hidden;}    
"""
st.markdown(hide_footer_style, unsafe_allow_html=True)


files = [f for f in os.listdir("./encoded_images") if os.path.isfile(os.path.join("./encoded_images", f))]
fi = [i.split()[0] for i in files] 
detected_obj = list(set(fi))

def play_video(vid_path):
    video_file = open(vid_path, 'rb')
    video_bytes = video_file.read()
    st.video(vid_path)
  

def filter_frame(txt_search):
    files = [f for f in os.listdir("./encoded_images") if os.path.isfile(os.path.join("./encoded_images", f))]
    files.sort(key = lambda x: int(x.split()[1][:-4]))
    indices = [i for i, s in enumerate(files) if txt_search.lower() in s]
    return files[indices[0]]


def main():
    global rez

    rez = "..."

    st.sidebar.title("Dashboard")

    home = st.sidebar.button('Home', key='home')
    upload = st.sidebar.button('Upload video',key='upload')


    if upload:
        f = st.file_uploader("Upload video")

        s1, s2, s3 = st.beta_columns([1,4,2])

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


        with st.beta_container():

            col1, col2 = st.beta_columns([2,6])

            with col1:
                st.write("Objects in video")
                for i in range(len(detected_obj)):
                    st.write(str(i+1) +  " "+str(detected_obj[i]))
            with col2:

                if f is not None:
                    tfile = tempfile.NamedTemporaryFile(delete=False) 
                    tfile.write(f.read())

                    with st.spinner('[*Extracting Frames] - Process Initialized...'):
                        extract_frames(tfile.name, "./images")
                    st.success('[*Extracting Frames] - Process Completed...')

                    with st.spinner('[**Encoding Frames] - Process Initialized...'):
                        label_frames(inputpath="./images", outputpath='./encoded_images/', videoFile=r"C:/Users/Genius/Videos/vid_cars.mp4")
                    st.success('[*Encoding Frames] - Process Completed...')

                    with st.spinner('[***Building Frames] - Process Initialized...'):
                        build_video(inputpath='./encoded_images/', outputpath='./videos/video.mp4',fps=5)
                    st.success('[*Building Frames] - Process Completed...')

                    play_video('./videos/video.mp4')

                    
    else:

        st.title('Object(s) Detection in video')

        hs1, hs2, hs3 = st.beta_columns([1,4,2])

        with hs2:
            h_search = st.text_input("Search for objects in video")
            if h_search.lower() in detected_obj:
                rez = "found"
            else:
                rez = "not found"
        
        with hs3:
            st.write('Search results')
            if h_search.lower() is None:
                status = st.write(f'{h_search} ...')
            else:
                status = st.write(f'{h_search} {rez}')


        if len(detected_obj) > 6:
            col1, col2, col3 = st.beta_columns([2,2,6])
            with col1:
                st.subheader("Objects in video")
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
                if h_search.lower() in detected_obj:
                    rez = "found"
                    img = Image.open('./encoded_images/'+str(filter_frame(h_search)))
                    st.image(img, caption=h_search.lower() + " frame found")
                else:
                    play_video("./videos/video.mp4")
        else:
            col1, col2 = st.columns([2,6])
            with col1:  
                st.write("Objects in video")
                for i in range(len(detected_obj)):
                    st.write(str(i+1) +  " "+str(detected_obj[i]))
            with col2:
                play_video("./videos/video.mp4")
    
                    
    


if __name__ == '__main__':
    main()