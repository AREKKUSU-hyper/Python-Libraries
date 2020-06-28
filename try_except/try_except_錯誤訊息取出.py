#我很確定可能的錯誤類型
# 範例1
while True:
    try:
        # 直接將輸入值轉換成數字，所以輸入的不是數字就會引發錯誤！
        x = int(input("#1 請輸入數字: "))
        print("#1 你剛才輸入的是:", x)
        break    # 跳出迴圈
    # 數值錯誤
    except ValueError:
        print("#1 糟糕！你輸入的不是數字，請你再輸入一次！...")
 
# 範例2
try:
    # 故意除以零
    print("#2 {0}除以零！".format(x/0))
# 數值除以零的錯誤
except ZeroDivisionError:
    print("#2 {0}不能除以零，誰都不行！".format(x))
 
# 範例3
try:
    # 故意用了沒宣告過的變數『magic_number』
    print("#3 兩數相乘: {0}", x * magic_number)
# 變數未宣告的錯誤
except NameError:
    print("#3 變數未宣告的錯誤！")


#無法確定會發生什麼錯誤時的做法
import sys
 
try:
    mm = 9 / 0
except:
    # sys.exc_info()[0] 就是用來取出except的錯誤訊息的方法
    print("Unexpected error:", sys.exc_info()[0])


# 完整的Try-catch架構
# Try-catch的完整結構應該是這樣：try, except, else, finally
# try：需要被監控是否會出錯的程式區塊
# except：出了哪種錯誤，要有怎樣相對應的處理
# else：都沒錯誤，就會執行此區塊的程式
# finally：不論如何都會執行此區塊的程式
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("不能除以零！")
    else:
        print("相除結果是:", result)
    finally:
        print("不論如何都會執行finally，你使用了除法函數")
###-------------------------------------------------------###
try:
    file=open("aaa.txt",mode="r+")
except Exception as e:
    print("error type: ",e)
    response=input("do u want to create a new file(y/n): ")
    if response=="y":
        file=open("aaa.txt",mode="w")
    else:
        pass
else:
    file.write("""qqqqqqq
ffdddddddd
qqqqqqq""")
file.close()