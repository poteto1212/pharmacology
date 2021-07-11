from yakuri.models import Detail

#返すメッセージをコントロール
#該当するものを順に返そう
#引数(メッセージ,クラス名)
def replay_controll(message):
    reply_list=[]
    
    #一般名を受け取った時は販売名リストを生成する
    if Detail.objects.filter(name__icontains=message):
        details=Detail.objects.filter(name__icontains=message)
        for detail in details:
            reply_message="1.商品名:"+detail.blandname+'\n\n一般名:'+detail.name
            reply_list.append(reply_message)
    #商品名を受け取った時は販売名リストを生成する
    elif Detail.objects.filter(blandname__icontains=message):
        details=Detail.objects.filter(blandname__icontains=message)

        for detail in details:
            reply_message="1.一般名:"+detail.name+'\n\n商品名:'+detail.blandname
            reply_list.append(reply_message)
    
    #何もない時はごめんなさい
    else:

        sorry_message="ごめんなさい"+message+"は登録されておりません・・・\n"+"順次追加して参ります！"
        reply_list.append(sorry_message)

    

    return reply_list