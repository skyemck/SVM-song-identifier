# GET COUNTRY FOR OUTPUTS
# Tested

def getCountry(data):
    for x in data:
        min = 100000.0
        minind = 0
        yindex = 0
        dif = 0
        for y in possibleoutputs:
            dif = abs((x[0] - y[0][0])) + abs((x[1] - y[0][1]))
            if dif < min:
                min = dif
                minind = yindex
            if yindex == 32:
                print("Origin in", possibleoutputs[minind][1], "at", x[0], ",", x[1])
            yindex += 1
            

def obtainWeights(filename):
    y=[]
    file = open(filename,'r')
    lines = file.readlines()
    for i in lines:
        y.append(i.rstrip('\\\n').split('\t'))
    file.close()
    return y

def makeintoDAG(Y):
    b = [[0 for i in range(32)]for j in range(32)]
    place = 0
    for i in range(len(b)):
        count = i
        while count < len(b):
            b[i][count] = Y[place]
            place +=1
            count +=1
    return b

randomindex = []
def TakeRandom(samples,n):
    r = []
    for i in range(n):
        s = random.randint(0,len(samples)-1)
        randomindex.append(s)
        r.append(samples[s])
    return r

#returns the dot product of two vectors
#assumes they're the same length
def LinearFunc(x,y):
    k = [0 for i in range(len(x))]
    for i in range(len(x)):
        k[i]=(x[i]*y[i])
    return sum(k)

#assumes first and versus both start at 0
#returns the index of the country of origin from the list possibleoutputs
def Dagtest(x,alpha,b,first,versus):
    if versus < len(alpha[0]):
        cura= alpha[first][versus]
        output = b[first][versus] + LinearFunc(x,cura)
        if output >=0:
            return Dagtest(x,alpha,b,first,versus+1)
        else :
            first = versus + 1
            return Dagtest(x,alpha,b,first,versus+1)
    else :
        return first

# TESTING CODE #
# Main file to use with run batch
# Calls all other functions from inside
if __name__ == '__main__':
    file2 = 'default_plus_chromatic_features_1059_tracks.txt'
    file = 'default_features_1059_tracks.txt'
    obtainSamples(file)
    string2float(samples)
    string2float(targets)
    cluster(samples, targets)

    #trainingLat is the samples data + just the latitude
    trainingLat = np.empty((1059, 69), dtype=float)
    for x in range(len(samples)-1):
        trainingLat[x] = np.append(samples[x], lat[x])
        
    trainingLong = np.empty((1059, 69), dtype=float)
    for x in range(len(samples)-1):
        trainingLong[x] = np.append(samples[x], long[x])
    
    
    lattrainingSet = trainingLat[0:1059]
    lattestSet = trainingLat[1050:1059,0:68]
    x = getClass(lattrainingSet, lattestSet, 33)
    
    longtrainingSet = trainingLong[0:1059]
    longtestSet = trainingLong[1050:1059,0:68]
    y = getClass(longtrainingSet, longtestSet, 33)
    
    end = [list(i) for i in zip(x, y)]
    getCountry(end)
    
    obtainChromeSamples(file2)
    string2float(Chromesamples)
    
    weights = obtainWeights("DAGweights.txt")
    bias = obtainWeights("Bias.txt")
    string2float(weights)
    string2float(bias)
    shortstr2float(bias)

    randomsamps = TakeRandom(Chromesamples,10)
    count = 0
    for i in randomsamps:
        n = Dagtest(i,weights,bias,0,0)
        print("Country of Origin is " +possibleoutputs[n][1])
        print("at Coordinates "+possibleoutputs[n][0])
        print("Target Coordinates are "+targets[randomindex[count]])
        
  
    
    
    
