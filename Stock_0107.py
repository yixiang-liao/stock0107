import twstock
import matplotlib.pyplot as plt

def TWstock(stock_id):
    # get該股資料
    stock = twstock.Stock(stock_id)
    
    # 總成交股數
    capacity = stock.capacity[-1]
    # 總成交金額
    turnover = stock.turnover[-1]
    # 開盤價
    open = stock.open[-1]
    # 最高價
    high = stock.high[-1]
    # 最低價
    low = stock.low[-1]
    # 收盤價
    price = stock.price[-1]
    # 漲跌價差
    change = stock.change[-1]
    # 成交筆數
    transaction = stock.transaction[-1]
    
    # 該股當前資料寫入list
    stock_data = [capacity , turnover , open , high , low , price , change , transaction]

    return stock_data

def stock_figure(stock_id):
    stockID=twstock.Stock(stock_id)
    stocklist=stockID.fetch_31()
    high_ID=[]
    low_ID=[]
    close_ID=[]
    listy=[]
    for i in stocklist:
        high_ID.append(i.high)
        low_ID.append(i.low)
        close_ID.append(i.close)
        listy.append(i.date.strftime('%m-%d'))

    plt.figure(figsize=[16,9])
    plt.plot(listy,high_ID,'r-.*',lw=2,ms=10,label='High')
    plt.plot(listy,low_ID,'g-.p',lw=2,ms=10,label='low')
    plt.plot(listy,close_ID,'y-.o',lw=2,ms=10,label='close')
    plt.legend(fontsize=16)
    # plt.ylim(300,600)
    title = f'{stock_id} Trend'
    plt.title(title , fontsize=28)
    plt.xlabel('Date',fontsize=20)
    plt.ylabel('Price',fontsize=20)
    plt.grid(color='k',ls=':',lw=1,alpha=0.5)
    plt.show() 

if __name__ == '__main__':
    stock_id = input('請輸入台股編號 : ')
    data = TWstock(stock_id)
    print(f'總成交股數 {data[0]}')
    print(f'總成交金額 {data[1]}')
    print(f'開盤價 {data[2]}')
    print(f'最高價 {data[3]}')
    print(f'最低價 {data[4]}')
    print(f'收盤價 {data[5]}')
    print(f'漲跌價差 {data[6]}')
    print(f'成交筆數 {data[7]}')
    stock_figure(stock_id)