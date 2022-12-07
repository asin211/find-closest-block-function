"""

*************Find an index of an array close to office and cafe in that block**********************
-If cafe and office is in the same block, return the index of that block(means facilities are at 0 step away).
- Otherwise return the block which is close to office and cafe, & is minimum steps away from the returned block for both facilities(each block is one step).

For Example: Index 7 which is currently commented has both facilities, should be returned, is 0 steps away(both facilities are in same block).
Another Case example: For index 1, cafe (on index 2) and office (on index 0) is only one step away OR for index 2 (cafe is on that index and office is only 1 step away)
OR index 3 (office is there and cafe is only one step away) is also 1 step for both facilities. 

NOTE : All three cases are only one step away from both facilities, return only one block out of these, if there is more than one block returning same number of steps.

NOTE: Function should return minimum steps for both facilities from return block.

"""
class ClosestBlock:
    def __init__(self):
        self.cafe_block = []
        self.office_block = []
        self.both_block = []

    def add_both(self, indexNum):
        self.both_block.append(indexNum)

    def add_cafe(self, indexNum):
        self.cafe_block.append(indexNum)

    def add_office(self, indexNum):
        self.office_block.append(indexNum)

    def checkClosestBlockForFacilities(self):  
        if self.both_block:
            return self.both_block[0]                              # returning the only 0 index of an array for both facilities
        else:
            new_block_index = False
            margin = 0
            new_margin = 100
            for i in self.office_block:
                for j in self.cafe_block:
                    if not margin:
                        margin = abs((i - j))                  #setting margin between index of facilities of two arrays, only return positive numbers
                        new_block_index = int((i + j) / 2)     #targeting int index closest to both facilities (adding both index and dividing by 2)
                    else:
                        new_margin = abs((i - j))              #setting new margin to compare with old margin
                    
                    if new_margin < margin:                    #replacing margin and index of returned block (closer) with new margin if its lower than margin
                        margin = new_margin                  
                        new_block_index = int((i + j) / 2)
            return new_block_index                             # returning the index of closest block for both facilities


# function which takes x array/list as an argument
# print(checkClosestBlockForFacilities(x))

