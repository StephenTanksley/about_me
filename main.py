import streamlit as st
import json
import requests
import datetime

PAGE_TITLE = "Stephen Tanksley Resume - {datetime.date.today()}"
PAGE_ICON = ":bicycle:"


def main():
    # username = "stephentanksley"
    # repo = "about_me"
    # filename = "resume.json"
    # REPO_URL = f"https://{username}:{TOKEN}@raw.githubusercontent.com/{username}/{repo}/main/{filename}"

    # headers = {
    #     "Authorization": f"token {TOKEN}",
    #     "Accept": "application/vnd.github.v4+raw"
    # }

    # res = requests.get(REPO_URL, headers=headers)

    # if res and res.status_code == 200:
    #     res = res.json()

    #     name = f"{res.get('first_name')} {res.get('last_name')}"
    #     email = res.get('email')
    #     linkedin = res.get('linkedin')
    #     github = res.get('github')
    #     education = res.get('education')
    #     languages = res.get('languages')
    #     frameworks_and_libraries = res.get('frameworks_and_libraries')
    #     databases = res.get('databases')
    #     architecture = res.get('architecture')
    #     currently_learning = res.get('currently_learning')
    #     professional_experience = res.get('professional_experience')
    #     personal_projects = res.get('personal_projects')

        
    #     st.markdown(body=f"""
    #     :small[{email} | {linkedin} | {github}]  
    #     ---  
    #     """)
    #     col1, col2 = st.columns(2, gap="small")
    #     with col1:
    #         st.write("Languages: ")
    #         st.write(languages)

    #         st.write("Frameworks/Libraries: ")
    #         st.write(frameworks_and_libraries)

    #         st.write("Databases: ")
    #         st.write(databases)

    #         st.write("Architecture: ")
    #         st.write(architecture)

    #         st.write("Education: ")
    #         st.write(education)
        
    #     with col2:
    #         st.markdown(f"""
    #         ### Stephen Tanksley
    #         #### Data Engineer
    #         """)
            
    #         st.write("An approachable, curious, driven data engineer committed to enacting progressive change to make peoples' lives better")

    #         st.markdown(f"""
    #         Professional Experience:  
              
    #         {[item for item in professional_experience]}
    #         """)

    #         st.markdown(f"""
    #         Personal Projects:  
              
    #         {[item for item in personal_projects]}
    #         """)
        
    # else:
    #     print(res)

    st.write("""
    # Stephen Tanksley


📧 [stephen.tanksley@gmail.com](mailto:stephen.tanksley@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/stephentanksley)  
💻 [GitHub](https://www.github.com/stephentanksley)

---

## 💼 Professional Experience

### **Application Engineer**  
**Select Rehabilitation** | *Jul 2022 - Present*  
- Architected extensible Docker-based Python CLI ETL utility for MS-SQL Server to Postgres migrations using Pandas and SQLAlchemy
- Developed pre-commit hooks to sanitize Pentaho Kettle files for consistent deployment across all production containers
- Modularized job configurations to allow per-table debugging, improving DX and flexibility
- Converted workflows to event-driven orchestration using Job Scheduler 7
- Provided Python mentorship to remove team blockers
- Automated project environment setup, cutting ramp-up time by 50%
- Integrated container with new batches of facilities into daily ETL processes
- Modeled new views to enhance data accuracy in Payroll Based Journaling procedures for HIPAA compliance, reducing miscategorized employees from ~125 per month to  <5
- Created PyTest integration test suite for PostgreSQL data validation

---

### **Data Engineer I**  
**JLL Technologies** | *Jul 2021 - Jul 2022*  
- Improved PySpark ETL framework using Azure
- Scheduled ETL jobs targeting SQL marts and Delta Lake
- Contributed to robust test suites to reduce regressions
- Migrated ~400,000 orphaned records to data lake, revealing an undiscovered clustering bug
- Standardized setup documentation, reducing onboarding from 6 to 2 hours
- Collaborated to migrate to config-driven ETL framework
- Created SME directory to expedite data ingestion efforts

---

## 🛠️ Technical Skills

**Languages:** Python, SQL, JavaScript, Rust, HTML, CSS  
**Frameworks & Libraries:** FastAPI, PySpark, Playwright, Pytest, SQLAlchemy, ReactJS, NodeJS, Express  
**Databases:** PostgreSQL, MS-SQL Server  
**Architecture:** AWS, Docker, Job Scheduler 7 (JS7), Pentaho Kettle  
**Currently Learning:** Rust, AWS Glue, AWS RDS, AWS EC2, Streamlit, Apache Kafka

---

## 🧪 Personal Projects

### **🚲 Bike Share Data Pipeline**
*Practice project to build a full-stack data pipeline and visualization tool from scratch*  
[Practicing Data Engineering from Scratch Ep. 1](https://www.linkedin.com/pulse/practicing-data-engineering-from-scratch-how-upended-tanksley-yrzgc) | [Practicing Data Engineering from Scratch Ep. 2](https://www.linkedin.com/pulse/practicing-data-engineering-from-scratch-how-upended-tanksley-u3thc)  
- Built dimensional PostgreSQL schema for Divvy Bike data
- Developed a web crawler with Playwright to retrieve and download CSVs from AWS S3
- Designed Ingestion and enrichment workflow to split records into appropriate tables and load to Docker-hosted Postgres database
- Wrote utility to handle over 75,000 Mapbox Directions API requests per run with async rate-limiting to enrich trip data
- Developed interactive Streamlit app with time filtering to show usage patterns over time
- Authored compelling copy highlighting environmental and spatial impacts of car usage in cities

**To Do:**
- Add modules on financial savings, health outcomes, advocacy outreach, and academic source references

---

### **🛡️ Pathfinder Docker Server**
*Self-hosted Foundry VTT using Raspberry Pi and Docker with Cloudflare tunneling*  
🔗 [Live Deployment](https://host.endtimes-foundry.online)  
- Migrated Foundry install from Windows to Raspberry Pi
- Created Docker Compose config for VTT deployment
- Configured Cloudflare tunnel for secure external access

---

## 🎓 Education

- **Lambda School / Bloom School of Technology**  
  *Web Development / Computer Science (Non-degree certificate)*  
  *Completed: October 2020*

- **Columbia College Chicago**  
  *MFA - Music Composition for the Screen*  
  *Completed: June 2015*

- **University of Minnesota - Duluth**  
  *MM - Master of Music, Performance*  
  *Completed: June 2012*

- **Wheaton College Conservatory of Music**  
  *BM - Bachelor of Music, Performance*  
  *Completed: June 2010*

- **Dallas Colleges**  
  *General Studies / Music (No degree awarded)*  
  *Completed: June 2006*

---

    """)

if __name__ == '__main__':
    main()