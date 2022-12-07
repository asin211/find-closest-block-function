# find-closest-block-function

*************Function for finding an index of an array/list close to the facilities (office and cafe) in that block**********************
  
-If cafe and office is in the same block, return the index of that block(means facilities are at 0 step away).

- Otherwise return the block which is close to office and cafe, & is minimum steps away from the returned block for both facilities(each block is one step).

For Example: Index 7 which is currently commented has both facilities, should be returned, is 0 steps away(both facilities are in same block).
Another Case example: For index 1, cafe (on index 2) and office (on index 0) is only one step away OR for index 2 (cafe is on that index and office is only 1 step away)
OR index 3 (office is there and cafe is only one step away) is also 1 step for both facilities. 

NOTE : All three cases are only one step away from both facilities, return only one block out of these, if there is more than one block returning same number of steps.

NOTE: Function should return minimum steps for both facilities from return block.
