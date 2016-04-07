
def compositeWallParallel(resistanceList):
    """This function calculates the resistance value of resstances in parallel
    the input ("resistanceList" is a list of resistances each of which is adictionary
    for example:R1={"name":"R1","type":"cond","length":0.03,"area":0.25,"k":0.026}
    and a set of resistances resistanceList= [R1,R2,R3]
    pay attention that the units are as follows: area : m2, length : m, k= W/m.K
    the output resistancesResults is a dictionary with the following structure
     {'R1': 4.62,  'R2': 0.36,'R6': 0.36,'R_total': 5.34}
    the unit of output values is degC/W 
    """
    resistancesResults = {}
    R_tot_inv=0
    for resistance in resistanceList:
        A = resistance["area"]
        L = resistance["length"]
        k = resistance["k"]
        R= round(L/(k*A),2) #I am just taking the first two decimal points
        R_inv= 1/(R)          
        R_tot_inv += R_inv #I am updating the R_tot_inv value
        nameOfResistance = resistance["name"]
        resistancesResults[nameOfResistance] = round(R,2) #here I am saving the R value of each resitance in the results dictionary
    R_tot = 1/R_tot_inv
    resistancesResults["R_total"] = round(R_tot,2)  
    return resistancesResults  
    
def compositeWallSeries(resistanceList):
    """This function calculates the resistance value of resstances in series
    the input ("resistanceList" is a list of resistances each of which is adictionary
    for example:R1={"name":"R1","type":"cond","length":0.03,"area":0.25,"k":0.026}
    and a set of resistances resistanceList= [R1,R2,R3]
    pay attention that the units are as follows: area : m2, length : m, k= W/m.K
    the output resistancesResults is a dictionary with the following structure
     {'R1': 4.62,  'R2': 0.36,'R6': 0.36,'R_total': 5.34}
    the unit of output values is degC/W 
    """
    resistancesResults = {}
    R_tot=0
    for resistance in resistanceList:
        A = resistance["area"]
        L = resistance["length"]
        k = resistance["k"]
        R= round(L/(k*A),2)       
        R_tot += R
        nameOfResistance = resistance["name"]
        resistancesResults[nameOfResistance] = round(R,2)
    resistancesResults["R_total"] = round(R_tot,2)  
    return resistancesResults  

def compositeWall(resistanceListSeries,resistanceListParallel):
    """This function calculates the resistance value of resitances in parallel and in series
    Here is the order (resistanceListSeries,resistanceListParallel)
    the input ("resistanceListSeries" is a list of resistances each of which is adictionary
    for example:R1={"name":"R1","type":"cond","length":0.03,"area":0.25,"k":0.026}
    and a set of resistances resistanceList= [R1,R2,R3]
    pay attention that the units are as follows: area : m2, length : m, k= W/m.K
    the output resistancesResults is a dictionary with the following structure
     {'R1': 4.62,  'R2': 0.36,'R6': 0.36,'R_total': 5.34}
    the unit of output values is degC/W 
    """
    ResultsWall = {}
    seriesResults=compositeWallSeries(resistanceListSeries)
    R_tot_series = seriesResults["R_total"]
    parallelResults=compositeWallParallel(resistanceListParallel)
    R_tot_parallel = parallelResults["R_total"]
    RtotalWall = R_tot_series + R_tot_parallel
    ResultsWall["Results of series resistances"]=seriesResults
    ResultsWall["Results of parallel resistances"]=parallelResults
    ResultsWall["Overall wall's resistance"] =  RtotalWall
    return ResultsWall
    
    
Ri={"name":"Ri","type":"conv","area":0.25,"hConv":10}
R1={"name":"R1","type":"cond","length":0.03,"area":0.25,"k":0.026}
R2={"name":"R2","type":"cond","length":0.02,"area":0.25,"k":0.22}
R3={"name":"R3","type":"cond","length":0.16,"area":0.015,"k":0.22}
R4={"name":"R4","type":"cond","length":0.16,"area":0.22,"k":0.72}
R5={"name":"R5","type":"cond","length":0.16,"area":0.015,"k":0.22}
R6={"name":"R6","type":"cond","length":0.02,"area":0.25,"k":0.22}
Ro={"name":"Ro","type":"conv","area":0.25,"hConv":25}

parallelSet = [R3,R4,R5]
resultsParallel=compositeWallParallel(parallelSet) 
serieSet= [R1,R2,R6]
resultsSeries=compositeWallSeries(serieSet)
results = compositeWall(serieSet,parallelSet)



