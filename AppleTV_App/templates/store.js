
        function thestore(){
            window.location.href ="apple_store.xhtml"
        }
        function store(){
            window.location.href ="store.xhtml"
        }
        function mac(){
            window.location.href ="mac.xhtml"
        }
        function iPad(){
            window.location.href ="iPad.xhtml"
        }
        function iPhone(){
            window.location.href ="iPhone.xhtml"
        }
        function Watch(){
            window.location.href ="Watch.xhtml"
        }
        function AirPods(){
            window.location.href ="AirPods.xhtml"
        }
        function AppleTV(){
            window.location.href ="AppleTV.xhtml"
        }
        function Accesories(){
            window.location.href ="accesories.xhtml"
        }
        function Support(){
            window.location.href ="https://support.apple.com/en-in"
        }
        function buy(product_name){
            json = localStorage.getItem('prod1')
            json = JSON.parse(json)
            if(!json){
                json = {}
            }
            product = $('.'+product_name);
            proname = product[1].innerText
            if(json[product_name]){
                json[product_name]['count'] += 1
            }
            else{
                if(product[2].innerText[0] == 'F'){
                    price = product[2].innerText.slice(6,-1)
                }
                else{
                    price = product[2].innerText.slice(0,-1)
                }
                json[product_name] = {'image': product[0].src, 'name':proname, 'price':price, 'count':1}
            }
            localStorage.setItem('prod1', JSON.stringify(json))
            alert("Added to Cart")
        }