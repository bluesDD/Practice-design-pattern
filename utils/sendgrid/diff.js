function get_diff() {
  const array1 = [1, 2, 3, 4, 5, 6];
  const array2 = [1, 2, 3, 4];


  array3 = array1.filter(i => array2.indexOf(i) == -1)
  return array3; // [5, 6]
}
