from pathlib import Path

import streamlit as st
from PIL import Image

##path section
current_dir = Path(__file__).resolve().parent
css_file = current_dir/"styles"/"main.css"
resume_file= current_dir/"assets"/"MASTER_RESUME_personal.pdf"
profile_image = current_dir/"assets"/"Profil.jpeg"

##General Settings##
Page_title ="Keerthi J S| Aerospace Engineer"
page_icon = ":wave:"
Name= "Keerthi J S"
Description = """
Aerospace Engineer| Master's student from Indian Institute of technology Madras.
"""

Email ="keerthijs70@gmail.com"

Social_media = {
    "Linkedin" :"https://www.linkedin.com/in/keerthi-j-s-a7b73623a/",
    "Github":"https://github.com/cfdcoder",
}
projects ={"BTech- OpenJet":"https://drive.google.com/file/d/1Q0GVY1fbQN-Kj0A2J6nYYD8azmaHlvb0/view?usp=sharing",
          "BTech- Computational Study of Shock wave boundary layer Interaction":"https://drive.google.com/file/d/1W1udYD87DSCjvdoqHHzELXyJc9-d9Ch4/view?usp=sharing"}



st.set_page_config(page_title= Page_title, page_icon= page_icon)
st.title("Hello There")

with open(css_file) as f:
    st.markdown("<style>{}<\style>".format(f.read()),unsafe_allow_html= True)

with open(resume_file,"rb") as pdf_file:
    PDFbyte= pdf_file.read()
profile_pic= Image.open(profile_image)

##head section
col1,col2 = st.columns(2,gap='small')
with col1:
    st.image(profile_pic,width=230)

with col2:
    st.title(Name)
    st.write(Description)
    st.download_button(
        label='Download Resume',
        data= PDFbyte,
        file_name= resume_file.name,
        mime = "application/octet-stream",
    )
    st.write(Email)

##Social links

#st.write("#")#empty space
#cols= st.columns(len(Social_media))
#for index,(platform,link) in enumerate(Social_media.items()):
#    cols[index].write(f"[{platform}({link})]") #to get current index we use enumerate


##Experience and Qualification

st.write("#")
st.subheader("Education Details")

st.write(
    """
    - Schooling- Radha Krishna Public School
    - High School- St. Aloysius PU College
    - Undergraduate- Ramaiah University of applied sciences
    - Post-Graduate- Indian Institute of technology, Madras
    """
)

#projects 

st.write('#')
st.subheader("Key projects")
st.write("---")
for project,link in projects.items():
    st.write(f"[{project}]({link})")
    
 
#Course projects

st.write("#")
st.subheader("Course Projects")

with st.expander("Design of Finocyl Solid Grain for Solid Rocket Motor (SRM)", expanded = True):
    st.markdown("""
    The solid grain in S139 motor has been redesigned to obtain the same thrust with 30% reduction in the length. Based on the CEA Analysis, BurnSim asimulation, Finocyl grain has been designed and tested.

    """)
    st.image(
        "images/finocyl_geometry.png",
        caption="Finocyl grain geometry",
        use_column_width= True
    )

with st.expander("Computational study of noise emission from a modified supersonic nozzle", expanded = True):
    st.markdown(
        """
        The project focuses on the acoustic study, for a supersonic nozzle when there is single and double shock structure present. The acoustic signals are gathered from the various location from ANSYS Fluent and the study is carried out.
        """
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(
            "images/nozzle_mach.png",
            caption="Mach contour"
        )
    with col2:
        st.image(
            "images/nozzle_pressure.png",
            caption="Pressure contour"
        )
    with col3:
        st.image(
            "images/nozzle_acoustic.png",
            caption="Acoustic Pressure varying with time"
        )
 

 
with st.expander("Numerical investigation of 2D curved shock/turbulent boundary layer interaction", expanded= True):
    st.markdown(
        """
        The project focuses on the study of shock wave boundary layer interaction, by validating the surface pressure validation along the flat plate for a curved shock generator. The study is performed at supersonic Mach number.
        """
    )
    col1, col2= st.columns(2)
    with col1:
        st.image(
            "images/SWBLI_Pressure.png",
            caption="Pressure variation along the flat plate for 14degree wedge angle"
        )
    with col2:
        st.image(
            "images/SWBLI_Mach.png",
            caption="Heat flux variation along the flat plate"

        )
with st.expander("Design of small UAV to neutralise the enemy drones", expanded= True):
    st.markdown(
        """
        The small 10kg drone is conceptually designed and modelled with a radio jamming technology. This is to ensure that the enemy drone is neutralized. The payload has weight of 2kg. The performance of the drone is studied in detail.
        """
    )
    col1, col2 = st.columns(2)
    with col1:
        st.image(
            "images/UAV1.png",
            caption = "CAD model of the UAV"
        )
    with col2:
        st.image(
            "image/UAV2.png",
            caption ="Performance parameter of UAV"
        )


