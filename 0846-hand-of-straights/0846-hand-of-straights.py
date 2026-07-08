class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        freq = {}
        hand.sort()
        if len(hand)%groupSize!=0:
            return False
        for num in hand:
            freq[num] = freq.get(num,0)+1
        for num in hand:
            if freq[num] == 0:
                continue
            start = num
            for i in range(groupSize):
                if freq.get(start+i,0)==0:
                    return False
                freq[start+i]-=1
        return True

        