def LengthOfLongestSubstring(s):
    subs=[]
    m_len=0
    lst=[]
    for c in s:
        if c not in subs:
            subs+=[c]
        else:
            m_len = max(m_len, len(subs))
            while c in subs:
                    subs.pop(0)
            subs+=[c]
        m_len = max(m_len, len(subs))
        return m_len
string=input()
print(LengthOfLongestSubstring(string))
