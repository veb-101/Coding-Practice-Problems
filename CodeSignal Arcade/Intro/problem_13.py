def reverseInParentheses(inp):
    final = list(inp[:])
    count = inp.count("(")
    start = end = 0
    for j in range(count):
        for i in range(len(inp)):
            if final[i] == "(":
                start = i
            elif final[i] == ")":
                end = i
                final[start] = final[end] = ""
                final[start + 1:end] = reversed(final[start + 1: end])
                start = end = 0
                break
    return "".join(final)


inp = ["(bar)", "foo(bar)baz", "foo(bar)baz(blim)", "foo(bar(baz))blim", "", "()",
       "(abc)d(efg)"]

for i, j in enumerate(inp, 1):
    print(f"Test {i}: {j} -> Ans -> {reverseInParentheses(j)}")
    print()


# soln by ostap95
# better than mine
def reverseInParentheses(inputString):
    stack = []
    for x in inputString:
        if x == ")":
            tmp = ""
            while stack[-1] != "(":
                tmp += stack.pop()
            stack.pop()  # pop the (
            # print(tmp)
            for item in tmp:
                stack.append(item)
            # print(stack)
        else:
            stack.append(x)

    return "".join(stack)


inp = ["(bar)", "foo(bar)baz", "foo(bar)baz(blim)", "foo(bar(baz))blim", "", "()",
       "(abc)d(efg)"]

for i, j in enumerate(inp, 1):
    print(f"Test {i}: {j} -> Ans -> {reverseInParentheses(j)}")
    print()


# soln by dubrov
# almost similar to mine


def reverseInParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return reverseInParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s
