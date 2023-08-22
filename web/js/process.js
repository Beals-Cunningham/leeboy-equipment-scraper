import indexProxy from "/direct.js"

async function Process(data){
    let url = window.location.protocol + "//" + window.location.hostname + ":7240/processing";
    $('#output').text("Ladling out Leeboy soup...")
    $.ajax({
        url: url,
        type: 'POST',
        dataType: 'json',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',
        success: callback,
        error: function (error) {
            $('#output').text = error
        }
    })
}

function callback(data){
    data = JSON.stringify(data)
    console.log(data)
    console.log()
    indexProxy.index += 1
    let existing_bowl = $('#bowl').html()
    let new_bowl = existing_bowl + "<br/><br/>" + data
    $('#bowl').html(new_bowl)
}

export default Process