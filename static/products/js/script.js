

// if($('.shoppingSection').offset().top == 0){
$('.textSection').attr('data-aos','fade-left')  
$('.shoppingImg').attr('data-aos','fade-in')  
$('.shoppingSection .itemList .row .card').attr('data-aos','fade-up')

// $('.shoppingSection .itemList .row .card').attr("data-aos-anchor-placement","bottom-bottom")
AOS.init()

$(document).ready(function(){

    $('#gotop').click(function(){
        window.scrollTo(0,0)
        
    })
   
    
})
