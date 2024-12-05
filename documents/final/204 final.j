CONJECTUREPANEL MostEpicSequents
PROOF "G, C, T ⊢ G→(C∨T)∨¬(C∨T)"
INFER G,
     C,
     T 
     ⊢ G→(C∨T)∨¬(C∨T)
FORMULAE
0 C∨T,
1 ¬(C∨T),
2 (C∨T)∨¬(C∨T),
3 G,
4 C,
5 T,
6 G→(C∨T)∨¬(C∨T)
IS
SEQ (cut[B,C\0,6]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\5,4]) (hyp[A\4])) ("→ intro"[A,B\3,2]) (cut[B,C\0,2]) (hyp[A\0]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\1,0]) (hyp[A\0]))
END
CONJECTUREPANEL MostEpicSequents
PROOF "A, C, T, D2, D4, D2∨D4∧¬CP→DM, A∧(C∨T)→CP ⊢ DM"
INFER A,
     C,
     T,
     D2,
     D4,
     D2∨D4∧¬CP→DM,
     A∧(C∨T)→CP 
     ⊢ DM 
FORMULAE
0 DM,
1 D2∨D4∧¬CP,
2 D2∨D4∧¬CP→DM,
3 D2,
4 D4∧¬CP,
5 A∧(C∨T),
6 A∧(C∨T)→CP,
7 CP,
8 C∨T,
9 A,
10 C,
11 T,
12 D4 
IS
SEQ (cut[B,C\8,0]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\11,10]) (hyp[A\10])) (cut[B,C\5,0]) ("∧ intro"[A,B\9,8]) (hyp[A\9]) (hyp[A\8]) (cut[B,C\7,0]) ("→ elim"[A,B\5,7]) (hyp[A\6]) (hyp[A\5]) (cut[B,C\1,0]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\4,3]) (hyp[A\3])) (cut[B,C\0,0]) ("→ elim"[A,B\1,0]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL MostEpicSequents
PROOF "CP, C, T, G ⊢ CP→C∨T∨G"
INFER CP,
     C,
     T,
     G 
     ⊢ CP→C∨T∨G 
FORMULAE
0 C∨T∨G,
1 CP,
2 C∨T,
3 G,
4 CP→C∨T∨G,
5 C,
6 T 
IS
SEQ (cut[B,C\2,4]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\6,5]) (hyp[A\5])) (cut[B,C\0,4]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\3,2]) (hyp[A\2])) ("→ intro"[A,B\1,0]) (hyp[A\0])
END
CONJECTUREPANEL MostEpicSequents
PROOF "D2, A2, D4, A4, DM ⊢ (D2∧¬A2)∨(D4∧¬A4)→¬CP∧DM"
INFER D2,
     A2,
     D4,
     A4,
     DM 
     ⊢ (D2∧¬A2)∨(D4∧¬A4)→¬CP∧DM 
FORMULAE
0 DM,
1 ¬CP,
2 ⊥,
3 ¬A4,
4 A4,
5 D4∧¬A4,
6 D4,
7 ¬A2,
8 A2,
9 D2∧¬A2,
10 D2,
11 D2∧¬A2∨D4∧¬A4,
12 ¬CP∧DM,
13 (D2∧¬A2)∨(D4∧¬A4)
IS
SEQ ("→ intro"[A,B\13,12]) (cut[B,C\1,12]) ("∨ elim"[A,B,C\9,5,1]) (hyp[A\11]) (cut[B,C\7,1]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\10,7]) (hyp[A\9])) (cut[B,C\2,1]) ("¬ elim"[B\8]) (hyp[A\8]) (hyp[A\7]) ("contra (constructive)"[B\1]) (hyp[A\2]) (cut[B,C\3,1]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\6,3]) (hyp[A\5])) (cut[B,C\2,1]) ("¬ elim"[B\4]) (hyp[A\4]) (hyp[A\3]) ("contra (constructive)"[B\1]) (hyp[A\2]) ("∧ intro"[A,B\1,0]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL MostEpicSequents
PROOF "A, R, S ⊢ A∧(¬R∧¬S)→CP"
INFER A,
     R,
     S 
     ⊢ A∧(¬R∧¬S)→CP 
FORMULAE
0 ⊥,
1 CP,
2 ¬S,
3 S,
4 ¬R∧¬S,
5 ¬R,
6 A∧(¬R∧¬S),
7 A,
8 A∧(¬R∧¬S),
9 R 
IS
SEQ ("→ intro"[A,B\8,1]) (cut[B,C\4,1]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\7,4]) (hyp[A\6])) (cut[B,C\2,1]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\5,2]) (hyp[A\4])) (cut[B,C\0,1]) ("¬ elim"[B\3]) (hyp[A\3]) (hyp[A\2]) ("contra (constructive)"[B\1]) (hyp[A\0])
END
