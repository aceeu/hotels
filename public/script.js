
function user(callback) {
    fetch('/htbin/user.py', {method: 'POST', headers: {'Content-Type': 'application/json'}})
        .then((response) => response.json()).then(json => {
            callback(json.name);
        });
}

function logout(callback) {
    fetch('/htbin/logout.py').then(callback)
}
