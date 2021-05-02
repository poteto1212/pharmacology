$(function(){//テンプレート処理が行われたとき
    var counter=0;//０行目
    var text="";
    var target="";
    
    //詰まりを防ぐ為に後ろから探索処理
    //get()メソッドはテンプレート側の値を取得
    //each()メソッドは繰り返し処理
    //text()は表の値をそのまま返す
    //attrはidや行数を取得して返す
    $($('#pharmacology tr:first .target').get().reverse()).each(function(){
        if ($(this).text()==text){//表の値が空の時
            //counter変数に１を足す
            counter++;
            
            if (target !="")//target変数が空白でない時
                target.remove();//要素を削除
        }else{//表の値がある時
            if (target !="")//target変数がある時　　
            　　target.attr('rowSpan',counter);//最終行とcounter変数を取得
            　　
            counter=1;
        }
        text=$(this).text()
        
        target=$(this)
    });
    
    
});
