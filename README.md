# Google-Form-Automation

Why spend minutes when all you need is seconds.

# Why this project ?

We are having regular online classes in our college where attendance is taken by google forms. So I decided to automate a part of it.Suggestions and pull request are most welcome.From here we divide the use cases for two needs: <br>
i. My classmates reading in the same section<br>
ii. People who want to use it as a template <br>

# Features :

We have implemented most of the form features in google form.
<ol>

1. Filling forms having multiple sections.
2. Filling the date
3. Filling Email-address
4. Filling numbers
5. Filling checkboxes/mutliple choices
6. Interaction using Terminal
7. Workaround to avoid Recaptcha
8. Minimum dependency
</ol> 

## For my classmates  (IEM ECE 2nd year sec-A) 

Follow these steps to register your attendence.
<ul>

* You need to clone the repository by clicking on the <img></img> to the local machine.Extract the zip(if applicable).

* Open the `attendence.py` and insert your details.<br>By details I mean your name,eamil-id and roll no.No need to change any other details as such.<p>
For Eg :
Your name is **Jhon Stones**.<br>Email is **JhonStoner@gmail.com**.<br>
Roll No is **9**.</p>
You should fill it like :
<a name="Details.png"/>
<div align="center">
<img src="src/Details.png" alt="Edit attendence.py" width="500" height="100"></img>
</div>
</a>

* Save the file.
* Run the file using python installed in your computer using Python IDLE or terminal.
* The python program will ask for period number.Enter the period number and the browser opens with all slots filled.Press Submit and it's done.

</ul>
This is a one time process.For the next attendence you need run last two steps only .<br> 
<b>Note : Script is not applicable for ESP and SDP classes for now.<br>The script should not be used for changed routines.</b>



## To use it as a template 

There is two google forms two different purposes.
<ul>

* For forms having no recaptcha.This can be done from the command line itself.For this you can use the `test_script.py`.As the name suggests you can use this script to interact with the link in it.
* For forms having recaptcha.We need a workaround for this.We fill up all the form details and ping the browser.You can use `attendence.py` as template<br>
I am looking forward to implement DL to bypass the basic recaptcha.
</ul>

NOTE : make sure to use the correct link and in correct format.Also check the data entry points of the google form you are entering.
