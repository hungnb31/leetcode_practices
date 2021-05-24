/**
 * @param {number} x
 * @return {number}
 */
 var reverse = function(x) {
  y = x.toString().split("").reverse().filter(ele => ele !== "-").join("")
  return +y >= Math.pow(2, 31) || +y < Math.pow(-2, 31) ? 0 : x < 0 ? +y * -1 : +y
};