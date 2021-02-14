var contextMenus = {};
contextMenus.createUDString = 
    chrome.contextMenus.create(
        {
            "id": 'UD_Menu',
            "title":"Fetch me a meme",
            "contexts" : ['all']
        },
        function (){
            if(chrome.runtime.lastError){
                console.error(chrome.runtime.lastError.message);
            }
        }
    );
chrome.contextMenus.onClicked.addListener(contextMenuHandler);

function contextMenuHandler(info, tab){
    if(info.menuItemId===contextMenus.createUDString){
        chrome.tabs.executeScript(tab.ib, {
            file : "getWord.js"
        }, _=>{
            let e = chrome.runtime.lastError;
            if(e !== undefined){
                console.log(tab.ib, _, e);
            }
        });
    }
}