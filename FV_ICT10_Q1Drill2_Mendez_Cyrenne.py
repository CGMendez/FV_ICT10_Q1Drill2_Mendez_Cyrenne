from js import document

def show_myinfo(event = None):
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    # Using a multiline string (triple quotes) to format the output.
    # Escape Characters used: \n (new line) and \t (tab).
    message = f"""  
    <div class='result-title'>Student Profile</div>
    Name: {name} <br>
    Age: {age} <br>
    School: {school} <br>

    <br>
    <div class='result-title notes-title'>More Info</div>
    <span class='notes'>\n\t{name} is at the of age of {age} years old and studies at the school of {school}. This information was gathered through input fields and 
    displayed using a multiline string in Python via PyScript</span>
        """
    
    # Clears the previous message before showing a new one.
    result = document.getElementById("result")
    result.innerHTML = message
    result.style.display = "block"

def clear_myinfo(event = None):
    document.getElementById("name").value = ""
    document.getElementById("age").value = ""
    document.getElementById("school").value = ""


    result = document.getElementById("result")
    result.innerHTML = ""
    result.style.display = "none"



