class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        current_string = []
        valid_answers = []

        def recurse (forward_parens_needed, backward_parens_needed):
            if forward_parens_needed == 0 and backward_parens_needed == 0:
                valid_answers.append("".join(current_string))
            if forward_parens_needed > 0:
                current_string.append("(")
                recurse(forward_parens_needed - 1, backward_parens_needed)
            if backward_parens_needed > 0 and forward_parens_needed < backward_parens_needed:
                current_string.append(")")
                recurse(forward_parens_needed, backward_parens_needed - 1)
            if len(current_string) > 0:
                current_string.pop()
        recurse(n, n)
        return valid_answers