# Find buy and sell price to maximize the stock
# Input arr   = [8, 5, 12, 9, 19, 1]
# Ouput 5,19

def find_buy_sell_stocks(arr):
    current_profit = float("-inf")
    global_profit = float("-inf")
    buy = arr[0]
    global_sell = 0
    for i in range(1,len(arr)):
        sell = arr[i]
        current_profit = sell - buy
        if current_profit > global_profit:
            global_profit = current_profit
            global_sell = arr[i]
        if buy > arr[i]:
            buy = arr[i]
    res = global_sell-global_profit,global_sell
    return res

if __name__ == '__main__':
    print(find_buy_sell_stocks([8, 5, 12, 9, 19, 1]))