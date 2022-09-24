def IsLeapYear(year) :
    if ( (year % 4) == 0 or (year % 400) == 0 ) and ( (year % 100) != 0 or (year % 400) == 0 ):
        return True
    else :
        return False

# 메인 코드 : -1 입력받을 때까지 루프 돌기

year = int(input())
if IsLeapYear(year) :
   print("1")
else :
  print("0")