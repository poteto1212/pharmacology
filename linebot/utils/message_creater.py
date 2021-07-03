#送られてきたメッセージに対応するメソッド

from yakuri.models import Detail

def create_single_text_message(message):
    
    
    test_message=[]
    #一般名が入力された時の処理
    if Detail.objects.filter(name__icontains=message):
        details=Detail.objects.filter(name__icontains=message)
        
        for detail in details:
        
            message='1.主な商品名\n'+detail.blandname+'\n\n2.特徴\n\n'+detail.detail
            #構造式がある時はリンクを後ろにつける
            if detail.structure:
                message=message+'\n\n\n〇構造式URL\n\n↓構造式を表示する\n\n'+detail.structure.url
            
            sendmessage={
                    'type': "text",
                    'text':message
                }
                
            
            test_message.append(sendmessage)
    
    #商品名が入力された時の処理
    elif Detail.objects.filter(blandname__icontains=message):
        details=Detail.objects.filter(blandname__icontains=message)
        
        for detail in details:
            message='1.一般名\n'+detail.name+'\n\n2.特徴\n\n'+detail.detail
            
            if detail.structure:
                message=message+'\n\n\n〇構造式URL\n\n↓構造式を表示する\n\n'+detail.structure.url
            
            sendmessage={
                    'type': 'text',
                    'text': message
                }
        
            
            test_message.append(sendmessage)
        
    else:
        message="ごめんなさい\n"+message+"は登録されていません。順次追加してまいります。"
        
        sendmessage={
                    'type': 'text',
                    'text': message
                }
            
            
            
    return test_message