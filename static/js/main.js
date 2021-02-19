/*
-------------- Line Charts -------------------
*/
var options = {
  bezierCurve : true,
  legend: {
    display: false,
  },
  scales: {
    xAxes: [{
      gridLines: {
        display: false,
        drawBorder: false,
      },
      ticks: {
        display: false,
      }
    }],
    yAxes: [{
      gridLines: {
          display: false,
          drawBorder: false,
      },
      ticks: {
        display: false,
        beginAtZero: true,
      }
    }]
  },
  elements: {
      point:{
          radius: 0
      }
  }
};

var charts = document.getElementsByClassName("crypt-marketcap-canvas");
if(charts.length > 0){
  for( let chart of charts ){
    let data = JSON.parse(chart.dataset.charts);
    let bg = chart.dataset.bg;
    let border = chart.dataset.border;

    let canvas = chart.querySelector('canvas');
    let ctx = canvas.getContext('2d');

    var gradient = ctx.createLinearGradient(0, 0, 0, 70);
      gradient.addColorStop(0, "transparent" );
      gradient.addColorStop(1, "transparent");
    let lineChartData = {
      labels : ["1","2","3","4","5","6","7","8","9"],
      datasets : [
          {
              backgroundColor : gradient,
              borderColor : '#' + border,
              data : data,
              bezierCurve : true
          }
      ]  
    }
    new Chart(ctx, {
      type:"line",
      data:lineChartData,
      options:options
    });
  }
}


var optionsForIndiv = {
  bezierCurve : true,
  legend: {
    display: false,
  },
  scales: {
    xAxes: [{
      gridLines: {
        display: false,
        drawBorder: false,
      },
      ticks: {
        display: false,
      }
    }],
    yAxes: [{
      gridLines: {
          display: false,
          drawBorder: false,
      },
      ticks: {
        display: false,
        beginAtZero: true,
      }
    }]
  },
  elements: {
      point:{
          radius: 0
      }
  }
};

var chartsIndiv = document.getElementsByClassName("crypt-individual-marketcap");
if(chartsIndiv.length > 0){
  for( let chart of chartsIndiv ){
    let data = JSON.parse(chart.dataset.charts);
    let bg = chart.dataset.bg;
    let border = chart.dataset.border;

    let canvas = chart.querySelector('canvas');
    let ctx = canvas.getContext('2d');

    var gradient = ctx.createLinearGradient(0, 0, 0, 150);
      gradient.addColorStop(0, "#" + bg);
      gradient.addColorStop(1, "transparent");
    let lineChartData = {
      labels : ["1","2","3","4","5","6","7","8","9"],
      datasets : [
          {
              backgroundColor : 'transparent',
              borderColor : '#' + border,
              data : data,
              bezierCurve : true
          }
      ]  
    }
    new Chart(ctx, {
      type:"line",
      data: lineChartData,
      options: optionsForIndiv
    });
  }
}


/*
-------------------  Theme JS  -----------------
*/
jQuery(document).ready(function() {
  jQuery(document).on('click', '.crypt-header i.menu-toggle', function(){
    jQuery('.crypt-mobile-menu').toggleClass('show');
    jQuery(this).toggleClass('open')
  });

  jQuery(document).on('hover', '.crypt-mega-dropdown-toggle', function(){
    jQuery('.crypt-mega-dropdown-menu-block').toggleClass('shown');
  });
  jQuery(document).on('click', '.crypt-mega-dropdown-toggle', function(e){
    e.preventDefault();
    jQuery('.crypt-mega-dropdown-menu-block').toggleClass('shown');
  });
  jQuery('[data-toggle="tooltip"]').tooltip();

  jQuery('#crypt-tab a').on('click', function (e) {
      
      e.preventDefault();

      var x = jQuery(this).attr('href');
    jQuery(this).parents().find('.crypt-tab-content .tab-pane').removeClass('active');
    jQuery(this).parents().find('.crypt-tab-content .tab-pane' + x).addClass('active');
  });

  jQuery(document).on( 'click', '.crypt-coin-select a', function(e){
    e.preventDefault();
    var div = jQuery(this).attr('href');
    jQuery('.crypt-dash-withdraw').removeClass('d-block').addClass('d-none');
    jQuery(div).removeClass('d-none').addClass('d-block');
  });
  var path = window.location.href; // because the 'href' property of the DOM element is the absolute path

   jQuery('ul.crypt-heading-menu > li > a').each(function() {
      if (this.href === path) {
         jQuery(this).parent('li').addClass('active');
      }else{
         jQuery(this).parent('li').removeClass('active');
      }
      jQuery('.crypt-box-menu').removeClass('active');
   });


   /*
        ----------------- Trading view ----------------0
   */

   if(document.getElementById('crypt-candle-chart')){
     new TradingView.widget(
       {
          "autosize": true,
          "symbol": "NASDAQ:AAPL",
          "interval": "D",
          "timezone": "Etc/UTC",
          "theme": "Light",
          "style": "1",
          "locale": "en",
          "toolbar_bg": "rgba(255, 255, 255, 1)",
          "enable_publishing": false,
          "allow_symbol_change": true,
          "container_id": "crypt-candle-chart"
      }
      );
   }
});