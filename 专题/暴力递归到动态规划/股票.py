def get_stock_profit(li):
    profit = 0
    for i in range(1, len(li)):
        sell_price = li[i]
        buy_price = min(li[:i])
        profit = max(profit, sell_price - buy_price)
    return profit


def test():
    li = [4, 1, 3, 4, 7, 8, 9, 20, 4]
    assert get_stock_profit(li) == 19


if __name__ == '__main__':
    test()