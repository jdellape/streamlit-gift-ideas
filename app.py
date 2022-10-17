import streamlit as st

tab1, tab2 = st.tabs(["John", "Hannah"])

with tab1:
   st.header("Clothes")
   st.subheader('Kuhl Engineered Krew')
   st.write("https://www.kuhl.com/kuhl/mens/short-sleeve/kuhl-engineered-krew/")
   st.write("Size: Medium, Style: Short Sleeve")
   st.image(["https://www.kuhl.com/media/versions/pdp/7361_aktiv_engineered_krew_cloud_gray_front_pdp_photo.jpg","https://www.kuhl.com/media/versions/pdp/7361_kuhl-engineered-krew_rusted-sun_front_pdp_photo.jpg"],
   caption=["Cloud Grey","Rusted Sun"])

   st.subheader('TreeBlend Classic T-Shirt')
   st.write("Size: Medium")
   st.write('https://www.tentree.com/collections/mens-shortsleeve-t-shirts/products/mens-basic-tshirt-white')
   st.image('https://cdn.shopify.com/s/files/1/2341/3995/products/WhiteRecycledPolyesterCrewNeckTee_TCM1869-00161-Edit_1.jpg?v=1656986726&width=400',
   caption='White')

   st.write('https://www.tentree.com/collections/mens-shortsleeve-t-shirts/products/mens-basic-tshirt-meteorite-black')
   st.image('https://cdn.shopify.com/s/files/1/2341/3995/products/BlackRecycledPolyesterCrewNeckTee_TCM1869-0164-2660_1.jpg?v=1656986730&width=400',
   caption='Meteorite Black')

   st.write('https://www.tentree.com/collections/mens-shortsleeve-t-shirts/products/mens-basic-tshirt-mushroom-heather')
   st.image('https://cdn.shopify.com/s/files/1/2341/3995/products/BrownRecycledPolyesterCrewNeckTee_TCM1869-2168_1.jpg?v=1656986727&width=400',
   caption='Mushroom Heather')

   st.subheader('Kuhl PIXELATR')
   st.write("https://www.kuhl.com/kuhl/mens/long-sleeve/pixelatr-ls/")
   st.write("Size: Medium")
   st.image(["https://www.kuhl.com/media/versions/pdp/7336_bkm_p_1_19006_pdp_photo.jpg","https://www.kuhl.com/media/versions/pdp/7336_obx_p_1_18946_pdp_photo.jpg"],
   caption=["Black Moss","Oxblood"])

   st.subheader('Spekter Pullover Hoody')
   st.write('https://www.kuhl.com/kuhl/mens/long-sleeve/spekter-pullover-hoody/')
   st.write('Size: Medium')
   st.image('https://www.kuhl.com/media/versions/pdp/3192_spekter-pullover_hoody_olive-grove_front_pdp_photo.jpg',
   caption='Olive Grove')

   st.subheader('Atlas Sweatpant')
   st.write("Size: Medium")
   st.write('https://www.tentree.com/collections/organic-cotton-sweatpants/products/mens-atlas-sweatpant-silver-cloud-grey-heather')
   st.image('https://cdn.shopify.com/s/files/1/2341/3995/products/grey_cotton_sweatpants_TCM1471_1634_1.jpg?v=1656986734&width=400',
   caption='Silver Cloud Grey Heather')

   st.header('Other')
   st.subheader('YETI Cooler Bag')
   st.write('Color: Navy, Size: M30')
   st.write('https://www.yeti.com/coolers/soft-coolers/totes/18060130090.html')
   st.image('https://yeti-web.imgix.net/7f4fbed3fb6079de/W-Hopper_M30_Navy_Front_Strap_1824_B.png?bg=0fff&auto=format&w=1920&h=1920',
   caption='Navy')
   st.subheader('Luggage')

with tab2:
   st.header("Hannah")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)