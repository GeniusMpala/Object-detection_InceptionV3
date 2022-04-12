#%%writefile about.py
import streamlit as st

def app():
    
    st.title('Object Detection using InceptionV3 Model...')

    c1, c2, c3 = st.columns([4,2,4])
    with c2:
        st.write('Done by:')

    b1,m1,l1 = st.columns([3,1,3])
    with b1:
        st.write('Genius Mpala')
        st.write('Reg:  R207386F')
        st.write('geniustuta@gmail.com')
        
    with m1:
        st.write("|")
        
    with l1:
        st.write('Tatenda P Munyanyi:  ')
        st.write("Reg: R205746K")
        st.write('tatendamunyanyi@gmail.com')
  