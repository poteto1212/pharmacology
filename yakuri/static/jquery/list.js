//結合プログラム
!function(t,n,e,i){"use strict";function a(n,e){this.element=n,this.settings=t.extend({},o,e),this._defaults=o,this._name=s,this.init()}var s="rowspanizer",o={vertical_align:"top"};t.extend(a.prototype,{init:function(){var n=this,e=t(this.element),i=[];e.find("tr").each(function(n,e){t(this).find("td").each(function(n,e){var a=t(e),s=a.html();if("undefined"!=typeof i[n]&&"dato"in i[n]&&i[n].dato==s){var o=i[n].elem.data("rowspan");("undefined"==o||isNaN(o))&&(o=1),i[n].elem.data("rowspan",parseInt(o)+1).addClass("rowspan-combine"),a.addClass("rowspan-remove")}else i[n]={dato:s,elem:a}})}),t(".rowspan-combine").each(function(e,i){var a=t(this);a.attr("rowspan",a.data("rowspan")).css({"vertical-align":n.settings.vertical_align})}),t(".rowspan-remove").remove()}}),t.fn[s]=function(n){return this.each(function(){t.data(this,"plugin_"+s)||t.data(this,"plugin_"+s,new a(this,n))})}}(jQuery,window,document);


$(function() {
  $(".mitabla").rowspanizer({vertical_align: 'middle'});
});
