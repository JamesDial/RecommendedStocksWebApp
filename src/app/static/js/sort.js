$(document).ready(function(){
    $("#list").show()
    $("#stock_list_price_asc").hide()
    $("#stock_list_alpha").hide()
    $("#stock_list_alpha_sym").hide()
    $("#stock_list_rev_alpha_sym").hide()
    $("#stock_list_price_desc").hide()
    $("#stock_list_rev_alpha").hide()



    $("#sortByPriceLH").click(function () {
        $("#list").hide()
        $("#stock_list_alpha_sym").hide()
        $("#stock_list_rev_alpha_sym").hide()
        $("#stock_list_alpha").hide()
        $("#stock_list_rev_alpha").hide()
        $("#stock_list_price_desc").hide()
        $("#stock_list_price_asc").show()
    });


    $("#sortByPriceHL").click(function (){
        $("#list").hide()
        $("#stock_list_alpha_sym").hide()
        $("#stock_list_rev_alpha_sym").hide()
        $("#stock_list_alpha").hide()
        $("#stock_list_rev_alpha").hide()
        $("#stock_list_price_asc").hide()
        $("#stock_list_price_desc").show()
    });



    $("#sortByNameAZ").click(function (){
        $("#list").hide()
        $("#stock_list_rev_alpha_sym").hide()
        $("#stock_list_alpha_sym").hide()
        $("#stock_list_price_asc").hide()
        $("#stock_list_price_desc").hide()
        $("#stock_list_rev_alpha").hide()
        $("#stock_list_alpha").show()
    });

    $("#sortByNameZA").click(function (){
        $("#list").hide()
        $("#stock_list_alpha_sym").hide()
        $("#stock_list_rev_alpha_sym").hide()
        $("#stock_list_price_asc").hide()
        $("#stock_list_price_desc").hide()
        $("#stock_list_alpha").hide()
        $("#stock_list_rev_alpha").show()
    });

    $("#sortBySymbolAZ").click(function (){
        $("#list").hide()
        $("#stock_list_price_asc").hide()
        $("#stock_list_alpha").hide()
        $("#stock_list_rev_alpha").hide()
        $("#stock_list_price_desc").hide()
        $("#stock_list_rev_alpha_sym").hide()
        $("#stock_list_alpha_sym").show()
    });

    $("#sortBySymbolZA").click(function (){
        $("#list").hide()
        $("#stock_list_price_asc").hide()
        $("#stock_list_alpha").hide()
        $("#stock_list_rev_alpha").hide()
        $("#stock_list_price_desc").hide()
        $("#stock_list_alpha_sym").hide()
        $("#stock_list_rev_alpha_sym").show()
    });

});
