from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "CV"
PAGE_ICON = ":computer:"
NAME = "Grzegorz Tomczyk"
DESCRIPTION = """
Data support lead
"""
EMAIL = "tomczykgreg@outlook.com"
SOCIAL_MEDIA = {
    
    "LinkedIn": "https://uk.linkedin.com/in/grzegorz-greg-tomczyk-122934167"
    
}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
Power BI, DAX, SAP, EXCEL (VLOOKUP, INDEX/MATCH, Pivot tables, nested if), VBA, SQL, Python (NumPy, Pandas, Matplotlib), Snowflake, AWS S3, ETL, Spotfire, IBM Maximo
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("**Data Support Lead  | Smith & Nephew plc**")
st.write("April 2022 - - Present")
st.write(
    """
- Responsible for modelling data, modifying the database design as needed, updating the database, and ingesting data from various on-premise and cloud data sources like SQL and Snowflake in products certification project. Creating reports for weekly and monthly summaries. Improved Power BI reports and dashboards for commercial, regulatory, and data portfolio teams.
Working with data engineers, business analysts, and directors on a system migration project. Responsible for data profiling, identifying discrepancies, and managing data transformation and mapping. Developed validation criteria and test cases. Assisted IT in the build, test, and deployment phases.
"""
)

# --- JOB 2
st.write('\n')
st.write( "**Data Analyst | SIEMENS**")
st.write("June 2019 – April 2022")
st.write(
    """
- Analysed rolling stock performance, energy consumption, usage statistics, and maintenance needs. Used time series analysis techniques to enhance operational effectiveness. Developed and maintained interactive dashboards and reports using Power BI.
"""
)

# --- JOB 3
st.write('\n')
st.write("**Data specialist | Kingfisher plc**")
st.write("May 2018 - June 2019")
st.write(
    """
- Handled a variety of information including product-related data, logistics, cost prices, vendor data, and Bill of Materials (BOM). Managed master data in SAP and worked with large datasets in Excel and SQL. Developed KPI dashboards to monitor metrics such as change requests and on-time completion percentages. Supported the data modelling team with data enrichment activities to ensure accurate capturing of data model changes. Collected data and resolved incidents within the agreed Service Level Agreements.
"""
)

# --- JOB 4
st.write('\n')
st.write("**Data specialist | Ultima Business Solutions**")
st.write("January 2018 – April 2018")
st.write(
    """
- Data cleansing and transformation. Developed and maintained KPI dashboards for the service operation department. Managed data within Microsoft Dynamics 365 (2016), assigning products and services to instances according to documentation standards.
"""
)
# --- JOB 5
st.write('\n')
st.write("**Master data officer| Clinigen plc**")
st.write("October 2017 – Dec 2017")
st.write(
    """
- Cleansed datasets to achieve desired data quality standards. Maintained master data in Oracle E-Business Suite; ran reports on vendors – products-prices related; created new users, granted access to modules, handled support tickets in IT Service for Oracle EBS; prepared testing upload templates (mapping-Excel-CSV-TXT) for consultants.
"""
)

# --- JOB 6
st.write('\n')
st.write("**Technical administrator| Telefonica O2**")
st.write("October 2016 – October 2017")
st.write(
    """
- Managed radio data in Excel, ensuring high accuracy; prepared data and executed 2G/3G network coverage predictions using ATOLL Radio Planning Software. Produced signal coverage zone maps using GIS software, MapInfo. Provided technical support to radio engineers and developed PowerPoint presentations. Produced detailed reports for internal teams and commercial O2 partners. Operated independently, taking responsibility for meeting critical deadlines.
"""
)

