# Google-Form-Automation

Why spend minutes when all you need is seconds.


## How this works

There are two scripts <br>1> `test_script` : If your form has no additional recaptcha
 <br> 2> `attendance` script : If yhe form has a recpatcha.<br>
 p.s. :I have added workaround for the recpatcha i.e. opening the form in browswer.I wish to add recaptcha bypassing using DL later.


### Adding your details

You can use these scripts as template or if you are from the same class as mine :) you can just edit the personal details in the script.If you are using it as a template you may need to add your own URL and entry points for the data.

## Running the Script

Clone the repository to your local machine.Copy the address of the folder.In this case the address is `home/user/`.<br>This project has been developed using minimum dependencies and packages that come with base python installation.Feel free to recheck if all packages are installed in your local machine.

Run the script using python :


```python /home/user/Google-Form-Automation/attendence.py```


It will ask you for the period number.

```Enter the preiod of the day :```

Enter the period number.For the first period enter 1 (n for the nth period).

## Last Steps.

If you are using non-captcha script then script is automatically submitted.<br>If you are using the  `attendance` script a browser opens with all slots filled.Just press `Sumbit`.

Congrats!! Your attendence is recorded.