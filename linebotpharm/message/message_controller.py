from yakuri.models import Detail
from django.db.models import Q
#返すメッセージをコントロール
#該当するものを順に返そう
#引数(メッセージ,クラス名)
def replay_controll(message):
    reply_list=[]
    
    #一般名を完全一致受け取った時は販売名リストを生成する
    if Detail.objects.filter(name=message):
        details=Detail.objects.filter(name=message)
        for detail in details:
            reply_message="1.商品名:"+detail.blandname+'\n\n一般名:'+detail.name+'\n\n2.特徴\n\n'+detail.detail

            if detail.structure:
                reply_message=reply_message+'\n\n構造式リンク\n\n'+detail.structure.url
            reply_list.append(reply_message)
    #商品名を完全一致受け取った時は販売名リストを生成する
    elif Detail.objects.filter(blandname=message):
        details=Detail.objects.filter(blandname=message)

        for detail in details:
            reply_message="1.一般名:"+detail.name+'\n\n商品名:'+detail.blandname+'\n\n2.特徴\n\n'+detail.detail
            if detail.structure:
                reply_message=reply_message+'\n\n構造式リンク\n\n'+detail.structure.url
            reply_list.append(reply_message)
    
    #何もない時はごめんなさい
    else:

        sorry_message="ごめんなさい"+message+"は登録されておりません・・・\n"+"順次追加して参ります！"
        reply_list.append(sorry_message)

    

    return reply_list

    #核種検索項目に対応出来るような設定を行う
   
        #薬品名の検索は弾く
    
       
        

