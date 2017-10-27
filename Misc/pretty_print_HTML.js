/* =====
  Function for pretty printing an HTML string
==== */

function prettify(s) {

  let pretty_string = ""; //: Formatted string
  let tab_count = 0;  //: Keep track of the number of tabs (spaces)

  //: Loop through HTML string, adding newline and spaces (tabs) for readability
  for (var i = 0; i < s.length; i++) {

    //: Check for opening of HTML tag
    if (s[i] === "<") {

      //: Add newline if previous character is not ">"
      if(s[i-1] !== ">" && i > 0) {
        pretty_string += "\n";
      }

      //: Don't change tab count if HTML comment
      if (s[i+1] === "!") {
        pretty_string += "  ".repeat(tab_count) + s[i];
      } else {
        //: Check if this is a closing tag --> decrease/increase tab count
        if (s[i+1] === "/") {
          tab_count--;
          pretty_string += "  ".repeat(tab_count) + s[i];
        } else {
          pretty_string += "  ".repeat(tab_count) + s[i];
          tab_count++;
        }
      }

    //: Check for end of HTML tag
    } else if (s[i] === ">" && i !== s.length-1) {
      pretty_string += s[i] + "\n";

      //: Don't automatically indent the next line if it is an HTML tag
      if (s[i+1] !== "<") {
        pretty_string += "  ".repeat(tab_count);
      }

    //: Add character to string
    } else {
      pretty_string += s[i];
    }

  } //: End of For loop

  //: Return the formatted string
  return pretty_string;
}

let str1 = "<html>hello<p>para</p><p>para2</p></html>";
console.log(prettify(str1));
