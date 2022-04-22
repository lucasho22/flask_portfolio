{% include navigation.html %}

# Create Task Project
My create task idea is to make a fun guessing game on shirts. The game has instuction on how to play it. It will have user input, procedures, and lists. First, there will be a input of what shirt to find so you can get information. Next, you answer the questions to get a result.

## Runtime
[CB Video](https://drive.google.com/file/d/1rJfjfHdiAOtJWwzvG578E0JszW91IDtJ/view?usp=sharing)
### 3a. 
* The purpose of my create task is to make a guessing game that users can interact with. It uses functions, lists, sequencing, and a lot of other things to help make the game work. 
* The first part is the one where you search for a shirt and it gives the list of data about the shirt. Here, I have a stored list of data and there is a function that gets the output based on the input. For the second part, you click buttons and answer questions truthfully about the shirt.
* The outputs are all based on the input. When you type in a shirt, it will go through the function and give you the output, which is the data of the shirt you imputed. For the buttons, the outputs happen because of the button you clicked. If you click yes, you will get to the next question.

### 3b.
* The name of the list is tableshirts. The id is tableshirts. 
* The data in the list shows the information about each shirt. You can use the information to play the game.
* This list manages complexity because it makes the actual script writing for the function easier. Instead of having to write out each word about the shirt for the function and then make a table and display only one. Without the list, the code wouldn't be possible because then I wouldn't only have one row showing when you searched one shirt. You just put an id and getElementById to get that row.

### 3c. 
* The procedure is for a search bar. Based on the shirt you type in, a certain row of data appears. If you search for a shirt, it finds the data and displays it. Because it is able to display data about the shirts, it allows users to then play the game by clicking yes or not buttons.
* The procedure's name is called "input" and what it does is it hides and unhides certain table rows that contain the data from the list. It hides and unhides certain rows based on which shirt the user searches. If you searched for Nike shirt, it would unhide the data for the Nike shirt but keep all the other data hidden. I assigned ids for each row of data so when you search up a shirt, it will unhide it. Also, in the buttons, I have functions for each button, and if you click that button, it has a certain output. 

### 3d. 
* The first call is for the search bar. What it does is it calls the id for terms, which is the id of the search bar. It uses the search bar for the function to work.
* The second call is for the buttons. There are multiple functions, but there are ids for each button, so it calls each button for each function so there can be a procedure for each button so it is actually clickable and has results.
 The condition for the first call is if the user typed in a certain shirt, it will display the data for that shirt. For the function to work, the words searched by the user have to match one of the listed shirts. 
 The condition for the second call is that if that button is clicked, then it goes through the function and executes the function. If the button is clicked, then the function will work.
 The result for the first call is for the data of the searched shirt to appear. Once the function has been done, and all the conditions are met for the call, then the function goes through the procedure and makes certain rows appear. 
 The result for the second call is for new questions and buttons to appear. If a user clicks the yes button, it will take them to the next question until the game guesses the shirt. 

## Code
python

``` 
{% block body %}

    <style>
        body {
            background: #5373e0;
        }
    </style>
## Instructions for how to use the create task
    <center style="font-size: x-large">Type in one of the four shirts you want to think about for the game. When you submit, it will give you the information you will need to know for the game. Choose from the nike shirt, the turtleneck, the flannel shirt, and the long sleeve shirt.</center>

    <table> # Pictures of the shirts, linked to static
        <tr>
            <td>Flannel Shirt <img id="image" src="/static/pictures/flannel.png" height = "270" width = "270"> </td>
            <td>Turtleneck Shirt <img id="image" src="/static/pictures/turtleneck.png" height ="270" width = "270"></td>
            <td>Nike Shirt <img id="image" src="/static/pictures/nikeShirt.png" height = "270" width = "270"> </td>
            <td>Long Sleeve Shirt <img id="image" src="/static/pictures/longSleeve.png" height ="220" width = "220"></td>
        </tr>
    </table>

    <div class="text-white pt-3"> # This stores data in a table list, so when you input the name, the data for the input will appear
        <table id="tableShirts" class="table" style="visibility: collapse">
            <thead>
            <tr id="shirtHeader" style="visibility: collapse">
                <th class="text-white bg-primary">Name</th>
                <th class="text-white bg-primary">Sleeves</th>
                <th class="text-white bg-primary">Buttons</th>
                <th class="text-white bg-primary">Formal</th>
            </tr>
            </thead>
            <tbody>
            <tr id="flannelShirt" style="visibility: collapse">
                <td class="text-dark bg-white">Flannel</td>
                <td class="text-dark bg-white">Long sleeves</td>
                <td class="text-dark bg-white">Yes buttons</td>
                <td class="text-dark bg-white">Not formal</td>
            </tr>
            <tr id="turtleneck" style="visibility: collapse">
                <td class="text-dark bg-white">Turtleneck</td>
                <td class="text-dark bg-white">Long sleeves</td>
                <td class="text-dark bg-white">No buttons</td>
                <td class="text-dark bg-white">Not formal</td>
            </tr>
            <tr id="nikeShirt" style="visibility: collapse">
                <td class="text-dark bg-white">Nike</td>
                <td class="text-dark bg-white">Short sleeves</td>
                <td class="text-dark bg-white">No buttons</td>
                <td class="text-dark bg-white">Not formal</td>
            </tr>
            <tr id="longSleeve" style="visibility: collapse">
                <td class="text-dark bg-white">Long sleeve shirt</td>
                <td class="text-dark bg-white">Long sleeves</td>
                <td class="text-dark bg-white">Yes buttons</td>
                <td class="text-dark bg-white">Formal</td>
            </tr>
            </tbody>
        </table>
    </div>

    <div class="align-center pt-5" style="padding-left: 10px"> # Input search
        <input type="text" id="terms" placeholder="Search for a shirt" size="50">
    </div>
    <div class="align-center" style="padding-left: 10px">
        <button id="submit_text" onclick="input();">Submit</button>
    </div>

    <div class="row align-center p-3">
        <div class="container text-white" id="output"> </div>
    </div>

    <script> <!--Function for the code. Certain rows are displayed based on the input. document.getElementById to make those ids from the table collapse or become visible-->
        function input() {
            if (document.getElementById('terms').value.toLowerCase() == 'flannel' ||
                document.getElementById('terms').value.toLowerCase() == 'flannel shirt') {
                document.getElementById('tableShirts').style.visibility = "visible";
                document.getElementById('shirtHeader').style.visibility = "visible";
                document.getElementById('nikeShirt').style.visibility = "collapse";
                document.getElementById('turtleneck').style.visibility = "collapse";
                document.getElementById('longSleeve').style.visibility = "collapse";
                document.getElementById('flannelShirt').style.visibility = "visible";
            } else if (document.getElementById('terms').value.toLowerCase() == 'nike' ||
                document.getElementById('terms').value.toLowerCase() == 'nike shirt') {
                document.getElementById('tableShirts').style.visibility = "visible";
                document.getElementById('shirtHeader').style.visibility = "visible";
                document.getElementById('flannelShirt').style.visibility = "collapse";
                document.getElementById('turtleneck').style.visibility = "collapse";
                document.getElementById('longSleeve').style.visibility = "collapse";
                document.getElementById('nikeShirt').style.visibility = "visible";
            } else if (document.getElementById('terms').value.toLowerCase() == 'turtleneck' ||
                document.getElementById('terms').value.toLowerCase() == 'turtleneck shirt') {
                document.getElementById('tableShirts').style.visibility = "visible";
                document.getElementById('shirtHeader').style.visibility = "visible";
                document.getElementById('flannelShirt').style.visibility = "collapse";
                document.getElementById('turtleneck').style.visibility = "visible";
                document.getElementById('longSleeve').style.visibility = "collapse";
                document.getElementById('nikeShirt').style.visibility = "collapse";
            } else if (document.getElementById('terms').value.toLowerCase() == 'long sleeve' ||
                document.getElementById('terms').value.toLowerCase() == 'long sleeve shirt') {
                document.getElementById('tableShirts').style.visibility = "visible";
                document.getElementById('shirtHeader').style.visibility = "visible";
                document.getElementById('flannelShirt').style.visibility = "collapse";
                document.getElementById('turtleneck').style.visibility = "collapse";
                document.getElementById('longSleeve').style.visibility = "visible";
                document.getElementById('nikeShirt').style.visibility = "collapse";
            }else {
                document.getElementById('tableShirts').style.visibility = "collapse";
                document.getElementById('shirtHeader').style.visibility = "collapse";
                document.getElementById('flannelShirt').style.visibility = "collapse";
                document.getElementById('turtleneck').style.visibility = "collapse";
                document.getElementById('longSleeve').style.visibility = "collapse";
                document.getElementById('nikeShirt').style.visibility = "collapse";
            }
        }
    </script>

    <form action="javascript:void(0);">

        # Makes the questions with yes or no answers, with ids to connect to the script
        <body>
        <div id="longSleeveQuestion" style="padding-left: 10px">
            <legend>Question 1</legend>
            <h4>Does your shirt have long sleeves?</h4>
            <button id="yes" style="font-size: x-large" onclick="yesClickLongSleeve();">yes</button>
            <button id="no" style="font-size: x-large" onclick="noClickLongSleeve();">no</button>
        </div>

        <div id="buttonQuestion" style="display: none; padding-left: 10px">
            <legend>Question 2</legend>
            <h4>Does your shirt have buttons?</h4>
            <button id="yes1" style="font-size: x-large" onclick="yesClickButtons();">yes</button>
            <button id="no1" style="font-size: x-large" onclick="noClickButtons();">no</button>
        </div>

        <div id="formalQuestion" style="display: none; padding-left: 10px">
            <legend>Question 3</legend>
            <h4>Is your shirt formal?</h4>
            <button id="yes2" style="font-size: x-large" onclick="yesClickFormal();">yes</button>
            <button id="no2" style="font-size: x-large" onclick="noClickFormal();">no</button>
        </div>

        <div id="outputDiv" style="font-size: x-large; color: darkred; padding-left: 10px">
        </div>
        </body>

        # Script goes through for each function, and gets the ids to hide it and get the next question 
        <script>
            function yesClickLongSleeve() {
                document.getElementById("longSleeveQuestion").style.display = "none";
                document.getElementById("buttonQuestion").style.display = "block";
            }

            function noClickLongSleeve() {
                document.getElementById("outputDiv").innerHTML = "Is your shirt the Nike shirt?";
            }

            function yesClickButtons() {
                document.getElementById("buttonQuestion").style.display = "none";
                document.getElementById("formalQuestion").style.display = "block";
            }

            function noClickButtons() {
                document.getElementById("outputDiv").innerHTML = "Is your shirt the turtleneck?";
            }

            function yesClickFormal() {
                document.getElementById("buttonQuestion").style.display = "none";
                document.getElementById("outputDiv").innerHTML = "Is your shirt the long sleeve dress shirt?";
            }

            function noClickFormal() {
                document.getElementById("outputDiv").innerHTML = "Is your shirt the flannel?";
            }
        </script>

    </form>

{% endblock %}
```
