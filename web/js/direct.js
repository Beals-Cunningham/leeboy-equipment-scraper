import Get from '/get.js'
import pages from '/pages.js'
var objIndex = {"index": 0}


var indexProxy = new Proxy(objIndex, {
    set: function(target, key, value) {
        target[key] = value
        try{
            Get(pages[value]["url"], pages[value]["flavor"])}  
        catch(err){
            console.log("Soup pot is empty")
            $('#output').text( "Tractor soup pot is empty (all pages have been scraped)\nMoving soup to database...")
            $('#canvas2').css('opacity', 1)
            $.ajax({
                url: window.location.protocol + "//" + window.location.hostname + ":7240/takeout",
                type: 'POST',
                dataType: 'json',
                data: JSON.stringify({"soup": $('#bowl').html()}), 
                contentType: 'application/json; charset=utf-8',
                success: callback,
                error: function (error) {
                    $('#output').text = error
                },
                
            })
        }
        return true
    }
})

Get(pages[0]["url"], pages[0]["flavor"])

function callback(data){
    console.log(data)
    $('#output').text( "Tractor soup moved to database")
    $('#canvas2').css('opacity', 0)
}

export default indexProxy


