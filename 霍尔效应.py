import numpy
import matplotlib.pyplot as plot
a = [[5.2,-5.1,5.1,-5.1],[10.3,-10.3,10.2,-10.1],[15.5,-15.2,15.3,-15.2],[20.6,-20.6,20.4,-20.3]]

b = [[5.2,-5.2,5.1,-5.0],[10.3,-10.1,10.2,-10.1],[15.4,-15.3,15.3,-15.4],[20.5,-20.4,20.4,-20.3]]

c = [[-28.1,28.0,-27.8,27.9],[-41.7,41.3,-41.2,41.3],[-54.9,54.4,-53.9,54.0],[-66.8,66.5,-65.7,66.0]]

d = [[-27.2,27.1,-27.0,27.0],[-54.3,54.1,-53.6,53.8],[-81.4,81.1,-79.8,80.0],[-108.5,108.2,-105.8,106.1]]

e = [[-9.62,9.54,-9.85,9.82],[-12.70,12.61,-12.90,12.65],[-16.12,16.05,-16.26,16.25],[-21.1,21.0,-21.2,21.1],
[-26.4,26.3,-26.4,26.4],[-37.1,37.1,-37.0,37.1],[-44.4,44.3,-44.0,44.1],[-48.6,48.5,-48.1,48.3],
[-51.6,51.5,-51.0,51.2],[-52.5,52.3,-51.9,52.0],[-53.0,52.8,-52.3,52.4],[-53.2,53.1,-52.5,52.6],
[-53.3,53.1,-52.6,52.8],[-53.2,53.1,-52.6,52.6],[-53.0,52.6,-52.1,52.2],[-52.3,52.1,-51.1,51.8],
[-51.6,51.4,-50.9,51.0],[-50.0,49.8,-49.4,49.5],[-48.6,48.4,-48.0,48.1],[-45.9,45.8,-45.4,45.5],
[-41.5,41.4,-41.4,41.2],[-34.1,34.0,-33.8,33.9],[-22.9,22.8,-22.8,22.7],[-13.7,13.6,-13.6,13.7],
[-10.6,10.6,-10.6,10.5],[-8.16,8.08,-8.15,8.12]]
def t1():
    j = numpy.array([])
    for i in a:
        t = numpy.array(i)
        j = numpy.append(j,numpy.abs(t).mean())
    return j

def t2():
    j = numpy.array([])
    for i in b:
        t = numpy.array(i)
        Vh = numpy.abs(t).mean()
        kh = 22
        Is = 4
        B = Vh/(kh*Is)
        #print((Vh,B))
        j = numpy.append(j,B)
    return j

def t3andt4():
    for t in (c,d):
        for i in t:
            j = numpy.array(i)
            print(numpy.abs(j).mean())
        print()

def t3():
    h = numpy.array([])
    for i in c:
        j = numpy.array(i)
        h = numpy.append(h,numpy.abs(j).mean()) 
    return h

def t4():
    h = numpy.array([])
    for i in d:
        j = numpy.array(i)
        h = numpy.append(h,numpy.abs(j).mean()) 
    return h

def t5():
    j = numpy.array([])
    for i in e:
        t = numpy.array(i)
        Vh = numpy.abs(t).mean()
        kh = 2737
        Is = 4
        B = Vh/(kh*Is)
        #print((Vh,B))
        j = numpy.append(j,B)
    return j
#print(t5())
rt1 = {"Is":[2.00,4.00,6.00,8.00],"Vh":t1()}
rt2 = {"IM":[200,400,600,800],"B":t2()}
rt3 = {"Is":[2.00,3.00,4.00,5.00],"VH":t3()}
rt4 = {"IM":[200,400,600,800],"VH":t4()}
figure = plot.figure(1,figsize=(10,10))
axes = figure.subplots(2,2)
axes[0][0].plot(rt1["Is"],rt1["Vh"])
axes[0][0].scatter(rt1["Is"],rt1["Vh"])
axes[0][0].set_title("VH-IS Curve (C1)")
axes[0][0].set_xlabel("Is(mA)")
axes[0][0].set_ylabel("VH(mV)")
axes[0][0].set_xlim(2,8)
axes[0][0].grid()

axes[0][1].plot(rt2["IM"],rt2["B"]*10e3)
axes[0][1].scatter(rt2["IM"],rt2["B"]*10e3)
axes[0][1].set_title("B-IM Curve (C2)")
axes[0][1].set_xlabel("IM(mA)")
axes[0][1].set_ylabel("B(*10e3 T)")
axes[0][1].set_xlim(200,800)
axes[0][1].grid()

axes[1][0].plot(rt3["Is"],rt3["VH"])
axes[1][0].scatter(rt3["Is"],rt3["VH"])
axes[1][0].set_title("VH-Is Curve (C3)")
axes[1][0].set_xlabel("Is(mA)")
axes[1][0].set_ylabel("VH(mV)")
axes[1][0].set_xlim(2,5)
axes[1][0].grid()

axes[1][1].plot(rt4["IM"],rt4["VH"])
axes[1][1].scatter(rt4["IM"],rt4["VH"])
axes[1][1].set_title("VH-IM Curve (C4)")
axes[1][1].set_xlabel("IM(mA)")
axes[1][1].set_ylabel("VH(mV)")
axes[1][1].set_xlim(200,800)
axes[1][1].grid()

f2 = plot.figure(2,figsize=(8,8))
a = f2.subplots()
x = [-10,-5,0,5]+[i for i in range(10,41,10)]+[i for i in range(60,241,20)]+[i for i in range(250,301,10)]+[305,310]
rt5 = {"X":x,"B":t5()*10e4}
plot.plot(rt5["X"],rt5["B"])
plot.scatter(rt5["X"],rt5["B"])
plot.title("B-X Curve (C5)")
plot.xlabel("x(mm)")
plot.ylabel("B(*10e-4 T)")
plot.grid()
plot.show()