def picker(prices):
    # print(prices)
    i=0
    buy_sell = [0,0]
    biggest_spread = 0
    for day in range(0,len(prices)) :
        # print(day)
        i = day+1
        for i in range(day+1,len(prices)) :
           
            if i < len(prices):
                # print(prices[i],prices[day])
                sum = (prices[i]  - prices[day])
                
                if biggest_spread < sum:
                    biggest_spread = sum
                    buy_sell[0]= day
                    buy_sell[1]= i
                # print(sum)
                i+=1
    return(buy_sell)