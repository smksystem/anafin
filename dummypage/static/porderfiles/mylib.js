var newWindow;
var ug = navigator.userAgent.toLowerCase();
var is_ie = ug.indexOf('msie') != -1; 		// is Internet Explorer??
var is_gecko = ug.indexOf('gecko') != -1;	// is Firefox??
var sptime;

String.prototype.startsWith = function(str) {return (this.match("^"+str)==str);};
String.prototype.endsWith = function(str) {return (this.match(str+"$")==str);};

function calcHeight(strFrame)
{
	//find the height of the internal page
	var ifrm = document.getElementById(strFrame);
	var the_height = 0;
	if (is_gecko) {
		the_height= ifrm.contentWindow.document.getElementsByTagName('html')[0].offsetHeight;
	} else if (is_ie) {
		the_height=ifrm.contentWindow.document.body.scrollHeight;
	}

	//change the height of the iframe
	ifrm.style.height = the_height +20 + 'px';
}
function getHostName(){
	var strHostName = window.location.host;
	var arrHostName = strHostName.split(".");
	var hostName = unescape(arrHostName[arrHostName.length - 2]) + "." + unescape(arrHostName[arrHostName.length - 1]);
	return hostName;
}
function MakeArray(n) {
	this.length=n; 
	for(var i=1; i<=n; i++) {
		this[i]=0;
	}
	return this;
}

function openWindow(url, windName, nWidth, nHeight){
	screenWidth = screen.availWidth; 
	screenHeight = screen.availHeight; 
	winTop = (screen.availHeight - nHeight) / 2; 
	winLeft = (screen.availWidth - nWidth) / 2; 
	var nProperty = "scrollbars=no,menubar=no,status=yes,toolbar=no,resizable=no,titlebar=no,alwaysRaised=yes,width="+(nWidth)+",height="+(nHeight)+",top="+(winTop)+",left="+(winLeft);
	if(is_ie) windName = windName.replace(/ +/g, "");
	OLTdgWindow = window.open(url, windName, nProperty);
	if(OLTdgWindow) OLTdgWindow.focus();
}
function openWindow2(url, name){
	if(is_ie) name = name.replace(/ +/g, "");
	newWindow = window.open(url,name,"scrollbars=yes,menubar=no,status=yes,toolbar=no,resizable=yes,titlebar=no,alwaysRaised=yes,width=780,height=460");
	if(newWindow) newWindow.focus();
}
function openWindow3(url){
	cWindow = window.open(url,"thewindow3","scrollbars=yes,menubar=no,status=yes,toolbar=no,resizable=yes,titlebar=no,alwaysRaised=yes,width=700,height=460");
	if(cWindow) cWindow.focus();
}
function openWindow4(url, name, nWidth, nHeigth){
	screenWidth = screen.width; 
	screenHeight = screen.height;
	var nProperty = "";
	if (screenHeight <= 600) {
		winTop = 0;
		winLeft = 0;
		nProperty = "scrollbars=no,menubar=no,status=yes,toolbar=no,resizable=yes,titlebar=no,alwaysRaised=yes,left="+(winLeft)+",top="+(winTop)+",width="+(screen.availWidth-10)+",height="+(screen.availHeight-28);		
	} else {
		winTop = (screen.availHeight-28 - nHeigth) / 2; 
		winLeft = (screen.availWidth-10 - nWidth) / 2; 	
		nProperty = "scrollbars=no,menubar=no,status=yes,toolbar=no,resizable=yes,titlebar=no,alwaysRaised=yes,left="+(winLeft)+",top="+(winTop)+",width="+(nWidth)+",height="+(nHeigth);
	}
	if(is_ie) name = name.replace(/ +/g, "");
	newWindow = window.open(url,name,nProperty);
	if(document.layers){ 
		if (screen.height == 600){newWindow.resizeTo(screen.availWidth-(newWindow.outerWidth-newWindow.innerWidth),screen.availHeight-(newWindow.outerHeight-newWindow.innerHeight));} 
	}		   
	if(newWindow) newWindow.focus();
}
function openWindow5(url, windName, nWidth, nHeight){
	screenWidth = screen.availWidth; 
	screenHeight = screen.availHeight; 
	winTop = (screen.availHeight - nHeight) / 2; 
	winLeft = (screen.availWidth - nWidth) / 2; 
	var indexURL = url.indexOf("MktRepDaytrade");
	var nProperty = "scrollbars=yes,menubar=no,status=yes,toolbar=no,titlebar=no,alwaysRaised=yes,width="+(nWidth)+",height="+(nHeight)+",top="+(winTop)+",left="+(winLeft);
	if(indexURL >= 0){
		nProperty += ",resizable=yes";
	} else {
		nProperty += ",resizable=no";
	}
	if(is_ie) windName = windName.replace(/ +/g, "");
	OLTdgWindow = window.open(url, windName, nProperty);
	if(OLTdgWindow) OLTdgWindow.focus();
}
function openWindow6(url, windName, nWidth, nHeight){
	screenWidth = screen.availWidth; 
	screenHeight = screen.availHeight;
	winTop = (screen.availHeight - nHeight) / 2;
	winLeft = (screen.availWidth - nWidth) / 2;
	var nProperty = "scrollbars=yes,menubar=no,status=no,toolbar=no,resizable=no,titlebar=no,alwaysRaised=yes,width="+(nWidth)+",height="+(nHeight)+",top="+(winTop)+",left="+(winLeft);
	if(is_ie) windName = windName.replace(/ +/g, "");
	OLTdgWindow = window.open(url, windName, nProperty);
	if(OLTdgWindow) OLTdgWindow.focus();
}

function openWin(url){
	newWindow = window.open(url);
	if(newWindow) newWindow.focus();
}
function helpWindow(url){
	hWindow = window.open(url,"thewindow4", 'scrollbars=1,menubar=no,status=no,toolbar=noresizable=no,width=355,height=430,titlebar=no,alwaysRaised=yes, left=330,top=2,screenX=330,screenY=2');
	hWindow.focus();
}
function helpWindow2(url, name){
	if(is_ie) name = name.replace(/ +/g, "");
	hWindow = window.open(url,name,'scrollbars=1,menubar=no,status=no,toolbar=noresizable=no,width=355,height=430,titlebar=no,alwaysRaised=yes, left=330,top=2,screenX=330,screenY=2');
	if(hWindow) hWindow.focus();
}
function symbolWindow(url){
	aWindow = window.open(url,'symbolWindow', 'scrollbars=1,menubar=no,width=380,height=140,titlebar=no,alwaysRaised=yes, left=0,top=0,screenX=0,screenY=0');
	if(aWindow) aWindow.focus();
}
function dealWindow(url){
	dWindow = window.open(url,"DealData", 'location=0,width=650,height=600,scrollbars=yes');
	if(dWindow) dWindow.focus();
}
function orderDetailWindow(url){
	odWindow = window.open(url,'OrderDetail','toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=1,resizable=0,width=650,height=500');
	if(odWindow) odWindow.focus();
}
function orderChangeWindow(url){
	odWindow = window.open(url,'OrderChange','toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=0,resizable=0,width=300,height=200');
	if(odWindow) odWindow.focus();
}
function openBasketOrderStatus(url){
	var tmp = window.open(url,"BasketOrderStatus","toolbar=1,location=0,directories=0,status=1,menubar=1,scrollbars=1,resizable=0,width=1200,height=750");
	if (tmp.focus){
		tmp.focus();
	}
}
function closeWindow(url, name){
	openWindow2(url,name);
	newWindow.close();
}
function closeAllWindows(){
	closeWindow("","RTQWindow");
	closeWindow("","TradeWindow");
}

function isNumber(inputVal, allownegative, allowdecimal) {
	oneDecimal = false;
	inputStr = "" + inputVal;

	for (var i = 0; i < inputStr.length; i++) {
		var oneChar = inputStr.charAt(i);
		if (i == 0 && oneChar == "-") {
			if (allownegative==true) {
				continue;
			} else {
				return false;
			}
		}
		if (oneChar == "." && !oneDecimal) {
			if (allowdecimal==true) {
				oneDecimal = true;
				continue;
			} else {
				return false;
			}
		}
		if (oneChar < "0" || oneChar > "9") {
			return false;
		}
	}
	return true;
}
function isDate(datestr,field1,fname) { 
	var MinYear = 0, MaxYear = 99; 
	var MinCent = 0, MaxCent = 99; 

	var dateOk = false; 
	var leap=false; 
	var parts = datestr.split('/'); 
	var months = new Array(31,28,31,30,31,30,31,31,30,31,30,31); 

	var cc = 0; 
	var yy = parseInt(parts[2]); 

	var mm = parseInt(parts[1]); 
	var dd = parseInt(parts[0]); 
	var ccyy = yy; 

	if(parts[1] == "08") { mm = 8; }
	if(parts[1] == "09") { mm = 9; }
	if(parts[0] == "08") { dd = 8; }
	if(parts[0] == "09") { dd = 9; }

	if (parts[2].length == 4) {
		cc = parts[2].substring(0,2); 
		yy = parts[2].substring(2,4); 
	} else { 
		if (ccyy >= 20 ){ccyy +=1900;} else {ccyy += 2000;} 
	}
	if((cc >= MinCent && cc <= MaxCent) && (yy >= MinYear && yy <= MaxYear) &&  (mm >= 1 && mm <= 12)) { 
		if (mm == 2)  { 
			if ( (ccyy % 4 != 0) || (ccyy % 100 == 0 && ccyy % 400 != 0) ){leap = false;} else {leap = true;}
			months[1] += leap; 
		} 
		if (dd >= 1 && dd <= months[mm-1]){dateOk = true;} 
	} 
	if (dateOk){CurrentDateObject = new Date(ccyy,parseInt(mm)-1,dd,0,0,0);} 
	if (!dateOk){
		alert("Invalid date format for " + fname + ".");
		field1.focus();
	}
	return dateOk; 
}
function checkfield(field1, type1, nlen, chknull, fname) {
	var isvalid =true;
	var min = nlen;
	var max = nlen;

	if (arguments.length == 6) { 
		min = arguments[2];
		max = arguments[3];
		chknull = arguments[4];
		fname = arguments[5];
	}
	if (chknull) {
		if (field1.value == null || field1.value == "") {
			alert(fname + " requires a value.");
			isvalid=false;
		}
	}
	var strVal=field1.value;
	if (arguments.length == 5) {
		if (nlen != 0 && isvalid==true) {		  
			if (strVal.length < nlen) {
				alert(fname + " minimum " + nlen + " of character.");
				isvalid=false;
			}
		}
	} else {
		if (min != 0 && max != 0 && isvalid==true ) {		  
			if (!((min <= strVal.length) && (strVal.length <= max))) {
				alert(fname + " minimum " + min + " and maximum " + max + " of character(s).");
				isvalid=false;
			}
		}
	}
	if (type1 == "n-" && isvalid==true) {
		if (!isNumber(field1.value, true, true)) {
			alert("Invalid number for " + fname);
			isvalid=false;
		}
	}
	if (type1 == "n" && isvalid==true) {
		if (!isNumber(field1.value, false, true)) {
			alert("Invalid positive number for " + fname);
			isvalid=false;
		}
	}
	if (type1 == "i-" && isvalid==true) {
		if (!isNumber(field1.value, true, false)) {
			alert("Invalid integer for " + fname);
			isvalid=false;
		}
	}
	if (type1 == "i" && isvalid==true) {
		if (!isNumber(field1.value, false, false)) {
			alert("Invalid positive integer for " + fname);
			isvalid=false;
		}
	}
	return isvalid;   
}
function checkfield_th(field1, type1, nlen, chknull, fname) {
	var isvalid =true;
	var min = nlen;
	var max = nlen;

	if (arguments.length == 6) { 
		min = arguments[2];
		max = arguments[3];
		chknull = arguments[4];
		fname = arguments[5];
	}
	if (chknull) {
		if (field1.value == null || field1.value == "") {
			alert(fname + " ��辺������");
			isvalid=false;
		}
	}
	var strVal=field1.value;
	if (arguments.length == 5) {
		if (nlen != 0 && isvalid==true) {		  
			if (strVal.length < nlen) {
				alert(fname + " �ӹǹ����ѡ�õ���ش " + nlen + " ����ѡ��");
				isvalid=false;
			}
		}
	} else {
		if (min != 0 && max != 0 && isvalid==true ) {		  
			if (!((min <= strVal.length) && (strVal.length <= max))) {
				alert(fname + " �ӹǹ����ѡ�õ���ش " + min + " ��Шӹǹ����ѡ���٧�ش " + max + " ����ѡ��");
				isvalid=false;
			}
		}
	}
	if (type1 == "n-" && isvalid==true) {
		if (!isNumber(field1.value, true, true)) {
			alert("�ô��͡����Ţ����Ѻ " + fname);
			isvalid=false;
		}
	}
	if (type1 == "n" && isvalid==true) {
		if (!isNumber(field1.value, false, true)) {
			alert("�ô��͡����Ţ�ǡ����Ѻ " + fname);
			isvalid=false;
		}; 
	}
	if (type1 == "i-" && isvalid==true) {
		if (!isNumber(field1.value, true, false)) {
			alert("�ô��͡�ӹǹ�������Ѻ " + fname);
			isvalid=false;
		}
	}
	if (type1 == "i" && isvalid==true) {
		if (!isNumber(field1.value, false, false)) {
			alert("�ô��͡�ӹǹ����ǡ����Ѻ " + fname);
			isvalid=false;
		}
	}
	return isvalid;   
}
function checkMaxfield(field1, type1, nlen, chknull, fname) {
	var isvalid = true;

	if (chknull) {
		 if (field1.value == null || field1.value == "") {
			 alert(fname + " requires a value.");
			 isvalid=false;
		 }
	}
	strVal=field1.value;
	if (nlen != 0 && isvalid == true) {		  
		if (strVal.length > nlen) {
			alert("Maximum length of " + fname + " is " + nlen);
			isvalid=false;
		}
	}
	if (type1 == "n-" && isvalid==true) {
		if (!isNumber(field1.value, true, true)) {
			alert("Invalid number for " + fname);
			isvalid=false;
		}
	}
	if (type1 == "n" && isvalid==true) {
		if (!isNumber(field1.value, false, true)) {
			alert("Invalid positive number for " + fname);
			isvalid=false;
		}
	}
	if (type1 == "i-" && isvalid==true) {
		if (!isNumber(field1.value, true, false)) {
			alert("Invalid integer for " + fname);
			isvalid=false;
		}
	}
	if (type1 == "i" && isvalid==true) {
		if (!isNumber(field1.value, false, false)) {
			alert("Invalid positive integer for " + fname);
			isvalid=false;
		}
	}
	return isvalid;
}
function validpswd(password1, password2){
	if (password1.value != password2.value) {
		alert ("Password validation failed please re-enter password.");
		password1.focus();
		return false;
	}
	return true;
}

function checkpasswordthai(field1){
	var psw = field1.value;
	var found = false;var i=0;var c = 0;
	// must have spacial character
	for(i=0;i<psw.length;i++){
		c = psw.charCodeAt(i);
		if(!( (c>64 && c<91) || (c>96 && c<123) || (c>47 && c<58))){
			found = true;
			break;
		}
	}
	if(!found){
		alert('\u00c3\u00cb\u00d1\u00ca\u00bc\u00e8\u00d2\u00b9\u00b5\u00e9\u00cd\u00a7\u00c1\u00d5\u00b5\u00d1\u00c7\u00cd\u00d1\u00a1\u00c9\u00c3\u00be\u00d4\u00e0\u00c8\u00c9');
		return false;
	}

	//must have upper case character
	found = false;
	for(i=0;i<psw.length;i++){
		c = psw.charCodeAt(i);
		if(c>64 && c<91){
			found = true;
			break;
		}
	}
	if(!found){
		alert('\u00c3\u00cb\u00d1\u00ca\u00bc\u00e8\u00d2\u00b9\u00b5\u00e9\u00cd\u00a7\u00c1\u00d5\u00b5\u00d1\u00c7\u00be\u00d4\u00c1\u00be\u00ec\u00e3\u00cb\u00ad\u00e8');
		return false;
	}

	//must have lower case character
	found = false;
	for(i=0;i<psw.length;i++){
		c = psw.charCodeAt(i);
		if(c>96 && c<123){
			found = true;
			break;
		}
	}
	if(!found){
		alert('\u00c3\u00cb\u00d1\u00ca\u00bc\u00e8\u00d2\u00b9\u00b5\u00e9\u00cd\u00a7\u00c1\u00d5\u00b5\u00d1\u00c7\u00be\u00d4\u00c1\u00be\u00ec\u00e0\u00c5\u00e7\u00a1');
		return false;
	}

	//must have number
	found = false;
	for(i=0;i<psw.length;i++){
		c = psw.charCodeAt(i);
		if(c>47 && c<58){
			found = true;
			break;
		}
	}
	if(!found){
		alert('\u00c3\u00cb\u00d1\u00ca\u00bc\u00e8\u00d2\u00b9\u00b5\u00e9\u00cd\u00a7\u00c1\u00d5\u00b5\u00d1\u00c7\u00e0\u00c5\u00a2');
		return false;
	}
}
function checkpassword2(field1){
	var psw = field1.value;
	var found = false;var i=0;var c = 0;
	// must have spacial character
	for(i=0;i<psw.length;i++){
		c = psw.charCodeAt(i);
		if(!( (c>64 && c<91) || (c>96 && c<123) || (c>47 && c<58))){
			found = true;
			break;
		}
	}
	if(!found){
		alert('password must have special character');
		return false;
	}

	//must have upper case character
	found = false;
	for(i=0;i<psw.length;i++){
		c = psw.charCodeAt(i);
		if(c>64 && c<91){
			found = true;
			break;
		}
	}
	if(!found){
		alert('password must have upper case character');
		return false;
	}

	//must have lower case character
	found = false;
	for(i=0;i<psw.length;i++){
		c = psw.charCodeAt(i);
		if(c>96 && c<123){
			found = true;
			break;
		}
	}
	if(!found){
		alert('password must have lower case character');
		return false;
	}

	//must have number
	found = false;
	for(i=0;i<psw.length;i++){
		c = psw.charCodeAt(i);
		if(c>47 && c<58){
			found = true;
			break;
		}
	}
	if(!found){
		alert('password must have number');
		return false;
	}
}
function checkpassword1(field1, type1, chknull, fname) {	
	if(checkpassword(field1, type1, chknull, fname) == false) {
		return false;
	} else {
		return true;
	}
}
function checkpassword(field1, type1, chknull, fname) {
	var isvalid = true;
	if (chknull) {
		if (field1.value == null || field1.value == "") {
			alert(fname + " requires a value.");
			isvalid=false;
		}
	}
	strVal = field1.value;
	if (isvalid==true){
		var offset = 0;
		offset = strVal.indexOf(' ');
		if (offset != -1)   {
			alert(fname + " cannot be space.");
			isvalid = false;
		}
	}
	strVal = field1.value;
	if (isvalid==true) {		  
		if( (strVal.length < 6) || (strVal.length > 10)){
			alert(fname + " must be 6-10 characters.");
			isvalid=false;
		}
	}
	if (isvalid==false) {
		if (field1.type == "text") {
			field1.focus();
		}
		return false;
	} else {
		return true;

	}
}
function checkPasswordComplexity(field1){
	var value = field1.value;
	var regex = /^.{6,10}$/;
	if(!regex.test(value)) {
		alert("Password must be 6 - 10 characters.");
		return false;
	}
	var regex2 = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,10}$/;
	if(!regex2.test(value)) {
		alert("Please choose a stronger password. Password must be a mix of A-Z, a-z and 0-9.");
		return false;
	}
	return true;
}

function daytradeWindow(fileName){
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Daytrade" + windowName;

	var time = getCurrentUTC();
	var concat = (fileName.indexOf('?') > -1) ? "&" : "?";	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");
	
	window.open(fileName + concat + "brokerid=" + brokerid  + "&userref=" + userref + '&' + time,windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=auto,resizable=1,width=780,height=550");
}
function daytradeWindowSCBS(fileName){
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Daytrade" + windowName;

	var time = getCurrentUTC();
	var concat = (fileName.indexOf('?') > -1) ? "&" : "?";	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");
	
	window.open(fileName + concat + "brokerid=" + brokerid  + "&userref=" + userref + '&' + time,windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=auto,resizable=1,width=780,height=370");
}

function technicalWindow(fileName){
	var tmp = window.open(fileName,"TechnicalAnalysis","toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=0,resizable=0,width=780,height=550");
	if (tmp.focus){
		tmp.focus();
	}
}
function openTechnicalWindow(fileName){
	var tmp = window.open(fileName,"TechnicalAnalysis","toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=0,resizable=0,width=780,height=550");
	if (tmp.focus){
		tmp.focus();
	}
}
function openTechnical(){
	var newWindow = window.open('/STTTechnical/index.jsp?txtBrokerId=003', 'Technical', 
					"scrollbars=no,menubar=no,status=no,toolbar=no,resizable=yes,titlebar=no," + 
					"alwaysRaised=yes,left=0,top=0,width=780,height=530");
	newWindow.focus();
}
function trim(inputString) {
	// Removes leading and trailing spaces from the passed string. Also removes
	// consecutive spaces and replaces it with one space. If something besides
	// a string is passed in (null, custom object, etc.) then return the input.
	// if (typeof inputString != "string") { return inputString; }
	var retValue = inputString;
	var ch = retValue.substring(0, 1);
	while (ch == " ") { // Check for spaces at the beginning of the string
		retValue = retValue.substring(1, retValue.length);
		ch = retValue.substring(0, 1);
	}
	ch = retValue.substring(retValue.length-1, retValue.length);
	while (ch == " ") { // Check for spaces at the end of the string
		retValue = retValue.substring(0, retValue.length-1);
		ch = retValue.substring(retValue.length-1, retValue.length);
	}
	/*
	while (retValue.indexOf("  ") != -1) { // Note that there are two spaces in the string - look for multiple spaces within the string
		retValue = retValue.substring(0, retValue.indexOf("  ")) + retValue.substring(retValue.indexOf("  ")+1, retValue.length); // Again,
	}
	*/
	return retValue; // Return the trimmed string back to the user
}
function windif() {
	var difx, dify, w = getwindow(),
	winx = w.w, winy = w.h;
	window.resizeTo( winx, winy );
	w = getwindow();
	difx = winx - w.w; dify = winy - w.h;
	window.resizeTo( winx + difx, winy + dify );
	return difx + 'px ? ' + dify + 'px';
}
function moveWindow(windowName, width, height) {
	try {
		screenWidth = screen.availWidth; 
		screenHeight = screen.availHeight; 
		winTop = (screen.availHeight - height) / 2; 
		winLeft = (screen.availWidth - width) / 2; 
		windowName.moveTo(winTop, winLeft);
		windowName.focus();
	}catch(e){}
}
function getHostName(){
	var strHostName = window.location.host;
	var arrHostName = strHostName.split(".");
	var hostName = unescape(arrHostName[arrHostName.length - 2]) + "." + unescape(arrHostName[arrHostName.length - 1]);
	return hostName;
}

var derivative;
var streamingWin;
function openOnlineTradeZone(){	
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming" + windowName;

	var time = getCurrentUTC();	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");	
	window.open('/scbs/realtime/OnlineTradeZone.jsp?brokerid=' + brokerid  + '&userref=' + userref + '&resolution='+screen.width + "&" + time,windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=0,resizable=1,width=1004,height=670");
}
function openOnlineTradeZoneWithAccount(accountNo){	
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming" + windowName;
	
	var time = getCurrentUTC();	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");	
	window.open('/scbs/realtime/OnlineTradeZone.jsp?brokerid=' + brokerid  + '&userref=' + userref + '&txtAccountNo='+accountNo+'&resolution='+screen.width + "&" + time,windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=0,resizable=1,width=1004,height=670");
}

function openStreaming(bypass){
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming" + windowName;

	var time = getCurrentUTC();	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");
	var url = '/daytradeflex/DaytradeFlexScreen.jsp?brokerid=' + brokerid  + '&userref=' + userref + '&resolution='+screen.width + "&" + time;
	if (bypass !== undefined){
		url = url + '&bypassMultiWindows=' + bypass;
	}
	var options = "toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=auto,resizable=1,width=780,height=550";
	streamingWin = window.open(url,windowName,options);
}
function openStreamingWithAccountNo(accountNo, bypass){
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming" + windowName;
	
	var time = getCurrentUTC();	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");
	var url = '/daytradeflex/DaytradeFlexScreen.jsp?brokerid=' + brokerid + '&userref=' + userref + '&txtAccountNo='+accountNo+'&resolution='+screen.width+'&'+time;
	if (bypass !== undefined){
		url = url + '&bypassMultiWindows=' + bypass;
	}
	var options = "toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=auto,resizable=1,width=780,height=550";
	window.open(url,windowName,options);
}
function openStreamingEInfo(){
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming" + windowName;
	
	var time = getCurrentUTC();	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");
	streamingWin = window.open('/daytradeflex/DaytradeFlexScreenEInfo.jsp?brokerid=' + brokerid + '&userref=' + userref + '&resolution='+screen.width + "&" + time,windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=auto,resizable=1,width=780,height=550");
}
function openStreaming_JP(){
	// customize for broker 038
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming_JP" + windowName;

	var time = getCurrentUTC(); 		
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");
	window.open('/daytradeflex/DaytradeFlexScreen.jsp?brokerid=' + brokerid + '&userref=' + userref+ '&resolution='+screen.width + "&" + time,windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=auto,resizable=1,width=780,height=550");
}
function openStreamingDGW(){
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming" + windowName;
	
	var time = getCurrentUTC();	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");
	window.open('/daytradeflex/DaytradeFlexScreenAsl.jsp?brokerid=' + brokerid + '&userref=' + userref+ '&resolution='+screen.width + "&" + time,windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=auto,resizable=1,width=780,height=550");
}
function openStreamingDGW_JP(){
	// customize for broker 038
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming_JP" + windowName;
	
	var time = getCurrentUTC();	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");
	window.open('/daytradeflex/DaytradeFlexScreenAsl.jsp?brokerid=' + brokerid + '&userref=' + userref+ '&resolution='+screen.width + "&" + time,windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=auto,resizable=1,width=780,height=550");
}
function openStreamingFullScreen(bypass){
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming" + windowName;

	var time = getCurrentUTC();
	var width = screen.width * 0.975;
	var height =  width * 0.70512820512820512820512820512821;	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");	
	var url = '/daytradeflex/DaytradeFlexScreen.jsp?brokerid=' + brokerid + '&userref=' + userref +'&resolution='+screen.width + "&" + time;	
	if (bypass !== undefined){
		url = url + '&bypassMultiWindows=' + bypass;
	}
	var options = 'toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=auto,resizable=1,width='+width+',height='+height;
	window.open(url, windowName,options);
}
function openStreamingFullScreenWithAccountNo(accountNo, bypass){
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming" + windowName;
	
	var time = getCurrentUTC();
	var width = screen.width * 0.975;
	var height =  width * 0.70512820512820512820512820512821;	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");
	var url = '/daytradeflex/DaytradeFlexScreen.jsp?brokerid=' + brokerid + '&userref=' + userref + '&txtAccountNo='+accountNo+'&resolution='+screen.width + "&" + time;
	if (bypass !== undefined){
		url = url + '&bypassMultiWindows=' + bypass;
	}
	var options = 'toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=auto,resizable=1,width='+width+',height='+height;
	window.open(url, windowName, options);
}
function openStreamingFullScreenDGW(){
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming" + windowName;
	
	var time = getCurrentUTC();
	var width = screen.width * 0.975;
	var height =  width * 0.70512820512820512820512820512821;	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");
	window.open('/daytradeflex/DaytradeFlexScreenAsl.jsp?brokerid=' + brokerid + '&userref=' + userref + '&resolution='+screen.width + "&" + time,windowName,'toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=auto,resizable=1,width='+width+',height='+height);
}
function openStreamingMktRep(){
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming" + windowName;
	streamingMktRepWin = window.open('/daytradeflex/DaytradeFlexScreenMktRep.jsp?resolution='+screen.width,windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=0,resizable=1,width=780,height=550");
}

function openStreamingPlus(){
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming" + windowName;
	
	//var time = getCurrentUTC();	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");	
	window.open('/multimarket/redirect_page.jsp?txtPage=streaming_plus?brokerid=' + brokerid + '&userref=' + userref ,windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=auto,resizable=1,width=954,height=715");
}
function openStreamingPlusMktRep(){
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming" + windowName;
	window.open('/multimarket/redirect_page.jsp?txtPage=streaming_plus' ,windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=auto,resizable=1,width=954,height=715");
}
function openStreaming4(){
	
	//var time = getCurrentUTC();	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");
	var url = '/multimarket/redirect_page.jsp?txtPage=streaming4&brokerid=' + brokerid + '&userref=' + userref;
	// Check for android browser
	var ua = navigator.userAgent.toLowerCase();
	var isAndroid = ua.indexOf("android") > -1; //&& ua.indexOf("mobile");
	// comment temporary for soft launch and will removed in aug 2011
	if(isAndroid) {
		deleteCookie("androidOpener");
		setCookie("androidOpener", window.location.href, false, "/" , getHostName(), true);
		window.location = url;
		return;
	} else {
		var windowName = getCookie("xid");
		if (windowName){
			windowName = "_" + windowName;
		}
		windowName = "Streaming" + windowName;
		window.open(url ,windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=auto,resizable=1,width=920,height=650");
	}
}
function openStreaming4E(){
	// check for login 2 broker
	checkRealtimeSession();

	//var time = getCurrentUTC();
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");
	var url = '/multimarket/redirect_page.jsp?txtPage=streaming4e&brokerid=' + brokerid + '&userref=' + userref ;
	// Check for android browser
	var ua = navigator.userAgent.toLowerCase();
	var isAndroid = ua.indexOf("android") > -1; //&& ua.indexOf("mobile");
	// comment temporary for soft launch and will removed in aug 2011
	if(isAndroid) {
		deleteCookie("androidOpener");
		setCookie("androidOpener", window.location.href, false, "/" , getHostName(), true);
		window.location = url;
		return;
	} else {
		var windowName = getCookie("xid");
		if (windowName){
			windowName = "_" + windowName;
		}
		windowName = "Streaming" + windowName;
		window.open(url,windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=auto,resizable=1,width=920,height=650");
	}
}
function openStreaming4D(){
	// check for login 2 broker
	checkRealtimeSession();

	//var time = getCurrentUTC();
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");
	var url = '/multimarket/redirect_page.jsp?txtPage=streaming4d&brokerid=' + brokerid + '&userref=' + userref;
	
	// Check for android browser
	var ua = navigator.userAgent.toLowerCase();
	var isAndroid = ua.indexOf("android") > -1; //&& ua.indexOf("mobile");
	// comment temporary for soft launch and will removed in aug 2011
	if(isAndroid) {
		deleteCookie("androidOpener");
		setCookie("androidOpener", window.location.href, false, "/" , getHostName(), true);
		window.location = url;
		return;
	} else {
		var windowName = getCookie("xid");
		if (windowName){
			windowName = "_" + windowName;
		}
		windowName = "Streaming" + windowName;
		window.open(url ,windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=auto,resizable=1,width=920,height=650");
	};
}

function openOneclick(toURL) {
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}	
	if (arguments.length == 0) {
		streamingWin = window.open('/multimarket/redirect_page.jsp?txtPage=oneclick' ,"OneClick" + windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=1,resizable=0,width=780,height=550");
	} else {
		streamingWin = window.open(toURL + '/multimarket/redirect_page.jsp?txtPage=oneclick' ,"OneClick" + windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=auto,resizable=0,width=780,height=550");
	}
}
function openBLSOneClick(toURL) {
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	//var time = getCurrentUTC();
	if (arguments.length == 0) {
		streamingWin = window.open('/bls/OpenOneClick.jsp?txtPage=oneclick' ,"OneClick" + windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=1,resizable=0,width=780,height=550");
	} else {
		streamingWin = window.open(toURL + '/bls/OpenOneClick.jsp?txtPage=oneclick' ,"OneClick" + windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=1,resizable=0,width=780,height=550");
	}
}
function checkRealtimeSession() {
	// check for login 2 broker
	if (document.chkSession && document.chkSession.txtBrokerId) {
		var brokerIdFromOpener = document.chkSession.txtBrokerId.value;
		var brokerIdFromSession = getCookie("__txtBrokerId");
		if (brokerIdFromOpener != brokerIdFromSession) {
			var msg = "Sorry, your session is not available due to the following reasons:\n";
			msg += "1. Your session is expired.\n";
			msg += "2. You have re-login at another windows.\n";
			msg += "3. Your do not have permission to access this page.\n\n";
			msg += "To continue with the service, please close your browser and re-login.\n\n";
			msg += "Thank you for using our service.";
			alert(msg);
		}
	}
}
function openPreStreaming(openBy, full, accountNo) {
	try {
		// check for login 2 broker
		checkRealtimeSession();

		var url = getURL(openBy);
		var time = getCurrentUTC(); 
		var concat = (url.indexOf('?') > -1) ? "&" : "?";			
		var brokerid = getCookie("__txtBrokerId");
		var userref = getCookie("__txtUserRef");			
		url = url + concat + "brokerid=" + brokerid + "&userref=" + userref + "&resolution=" + screen.width + "&" + time;

		// Check for android browser
		var ua = navigator.userAgent.toLowerCase();
		var isAndroid = ua.indexOf("android") > -1; //&& ua.indexOf("mobile");
		
		if(isAndroid) {
			deleteCookie("androidOpener");
			var backURL = window.location.href;
			if(openBy=='BLS_Streaming4'){
				backURL = 'https://'+top.location.hostname+"/bls";
			}
			setCookie("androidOpener", backURL, false, "/" , getHostName(), true);
			top.location.href = url;
			return;
		}

		if (url) {			
			var windowName = getCookie("xid");
			if (windowName){
				windowName = "_" + windowName;
			}

			if (openBy.endsWith("TH")) { 
				openBy = openBy.substring(0, openBy.indexOf("TH")); 
			}

			if(openBy=="Streaming" || openBy=="StreamingD" || openBy=="StreamingDGW" || openBy=="StreamingPlus" || openBy=="Streaming4"
				|| openBy=="BLS_Streaming" || openBy=="BLS_StreamingPlus" || openBy=="BLS_Streaming4" 
				|| openBy=="TiscoFlashQuote" || openBy=="ASLRealtime" || openBy=="DBSVQuickTrade" 
				|| openBy=="IWinner" || openBy=="SCBSOnlineTradeZone" || openBy=="PhatraStreaming"
			){
				windowName = "Streaming"+windowName;
			} else if(openBy=="Streaming5" || openBy=="BLS_Streaming5") {
				windowName = "Streaming5Screen1"+windowName;
			} else {
				windowName = openBy + windowName;
			}

			streamingWin = window.open(url, windowName, getProp(openBy));
		} else {
			alert("Cannot open, please check parameter. [" + openBy + "]");
		}

	} catch(e) {
		alert("An exception occurred in the script. Error message: " + e.message); 
	}
}
function openPreStreamingMktRep(openBy, full, accountNo) {
	try {
		// check for login 2 broker
		checkRealtimeSession();

		var url = getURL(openBy);
		//var brokerid = getCookie("__txtBrokerId");
		// Check for android browser
		var ua = navigator.userAgent.toLowerCase();
		var isAndroid = ua.indexOf("android") > -1; //&& ua.indexOf("mobile");
		// comment temporary for soft launch and will removed in aug 2011
		if(isAndroid && openBy=="Streaming4") {
			deleteCookie("androidOpener");
			setCookie("androidOpener", window.location.href, false, "/" , getHostName(), true);
			window.location.href = url;
			return;
		}
		
		if (url) {
			var windowName = getCookie("xid");
			if (windowName){
				windowName = "_" + windowName;
			}
			
			if (openBy.endsWith("TH")) { openBy = openBy.substring(0, openBy.indexOf("TH")); }
			
			if(openBy=="Streaming" || openBy=="StreamingPlus" || openBy=="Streaming4"){
				windowName = "Streaming"+windowName;
			} else if(openBy=="Streaming5" || openBy=="Streaming5SN3") {
				windowName = "Streaming5Screen1"+windowName;
			}else {
				windowName = openBy + windowName;
			}
	
			streamingWin = window.open(url, windowName, getProp(openBy));
		} else {
			alert("Cannot open, please check parameter. [" + openBy + "]");
		}

	} catch(e) {
		alert("An exception occurred in the script. Error message: " + e.message); 
	}
}
/*
function openKsecPage(openBy, toURL){
	if (openBy == "") {
		alert("Parameter Requires value.");
		return false;
	}
	var time = getCurrentUTC();
	if (arguments.length == 2) {
		window.open(toURL + '/ksec/ksecControlPage.jsp?page=' + openBy  + '&' + time ,"PreStreaming","toolbar=0,location=0,directories=0,status=1,menubar=0,scrollbars=0,resizable=0,width=800,height=600");
	} else {
		alert("Require parameter.");
	}
}
*/
function openRealtime(){
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Realtime"+windowName;
	
	var time = getCurrentUTC();
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");
	
	newWindow = window.open('/adkinson/ASLRealTimeScreen.jsp?brokerid=' + brokerid  + '&userref=' + userref + '&' + time, windowName, 
				"scrollbars=no,menubar=no,status=no,toolbar=no,resizable=yes,titlebar=no," + 
				"alwaysRaised=yes,left=0,top=0,width=792,height=543");
	try {
		newWindow.focus();
	} catch(e){}
}
function openRealTimeScreen(url, width, height) {
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming"+windowName;
	
	var time = getCurrentUTC();
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");	
	var concat = (url.indexOf('?') > -1) ? "&" : "?";
	streamingWin = window.open(url + concat + 'brokerid=' + brokerid + '&userref=' + userref + '&' + time,windowName,'toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=0,resizable=1,width='+width+',height='+height);
}
function openRealTimeFullScreen(url, width, height) {
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Daytrade"+windowName;
	
	var time = getCurrentUTC();
	var newHeight = screen.availHeight * 0.95;
	var newWidth = newHeight * (width / height);
	if (newWidth > width || newHeight > height) {
		newWidth = width;
		newHeight = height;
	}	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");
	streamingWin = window.open(url + '&brokerid=' + brokerid + '&userref=' + userref +'&width='+newWidth+'&height='+newHeight + "&"+ time,
				windowName,'toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=0,resizable=1,width='+newWidth+',height='+newHeight);
}
function openBuySell(url, width, height) {
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Daytrade"+windowName;
	
	var time = getCurrentUTC();
	try{
		if (streamingWin && streamingWin.open && !streamingWin.closed){streamingWin.close();}
	}catch(e){}
	var concat = (url.indexOf('?') > -1) ? "&" : "?";
	streamingWin = window.open(url + concat + time,windowName,'toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=1,resizable=0,width='+width+',height='+height);
	moveWindow(streamingWin, width, height);
}
function openQuickTrade(url, width, height) {
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Daytrade"+windowName;
	
	var time = getCurrentUTC();
	try{
		if (streamingWin && streamingWin.open && !streamingWin.closed){streamingWin.close();}
	}catch(e){}
	var concat = (url.indexOf('?') > -1) ? "&" : "?";
	streamingWin = window.open(url + concat + time,windowName,'toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=1,resizable=0,width='+width+',height='+height);
	screenWidth = screen.availWidth; 
	screenHeight = screen.availHeight; 
	winTop = screenHeight - height - 30; 
	winLeft = (screenWidth - width) / 2; 
	streamingWin.moveTo(winLeft, winTop);
	streamingWin.focus();
}
function openTiscoRealtime(fileName){
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming"+windowName;
	
	var time = getCurrentUTC();
	var concat = (fileName.indexOf('?') > -1) ? "&" : "?";
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");
	window.open(fileName + concat + 'brokerid=' + brokerid + '&userref=' + userref + '&' +time,windowName,"toolbar=0,width=780,height=550,resizable=1");
}

var streamingWinD;
var realtimeWinD;
function openStreamingD(server){
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming"+windowName;
	
	var time = getCurrentUTC();	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");	
	if (streamingWinD && streamingWinD.open && !streamingWinD.closed){streamingWinD.close();}
	streamingWinD = window.open(server + '/StreamingDScreen.jsp?brokerid=' + brokerid + '&userref=' + userref + '&resolution='+screen.width + "&" + time,windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=0,resizable=1,width=780,height=550");
}
function openStreamingDFullScreen(server){
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming"+windowName;
	
	var time = getCurrentUTC();
	var width = screen.width * 0.975;
	var height =  width * 0.70512820512820512820512820512821;	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");	
	if (streamingWinD && streamingWinD.open && !streamingWinD.closed){streamingWinD.close();}
	streamingWinD = window.open(server + '/StreamingDScreen.jsp?brokerid=' + brokerid + '&userref=' + userref + '&resolution='+screen.width + "&" + time,windowName,'toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=0,resizable=0,width='+width+',height='+height);
}
function openRealTimeDScreen(url, width, height) {
	if (realtimeWinD && realtimeWinD.open && !realtimeWinD.closed){realtimeWinD.close();}
	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");
	var concat = (url.indexOf('?') > -1) ? "&" : "?";	
	realtimeWinD = window.open(url + concat + 'brokerid=' + brokerid + '&userref=' + userref,'RealTimeD','toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=0,resizable=1,width='+width+',height='+height);
}
function openStreamingDScreen(url, width, height) {
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming"+windowName;
	
	var time = getCurrentUTC();	
	var brokerid = getCookie("__txtBrokerId");
	var userref = getCookie("__txtUserRef");	
	if (streamingWinD && streamingWinD.open && !streamingWinD.closed){streamingWinD.close();}
	var concat = (url.indexOf('?') > -1) ? "&" : "?";
	streamingWinD = window.open(url + concat + 'brokerid=' + brokerid + '&userref=' + userref + '&' + time,windowName,'toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=0,resizable=1,width='+width+',height='+height);
}
function openPlaceOrderD(url, width, height) {
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Streaming"+windowName;
	
	var time = getCurrentUTC();
	//var brokerid = getCookie("__txtBrokerId");
	//var userref = getCookie("__txtUserRef");	
	if (streamingWinD && streamingWinD.open && !streamingWinD.closed){streamingWinD.close();}
	var concat = (url.indexOf('?') > -1) ? "&" : "?";
	streamingWinD = window.open(url + concat + time,windowName,'toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=yes,resizable=0,width='+width+',height='+height);
}
function openDerivative(fileName) {
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "DerivativesPopup"+windowName;
	
	var time = getCurrentUTC();
	var concat = (fileName.indexOf('?') > -1) ? "&" : "?";
	derivative = window.open(fileName + concat + time, windowName,'toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=no,resizable=0,width=653,height=560');
	derivative.focus();
}
function onOpenDerivative(){
	window.open("/C16_MktRepDerivativesRedirect.jsp", "MarketRepD");
}
function openDerivativeMain(fileName) {
	var windowName = getCookie("xid");
	if (windowName){
		windowName = "_" + windowName;
	}
	windowName = "Derivatives"+ windowName;
	
	var time = getCurrentUTC();
	var concat = (fileName.indexOf('?') > -1) ? "&" : "?";
	if (fileName == "") {
		fileName =  "/C16_MktRepDerivativesRedirect.jsp";
	}
	var derivative = window.open(fileName + concat + time, windowName);
	derivative.focus();
}
function openDerivativeMainNoPopup(fileName) {
	parent.location = fileName;
}
function openHelpPage(url){
	var helpWindow = window.open(url,'HelpPage', 'location=0,width=500,height=500,scrollbars=yes');
	helpWindow.focus();
}

//for left menu
function preload(){
	if(document.images){
		Open = new Image(16,13);   
		Closed = new Image(16,13);
		Open.src = "open.gif";
		Closed.src = "closed.gif";
	}
}
function showhide(what){
	if (what.style.display=='none'){
		what.style.display='';
	}else{
		what.style.display='none';
	}
}
function setCookie( name, value, expires, path, domain, secure )
{
	var today = new Date();
	today.setTime(today.getTime());	
	if(expires)	{
		expires = expires * 1000 * 60 * 60 * 24;
	}
	var expires_date = new Date( today.getTime() + (expires) );
	
	document.cookie = name + "=" +escape( value ) +
	((expires) ? ";expires=" + expires_date.toGMTString() : "" ) +
	((path) ? ";path=" + path : "" ) +
	((domain) ? ";domain=" + domain : "" ) +
	((secure) ? ";secure" : "" );
}
function getCookie(c_name) {
	if (document.cookie.length>0) {
		c_start=document.cookie.indexOf(c_name + "=");
		if (c_start!=-1) { 
			c_start=c_start + c_name.length+1 ;
			c_end=document.cookie.indexOf(";",c_start);
			if (c_end==-1){
				c_end=document.cookie.length;
			}
			return unescape(document.cookie.substring(c_start,c_end));
		} 
	}
	return "";
}
function deleteCookie( name, path, domain ) {
	if (getCookie(name)) document.cookie = name + "=" +
	((path) ? ";path=" + path : "") +
	((domain) ? ";domain=" + domain : "" ) +
	";expires=Thu, 01-Jan-1970 00:00:01 GMT";
}
function getCurrentUTC() {
	var currentTime = new Date();
	return Date.UTC(
			currentTime.getUTCFullYear(),
			currentTime.getUTCMonth(),
			currentTime.getUTCDate(),
			currentTime.getUTCHours(),
			currentTime.getUTCMinutes(),
			currentTime.getUTCSeconds(),
			currentTime.getUTCMilliseconds());
}
function MM_preloadImages() { //v3.0
	var d=document;
	if(d.images){ 
		if(!d.MM_p) d.MM_p=new Array();
		var i,j=d.MM_p.length,a=MM_preloadImages.arguments;
		for(i=0; i<a.length; i++){
			if (a[i].indexOf("#")!=0){
				d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];
			}
		}
	}
}

function MM_swapImgRestore() { //v3.0
	var i,x,a=document.MM_sr;
	for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++)
		x.src=x.oSrc;
}

function MM_findObj(n, d) { //v4.01
	var p,i,x;
	if(!d) 
		d=document;
	if((p=n.indexOf("?"))>0&&parent.frames.length) {
		d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);
	}
	if(!(x=d[n])&&d.all)
		x=d.all[n];
	for (i=0;!x&&i<d.forms.length;i++)
		x=d.forms[i][n];
	for(i=0;!x&&d.layers&&i<d.layers.length;i++)
		x=MM_findObj(n,d.layers[i].document);
	if(!x && d.getElementById)
		x=d.getElementById(n);
	return x;
}
function MM_swapImage() { //v3.0
	var i,j=0,x,a=MM_swapImage.arguments;
	document.MM_sr=new Array;
	for(i=0;i<(a.length-2);i+=3){
		if ((x=MM_findObj(a[i]))!=null){
			document.MM_sr[j++]=x; 
			if(!x.oSrc) 
				x.oSrc=x.src; 
			x.src=a[i+2];
		}
	}
}
function MM_openBrWindow(theURL,winName,features) { //v2.0
  window.open(theURL,winName,features);
}

function openFastOrder(platform, options){
	// check for login 2 broker
	checkRealtimeSession();

	if(platform==undefined) platform = "mm";
	var param = '';
	var height = 550;
	if(options) {
		if(options.side) param += '&side=' + options.side;
		if(options.accNo) param += '&accNo=' + options.accNo;
		if(options.symbol) param += '&placeSym=' + escape(options.symbol);
		if(options.symbolMkt) param += '&placeSys=' + options.symbolMkt;
		if(options.frameHeight){
			var frameHeight = parseInt(options.frameHeight);
			if(!isNaN(frameHeight)){
				height += frameHeight; 
				param += '&frameHeight=' + options.frameHeight;
			}
		}
	}
    var url = '/realtime/fastorder/fastorder.jsp?platform=' + platform + param;
    var windowName = getCookie("xid");
    if (windowName){
            windowName = "_" + windowName;
    }
    windowName = "FastOrder" + windowName;
    window.open(url ,windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=auto,resizable=1,width=920,height=" + height);
}

function openTechnicalChartHTML5(options){
	// options is not used in this version. This has been defined for future use
	windowName = "TechnicalChart";
	urlTechnicalChart = '/C00_ChartRedirect.jsp';
    window.open(urlTechnicalChart ,windowName,"toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=0,resizable=1");
}
