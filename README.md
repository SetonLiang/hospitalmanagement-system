# Hospitalmanagement System
The advent of Hospital Database Management Systems (HDMS) marks a transformative era in healthcare informatics, where the efficiency and accuracy of patient care are significantly enhanced through digital solutions. These systems are designed to handle a vast array of data types integral to hospital operations, including patient medical records, staff management, departmental data, and hospital resource information.
### Homepage
![image](https://github.com/SetonLiang/hospitalmanagement-system/assets/127169275/efd967b3-ce1c-4213-974f-9a6588db5036#pic_center)
### Admin dashboard
![image](https://github.com/SetonLiang/hospitalmanagement-system/assets/127169275/ccc5ef0e-b7e0-4b27-88dc-a467b99a784d)
### Doctor dashboard
![image](https://github.com/SetonLiang/hospitalmanagement-system/assets/127169275/7e3b8f57-38a2-41a3-b4c7-c98c31c0ec2d)
### Patient dashboard
![image](https://github.com/SetonLiang/hospitalmanagement-system/assets/127169275/a1d267e1-6b1e-46ed-a644-3cb3c2556df7)
## Techniques
We develop a Hospital Management System using python+Django, the process unfolds in a sequential, step-by-step manner.  
- Front-end Design
- Back-end Design
- SQL and Database Visualization
## Main Functions
- Patients can register their unique accounts in the database. 
- Doctors can register their unique account but need to be verified by the administrator. Doctors can revise their personal information, but not their department information. 
- The patients can revise some of their personal information, e.g., contact number, etc, but not their treatment information. 
- Administrator can update the database. 

## HOW TO RUN THIS PROJECT
1. Install Python(3.9.1)
2. Open Terminal and Execute Following Commands:
```
pip install django==3.0.5
pip install django-widget-tweaks
pip install xhtml2pdf
```
4. Download This Project Zip Folder and Extract it
5. Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
6. Enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```
