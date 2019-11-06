
import matplotlib.pyplot as plt
import numpy as np
import json

jsonFilePath = 'month2003_3.json'
jsonFilePath2 = 'month2005_3.json'
with open(jsonFilePath, 'r') as f:
    data3 = json.loads(f.read())
    
with open(jsonFilePath2, 'r') as f2:
    data32 = json.loads(f2.read())

def myplot():
    
    plt.figure(0)
    plt.plot(datax(data3),datay(data3),'ro')   
    plt.plot(datax(data32),datay(data32),'bo')
    plt.xlabel('Ozone Concentration (ppvm)')
    plt.ylabel('Altitude (Km)')
    plt.title("Ozone Distribution between Time Periods")
    plt.xlim(-0.00001, 0.00001)
    ax = plt.axes()
    plt.yticks(np.arange(0, 100,10)) 
    plt.xticks(np.arange(-0.00001, 0.00001,0.000001)) 
    plt.legend(['March 2003', 'March 2005'], loc=4)
    ax.ticklabel_format(style = 'sci', axis='x', scilimits=(0,0))
    
    plt.figure(1)
    plt.title("Mean Ozone Distribution between Time Periods")
    plt.xlabel('Ozone Concentration (ppvm)')
    plt.ylabel('Altitude (Km)')   
    datamx3,datamy3=mean(data3)
    datamx32,datamy32=mean(data32)   
    plt.plot(datamx3,datamy3,'ro')
    plt.plot(datamx32,datamy32,'bo') 
    plt.legend(['March 2003', 'March 2005'], loc=4)
    ax = plt.axes()
    ax.ticklabel_format(style = 'sci', axis='x', scilimits=(0,0))
    
    plt.show()
    

def datax(data3):
    x1=[]
    for data in data3:
        for x in data['alt_conc']:
            for y in x:
                if(y[0]!=-999.0):
                    x1.append(y[0])
    return x1
            
def datay(data3):
    y1=[]
    for data in data3:
        for x in data['alt_conc']:
            for y in x:
                if(y[0]!=-999.0):
                    y1.append(y[1])
    return y1

#def latlon():
    #lat=[]
    #lon=[]
    #for data in data3:
        #for x in data['latitude']:
            #lat.append(x)
        #for x in data['longitude']:
            #lon.append(x)
    #print(lat)
    #print(lon)
    #return lat,lon    
    
    
def mean(data3):
    alts={}
    for data in data3:
        for x in data['alt_conc']:
            for y in x:
                if(y[0]!=-999.0):
                    if round(y[1]) not in alts:
                        alts[round(y[1])]=[]
                    alts[round(y[1])].append(y[0])
    meanx=[]
    meany=[]
    for alt in alts:
        #print(alt)
        #print(alts[a1])
        sum=0
        ctr=0
        for conc in alts[alt]:
            sum+=conc
            ctr+=1
        meany.append(alt)
        meanx.append(sum/ctr)
    
    #print(meanx)
    #print(meany)
        
            
    
    return meanx,meany  
    
def main():
    #latlon()
    #for data in data3:
        #print(data)
        #for x in data['alt_conc']:
            #for y in x:
                #print(y)
    #print(data3[0]['alt_conc'][0][0][1])
    #for x in datax():
        #print(x)
    myplot()
    
if __name__ == "__main__":
    main()