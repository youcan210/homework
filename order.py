import csv
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

    def get_total_price(self,unit):
        total = self.price * int(unit)
        return total
    
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
    
    def add_item_order(self,order_data,unit):
        self.item_order_list.append(order_data)
        self.unit.append(unit)
        return order_data,unit
        
    # マスタを表示する
    def view_item_master(self,item_master):
        for item in self.item_master:
            print(f'商品コード:{item.item_code}:{item.item_name},{item.price}円')
            """
            forループで商品コードを繰り返す
            for 要素 in 対応するリスト
            
            """
    # リストは空かどうか調べる
    def view_order_list(self,order_data,unit):
        # オーダーリストの中が空ではないのなら、
        if self.item_order_list is not None or len(self.item_order_list) == 0:
            print(f'オーダーリストには{order_data.item_name}が{unit}個、{order_data.get_total_price(unit)}円入っています')# print('オーダーリストに{}:{}が{}個あります',format(o.item_code,o.item_name,unit))
            # return order_data.item_code,order_data.item_name
    def pay(self):
        """
        扱う数は金額、お札、効果の枚数なので変数の型はint
        """
        pass
    # def validate(該当する入力を引数とする):
    #     if 入力されたコードなら:
    #         return Falseを返す
    #     return True 真を返す
    
    # アイテムのデータを取得する関数
            

    # オーダーをリストへ登録する
    def register(self,order_data,unit,apple,orange,pear):
        print('-' * 20)
        #もしオーダーが入力されたら
        if order_data == '001':
            # オーダーリストにオーダー要素を追加する
            print(f'{apple.item_code}:{apple.item_name}{unit}個、追加されました')
            # return int(order_data),int(unit)
        elif order_data == '002':
            # オーダーリストにオーダー要素を追加する
            print(f'{pear.item_code}:{pear.item_name}{unit}個、追加されました')
            # return int(order_data),int(unit)
        elif order_data == '003':
            # オーダーリストにオーダー要素を追加する
            print(f'{orange.item_code}:{orange.item_name}{unit}個、追加されました')
            # return int(order_data),int(unit)
        # return order_data
    def read_csv(self):
        """
        csv読み込み処理
        """
        with open('pos.csv',encoding='utf-8')as f:
                for row in csv.reader(f):
                    print(','.join(row))
    def write_csv(self,total_price):
        """
        csv書き込み処理
        """
        with open('pos.csv','a',encoding='utf-8') as f:
                to_csv = [self.item_order_list,self.unit,total_price]
                writer = csv.writer(f)
                writer.writerow(to_csv)
    
    def get_data(self,item_code):
        """
        したいこと:オーダーリストを表示するためにマスタ情報を取得したい
        
        アイテムが入っているリスト: item_master
        ほしい情報:マスタアイテム情報
        値として返す変数: 合致したマスタのitemを取得する
        """
        for item in self.item_master:
            if item_code == item.item_code:
                return item

    def view_total_price(self,total_price):
        print('合計金額は'+str(total_price)+'円です')
        
    def payment(self,total_price):
        while True:
            #標準入力が正しい支払額になるまで繰り返す
            print('-' *10,'お支払い','-'*10)
            payment = int(input('お支払金額を入力してください:'))
            print()
            if payment >= total_price:
                
                change_calc = payment - total_price
                print('お釣りは:', change_calc,'円になります')
                print('payment OK!!')
                break
            else:
                more_payment = total_price - payment 
                print('支払金額がたりません:',more_payment,'円')
                print('も一度入力してください')
                continue

### メイン処理
def main():
    # マスタ登録
    item_master=[]
    item_master.append(Item("001","りんご",100))
    item_master.append(Item("002","なし",120))
    item_master.append(Item("003","みかん",150))
    # 実体化
    # print(item_master)
    order=Order(item_master)
    apple = Item("001","りんご",100)
    pear = Item("002","なし",120)
    orange = Item("003","みかん",150)
    # print(type(apple))
    # print(item_order_list)
    #マスタ表示
    print(type(apple))
    print('-' *10,'いらっしゃいませ','-'*10)
    order.view_item_master(item_master)
    print('-' *10,'masterから選んでください','-'*10)
    """
    各商品をまとめた要素 = [apple,orange,pear]
    
    """
    # print(item_master)
    #追加したリンゴをオーダーリストに001として表示する
    order_in = input('注文を入力:')
    unit = input('個数を入力:')
    
    order_data = order.get_data(order_in) # オーダーとマスタの判定
    order.register(order_data,unit,apple,orange,pear)
    # 入力されたコードから情報をもたせる
    # オーダー登録開始
    order.add_item_order(order_data,unit)
    # オーダー表示
    order.view_order_list(order_data,unit)
    # print('order_data:',order_data)
    # 合計金額
    total_price = order_data.get_total_price(unit)
    order.view_total_price(total_price)
    # マスタをCSVから書き込みする
    # print('total_price:',type(total_price))
    #コード、商品名、注文個数、合計金額
    order.write_csv(total_price)
    
    # 預かり金額を入力して、お釣りを計算する
    order.payment(total_price)
if __name__ == "__main__":
    main()