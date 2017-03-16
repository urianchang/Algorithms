/*
Flood Fill

Most graphical "paint" applications have a 'paintcan fill' function
that floods part of an image with a certain color. Build floodFill(canvas2D, startXY, newColor).
Replace a pixel's color value only if it is the same color as the origin coordinate
and is directly adjacent via X or Y to another pixel you will change.

NOTE: diagonally related pixels are not considered adjacent.
*/

var canvas2D = [[3,2,3,4,3],[2,3,3,4,0],[7,3,3,5,3],[6,5,3,4,1],[1,2,3,3,3]];
console.log("Before: \n", canvas2D);

function floodFill(canvas, startXY, newcolor){
  oldcolor = canvas[startXY[1]][startXY[0]];
  canvas[startXY[1]][startXY[0]] = newcolor;
  if (canvas[startXY[1]-1] != undefined){
    if (canvas[startXY[1]-1][startXY[0]] == oldcolor){
      floodFill(canvas, [startXY[0],startXY[1]-1], newcolor);
    }
  }
  if (canvas[startXY[1]][startXY[0]-1] == oldcolor){
    floodFill(canvas, [startXY[0]-1, startXY[1]], newcolor);
  }
  if (canvas[startXY[1]][startXY[0]+1] == oldcolor){
    floodFill(canvas, [startXY[0]+1, startXY[1]], newcolor);
  }
  if (canvas[startXY[1]+1] != undefined){
    if (canvas[startXY[1]+1][startXY[0]] == oldcolor){
      floodFill(canvas, [startXY[0], startXY[1]+1], newcolor);
    }
  }
}
floodFill(canvas2D, [2,2], 1);
console.log("After: \n", canvas2D);
