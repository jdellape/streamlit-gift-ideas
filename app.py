import streamlit as st

tab1, tab2 = st.tabs(["John", "Hannah"])

with tab1:
   st.header("Clothes")
   st.subheader('Kuhl Engineered Krew')
   st.write("https://www.kuhl.com/kuhl/mens/short-sleeve/kuhl-engineered-krew/")
   st.write("Size: Medium, Style: Short Sleeve")
   st.image(["https://www.kuhl.com/media/versions/pdp/7361_aktiv_engineered_krew_cloud_gray_front_pdp_photo.jpg","https://www.kuhl.com/media/versions/pdp/7361_kuhl-engineered-krew_rusted-sun_front_pdp_photo.jpg"],
   caption=["Cloud Grey","Rusted Sun"])

   st.subheader('Kuhl PIXELATR')
   st.write("https://www.kuhl.com/kuhl/mens/long-sleeve/pixelatr-ls/")
   st.write("Size: Medium")
   st.image(["https://www.kuhl.com/media/versions/pdp/7336_bkm_p_1_19006_pdp_photo.jpg","https://www.kuhl.com/media/versions/pdp/7336_obx_p_1_18946_pdp_photo.jpg"],
   caption=["Black Moss","Oxblood"])

with tab2:
   st.header("Hannah")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)