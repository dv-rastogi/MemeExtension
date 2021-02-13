var contextMenus = {};
contextMenus.createUDString = 
    chrome.contextMenus.create(
        {
            "id": 'UD_Menu',
            "title":"Search Urban Dictionary",
            "contexts" : ['all']
        },
        function (){
            if(chrome.runtime.lastError){
                console.error(chrome.runtime.lastError.message);
            }
        }
    );
