Class=[['harry','37.21'],['berry','37.21'],['tina','37.2'],['akriti','41'],['harsh','39']]
for i in range(0,4):
    if Class[i][1]==Class[i+1][1]:
        print(Class[i][0])
        print(Class[i+1][0])