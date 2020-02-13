
function fetch2(url, params, callback) {
    const request = new XMLHttpRequest();
    
    //	Здесь нужно указать в каком формате мы будем принимать данные вот и все	отличие 
    request.open("POST", url, true);
    request.setRequestHeader("Content-type", "application/json;charset=UTF-8");
    
    request.addEventListener("readystatechange", () => {
    
        if (request.readyState === 4 && request.status === 200) {
            let obj = request.response;
        
            console.log(obj);  
            callback(obj);     
        }
    });
    
    request.send(params);
}