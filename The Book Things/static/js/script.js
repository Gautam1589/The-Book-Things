$(document).ready(function() {
    $('#autoWidth,#autoWidth1,#autoWidth2').lightSlider({
        autoWidth:true,
        loop:true,
        onSliderLoad: function() {
            $('#autoWidth,#autoWidth1,#autoWidth2').removeClass('cS-hidden');
        } 
    });  
  });