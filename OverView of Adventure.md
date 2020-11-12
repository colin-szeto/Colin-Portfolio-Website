# Adventure using POST Overview: https://bit.ly/3khB2JI 

the objective of this document is to provide a framework and explanation of a flashy piece of code which will allow students to see an application using post client side (without communicating to the server). Expected understanding of routes, jinja, integration of python and html. Please excuse any spelling mistakes.

* here is a video overviewing the basics of POST: https://bit.ly/35fw1gt
* line by line explanation of POST here: https://bit.ly/3lsX0KU

### Abstract
the code is a remix of an attempt to create a chess board from dictionaries. The objective was to take the key of the decenary and use that as the identifier for interactive buttons to allow for different dimensions of the board to be configured. After getting the button to match with the keys of the dictionary the routes were configured in such a way that the routes stacked on top of one another ex: http://127.0.0.1:5000/id=c8/id=c6/id=c4/. This meant that would be many unique combinations of 64 buttons that are available to be pressed by the user. However, if one did not press buttons with POST configured, the 404-error screen for unknown path would pop up. This inspired using the 404 screens as a restart screen to route the player back the adventure homepage. So, if the player does not click the correct combination of cells, they would be redirected to home location. This meant that the programmer through the back-end would only have to define the win condition as the 404-error screen would take care of the loose screen. As there are 3 levels and 64 options with 1 correct option for each level, there are 64 * 3 possible combinations and 1 winning outcome. Perfect for a brutal role-playing game. 

### the code is broken into main parts
1."chessDict.html" - https://bit.ly/3pfPNAb - the adventure home screen (template) 
2. "main.py" - https://bit.ly/3lkju0W - route storage
3. "chessData.py" - https://bit.ly/3pg1yXC - where the story is controlled
4. "404.html" - https://bit.ly/3pbCzEF - the lose screen where player is provided opportunity to go back to the adventure home screen

### the playthrough goes as follows
1. start game
2. pick square - if wrong square restart
3. pick square - if wrong square restart
4. pick square - if wrong square restart
5. win screen

### going through the syntax
1. "404.html" - loose screen - https://bit.ly/3pbCzEF
    - a simple screen, syntax within code displays a message to prompt the player that they died
    - linked text to allow the user to click back to the adventure home screen 
    - image to father communicate to the player that they have died

2. "chessData.py" - controlling the story - https://bit.ly/3pg1yXC
    - prominently at the top of the code is the board dicot nary, again this is a dictionary used to represent the chess board, users can remove any of the keys and terms that are not the win conditions to allow for less square/options/buttons to be displayed to the user through the play through 
    - https://bit.ly/3n6JX2k - this bit of code splits up the dicot nary to only contain the keys in the dictionaries (keys in this case are "a8", "c8", "e4" etc.
    - routes List an empty list that we use to append reformatted keys to reformatted pass into chessDict.html template to label and identify the buttons
    - https://bit.ly/36pGC81 - this function "preCursor" takes the keys from keysBoard and converts the keys into routes that the buttons can use to redirect the user i.e.: "a8" is turned into "/a8"
    - everything else in the file is work in progress to support a chess game 
    
3. "main.py" - route storage - https://bit.ly/3lkju0W
    - specifically, here: https://bit.ly/3lkju0W
    - this first app.route - https://bit.ly/3pheVGM - redirects the user the apparatus adventure homepage
    - second app.route - https://bit.ly/3phftMT - creates the board (shows all of the buttons that the user can press)
        - https://bit.ly/2JUIVIz - here we see the syntax for the board being assigned as well as the hint for jinja to format in the template
    - third route - https://bit.ly/38uM0JI - this route provides user with the second hint, the URL should be seen http://127.0.0.1:5000/id=c8/
    - fourth route - https://bit.ly/3llyoE0 - this route provides user with the second hint, the URL should be seen http://127.0.0.1:5000/id=c8/id=c6/
    - fifth route - https://bit.ly/35g89Jr - the URL will be http://127.0.0.1:5000/id=c8/id=c6/id=c4/
        - this is the win screen 3 lines below, the displayCLicked = "You found the treasure!" and displays an image of the treasure chest =
    - 404 route - https://bit.ly/3lhRZF1 - this occurs when a non existing route is selected i.e.: http://127.0.0.1:5000/id=c8/id=a7/
        - the route http://127.0.0.1:5000/id=c8/id=a7/ is not defined in the main.py file and therefore will provide the player with a 404 error, using this know logic, this redirects the users to the "404.html" page which communicates to the player that they have died and are provided the opportunity to respawn    
        
4. "chessDict.html" - template - adventure home screen - https://bit.ly/3pfPNAb
    - https://bit.ly/3pbHm97 - this is the first form notice the tag <form method="post"> this is the communication protocol that the form is using, post uses URLs to send data

                <input class="button" type ="submit" formaction="/createBoard" value="Go on an adventure!" /> 

    - class="button" defines what the user interacts with
    - type="submit" defines how the user interacts with it
    - formaction="/createBoard" redirects the user to: https://bit.ly/3phftMT - creates the board (shows all of the buttons that the user can press
        
    - https://bit.ly/3khvGhA this form tag encloses the jinja logic that we use to itterate through the "oard"dictonary defined in "hessData.py"
     
                {% for header in rowList %} <!-- using jinja to make as many buttons as included in the board dictonary -->
                    <th><input class="button" type ="submit" value={{header}} formaction={{keyRoutes[header]}} id={{header}}/></th>
                {% endfor %}
 
    - class="button" defines what the user interacts with
    - type="submit" defines how the user interacts with it\
    - value={{header}} is the value that the users sees i.e.: "a8"
    - formaction={{keyRoutes[header]}} redirects the user to: https://bit.ly/3phftMT - creates the board (shows all of the buttons that the user can press
     
     for reference if you want to edit the CSS styles of the code:
     
                {{ displayClicked }} <!-- this line is to communicate hints to the player -->

                <img src="{{ displayImage }}"> <!-- this is to display the win image -->


## Ending thoughts

this code was brought together through testing and playing around with code. Taking intential patterns of code 404 page and using it to one's advantage

can you remix this code to include multiple death screens using randrange() within functions which redirect and pass information into templates
can you add a timer with js to allow for people to complete
can you add in multiple win conditions
can you reduce the amout of items within the diconary to four to represent forward left right back 
can you change the logic in data.py and main.py to use the buttons as interactions?
