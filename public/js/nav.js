var menu = document.getElementsByClassName("icon");
menu.addEventListener("click", function() {
    var x = document.getElementById("topBar");
    if (x.className === "menuBar") {
        x.className += " responsive";
    } else {
        x.className = "menuBar";
    }
  }
);
