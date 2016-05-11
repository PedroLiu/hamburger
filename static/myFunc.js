//$(document).ready(function(){
	//$.get("/api/menu",function(data,status){
		//new Date().getTime();
		//if (status == 'success') {
			//bye = data['bye'];
			//add(data);
		//} else {
			//alert('数据读取失败！我也不知道为什么~');
		//}
	//});
//});

function add(data) {
	for (var step in data['step']) {
		var name = data['step'][step];
		var row = document.getElementById(name);
		var content = data[name];
		for (var i = 0; i < content.length; i++) {
			// check the 1st item
			var chk = i == 0 ? '" checked="checked"' : '"';

			// multi or single ???
			var type='checkbox';
			var type='radio';

			// insert HTML
			var inner = '<input type="' + type +'" value="' + content[i] + '" name="' + name + chk + '/>' + content[i];
			row.insertCell().innerHTML = inner;
		}
	}
}

function done() {
	var rand = Math.round( Math.random() * (bye.length - 1));
	alert(bye[rand]);
	//alert(document.order.elements['bread'].value);
}

