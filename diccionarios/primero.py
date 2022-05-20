from xml.dom.expatbuilder import theDOMImplementation 

a1=dict(
    ibague=13.000,
    bogota=15.000,
    cali=56.000,
)
print(a1)
tr=0
for i in a1.values():
    tr+=i
print('Ploblacion Total es: ',tr, f'Habitantes')


    