
function user(callback) {
    fetch('/htbin/user.py', {method: 'POST', headers: {'Content-Type': 'application/json'}})
        .then((response) => response.json()).then(callback);
}

function listHotelsWithoutAdmin(callback) {
    fetch('/htbin/hotels.py?addadmin', {
        method: 'GET', headers: {
        'Content-Type': 'application/json;charset=utf-8'
        }
    })
    .then(resp => resp.json())
    .then(callback)
}

function logout(callback) {
    fetch('/htbin/logout.py').then(callback)
}

