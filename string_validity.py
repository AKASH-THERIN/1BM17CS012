class string_sol:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for a in str1:
            if a in pchar:
                stack.append(a)
            elif len(stack) == 0 or pchar[stack.pop()] != a:
                return False
        return len(stack) == 0

print(string_sol().is_valid_parenthese("(){}[]"))
print(string_sol().is_valid_parenthese("()[{)}"))
print(string_sol().is_valid_parenthese("()"))
