import sys
f=open(sys.argv[1], 'r')
states=[]
alphabet=[]
F=[]
transitions={}
while line:=f.readline():   #cat timp mai sunt linii de citit
    if "Sigma" in line:    #daca pe linie e Sigma atunci incepe citirea alfabetului
        while "End" not in (line:=f.readline()):
            alphabet.append(int(line.split('letter')[1][0]))
    elif "States" in line:    #daca pe linie e States atunci incepe citirea starilor
        while "End" not in (line:=f.readline()):
            if ("S" in line) and ("F" in line):    #trateaza cazul cand pe linie e si S si F
                S=int(line.split('state')[1].split()[0])
                states.append(S)
                F.append(S)
            elif "S" in line:   #trateaza cazul cand starea e cea initiala
                S=int(line.split('state')[1].split()[0])
                states.append(S)
            elif "F" in line:   #trateaza cazul cand starea e finala
                F.append(int(line.split('state')[1].split()[0]))
                states.append(int(line.split('state')[1].split()[0]))
            else:
                states.append(int(line.split('state')[1]))
    elif "Transitions" in line:   #daca pe linie e Transitions, incepe citirea tranzitiilor de la linia urmatoare
        while "End" not in (line:=f.readline()):    #citim pana dam de End pe linie
            line=line.split(',')
            t=[]
            for x in line:
                t.append(int(x[len(x)-2]))
            if (t[0] not in states) or (t[2] not in states) or (t[1] not in alphabet):
                exit("INVALID DFA syntax")     #tratez validitatea starilor si a literei
            transitions[(t[0], t[2])]=t[1]     #pentru formatul din pdf, t[0] si t[2] sunt stari, iar t[1] e litera din alfabet
for x in states:
    for y in states:
        if (x, y) in transitions:
            for z in states:    #pentru toate combinatiile (x, y) existente caut (x, z) valid cu valoare muchiei(x, y)= valoarea muchiei (x, z)
                if y!=z and ((x, z) in transitions) and transitions[(x, y)]==transitions[(x, z)]:
                    exit("INVALID DFA transitions")     #daca exista o pereche (x, y, z) care satisface conditiile de mai sus, DFA-ul e nedeterminist
exit("VALID DFA")      #daca ajunge pana la sfarsit fara sa dea de celelalte stopuri, e valid
