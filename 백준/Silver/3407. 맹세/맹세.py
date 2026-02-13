import sys
input=sys.stdin.readline

word=['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F',
'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co',
'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh',
'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',
'Cs', 'Ba', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt',
'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
'Fr', 'Ra', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds',
'Rg', 'Cn', 'Fl', 'Lv', 'La', 'Ce', 'Pr', 'Nd',
'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm',
'Yb', 'Lu', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am',
'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']
d={}
for i in word:
    d[i.lower()]=1

for _ in range(int(input())):
    S=input().rstrip()
    dp=[0]*(len(S))
    for i in range(len(S)):
        if i==0:
            if S[i] in d:
                dp[0]=1
            if len(S)>0 and S[i]+S[i+1] in d:
                dp[1]=1
        else:
            if S[i] in d:
                dp[i]=max(dp[i],dp[i-1])
            if i+1<len(S) and S[i]+S[i+1] in d:
                dp[i+1]=max(dp[i+1],dp[i-1])
    print('YES' if dp[-1]==1 else 'NO')