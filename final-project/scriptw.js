"use strict";
(function() {
    var wear = [{
            "name": "Africa",
            "description": "2 equipos",
            "author": "ABCD",
            "collection": "Summer/Winter",
            "wear": "./img/soccer1.jpeg",
            "see_more": "shop.html"
        },
        { "name": "Africa", "description": "$229.00", "author": "ABCD", "collection": "Summer/Winter", "wear": "./img/soccer1.jpeg", "see_more": "https://kimoa.com" },
        { "name": "Europa", "description": "$299.00", "author": "ABCD", "collection": "Summer/Winter", "wear": "./img/soccer1.jpeg", "see_more": "https://kimoa.com" },
        { "name": "Oceania", "description": "$479.00", "author": "ABCD", "collection": "Summer/Winter", "wear": "./img/soccer1.jpeg", "see_more": "https://kimoa.com" },
        { "name": "America", "description": "$299.00", "author": "ABCD", "collection": "Summer/Winter", "wear": "./img/soccer1.jpeg", "see_more": "https://kimoa.com" },
        { "name": "Conjunto print sport", "description": "$229.00", "author": "ABCD", "collection": "Summer/Winter", "wear": "./img/soccer1.jpeg", "see_more": "https://kimoa.com" }
    ]


    function buildCard(portfolio) {
        var html = "<div class='col-md-3'>" +
            "<div class='card'>" +
            "<img src='" + portfolio.wear + "' class='card-img-top'>" +
            "<div class='card-body'>" +
            "<h5 class='card-title'>" + portfolio.name + "</h5>" +
            "<p class='card-middle'>" + portfolio.description + "</p>" +
            "<a class='card-text'>" + portfolio.author + "</a><br>" +
            "<a class='card-text'>" + portfolio.collection + "</a>" +
            "<a href='" + portfolio.see_more + "'class='btn btn-primary'>Comprar</a>" +
            "</div>" +
            "</div>" +
            "</div>";

        return html;
    }

    for (var i = 0; i < wear.length; i++) {
        document.getElementById('wear').innerHTML = document.getElementById('wear').innerHTML + buildCard(wear[i]);
    }

})();