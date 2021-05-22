/**
 * @param {string} s
 * @return {number}
 */
 var lengthOfLastWord = function(s) {
  s = s.trim()
  return (s.slice(s.lastIndexOf(" ") + 1, s.length)).length || 0
};