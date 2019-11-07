
def minCoins(coins, m, V): 
    dummy=999
    table = [0 for i in range(V + 1)] 
    table[0] = 0
  
    
    for i in range(1, V + 1): 
        table[i] = dummy
    for i in range(1, V + 1): 
        for j in range(m): 
            if (coins[j] <= i): 
                sub_res = table[i - coins[j]] 
                if (sub_res != dummy and 
                    sub_res + 1 < table[i]): 
                    table[i] = sub_res + 1
    print(table)                
    return table[V] 
  

if __name__ == "__main__": 
  
    coins = [ int(i) for i in input(" yo enter the coins you have ....").split()]
    V=int(input("yo how much money do i have to give change for..."))
    m = len(coins) 
    print("Minimum number of coin is ",  
                 minCoins(coins, m, V)) 
  
   




















































