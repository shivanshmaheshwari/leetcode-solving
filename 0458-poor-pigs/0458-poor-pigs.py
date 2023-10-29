class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        no_of_tests = int(minutesToTest/minutesToDie)

        possible_attempts = no_of_tests + 1
        pegs = 0
        while possible_attempts ** pegs < buckets:
            pegs +=1
        return pegs