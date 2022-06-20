class Solution:
    def areaEdge(self, h_w: int, Cuts: List[int]) -> int:
        Cuts.insert(len(Cuts), h_w)
    
        temp_list = Cuts[:-1]
        temp_list.insert(0,0)
        
        Cuts.sort()
        temp_list.sort()
        
        return [x - y for x, y in zip(Cuts, temp_list)]
    
    
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
       
        Height_edge = max(self.areaEdge(h, horizontalCuts))
        Width_edge  = max(self.areaEdge(w, verticalCuts))


        return (Height_edge*Width_edge)%(10**9+7)
    
                                           #      Question      #
      
"""Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and 
verticalCuts where horizontalCuts[i] is the distancefrom the top of the rectangular cake to the ith horizontal cut and similarly, 
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal and 
vertical position provided in the arrays horizontalCuts and verticalCuts. 
Since the answer can be a huge number, return this modulo 10^9 + 7."""

# https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3766/