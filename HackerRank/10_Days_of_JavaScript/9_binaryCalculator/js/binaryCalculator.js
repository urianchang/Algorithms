let res = document.getElementById("res");

function handleClick(ev) {
  let btn = ev.target || ev.srcElement;
  let txt = document.getElementById(btn.id).innerHTML;
  if (txt === "C") {
    res.innerHTML = "";
  } else if (txt === "=") {
    //: Look for binary number strings and replace with base-10 integers
    const reBinary = /[01]+/g;
    const convertedStr = res.innerHTML.replace(reBinary, (m) => parseInt(m, 2));
    //: Evaluate and return a binary number
    res.innerHTML = eval(convertedStr).toString(2);
  } else {
    res.innerHTML = res.innerHTML + txt;
  }
}

//: Add button functionality
document.getElementById('btn0').onclick = handleClick;
document.getElementById('btn1').onclick = handleClick;
document.getElementById('btnClr').onclick = handleClick;
document.getElementById('btnEql').onclick = handleClick;
document.getElementById('btnSum').onclick = handleClick;
document.getElementById('btnSub').onclick = handleClick;
document.getElementById('btnMul').onclick = handleClick;
document.getElementById('btnDiv').onclick = handleClick;
