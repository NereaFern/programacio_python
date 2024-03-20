#RO_Pag_83_ex_2_mesos_setmanes_i_dies.py
'''2. Dado un dato con la cantidad de días. Encuentre el equivalente en meses, semanas y
días sobrantes. Suponga que cada mes tiene treinta días. '''

dies=int(input("Posi la quantitat de dies: "))

mesos = dies//30
setmanes = (dies%30)//7
dies = dies-(setmanes*7)-(mesos*30)
print(mesos, "mesos, ", setmanes, "setmanes i ", dies, "dies")