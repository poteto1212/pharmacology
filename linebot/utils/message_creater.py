#送られてきたメッセージに対応するメソッド

from yakuri.models import Detail

def create_single_text_message(message):
    
    
    
    #一般名が入力された時の処理
    if Detail.objects.filter(name__icontains=message):
        detail=Detail.objects.filter(name__icontains=message)[0]
        
        
        message='1.主な商品名\n'+detail.blandname+'\n2.特徴\n'+detail.detail
    
    #商品名が入力された時の処理
    elif Detail.objects.filter(blandname__icontains=message):
        detail=Detail.objects.filter(blandname__icontains=message)[0]
        message='1.一般名\n'+detail.name+'\n2.特徴\n'+detail.detail
        
    else:
        message="ごめんなさい\n"+message+"は登録されていません。順次追加してまいります。"
        
    test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
    return test_message