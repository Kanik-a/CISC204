CONJECTUREPANEL MostEpicSequents
PROOF "G, C, T ⊢ G→(C∨T)∨¬(C∨T)"
INFER G,
     C,
     T 
     ⊢ G→(C∨T)∨¬(C∨T)
FORMULAE
0 C∨T,
1 ¬(C∨T),
2 G,
3 (C∨T)∨¬(C∨T),
4 C,
5 T,
6 G→(C∨T)∨¬(C∨T)
IS
SEQ (cut[B,C\0,6]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\5,4]) (hyp[A\4])) ("→ intro"[A,B\2,3]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\1,0]) (hyp[A\0]))
END
CONJECTUREPANEL MostEpicSequents
PROOF "B, C, T, G ⊢ B→C∨T∨G"
INFER B,
     C,
     T,
     G 
     ⊢ B→C∨T∨G 
FORMULAE
0 C∨T∨G,
1 B,
2 C∨T,
3 G,
4 B→C∨T∨G,
5 C,
6 T 
IS
SEQ (cut[B,C\2,4]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\6,5]) (hyp[A\5])) (cut[B,C\0,4]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\3,2]) (hyp[A\2])) ("→ intro"[A,B\1,0]) (hyp[A\0])
END
CONJECTUREPANEL MostEpicSequents
PROOF "A, B, R, S, P ⊢ A∧B∧¬(R∨S)→P"
INFER A,
     B,
     R,
     S,
     P 
     ⊢ A∧B∧¬(R∨S)→P 
FORMULAE
0 P,
1 A∧B∧¬(R∨S),
2 B,
3 S,
4 R,
5 A 
IS
SEQ ("→ intro"[A,B\1,0]) (hyp[A\0])
END
CONJECTUREPANEL MostEpicSequents
PROOF "A ⊢ A∨¬A"
INFER A 
     ⊢ A∨¬A 
FORMULAE
0 A,
1 ¬A 
IS
LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\1,0]) (hyp[A\0])
END
CONJECTUREPANEL MostEpicSequents
PROOF "F, E, ¬P, D ⊢ (F∨E)→(¬P∧D)"
INFER F,
     E,
     ¬P,
     D 
     ⊢ (F∨E)→(¬P∧D)
FORMULAE
0 D,
1 ¬P,
2 F∨E,
3 ¬P∧D,
4 F,
5 E,
6 (F∨E)→(¬P∧D)
IS
SEQ (cut[B,C\2,6]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\5,4]) (hyp[A\4])) ("→ intro"[A,B\2,3]) ("∧ intro"[A,B\1,0]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL MostEpicSequents
PROOF "A, H ⊢ ¬A→H"
INFER A,
     H 
     ⊢ ¬A→H 
FORMULAE
0 H,
1 ¬A,
2 A 
IS
SEQ ("→ intro"[A,B\1,0]) (hyp[A\0])
END
