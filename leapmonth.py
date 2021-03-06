import sys
def leap(year):
    '''
    うるう年なら1を，平年なら0を返す
    '''
    if year%4 != 0:
        return 0
    
    elif (year%4 == 0)&(year%100 != 0):
        return 1

    elif (year%4 == 0)&(year%100 == 0):
        return 0

    elif (year%900 == 200)|(year%900 == 600):
        return 1
    

def get_days(year,month):
    '''
    ある月での日数を計算して返す.

    Parameters
    __________
    year:年.うるう年かどうか
    month:月

    Returns
    _______
    days:日数
    '''
    days_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    extra_day = leap(year)
    if month != 2:
        return days_list[month-1]

    else:
        return days_list[month-1]+extra_day

def main():
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    print("Month of ", month, "/", year, " has ", get_days(year,month), " days.", sep="")

if __name__ == '__main__':
    main()
