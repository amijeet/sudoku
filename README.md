[![HitCount](http://hits.dwyl.com/amijeet/sudoku.svg)](http://hits.dwyl.com/amijeet/sudoku)
<!-- PROJECT LOGO -->
<p align="center">
  <a href="https://en.wikipedia.org/wiki/Sudoku">
    <img src="images/sudokuLogo.jpg" alt="Logo" width="115" height="100">
  </a>

  <h1 align="center">Sudoku Solver</h1>

  <p align="center">
    Visual demonstration of a backtracking algorithm solving any sudoku!
  </p>
</p>

<!-- ABOUT THE PROJECT -->
## About The Project

Like all other Backtracking problems, Sudoku can be solved by one by one assigning numbers to empty cells. Before assigning a number, check whether it is safe to assign. Check that the same number is not present in the current row, current column and current 3X3 subgrid. After checking for safety, assign the number, and recursively check whether this assignment leads to a solution or not. If the assignment doesn’t lead to a solution, then try the next number for the current empty cell. And if none of the number (1 to 9) leads to a solution, return false and print no solution exists.

Algorithm: 

1. Create a function that checks after assigning the current index the grid becomes unsafe or not. Keep Hashmap for a row, column and boxes. If any number has a frequency greater than 1 in the hashMap return false else return true; hashMap can be avoided by using loops.
2. Create a recursive function that takes a grid.
3. Check for any unassigned location. If present then assign a number from 1 to 9, check if assigning the number to current index makes the grid unsafe or not, if safe then recursively call the function for all safe cases from 0 to 9. if any recursive call returns true, end the loop and return true. If no recursive call returns true then return false.
4. If there is no unassigned location then return true. 
Check the source code from [here](https://github.com/amijeet/sudoku/blob/master/sudoku.py).

[![Product GIF][product-GIF]](https://en.wikipedia.org/wiki/Pathfinding)

<!-- USAGE EXAMPLES -->
## How to use

Just run the python script to see how backtracking would solve any sudoku.

<!-- CONTACT -->
## Contact

Amijeet Thakur - [amijeetthakur@gmail.com](mailto:amijeetthakur@gmail.com)

Project Link: [https://github.com/amijeet/sudoku](https://github.com/amijeet/sudoku)

<!-- MARKDOWN LINKS & IMAGES -->

[product-GIF]: images/sudokuGIF.gif
