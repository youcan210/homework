import csv
import os
import datetime
### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price
    
    def __repr__(self):
        return f'{self.item_code,self.item_name,self.price}'

    
    def get_item_data(self):
        return self.item_code,self.item_name,self.price

    def has_code(self,order_in):
        """
        各注文オーダーの値が正しいかチェックするOKならTrue,NGならFalse
        if オーダーリストとマスタが合致するか確認する
        あればTrue
        なければFalse
        check_codeを返り値として返す
        """
        if order_in == self.item_code:
            return True
        else:
            return False
    
### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master
        self.unit = []
        self.total_list = []
    
    def add_item_order(self,order_data,unit):
        self.item_order_list.append(order_data)
        self.unit.append(unit)
        
    def add_total_list(self,total):
        self.total_list.append(total)
        
    # マスタを表示する
    def view_item_master(self):
        for item in self.item_master:
            print(f'商品コード:{item.item_code}:{item.item_name},{item.price}円')

    def view_order_list(self):
        if self.item_order_list is not None or len(self.item_order_list) == 0:
            for item,unit in zip(self.item_order_list,self.unit):
                print(f'オーダーリストには{item.item_name}が{unit}個入っています')
                
    # オーダーをリストへ登録する
    def register(self,order_data,unit):
        print('-' * 20)
        #もしオーダーが入力されたら
        if order_data == '001':
            # オーダーリストにオーダー要素を追加する
            print(f'{self.item_code}:{self.item_name}{unit}個、追加されました')
            # return int(order_data),int(unit)
        elif order_data == '002':
            # オーダーリストにオーダー要素を追加する
            print(f'{self.item_code}:{self.item_name}{unit}個、追加されました')
            # return int(order_data),int(unit)
        elif order_data == '003':
            # オーダーリストにオーダー要素を追加する
            print(f'{self.item_code}:{self.item_name}{unit}個、追加されました')
            # return int(order_data),int(unit)
        

    def read_csv(self):
        """
        csv読み込み処理
        """
        with open('pos.csv',encoding='utf-8')as f:
                for row in csv.reader(f):
                    print(','.join(row))
                    
    def write_csv(self,value_price):
        """
        csv書き込み処理
        """
        with open('pos.csv','a',encoding='utf-8') as f:
                to_csv = [self.item_order_list,self.unit,value_price]
                writer = csv.writer(f)
                writer.writerow(to_csv)
        return to_csv
    
    def get_data(self,item_code):
        for item in self.item_master:
            if item_code == item.item_code:
                return item

    def payment(self,value_price):
        while True:
            #標準入力が正しい支払額になるまで繰り返す
            print('-' *10,'お支払い','-'*10)
            payment = int(input('お支払金額を入力してください:'))
            print()
            if payment >= value_price:
                
                change_calc = payment - value_price
                print('お釣りは:', change_calc,'円になります')
                print('payment OK!!')
                break
            else:
                more_payment = value_price - payment 
                print('支払金額がたりません:',more_payment,'円')
                print('も一度入力してください')
                continue
        return change_calc,payment
    
    # 日付時刻をファイル名としてレシートファイルを出力する
    def recept(self,total_price_info,payment_info):
        now = datetime.datetime.now()
        time_format = 'log_'+now.strftime('%Y%m%d%H%M')
        text = 'レシートを発行します'
        print(total_price_info)
        f = open(time_format,'w',encoding='utf-8')
        writer = csv.writer(f,delimiter='\t')
        writer.writerow([text])
        
        for data,unit in zip(total_price_info[0],total_price_info[1]):
            write_item = '商品コード:',data.item_code,'商品名:',data.item_name,'商品金額:¥',data.price,'円','購入個数',unit,'個'
            print(write_item)
            writer.writerow(write_item)
        write_payment = f'お釣り:¥{payment_info[0]}円 支払額:¥{payment_info[1]}円'
        writer.writerow([write_payment])
        
    def total_price(self,order_data):
        total_price = 0
        each_total_price = order_data.price * self.unit[-1]
        total_price += each_total_price
        return total_price

    def view_total(self,sum_total_value):
        if sum_total_value:
            print('合計金額:',sum_total_value,'円になります')
### メイン処理
def main():
    # マスタ登録
    item_master=[]
    item_master.append(Item("001","りんご",100))
    item_master.append(Item("002","なし",120))
    item_master.append(Item("003","みかん",150))
    
    order=Order(item_master)
    apple = Item("001","りんご",100)
    pear = Item("002","なし",120)
    orange = Item("003","みかん",150)
    #マスタ表示
    print('-' *10,'いらっしゃいませ','-'*10)
    order.view_item_master()
    print('-' *10,'masterから選んでください','-'*10)
    
    #追加したリンゴをオーダーリストに001として表示する
    while True:
        selectmode = input('(y)で処理実行(n)で注文を終了します:')
        print()
        
        if selectmode == 'n':
            break
        elif selectmode == 'y':
            order_in = input('注文を入力:')
            unit = int(input('個数を入力:'))
            # 入力されたコードから情報をもたせる
            order_data = order.get_data(order_in) # オーダーとマスタの判定
            # オーダー登録開始
            order.register(order_data,unit)
            order.add_item_order(order_data,unit)#オーダーリスト追加情報
            # オーダーの合計計算
            total = order.total_price(order_data)
            order.add_total_list(total)
            global sum_total_value
            sum_total_value = sum(order.total_list)
            order.view_total(sum_total_value)
            continue
    # オーダー表示
    order.view_order_list()
    # 合計金額
    order.view_total(sum_total_value)
    # # マスタをCSVから書き込みする
    total_price_info = order.write_csv(sum_total_value)    
    # 預かり金額を入力して、お釣りを計算する
    payment_info = order.payment(sum_total_value)# 支払額、お釣り    
    # 日付時刻をファイル名としてレシートファイルを出力する
    order.recept(total_price_info,payment_info)
if __name__ == "__main__":
    main()