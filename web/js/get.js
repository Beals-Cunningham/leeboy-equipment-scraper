import Process from "/process.js"

async function Get(data, flavor){
    let url = window.location.protocol + "//" + window.location.hostname + ":7240/incoming";
    $('#output').text("Stirring tractor soup...")
    $.ajax({
        url: url,
        type: 'POST',
        dataType: 'json',
        data: JSON.stringify({"url": data, "flavor": flavor}),
        contentType: 'application/json; charset=utf-8',
        success: callback,
        error: function (error) {
            $('#output').text = error
        }
    })
}

function callback(data){
    Process(data)
}

export default Get