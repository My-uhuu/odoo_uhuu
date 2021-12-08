if( !window.UHUUWidget ){
        var h = document.getElementsByTagName('script')[0], j = document.createElement('script');
        j.async = false; 
        j.src = 'https://uhuuvoipfiles.s3.us-west-1.amazonaws.com/uhuuWidgets.js';//Revisar url correcta
        h.parentNode.insertBefore(j, h);
        j.addEventListener('load', () => {
            if( !window.UhuuChat ){
                setTimeout(function(){ 
                    window.UhuuChatUrl = "https://omnichannelqa.myuhuu.com";
                    console.log("handleUhuuBtn -- uhuuchat : afterload script - window.UHUUWidget = ",window.UHUUWidget)
                    //window.UHUUWidget.setUhuuWidgetOption( option.name, option.urlApp, option.params )
                    var h2 = document.getElementsByTagName('script')[0], j2 = document.createElement('script');
                    j2.async = false; 
                    j2.src = 'https://omnichannelqa.myuhuu.com/uhuuchatmini.min.js';
                    h2.parentNode.insertBefore(j2, h2);
                    j2.addEventListener('load', () => {
                        console.log("handleUhuuChatBtn -- UHUUWidget.options 1:: ", window.UHUUWidget.options)
                        console.log("Hemos cargado los 2 scripts")
                    })
                },100)
            }
            
        })
    }