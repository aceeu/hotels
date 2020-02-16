
function user(callback) {
    fetch('/htbin/user.py', {method: 'POST', headers: {'Content-Type': 'application/json'}})
        .then((response) => response.json()).then(json => {
            callback(json.name);
        });
}

function removeHotel(uuid, callback) {
    fetch('/htbin/hotels.py', {
        method: 'POST', headers: {
        'Content-Type': 'application/json;charset=utf-8'
        },
        body: "action=delete&uuid="+uuid
    })
    .then(resp => resp.json())
    .then(json => callback())

}

function logout(callback) {
    fetch('/htbin/logout.py').then(callback)
}

