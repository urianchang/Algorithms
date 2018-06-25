//: Create button grid
let btns = document.createElement('div');
btns.id = "btns";

//: Create buttons
for (let i = 1; i <= 9; i++) {
  let btn = document.createElement('button');
  btn.id = `btn${i}`;
  btn.className = 'btn';
  btn.innerHTML = i;

  //: When btn5 is clicked, rotate outside button values clockwise
  if (i === 5) {
    btn.onclick = function() {
      let rotArr = [1, 4, 7, 8, 9, 6, 3, 2];
      let temp = btn1.innerHTML;
      for (let i = 0; i < rotArr.length - 1; i++) {
        let b1 = document.getElementById(`btn${rotArr[i]}`);
        let b2 = document.getElementById(`btn${rotArr[i+1]}`);
        b1.innerHTML = b2.innerHTML;
      }
      document.getElementById('btn2').innerHTML = temp;
    }
  }

  btns.appendChild(btn);
}

//: Add button grid to body
document.body.appendChild(btns);
