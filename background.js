chrome.runtime.onMessage.addListener(gotMessage);

function gotMessage(request,response,sendResponse){
    console.log(request.text);
}