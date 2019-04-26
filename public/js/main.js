
function dropDownMenu() {
    var x = document.getElementById("topBar");
    if (x.className === "menuBar") {
        x.className += " responsive";
    } else {
        x.className = "menuBar";
    }
}

var menu = document.getElementsByClassName("icon");
menu.addEventListener("click", dropDownMenu, false)

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var content = this.nextElementSibling;
            if (content.style.display === "block") {
            content.style.display = "none";
            } else {
            content.style.display = "block";
        }
    });
}