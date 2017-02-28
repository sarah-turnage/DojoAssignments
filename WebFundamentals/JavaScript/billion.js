var penny = 0.01;
for (day= 1; day <= 30; day++) {
  if (day < 30) {
    penny = penny * 2;
  }
  else if (day == 30) {
    console.log("The reward was " + penny + " after 30 days.");
  }
}
