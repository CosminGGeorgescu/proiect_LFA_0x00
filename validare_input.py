import sys
f=open(sys.argv[1], 'r')
states=[]
alphabet=[]
F=[]
transitions={}      #pentru explicatii la citire, vezi "validare AFD"
while line:=f.readline():
    if "Sigma" in line:
        while "End" not in (line:=f.readline()):
            alphabet.append(int(line.split('letter')[1][0]))
    elif "States" in line:
        while "End" not in (line:=f.readline()):
            if ("S" in line) and ("F" in line):
                S=int(line.split('state')[1].split()[0])
                states.append(S)
                F.append(S)
            elif "S" in line:
                S=int(line.split('state')[1].split()[0])
                states.append(S)
            elif "F" in line:
                F.append(int(line.split('state')[1].split()[0]))
                states.append(int(line.split('state')[1].split()[0]))
            else:
                states.append(int(line.split('state')[1]))
    elif "Transitions" in line:
        while "End" not in (line:=f.readline()):
            line=line.split(',')
            t=[]
            for x in line:
                t.append(int(x[len(x)-2]))
            transitions[(t[0], t[2])]=t[1]
input=sys.argv[2] #inputul de validat
i=S     #incepem de la inceput
for x in input:  #pentru fiecare litera a inputului
    j=0; s=0
    while j<len(states) and s==0:   #pentru input[x], caut pereche (i, j) cu valoarea muchiei=input[x]
        if ((i, j) in transitions) and transitions[(i, j)]==int(x):
            i=j
            s=1     #variabla kill switch
        j=j+1
    if s==0:  #la prima litera pentru care nu gaseste pereche (i, j) care sa satisfaca conditiile de mai sus, input invalid
        exit("INVALID INPUT")
if i in F:
    exit("VALID INPUT")
else:  #daca starea la care se opreste validarea inputului nu e finala, input invalid
    exit("INVALID INPUT")
