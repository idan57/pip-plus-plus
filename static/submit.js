function GetData() {
	option_name = document.getElementById("option").value
	packgeName = document.getElementById("package-name").value
	httpProxy = document.getElementById("http-proxy").value
	httpsProxy = document.getElementById("https-proxy").value
	json_to_send = {
		"option": option_name,
		"package": packgeName,
		"http-proxy": httpProxy,
		"https-proxy": httpsProxy
	}
	return json_to_send
}
	

function SubmitReq() {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/submit", true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.send(JSON.stringify(GetData()));
}
	
// Material Select Initialization
$(document).ready(function() {
$('.mdb-select').materialSelect();
});