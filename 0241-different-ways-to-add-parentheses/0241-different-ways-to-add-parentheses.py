class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        # Memoization dictionary to store the results of subproblems
        memo = {}
        
        def compute(expression):
            if expression.isdigit():
                return [int(expression)]
            if expression in memo:
                return memo[expression]
            
            res = []
            for i in range(len(expression)):
                if expression[i] in "-+*":
                    left = compute(expression[:i])
                    right = compute(expression[i+1:])
                    for l in left:
                        for r in right:
                            if expression[i] == '+':
                                res.append(l + r)
                            elif expression[i] == '-':
                                res.append(l - r)
                            elif expression[i] == '*':
                                res.append(l * r)
            
            memo[expression] = res
            return res
        
        return compute(input)
