CONJECTUREPANEL MostEpicSequents
PROOF "∀x.A(x)∧∀x.B(x)∧∀x.(¬R(x)∨S(x)) ⊢ ∀x.(A(x)∧B(x)∧(¬R(x)∨S(x)))"
INFER ∀x.A(x)∧∀x.B(x)∧∀x.(¬R(x)∨S(x))
     ⊢ ∀x.(A(x)∧B(x)∧(¬R(x)∨S(x)))
FORMULAE
0 ¬R(i)∨S(i),
1 A(i)∧B(i),
2 B(i),
3 A(i),
4 A(i)∧B(i)∧(¬R(i)∨S(i)),
5 actual i,
6 ∀x.A(x),
7 A(x),
8 i,
9 x,
10 ∀x.B(x),
11 B(x),
12 ∀x.(¬R(x)∨S(x)),
13 ¬R(x)∨S(x),
14 A(x)∧B(x)∧(¬R(x)∨S(x)),
15 ∀x.A(x)∧∀x.B(x),
16 ∀x.(A(x)∧B(x)∧(¬R(x)∨S(x))),
17 ∀x.A(x)∧∀x.B(x)∧∀x.(¬R(x)∨S(x)),
18 ∀x.(¬R(x)∨S(x))
IS
SEQ (cut[B,C\18,16]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\15,18]) (hyp[A\17])) (cut[B,C\15,16]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\15,18]) (hyp[A\17])) (cut[B,C\10,16]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\6,10]) (hyp[A\15])) (cut[B,C\6,16]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\6,10]) (hyp[A\15])) ("∀ intro"[i,P,x\8,14,9]) (cut[B,C\0,4]) ("∀ elim"[P,i,x\13,8,9]) (hyp[A\12]) (hyp[A\5]) (cut[B,C\2,4]) ("∀ elim"[P,i,x\11,8,9]) (hyp[A\10]) (hyp[A\5]) (cut[B,C\3,4]) ("∀ elim"[P,i,x\7,8,9]) (hyp[A\6]) (hyp[A\5]) (cut[B,C\1,4]) ("∧ intro"[A,B\3,2]) (hyp[A\3]) (hyp[A\2]) ("∧ intro"[A,B\1,0]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL MostEpicSequents
PROOF "∀x.((F(x)∨E(x))→(¬P(x)∧D(x))), ∃x.(F(x)∨E(x)) ⊢ ∃x.(¬P(x)∧D(x))"
INFER ∀x.((F(x)∨E(x))→(¬P(x)∧D(x))),
     ∃x.(F(x)∨E(x))
     ⊢ ∃x.(¬P(x)∧D(x))
FORMULAE
0 actual i,
1 ¬P(i)∧D(i),
2 ¬P(x)∧D(x),
3 i,
4 x,
5 ∃x.(¬P(x)∧D(x)),
6 F(i)∨E(i),
7 F(i)∨E(i)→¬P(i)∧D(i),
8 ∀x.((F(x)∨E(x))→(¬P(x)∧D(x))),
9 (F(x)∨E(x))→(¬P(x)∧D(x)),
10 (F(i)∨E(i))→(¬P(i)∧D(i)),
11 ∃x.(F(x)∨E(x)),
12 F(x)∨E(x),
13 ∀x.((F(x)∨E(x))→(¬P(x)∧D(x))),
14 ∃x.(F(x)∨E(x))
IS
SEQ ("∃ elim"[i,C,P,x\3,5,12,4]) (hyp[A\11]) (cut[B,C\10,5]) ("∀ elim"[P,i,x\9,3,4]) (hyp[A\8]) (hyp[A\0]) (cut[B,C\1,5]) ("→ elim"[A,B\6,1]) (hyp[A\7]) (hyp[A\6]) (cut[B,C\1,5]) (hyp[A\1]) ("∃ intro"[P,i,x\2,3,4]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL MostEpicSequents
PROOF "∀x.(¬A(x)→H(x)) ⊢ ∀x.(¬A(x))→∀x.(H(x))"
INFER ∀x.(¬A(x)→H(x))
     ⊢ ∀x.(¬A(x))→∀x.(H(x))
FORMULAE
0 H(i),
1 ¬A(i),
2 ¬A(i)→H(i),
3 actual i,
4 ∀x.(¬A(x)→H(x)),
5 ¬A(x)→H(x),
6 i,
7 x,
8 ∀x.¬A(x),
9 ¬A(x),
10 H(x),
11 ∀x.(¬A(x)),
12 ∀x.(H(x))
IS
SEQ ("→ intro"[A,B\11,12]) ("∀ intro"[i,P,x\6,10,7]) (cut[B,C\1,0]) ("∀ elim"[P,i,x\9,6,7]) (hyp[A\8]) (hyp[A\3]) (cut[B,C\2,0]) ("∀ elim"[P,i,x\5,6,7]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("→ elim"[A,B\1,0]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END