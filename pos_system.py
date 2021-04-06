
### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    #↑商品のコード、商品名、金額の生成
    def get_price(self):
        return self.price
    #↑商品の価格

### オーダークラス
class Order:
    # ↓アイテム一覧
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master

        print("*" * 30 + "注文をどうぞ" + "*" * 31 + "\n"
                "\t(1:) りんご\n"
                "\t(2:) なし\n"
                "\t(3:) みかん\n"
                "\t(4:) EXIT\n" +
                "_" * 70)
    # ↓アイテムコード
    def add_item_order(self,item_code):
        self.item_order_list.append(item_code)

    # ↓オーダーリスト
    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))
            # ここに追加登録した商品を書く？
            
            

# メイン処理
def main():
    # マスタ登録
    item_master=[]
    item_master.append(Item("001","りんご",100))
    item_master.append(Item("002","なし",120))
    item_master.append(Item("003","みかん",150))
    item_master.append(Item("004","パイナップル",200))

    # オーダー登録
    order=Order(item_master)
    order.add_item_order("001")
    order.add_item_order("002")
    order.add_item_order("003")
    order.add_item_order("004")
    try:
        while True:  # なんらかの重い処理 (for だったり while だったり。。。)
            # process
            response = str(input('\nご注文の商品を入力してください:\n'))
            for item in item_master:
                if response in item.item_code:
                    item.item_name
                    print('check!!')
                    # print('りんごを購入しました')
                    # 商品コード 金額←商品名の変更は後で.format
                    
                elif response == 2:
                    
                    print('なしを購入しました') # 商品コード 金額←商品名の変更は後で.format
                elif response == 3:
                    order.item_master(response)
                    print('みかんを購入しました') # 商品コード 金額←商品名の変更は後で.format
                elif response == 4:
                    order.item_master(response)
                    print('パイナップルを購入しました') # 商品コード 金額←商品名の変更は後で.format
                    # 文字列の入力、登録番号以外の入力の場合↓
                else:
                    # ここで登録外の商品を追加したい、文字列を格納したい
                    print('商品マスタにありません')
                    
                    # 初期化メソッドでインスタンスを設定している変数、
        pass  # ここに、Ctrl-C で止めたい処理を書く
    except KeyboardInterrupt:
        print('\n----エラー内容-----')
        print('ループ発生')
        print('処理終了')
        # Ctrl-C を捕まえた！
        # print('interrupted!')
        pass  # なにか特別な後片付けが必要ならここに書く
        # プログラムをこの時点で殺すなら sys.exit する
        # sys.exit(0)
    # あとは普通の処理を書けば良いが、Ctrl-C を握りつぶして処理続行は大変お行儀が悪いので注意
    # オーダー表示
    order.view_item_list()
# print('コード番号:{0},商品名:{1}'.format(item_code,item_name))
# インスタンスの生成
if __name__ == "__main__":
    main()