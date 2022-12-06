def isValid( s):
    st = []
    for c in s:
        if c == '(':
            st.append(')')
        elif c == '{':
            st.append('}')
        elif c == '[':
            st.append(']')
        elif not st or st.pop() != c:
            return False
    return not st
print(isValid(input()))
