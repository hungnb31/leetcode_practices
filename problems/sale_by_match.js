function sockMerchant(n, ar) {
  // Write your code here
  const pairing = [];
  let total = 0;
  for (let i of ar) {
    if (!pairing.includes(i)) {
      pairing.push(i);
    } else {
      pairing.splice(pairing.indexOf(i), 1);
      total += 1;
    }
  }
  return total;
}
