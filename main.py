def check_avaliable():
    return 'It works!'

def remove_odd(nums=[1,2,3,4]):
    return [num for num in nums if num%2==0]

if __name__=='__main__':
    print(check_avaliable())
    print(remove_odd())
