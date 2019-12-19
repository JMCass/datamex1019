"use strict";
(function() {
    var wear = [{
            "name": "África",
            "description": "2 equipos profesionales",
            "count": "1,214 jugadores",
            "wear": "./img/africa.jpeg",
            "see_more": "africa.html"
        },
        { "name": "Asia", "description": "65 equipos profesionales", "count": "2,035 jugadores", "wear": "./img/asia.jpeg", "see_more": "asia.html" },
        { "name": "América", "description": "118 equipos profesionales", "count": "4,132 jugadores", "wear": "./img/america.jpeg", "see_more": "america.html" },
        { "name": "Europa", "description": "456 equipos profesionales", "count": "10,543 jugadores", "wear": "./img/europe.jpeg", "see_more": "europe.html" },
        { "name": "Oceanía", "description": "10 equipos profesionales", "count": "283 jugadores", "wear": "./img/oceania.jpeg", "see_more": "oceania.html" },
        { "name": "Insights", "description": "Análisis gráfico de FIFA 19", "count": "Interpretación económica de los datos", "wear": "./img/data.jpeg", "see_more": "insights.html" }
    ]


    function buildCard(portfolio) {
        var html = "<div class='col-md-4'>" +
            "<div class='card'>" +
            "</div>" +
            "<img src='" + portfolio.wear + "' class='card-img-top'>" +
            "<div class='card-body'>" +
            "<h5 class='card-title'>" + portfolio.name + "</h5>" +
            "<p class='card-middle'>" + portfolio.description + "</p>" +
            "<p class='card-middle'>" + portfolio.count + "</p>" +
            "<a href='" + portfolio.see_more + "'class='btn btn-primary'>Go to data</a>" +
            "</div>" +
            "</div>" +
            "</div>";

        return html;
    }

    for (var i = 0; i < wear.length; i++) {
        document.getElementById('wear').innerHTML = document.getElementById('wear').innerHTML + buildCard(wear[i]);
    }

})();