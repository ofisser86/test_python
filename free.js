/**
 * Created by greta on 13.07.17.
 */
var array = [4,5,6,7,8];
var singleVal = 0;

// Only change code below this line.

singleVal = array.reduce(function(prev, current){return prev + current;}, 0);