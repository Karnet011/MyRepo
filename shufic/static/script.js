jQuery("document").ready(function(){
    jQuery("#ert1").on('click', function(){
            var href = document.getElementById('ert1').name;
            jQuery.ajax({
                type: "GET",

                url: "/video/addlike/ajax/",

                data:{ "addlike" : href,},

                dataType: "text",

                catch: false,

                success: function(data){
                    jQuery("ty").html(data);
                }
            });
    });
});