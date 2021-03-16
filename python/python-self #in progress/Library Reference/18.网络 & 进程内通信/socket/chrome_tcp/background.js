
var sockeid = 0;
var info_global = "";

chrome.app.runtime.onLaunched.addListener(function() {
    chrome.app.window.create('window.html', {
			id: "mainwin",
			innerBounds: {
				width: 700,
				height: 600
			}},function(createdWindow){
				chrome.app.window.onClosed.addListener(
					function(){
						console.log("closed")
					}
				);
			}
			
	);
});


chrome.sockets.tcp.create(
	{},
	function(createInfo) { 
		var socketId = createInfo.socketId;
		console.log(createInfo.socketId)
		// 与tcp连接
		chrome.sockets.tcp.connect(createInfo.socketId,"127.0.0.1", 12345, function(ret){});

		// 从tcp接收数据
		chrome.sockets.tcp.onReceive.addListener(function(info) {
			if (info.socketId != createInfo.socketId){
				console.log("not you")
				return;
			}
			else{
				// info.data is an arrayBuffer.
				console.log("-------------")
				console.log(info);
				info_global = info;

			}
			
		});

		// chrome.sockets.tcp.disconnect(socketId, function(){console.log("disconnect");});
	
		// chrome.sockets.tcp.close(socketId, function(){});
	}
);

// 与web页面连接
chrome.runtime.onConnectExternal.addListener(
    function (port) {
		console.log("app已与页面连接")
        // var portIndex = getGUID();
        // serialPort[portIndex] = port;
        port.postMessage({
            header: "guid",
            guid: "portIndex"
		});

		port.postMessage({
            header: "guid1",
            guid: info_global
		});
		
		

        port.onDisconnect.addListener(
            function () {
                // serialPort.splice(portIndex, 1);
				// console.log("Web page closed guid " + portIndex);
				console.log("web page closed")
            }
        );

        // console.log("New web page with guid " + portIndex);
    }
);


/**
 * 监听并处理Web page来请求。
 * Commands:
 *  - open -> 请求打开一个串口
 * - close -> 请求关闭一个串口
 * - list -> 请求获取串口列表
 * - write -> 请求向串口发送数据
 * - installed -> 请求检查本app是否已安装在浏览器中
 */
chrome.runtime.onMessageExternal.addListener(
    function (request, sender, sendResponse) {
		console.log("app接收到了web页面的消息")
		console.log(request);
		console.log(sender);
		sendResponse({
			result: "ok",
			connectionInfo: "connectionInfo"
		})

        if (request.cmd === "open") {
            openPort(request, sender, sendResponse);
        } else if (request.cmd === "close") {
            closePort(request, sender, sendResponse);
        } else if (request.cmd === "list") {
            getPortList(request, sender, sendResponse);
        } else if (request.cmd === "write") {
            writeOnPort(request, sender, sendResponse);
        } else if (request.cmd === "installed") {
            checkInstalled(request, sender, sendResponse);
        }

        return true;
    });


// var current_window = chrome.app.window.current();
// chrome.app.window.onClosed.addListener(
// 	function(){
// 		console.log("closed")
// 	}
// );





















