#Load the packages needed
from itertools import product
#This part you should enter the inputs:
#Example:
#    Female: +/+;A/a;B/b;+/+
#    Male:   +/y;A/a;B/b;+/+
#    Location: /Users/user1/Desktop    
female=input('please enter the genotype of the female fly: \nExample: A/a;B/b;C/c;D/d\n')
male=input('please enter the genotype of the male fly: \nExample: A/a;B/b;C/c;D/d\n')
location=input('Where Should the file be saved:\nExample: /Users/User1/Desktop\n').strip()
#this line will split chromosomes based on ; for each single fly
def split_chromosome(x):
    x1=x.split(';')
    return(x1)
#example
#print(split_chromosome(male))
#this code will make the f1 generation of each chromosome seperately
def split_each_chromosome(p1,p2):
    listt1=[]
    elements_p1 = p1.split('/')
    elements_p2 = p2.split('/')
    combinations = list(product(elements_p1, elements_p2))
    listt1.append(combinations)
    return listt1
#example:
#split_each_chromosome('+/+','+/y')

#this line will mate based on each chromosome individually
def combination_single_chromosome(g1,g2):
    d={}
    for n in range(4):
        l1=split_chromosome(g1)
        l2=split_chromosome(g2)
        l3=split_each_chromosome(l1[n],l2[n])
        x=('chromosome'+str(n))
        d[x]=l3[0]
    return d
d1=combination_single_chromosome(male,female)
#d1
#This line generate all the possible combinations between 4 chromosomes
#* operator is used for iterable unpacking
#the  lenght of combinations_final should be 256
all_combinations = list(d1.values())
combinations_final = list(product(*all_combinations))
#combinations_final
#len(combinations_final)
lst=[]
for n in combinations_final:
    tuple_to_format=n
    formatted_string=str(";".join(map(lambda item: f"{item[0]}/{item[1]}", tuple_to_format)))
    #print(formatted_string)
    lst.append(formatted_string)
l=[]
for n in lst:
    
    #print(n)
    x1=n.split(';')
    #print(x1)
    dd=';'.join(list(map(lambda u : '/'.join(u),list(map(lambda u : sorted(u.split('/')),x1))))).strip()
    #print(dd)
    l.append(dd)
    
outputs=set(l)
#outputs
with open(f"{location}/mating_scheme.txt", 'w') as f:
    for n in outputs:
        f.write(str(n) + '\n')
f.close()
