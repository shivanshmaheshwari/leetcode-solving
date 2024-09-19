class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        # Memoization dictionary to store results of subproblems
        memo = {}

        def compute(expression):
            if expression.isdigit():
                return [int(expression)]
            if expression in memo:
                return memo[expression]
            
            res = []
            for i in range(len(expression)):
                if expression[i] in "+-*":
                    # Split expression into left and right parts
                    left = compute(expression[:i])
                    right = compute(expression[i+1:])
                    
                    # Combine results from left and right
                    for l in left:
                        for r in right:
                            if expression[i] == '+':
                                res.append(l + r)
                            elif expression[i] == '-':
                                res.append(l - r)
                            elif expression[i] == '*':
                                res.append(l * r)
            
            # Cache the result for the current expression
            memo[expression] = res
            return res
        
        # Start computation with the full input expression
        return compute(input)
