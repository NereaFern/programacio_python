#RO_Pag_83_ex_1_anys_mesos_i_dies.py
'''1. Dado un número entero (dias), determine y muestre el equivalente en años, meses y
días sobrantes. Por simplicidad suponga que un año tiene 365 días y que cada mes tiene
30 días. Use los operadores // y % para obtener cociente y resíduo.'''
dies = int(input("Escrigui el nombre de dies: "))
anys = dies//365
mesos = (dies%365)//30
dies =dies-(mesos*30)-(anys*365)

print(anys, "anys,", mesos, "mesos i ", dies, "dies")
