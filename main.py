def check_avaliable():
    return 'It works!'

def split_odd(nums=[1,2,3,4]):
    odds = []
    evens = []
    for i in nums:
        if i % 2 == 0:
            evens.append(i)
        else:    
            odds.append(i)
    return (odds, evens)

if __name__=='__main__':
    print(check_avaliable())
    print(split_odd())
