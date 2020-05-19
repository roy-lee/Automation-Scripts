// Simply copy the script here and paste it in the MTX page of your web browser console.
// https://www.pathofexile.com/shop/category/daily-deals

var shopBox = $(".shopItems");
var mtxArray = $(".shopItem");
var mtxObj = [];

// Copy over existing items in shop
$.each(mtxArray, function (i, mtx) {
    console.log(mtx);
    var obj = {
        id : i,
        mtx : mtx,
        price : parseInt($(mtx).find(".price").text())
    }
    mtxObj.push(obj);
});

// Sort and reorder DOM elements
mtxObj.sort((a, b) => parseInt(a.price) - parseInt(b.price));
shopBox.empty();
mtxObj.forEach(element => $(element.mtx).appendTo(shopBox));