import sys
f=open(sys.argv[1], 'r')
states=[]
alphabet=[]
S=0
F=[]
transitions={}
while line:=f.readline():   #cat timp mai sunt linii de citit
    if "Sigma" in line:    #daca pe linie e Sigma atunci incepe citirea alfabetului
        while "End" not in (line:=f.readline()):
            alphabet.append(line.split('letter')[1].split('\n')[0])
    elif "States" in line:    #daca pe linie e States atunci incepe citirea starilor
        while "End" not in (line:=f.readline()):
            if ("S" in line) and ("F" in line):    #trateaza cazul cand pe linie e si S si F
                S=line.split('state')[1].split(' ,S ,F')[0]
                F.append(S)
                states.append(S)
            elif "S" in line:   #trateaza cazul cand starea e cea initiala
                S=line.split('state')[1].split(' ,S')[0]
                states.append(S)
            elif "F" in line:   #trateaza cazul cand starea e finala
                F.append(line.split('state')[1].split(' ,F')[0])
                states.append(F[len(F)-1])
            else:
                states.append(line.split('state')[1].split('\n')[0])
    elif "Transitions" in line:   #daca pe linie e Transitions, incepe citirea tranzitiilor de la linia urmatoare
        while "End" not in (line:=f.readline()):    #citim pana dam de End pe linie
            line=line.split(' ,')
            t=[]
            t.append(line[0].split('state')[1])
            t.append(line[1].split('letter')[1])
            t.append(line[2].split('state')[1].split('\n')[0])
            if (t[0] not in states) or (t[2] not in states) or (t[1] not in alphabet):
                exit("INVALID DFA")     #tratez validitatea starilor si a literei
            if (t[0], t[2]) in transitions:
                transitions[(t[0], t[2])].append(t[1])    
            else:
                transitions[(t[0], t[2])]=[t[1]]    #pentru formatul din pdf, t[0] si t[2] sunt stari, iar t[1] e litera din alfabet
for (x, y) in transitions:
    for cost1 in transitions[(x, y)]: #pentru toate combinatiile (x, y) existente caut (x, z) valid cu valoare muchiei(x, y)= valoarea muchiei (x, z)
        for z in states:
            if (x, z) in transitions and y!=z:
                for cost2 in transitions[(x, z)]:
                    if cost1==cost2: #daca exista o pereche (x, y, z) care satisface conditiile de mai sus, DFA-ul e nedeterminist
                        exit("INVALID DFA")
exit("VALID DFA")      #daca ajunge pana la sfarsit fara sa dea de celelalte stopuri, e valid
