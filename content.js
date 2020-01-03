window.word = "coding rainbow";


$(".question-hyperlink").dblclick(function(){
    alert("The question is :"+$(this).text());
    word = $(this).text();
    if(word.length > 0){
        let msg = {
            text: word
        };
       chrome.runtime.sendMessage(msg);
    }
});
