//: Create the button
let theButton = document.createElement('button');
theButton.innerHTML = "0";
theButton.id = "btn";
theButton.className = "button";
theButton.onclick = function() {
  theButton.innerHTML = Number(theButton.innerHTML) + 1;
};

//: Add it to the document body
document.body.appendChild(theButton);
