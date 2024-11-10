def get_avg():
    with open('files\data.txt','r') as f:
        data=f.readlines()
    values=data[1:]
    values = [float(i) for i in values]
    average=sum(values)/len(values)
    return average

avg=get_avg()
print(avg)
