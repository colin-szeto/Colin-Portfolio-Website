# this file is to guide the PO team through how to use post

### setting up the page (regular HTML) 
be sure to create your page for people to navigate through in main: https://bit.ly/32dFYJk

### default display of the page
We are using jinja here to defalut the display of the page to nothing: https://bit.ly/3p5MTyf

### overview of the page
here is the page where people will enter in there name: https://bit.ly/34Y55Sb
we create a table in a post tag for easy formating

this line is for the input: https://bit.ly/3oYnLcw
```html <td> Your Name: </td> ``` is what labels the box

link on the logic of using post: https://bit.ly/387bwV4
```<td> <input type="text" name="inputName" required/></td> ``` is what is the text entry that the users can use to type in their name

```<input class="button" type ="submit" formaction="/printName" value="What is My name?" />``` this is what the user pressess to submit their text entry to the code. 
``` formaction="/printName" " is what calls the code in the "main.py``` file seen here: https://bit.ly/3er3ura
in the "main.py" file be sure to import ```request, redirect``` as seen here: https://bit.ly/3k76Ocp

### overview of the logic in "main.py"
see here: https://bit.ly/2HVs4Vt
