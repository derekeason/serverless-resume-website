var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:
       document.getElementById("visits").innerHTML = xhttp.responseText;
    }
};
xhttp.open("GET", "https://i3y29g1rz2.execute-api.us-west-1.amazonaws.com/Prod/counter", true);
xhttp.send();
