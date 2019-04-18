var TAB_KEY_CODE = 9;
var ENTER_KEY_CODE = 13;
function initStreamingLite() {

	// alert(1);
	updateAccList();
	bindUi();

	initLayout();
	
	initData();
	// fixIE();
	// stampStat();
}
function updateAccList() {
	// alert(1);
	var user = Session.user;
	var accs = user.accsEq.concat(user.accsDeriv);
	var i = 0;
	if(Global.requestAccNo) {
		i = findAcc(accs, Global.requestAccNo);
		i = i >= 0 ? i : 0;
	} else if(Session.user.defaultAccNo && Session.user.defaultAccSystem) {
		var defaultAccNo = Session.user.defaultAccNo;
		var defaultAccSystem = Session.user.defaultAccSystem;
		var index = findAcc(accs, defaultAccNo, defaultAccSystem);
		i = index >= 0 ? index : 0;
	}
	AccDisplayInv.updateAccList(accs, i);
}
function findAcc(accs, accNo, system) {
	if(system==undefined) system = 'E';
	var i =0;
	for (i=0;i<accs.length;i++) {
		if(accs[i].accNo == accNo && accs[i].system == system) {
			return i;
		}
	}
	if(i==accs.length)
		return -1;
}
function initLayout() {
	var user = Session.user;
	AccDisplay.setRole(user.role);
	if(user.isMkt()) {
		if(user.isEq) AccDisplayMkt.addSystemOption(Account.SYSTEM_EQUITY);
		if(user.isDeriv) AccDisplayMkt.addSystemOption(Account.SYSTEM_DERIV);
		AccDisplayMkt.refreshDisplay(Config.Host.current);
	}
	initMenuLayout();
	AccDisplay.refreshDisplay(user.role);
	var system = Global.requestPlaceSys ? Global.requestPlaceSys : AccDisplay.currentAcc().system;
	PlaceDisplay.refreshDisplay(system);
	PortDisplay.refreshDisplay(system);
	OrderDisplay.refreshDisplay(system);
	if(MenuDisplay.current==MenuDisplay.Home) {
		if(Global.requestQuoteSys) {
			InstQuoteDisplay.refreshDisplay(Global.requestQuoteSys);
		} else {
			InstQuoteDisplay.refreshDisplay(system);
		} 
	}
}
function initMenuLayout() {
	if(Global.requestTab && Global.requestTab == MenuDisplay.Port) {
		MenuDisplay.onClickPort();
	} else {
		MenuDisplay.onClickHome();
	}
}
function initData() {
	var user = Session.user;
	if(!user.isMkt()) {
		// AccCredDisplay.refresh();
		// OrderDisplay.refresh();
		// PortDisplay.refresh();
		if(Config.Platform.isEq && Config.Host.current == Account.SYSTEM_DERIV) {
			// AccDisplayInv.loadAccEqList();
		}
	}
	// MktSumDisplay.refreshData();
	if(Global.requestQuoteSym && MenuDisplay.current==MenuDisplay.Home) {
		// InstQuoteDisplay.submitSymbol(Global.requestQuoteSym);
	}
	if(Global.requestPlaceSym && Global.requestPlaceSys) {
		if(Global.requestPlaceSys == 'E') {
			// PlaceDisplayEq.setSymbol(Global.requestPlaceSym);
			// PlaceDisplayEq.setSide(Global.requestSide);
		} else if(Global.requestPlaceSys == 'D') {
			// PlaceDisplayDeriv.setSymbol(Global.requestPlaceSym);
			// PlaceDisplayDeriv.setSide(Global.requestSide);
		}
	}
}
function bindUi() {
	$('input.symbol').keypress(function(e) {
		onChangeSymbol(this, e);	  
	});
	if(Session.user.isMkt()) {
		$('.place span.pin').css('visibility','hidden');
	}
	AccDisplayInv.bindUi();
	AccDisplayMkt.bindUi();
	ConfirmCancelDialog.init();
	InstQuoteDisplay.bindUi();
	InstQuoteDisplayDeriv.bindUi();
	InstQuoteDisplayEq.bindUi();
	MenuDisplay.bindUi();
	OrderDisplay.bindUi();
	OrderDisplayDeriv.bindUi();
	OrderDisplayEq.bindUi();
	PlaceDisplayDeriv.bindUi();
	PlaceDisplayEq.bindUi();
}
function fixIE() {
	if(typeof String.prototype.trim !== 'function') {
	  String.prototype.trim = function() {
		return this.replace(/^\s+|\s+$|^\xA0+|\xA0+$/g, ''); 
	  };
	}
	if($.browser.msie && /MSIE 6.0/.test(navigator.userAgent)) {
		$('#confirmCancel').bgiframe();		//fix drop-down boxes floating over modal dialog with IE6
	}
}
function stampStat() {
	var url = window.location.href;
	if(url.indexOf('stat=no') == -1) {	//lazy check
		var listener = new ConnListener();
		var conn = new ServiceConn(listener);
		var url = '/realtime/fastorder/stat.jsp';
		conn.loadJSON(url, 'open=1');
	}
}
function onChangeSymbol(input, e) {
	if(e.ctrlKey) return;
	var keychar = EventUtil.charFromEvent(e);
	var alphaCheck = /[A-Za-z]/;
	if(alphaCheck.test(keychar)) {
		var sel = InputUtil.getSelection(input);
		var val = input.value;
		var pre = val.substring(0, sel.start);
		var post = val.substring(sel.end, val.length);
		input.value = pre + keychar.toUpperCase() + post;
		InputUtil.setCaretPosition(input, pre.length + 1);
		e.preventDefault();
	}
}
function lastUpdate() {
	var d = new Date().format('ddd dd MMM yyyy HH:mm:ss');
	return 'Last Update: ' + d + '';
}

function AccDisplay() {}
AccDisplay.current = User.ROLE_INTERNET;
AccDisplay.switchHost = function() {
	var acc = this.currentAcc();
	if(acc.system == Account.SYSTEM_DERIV) {
		AccDisplay._switchToDerivHost();
		return;
	} else {
		AccDisplay._switchHost();
	}
};
AccDisplay._switchHost = function() {
	var acc = this.currentAcc();
	var host = acc.system == Account.SYSTEM_EQUITY ? Config.Host.eq : Config.Host.deriv;
	var accNo = acc.accNo;
	var tab = MenuDisplay.current;
	var quoteSym = InstQuoteDisplay.currentSymbol;
	var quoteSys = InstQuoteDisplay.current;		//Account.SYSTEM_...
	var frameHeight = $("#disclaimer").height();
	var param = '?platform=mm';
	param += '&accNo=' + accNo;
	param += '&tab=' + tab;
	param += '&stat=no';
	if(quoteSym != undefined) {
		param += '&quoteSym=' + quoteSym;
		param += '&quoteSys=' + quoteSys;
	}
	if(frameHeight != undefined) {
		param += '&frameHeight=' + frameHeight;
	}
	window.location.href = host + '/realtime/fastorder/fastorder.jsp' + param;	
};
AccDisplay._switchToDerivHost = function() {
	var listener = new ConnListener();
	var conn = new ServiceConn(listener);
	listener.success = function() {
		AccDisplay._switchHost();
	};
	//if fail
	window.setTimeout("alert('Cannot connect to server')", 10000);
	
	var url = Config.Host.deriv + '/realtime/fastorder/ping.jsp?jsoncallback=?';
	conn.loadJSONP(url, '');
};
AccDisplay.currentAcc = function() {
	if(this.current == User.ROLE_INTERNET) {
		return AccDisplayInv.currentAcc();
	} else {
		return AccDisplayMkt.currentAcc();
	}	
};
AccDisplay.refresh = function() {
	this.refreshDisplay(this.current);
};
AccDisplay.refreshDisplay = function(role) {
	this.visible(false);
	if(User.isInternet(role)) {
		AccDisplayInv.visible(true);
	} else {
		AccDisplayMkt.visible(true);
		AccDisplayMkt.refreshDisplay();
	}
};
AccDisplay.setRole = function(role) {
	this.visible(false);
	if(User.isInternet(role)) {
		this.current = role;
		AccDisplayInv.visible(true);	
	} else if(User.isMkt(role)) {
		this.current = role;
		AccDisplayMkt.visible(true);	
	}
};
AccDisplay.visible = function(visible) {
	AccDisplayInv.visible(visible);
	AccDisplayMkt.visible(visible);
};

function AccDisplayInv() {}
AccDisplayInv.accs = new Array();
AccDisplayInv.bindUi = function() {
	$('#accInv').change(function() {
		AccDisplayInv.onChangeAcc();
	});
};
AccDisplayInv.currentAcc = function() {
	var currentAccIndex = $('#accInv')[0].selectedIndex;
	return this.accs[currentAccIndex];
};
AccDisplayInv.handleAccEqList = function(data) {
	var accsEq = StreamingDecoderEq.getAccList(data);
	if(this.accs.length == 1) {
		var accs = accsEq.concat(this.accs);
		this.updateAccList(accs, accs.length-1);
	}
};
AccDisplayInv.loadAccEqList = function() {
	var listener = new ConnListener();
	var conn = new S4AccListConnEq(listener);
	var accDisplay = this;
	listener.success = function(conn, data) {
		accDisplay.handleAccEqList(data);
	};
	listener.fail = function(conn, data) {
		alert("AccDisplayInv load acc EqList Cannot connect to server");
	};
	conn.reqAcc(acc);
};
AccDisplayInv.setDefaultAccIndex = function(defaultAccIndex) {
	if(defaultAccIndex == undefined || defaultAccIndex < 0 || defaultAccIndex >= this.accs.length) defaultAccIndex = 0;
	$('#accInv')[0].selectedIndex = defaultAccIndex;
	AccDisplayInv.onChangeAcc();
};
AccDisplayInv.updateAccList = function(accs, defaultAccIndex) {
	if(defaultAccIndex == undefined || defaultAccIndex < 0 || defaultAccIndex >= accs.length) defaultAccIndex = 0;
	this.accs = accs;
	var options = "";
	for(var i=0;i<accs.length;i++) {
		var isSelected = i == defaultAccIndex;
		var systemLabel = this.accs[i].system == Account.SYSTEM_EQUITY ? " (Equity)" : " (Derivatives)";
		options += "<option " + (isSelected?"selected":"") + ">" + accs[i].accNo + systemLabel + "</option>";
	}
	$('#accInv').html(options);
};
AccDisplayInv.onChangeAcc = function() {
	var acc = AccDisplay.currentAcc();
	if(acc.system != Config.Host.current) {
		AccDisplay.switchHost();
		return;
	}
	AccCredDisplay.clear();
	OrderDisplay.clear();
	PortDisplay.clear();
	AccCredDisplay.refresh();
	OrderDisplay.onChangeAcc(acc);
	PortDisplay.onChangeAcc(acc);
	PlaceDisplay.onChangeAcc(acc);
};
AccDisplayInv.visible = function(visible) {
	if(visible) $('#accInv').show();
	else $('#accInv').hide();
};

function AccDisplayMkt() {}
AccDisplayMkt.acc = undefined;
AccDisplayMkt.current = Account.SYSTEM_EQUITY;
AccDisplayMkt.bindUi = function() {
	$('#accMkt .system').change(function() {
		AccDisplayMkt.onChangeSystem();
	});
	$('#accMkt #accEq, #accMkt #accDeriv').keypress(function(e) {
		if(e.keyCode == ENTER_KEY_CODE) {
			AccCredDisplay.refresh();
			OrderDisplay.refresh();
			PortDisplay.refresh();
		}
	});
};
AccDisplayMkt.currentAcc = function() {
	if(!AccDisplayMkt.acc) AccDisplayMkt.acc = new Account();
	var acc = AccDisplayMkt.acc;
	acc.frontType = Account.FRONT_TYPE_SEOS;
	if($('#accMkt .system').val() == "eq") {
		if(acc.system != Account.SYSTEM_EQUITY
				|| acc.accNo !=  $('#accMkt #accEq').val()) {
			acc.system = Account.SYSTEM_EQUITY;
			acc.accNo = $('#accMkt #accEq').val();
			acc.clientType = undefined;
		}
	} else {
		if(acc.system != Account.SYSTEM_DERIV
				|| acc.accNo != $('#accMkt #accDeriv').val()) {
			acc.system = Account.SYSTEM_DERIV;
			acc.accNo = $('#accMkt #accDeriv').val();
			acc.clientType = undefined;
		}
	}
	return acc;
};
AccDisplayMkt.currentSystem = function() {
	return AccDisplay.currentAcc().system;
};
AccDisplayMkt.addSystemOption = function(system) {
	if(system == Account.SYSTEM_EQUITY) {
		$('#accMkt .system').append("<option value='eq'>Equity</option>");
	} else if(system == Account.SYSTEM_DERIV) {
		$('#accMkt .system').append("<option value='deriv'>Derivatives</option>");
	}
};
AccDisplayMkt.onChangeSystem = function() {
	if($('#accMkt .system').val() == "eq") {
		this.current = Account.SYSTEM_EQUITY;
	} else {
		this.current = Account.SYSTEM_DERIV;
	}
	if(this.current != Config.Host.current) {
		AccDisplay.switchHost();
		return;
	}
	this.refreshDisplay();
	var acc = this.currentAcc();
	AccCredDisplay.refreshDisplay(acc);
	PortDisplay.refreshDisplay(acc.system);
	PlaceDisplay.refreshDisplay(acc.system);
	OrderDisplay.refreshDisplay(acc.system);
};
AccDisplayMkt.refreshDisplay = function(system) {
	if(system==undefined) system=this.currentSystem();
	$('#accMkt input').hide();
	try{
		$('#accMkt select option').removeAttr('selected');
	}catch(e){}	//silly ie will throw ignorable error
	if(system == Account.SYSTEM_EQUITY) {
		try{
		$('#accMkt select option[value="eq"]').attr('selected', 'selected');
		}catch(e){}	//silly ie will throw ignorable error
		$('#accMkt #accEq').show();
	} else {
		try{
		$('#accMkt select option[value="deriv"]').attr('selected', 'selected');
		}catch(e){}	//silly ie will throw ignorable error
		$('#accMkt #accDeriv').show();
	}
};
AccDisplayMkt.visible = function(visible) {
	if(visible) $('#accMkt').show();
	else $('#accMkt').hide();
};

function AccCredDisplay() {}
AccCredDisplay.clear = function() {
	AccCredDisplayDeriv.clear();
	AccCredDisplayEq.clear();
};
AccCredDisplay.refresh = function() {
	var acc = AccDisplay.currentAcc();
	this.refreshDisplay(acc);
	this.refreshData(acc);
};
AccCredDisplay.refreshDisplay = function(acc) {
	this.visible(false);
	if(acc.system == Account.SYSTEM_EQUITY) {
		AccCredDisplayEq.visible(true);
		AccCredDisplayEq.refreshDisplay(acc);
	} else if (acc.system == Account.SYSTEM_DERIV) {
		AccCredDisplayDeriv.visible(true);
	}
};
AccCredDisplay.refreshData = function(acc) {
	if(acc.system == Account.SYSTEM_EQUITY) {
		AccCredDisplayEq.refreshData(acc);
	} else {
		AccCredDisplayDeriv.refreshData(acc);
	}
};
AccCredDisplay.visible = function(visible) {
	AccCredDisplayDeriv.visible(visible);
	AccCredDisplayEq.visible(visible);
};

function AccCredDisplayDeriv() {}
AccCredDisplayDeriv.clear = function() {
	$('#accCreditDeriv .line').text('');
	$('#accCreditDeriv .ee').text('');
	$('#accCreditDeriv .equity').text('');
};
AccCredDisplayDeriv.handleAccInfo = function(data) {
	var err = StreamingDecoderDeriv.getErr(data);
	if(err != undefined) alert(err);
	var accInfo = StreamingDecoderDeriv.getAccInfo(data);
	if(accInfo != undefined) {
		this.updateCredit(accInfo);
		this.updatePositionType(accInfo);
	}
};
AccCredDisplayDeriv.refreshData = function(acc) {
	var listener = new ConnListener();
	var conn = new S4AccInfoConnDeriv(listener);
	var accDisplay = this;
	listener.success = function(conn, data) {
		PlaceDisplay.status(acc.system, '');
		accDisplay.handleAccInfo(data);
	};
	listener.fail = function(conn, data) {
		PlaceDisplay.status(acc.system, '');
		alert("AccCreaditDisplayDeriv refresh Cannot connect to server");
	};
	conn.reqAcc(acc);
	PlaceDisplay.status(acc.system, "Fetching Data...");
};

AccCredDisplayDeriv.updateCredit = function(accInfo) {
	$('#accCreditDeriv .line').text(S4Fmt.formatPrice(accInfo.line, 2));
	$('#accCreditDeriv .ee').text(S4Fmt.formatPrice(accInfo.ee,2));
	$('#accCreditDeriv .equity').text(S4Fmt.formatPrice(accInfo.equity,2));
};
AccCredDisplayDeriv.updatePositionType = function(accInfo) {
	if(accInfo.autoNet != undefined){
		$("#placeDeriv #position").empty();
		var newOptions = new Array();
		if (accInfo.autoNet == 'Y') {
			$('"#placeDeriv #positionLabel').html('&nbsp;&nbsp;');
			$("#placeDeriv #position").css({'width': 95});
			newOptions = {"Open/Close":"A"};
		} else {
			$('#positionLabel').html('&nbsp;Position:&nbsp;');
			$("#placeDeriv #position").css({'width': 55});
			newOptions = {"Open":"O", "Close":"C"};
		}
		$.each(newOptions, function(key, value) {
			var tmp = $("<option></option>").attr("value", value).text(key);
			$("#placeDeriv #position").append(tmp);
		});
	}
};
AccCredDisplayDeriv.visible = function(visible) {
	if(visible) $('#accCreditDeriv').show();
	else $('#accCreditDeriv').hide();
};

function AccCredDisplayEq() {}
AccCredDisplayEq.clear = function() {
	this.clearCreditDGWCredBal();
	this.clearCreditDGW();
	this.clearCreditCredBal();
	this.clearCredit();
};
AccCredDisplayEq.clearCreditDGWCredBal = function() {
	$('#accCreditEqDGWCredBal .credit').text('');
	$('#accCreditEqDGWCredBal .ee').text('');
};
AccCredDisplayEq.clearCreditDGW = function() {
	$('#accCreditEqDGW .credit').text('');
	$('#accCreditEqDGW .pp').text('');
	$('#accCreditEqDGW .cashAvail').text('');
};
AccCredDisplayEq.clearCreditCredBal = function() {
	$('#accCreditEqCredBal .credit').text('');
	$('#accCreditEqCredBal .line').text('');
	$('#accCreditEqCredBal .ee').text('');
};
AccCredDisplayEq.clearCredit = function() {
	$('#accCreditEq .credit').text('');
	$('#accCreditEq .line').text('');
	$('#accCreditEq .cash').text('');
};
AccCredDisplayEq.handleAccInfo = function(acc, data) {
	var err = StreamingDecoderEq.getErr(data);
	if(err!=undefined) {
		alert(err);
		return;
	}
	var accInfo = StreamingDecoderEq.getAccInfo(data, acc);
	if(accInfo != undefined) {
		if(acc.clientType == undefined || acc.clientType == '') {
			acc.clientType = accInfo.clientType;
		}
		this.updateAccCredit(acc, accInfo);
		this.refreshDisplay(acc);
	}
};
AccCredDisplayEq.refreshData = function(acc) {
	var listener = new ConnListener();
	var conn = new S4AccInfoConnEq(listener);
	var accDisplay = this;
	listener.success = function(conn, data) {
		PlaceDisplay.status(acc.system, '');
		accDisplay.handleAccInfo(acc, data);
	};
	listener.fail = function(conn, data) {
		PlaceDisplay.status(acc.system, '');
		alert("AccCredDisplayEq.refreshData Cannot connect to server");
	};
	conn.reqAcc(acc);

	// get account name
	var listenerName = new ConnListener();
	var connName = new S4AccInfoConnEqName(listenerName);
	listenerName.success = function(connName, data) {
		PlaceDisplay.status(acc.system, '');
		accDisplay.handleAccNameInfo(data);
	};
	listenerName.fail = function(connName, data) {
		PlaceDisplay.status(acc.system, '');
	};
	connName.reqAccName(acc);

	PlaceDisplay.status(acc.system, "Fetching Data...");
};
AccCredDisplayEq.refreshDisplay = function(acc) {
	$('.accCredit').hide();
	if(acc.frontType == Account.FRONT_TYPE_DGW) {
		if(acc.accType == Account.ACC_TYPE_CREDIT_BAL) {
			$('#accCreditEqDGWCredBal').show();
		} else {
			$('#accCreditEqDGW').show();
		}
	} else {
		if(acc.accType == Account.ACC_TYPE_CREDIT_BAL) {
			$('#accCreditEqCredBal').show();
		} else {
			$('#accCreditEq').show();
		}
	}
};
AccCredDisplayEq.updateAccCredit = function(acc, accInfo) {
	if(acc.frontType == Account.FRONT_TYPE_DGW) {
		if(acc.accType == Account.ACC_TYPE_CREDIT_BAL) {
			this.updateCreditDGWCredBal(accInfo);
		} else {
			this.updateCreditDGW(accInfo);
		}
	} else {
		if(acc.accType == Account.ACC_TYPE_CREDIT_BAL) {
			this.updateCreditCredBal(accInfo);
		} else {
			this.updateCredit(accInfo);
		}
	}
};
AccCredDisplayEq.updateCreditDGWCredBal = function(accInfo) {
	$('#accCreditEqDGWCredBal .credit').text(S4Fmt.formatPrice(accInfo.credit,2));
	$('#accCreditEqDGWCredBal .ee').text(S4Fmt.formatPrice(accInfo.ee,2));
};
AccCredDisplayEq.updateCreditDGW = function(accInfo) {
	$('#accCreditEqDGW .credit').text(S4Fmt.formatPrice(accInfo.credit,2));
	$('#accCreditEqDGW .pp').text(S4Fmt.formatPrice(accInfo.pp,2));
	if (accInfo.cashAvail == "N/A") {
		$('#accCreditEqDGW .cashAvailLabel').hide();
		$('#accCreditEqDGW .cashAvail').hide();
	} else {
		$('#accCreditEqDGW .cashAvailLabel').show();
		$('#accCreditEqDGW .cashAvail').show();
		$('#accCreditEqDGW .cashAvail').text(S4Fmt.formatPrice(accInfo.cashAvail,2));
	}
};
AccCredDisplayEq.updateCreditCredBal = function(accInfo) {
	$('#accCreditEqCredBal .credit').text(S4Fmt.formatPrice(accInfo.credit,2));
	$('#accCreditEqCredBal .line').text(S4Fmt.formatPrice(accInfo.line,2));
	$('#accCreditEqCredBal .ee').text(S4Fmt.formatPrice(accInfo.ee,2));
};
AccCredDisplayEq.updateCredit = function(accInfo) {
	$('#accCreditEq .credit').text(S4Fmt.formatPrice(accInfo.credit,2));
	$('#accCreditEq .line').text(S4Fmt.formatPrice(accInfo.line,2));
	$('#accCreditEq .cash').text(S4Fmt.formatPrice(accInfo.cash,2));
};
AccCredDisplayEq.handleAccNameInfo = function(data) {
	var msgToken = data.split( DELIMITER_LV1 );
	if (msgToken.length >= 2 && msgToken[0] == "T") {
		var name = msgToken[1].trim();
		if(name.length > 18) name = name.substring(0,18) + '...';
		$('#accName').text(name);
	} else {
		$('#accName').text("");
	}
};
AccCredDisplayEq.visible = function(visible) {
	if(visible) $('.accCredit').show();
	else $('.accCredit').hide();
};

function ConfirmCancelDialog() {}
ConfirmCancelDialog.callback = function(){};
ConfirmCancelDialog.ok = false;
ConfirmCancelDialog.isMkt = false;
ConfirmCancelDialog.close = function() {
	$('#confirmCancel').dialog('close');
};
ConfirmCancelDialog.init = function() {
	$('#confirmCancel').dialog({ 
		autoOpen : false,
		buttons: {
			"No Cancel": function() {
				ConfirmCancelDialog.ok = false;
				$(this).dialog("close");
			},
			"Confirm Cancel": function() {
				ConfirmCancelDialog.ok = true;
				var isMkt = ConfirmCancelDialog.isMkt;
				var pin = ConfirmCancelDialog.getPin();
				if(!isMkt && pin=='') {
					ConfirmCancelDialog.setStatus("Please insert PIN");
				} else if(!isMkt && !validatePin(pin)) {
					ConfirmCancelDialog.setStatus("Invalid PIN format");	
				} else {
					$(this).dialog("close");
				}
			}
		},
		open: function(event, ui) { 
			ConfirmCancelDialog.ok = false; 
			if(!ConfirmCancelDialog.isMkt) {
				$('#confirmCancel input.pin').focus();
			} else {
				$('.ui-dialog-buttonpane > button:last').focus();		//confirm button
			}
		},
		width : 400,
		close : function() {
			ConfirmCancelDialog.callback.call(this, ConfirmCancelDialog.ok);
		},
		modal : true
	});
	$('#confirmCancel input.pin').keypress(function(e) {
		if(e.keyCode == ENTER_KEY_CODE) {
			$('.ui-dialog-buttonpane > button:last').click();		//confirm button
		}
	});
};
ConfirmCancelDialog.open = function(isMkt, onClose, pin) {
	ConfirmCancelDialog.isMkt = isMkt;
	ConfirmCancelDialog.callback = onClose;
	if(!isMkt) $('#confirmCancel div.pin').show();
	else $('#confirmCancel div.pin').hide();
	if(pin==undefined) $('#confirmCancel input.pin').val('');
	else $('#confirmCancel input.pin').val(pin);
	$('#confirmCancel .status').html('');
	$('#confirmCancel').dialog('open');
};
ConfirmCancelDialog.setMsg = function(msg) {
	$('#confirmCancel .msg').html(msg);
};
ConfirmCancelDialog.getPin = function() {
	return $('#confirmCancel input.pin').val();
};
ConfirmCancelDialog.setStatus = function(status) {
	$('#confirmCancel .status').html(status);
};

function Display() {}
Display.styleBidOffer = function(element, close, priceDigit) {
	var text = $(element).text().toLowerCase();
	if(text.trim().length  >0 && text != 'ato' && text != 'atc' && text != 'mp' && text != 'market') {
		Display.stylePrice(element, close, priceDigit);
	}
};
Display.styleRealizedPL = function(element) {
	var real = $(element).text().toLowerCase();
	if(real != '-' && real != 'n/a') {
		$(element).text(S4Fmt.formatChg(real, 2));
		var color = Style.Color.realizedPL(real);
		$(element).css('color', color);
	}
};
Display.styleChg = function(element, close, priceDigit) {
	var chg = $(element).text();
	$(element).text(S4Fmt.formatChg(chg, priceDigit));
	var color = Style.Color.colorChg(chg, close);
	$(element).css('color', color);
};
Display.stylePChg = function(element, close) {
	this.styleChg(element, close, 2);
};
Display.styleClose = function(element, priceDigit) {
	var price = $(element).text();
	$(element).text(S4Fmt.formatPrice(price, priceDigit));
};
Display.stylePrice = function(element, close, priceDigit) {
	var price = $(element).text();
	if(price.trim().length > 0) {
		$(element).text(S4Fmt.formatPrice(price, priceDigit));
		var color = Style.Color.colorPrice(price, close);
		$(element).css('color', color);
	}
};
Display.styleVol = function(element) {
	var vol = $(element).text();
	if(vol.trim().length > 0) {
		$(element).text(S4Fmt.formatVol(vol));
	}
};

function InstQuoteDisplay() {}
InstQuoteDisplay.current = Account.SYSTEM_EQUITY;
InstQuoteDisplay.currentSymbol = undefined;
InstQuoteDisplay.bindUi = function() {
	$('#instInfo td.symbol div').hover(
		function () {
			$(this).children('span').css('visibility', 'visible');
			$(this).css('border','solid 1px #3FF');
		},
		function () {
			$(this).children('span').css('visibility', 'hidden');
			$(this).css('border','none');
		}
	);
};
InstQuoteDisplay.clear = function() {
	InstQuoteDisplay.currentSymbol = undefined;
	InstQuoteDisplayDeriv.clear();
	InstQuoteDisplayEq.clear();
};
InstQuoteDisplay.handleInstQuote = function(data) {
	var err = FastQuoteDecoder.getError(data);
	if(err!=undefined) {
		alert(err.message);
		this.clear();
		return;
	}
	if(FastQuoteDecoder.isEquity(data) && !Config.Platform.isEq) {
		alert("Stock not found");
		this.clear();
		return
	}
	if(!FastQuoteDecoder.isEquity(data) && !Config.Platform.isDeriv) {
		alert("Stock not found");
		this.clear();
		return
	}
	var show = this.visible();
	this.visible(false);
	if(FastQuoteDecoder.isEquity(data)) {
		InstQuoteDisplay.current = Account.SYSTEM_EQUITY;
		InstQuoteDisplayEq.visible(show);
		InstQuoteDisplayEq.handleInstQuote(data);
	} else {
		InstQuoteDisplay.current = Account.SYSTEM_DERIV;
		InstQuoteDisplayDeriv.visible(show);
		InstQuoteDisplayDeriv.handleInstQuote(data);
	}
};
InstQuoteDisplay.refresh = function() {
	InstQuoteDisplay.refreshData();
	InstQuoteDisplay.refreshDisplay (InstQuoteDisplay.current);
};
InstQuoteDisplay.refreshData = function() {
	if(InstQuoteDisplay.currentSymbol != undefined) {
		InstQuoteDisplay.submitSymbol(InstQuoteDisplay.currentSymbol);
	}
};
InstQuoteDisplay.refreshDisplay = function(system) {
	this.visible(false);
	if(system == Account.SYSTEM_EQUITY) {
		InstQuoteDisplayEq.visible(true);
	} else {
		InstQuoteDisplayDeriv.visible(true);
	}
};
InstQuoteDisplay.submitSymbol = function(symbol) {
	if(symbol == undefined || symbol == '') return;
	InstQuoteDisplay.currentSymbol = symbol;
	var listener = new ConnListener();
	var conn = new FQInstInfoConn(listener);
	listener.success = function(conn, data) {
		$('.instQuote .loading').css('visibility', 'hidden');
		$('.instQuote .loading').dotdotdot("stop");
		if(!data.exception) {
			InstQuoteDisplay.handleInstQuote(data);
		}
	};
	listener.fail = function(conn, data) {
		$('.instQuote .loading').css('visibility', 'hidden');
		$('.instQuote .loading').dotdotdot("stop");
	};
	conn.request(symbol);
	$('.instQuote .loading').css('visibility', 'visible');
	$('.instQuote .loading').dotdotdot();
};
InstQuoteDisplay.visible = function(visible) {
	if(visible==undefined) {
		return this._visible();	
	}
	InstQuoteDisplayEq.visible(visible);
	InstQuoteDisplayDeriv.visible(visible);
};
InstQuoteDisplay._visible = function() {
	return InstQuoteDisplayEq.visible() || InstQuoteDisplayDeriv.visible();
};

function InstQuoteDisplayDeriv() {}
InstQuoteDisplayDeriv.bindUi = function() {
	$('#instQuoteDeriv td.symbol input.symbol').keyup(function(e) {
		if(e.keyCode == ENTER_KEY_CODE) {
			//var symbol = this.value;
			InstQuoteDisplayDeriv.onSubmitSymbolInput();
			MktSumDisplay.refreshData();
		}
	});
	$('#instQuoteDeriv td.symbol input.symbol').focus(function() {
		if(this.value=='Enter Symbol') {
			this.value = '';
			$(this).css('color', '#000');
			$(this).css('font-weight', 'bold');
		}
	});
	$('#instQuoteDeriv td.symbol input.symbol').blur(function() {
		if(this.value=='') {
			this.value = 'Enter Symbol';
			$(this).css('color', '#999');
			$(this).css('font-weight', '');
		}
	});
	$('#instQuoteDeriv .refreshQuoteBtn').click(function() {
			InstQuoteDisplayDeriv.onSubmitSymbolInput();
			MktSumDisplay.refreshData();
	});
};
InstQuoteDisplayDeriv.clear = function() {
	$('#instBidOfferDeriv .bid').text('');
	$('#instBidOfferDeriv .offer').text('');
	$('#instBidOfferDeriv .volBid').text('');
	$('#instBidOfferDeriv .volOffer').text('');
	$('#instInfoDeriv td.symbol input.symbol').val('');
	$('#instInfoDeriv input.symbol').val('');
	$('#instInfoDeriv .last').text('');
	$('#instInfoDeriv .chgGrp').css('visibility', 'hidden');
	$('#instInfoDeriv .chg').text('');
	$('#instInfoDeriv .pChg').text('');
	$('#instInfoDeriv .volume').text('');
	$('#instInfoDeriv .oi').text('');
	$('#instInfoDeriv .high').text('');
	$('#instInfoDeriv .low').text('');
	$('#instInfoDeriv .ceil').text('');
	$('#instInfoDeriv .floor').text('');
	$('#instInfoDeriv .avg').text('');
	$('#instInfoDeriv .prevSettle').text('');
	$('#instInfoDeriv .state').text('');
	$('#instInfoDeriv .stateVal').text('');
	$('#instTickerDeriv td.time').html('&nbsp;');
	$('#instTickerDeriv td.side').html('&nbsp;');
	$('#instTickerDeriv td.volume').html('&nbsp;');
	$('#instTickerDeriv td.price').html('&nbsp;');
	$('#instBuySellDeriv .label .pBuy').text('Buy ');
	$('#instBuySellDeriv .label .pSell').text(' Sell');
	$('#instBuySellDeriv .bar .pBuy').css('width', '1%');
	$('#instBuySellDeriv .bar .pSell').css('width', '1%');
};
InstQuoteDisplayDeriv.handleInstQuote = function(data) {
	var info = FastQuoteDecoder.getInstInfoDeriv(data);
	var ticker = FastQuoteDecoder.getInstShortTicker(data);
	if(ticker) {
		InstQuoteDisplayDeriv.replaceDataTicker(ticker);
	}
	if(info) {
		InstQuoteDisplayDeriv.lastUpdate();
		InstQuoteDisplayDeriv.replaceDataInfo(info);
		InstQuoteDisplayDeriv.replaceDataState(info);
		InstQuoteDisplayDeriv.replaceDataBidOffer(info);
		InstQuoteDisplayDeriv.replaceDataBuySell(info);
		var prevSettle = info.prevSettle;
		var priceDigit = info.priceDigit;
		InstQuoteDisplayDeriv.styleBidOffer(prevSettle, priceDigit);
		InstQuoteDisplayDeriv.styleInfo(info);
		InstQuoteDisplayDeriv.styleTicker(prevSettle, priceDigit);
		if(PlaceDisplayDeriv.isVisible()) {
			PlaceDisplayDeriv.setSymbol(info.instrument);
		}
	}
};
InstQuoteDisplayDeriv.lastUpdate = function() {
	$('#instQuoteDeriv .lastUpdate').html(lastUpdate());
};
InstQuoteDisplayDeriv.onSubmitSymbolInput = function() {
	var symbol = $('#instQuoteDeriv td.symbol input.symbol').val().toUpperCase();
	InstQuoteDisplay.submitSymbol(symbol);
};
InstQuoteDisplayDeriv.replaceDataBidOffer = function(info) {
	$('#instBidOfferDeriv .bid').each(function(i) {
		$(this).text(info.bid[i]);
	});
	$('#instBidOfferDeriv .offer').each(function(i) {
		$(this).text(info.offer[i]);
	});
	$('#instBidOfferDeriv .volBid').each(function(i) {
		$(this).text(info.volBid[i]);
	});
	$('#instBidOfferDeriv .volOffer').each(function(i) {
		$(this).text(info.volOffer[i]);
	});
};
InstQuoteDisplayDeriv.replaceDataInfo = function(info) {
	$('#instInfoDeriv td.symbol input.symbol').val(info.instrument);
	$('#instInfoDeriv input.symbol').val(info.instrument);
	$('#instInfoDeriv .last').text(info.last);
	$('#instInfoDeriv .chgGrp').css('visibility', 'visible');
	$('#instInfoDeriv .chg').text(info.chg);
	$('#instInfoDeriv .pChg').text(info.pChg);
	$('#instInfoDeriv .volume').text(info.totalVol);
	$('#instInfoDeriv .oi').text(info.oi);
	$('#instInfoDeriv .high').text(info.high);
	$('#instInfoDeriv .low').text(info.low);
	$('#instInfoDeriv .ceil').text(info.ceil);
	$('#instInfoDeriv .floor').text(info.floor);
	$('#instInfoDeriv .avg').text(info.avg);
	$('#instInfoDeriv .prevSettle').text(info.prevSettle);
};
InstQuoteDisplayDeriv.replaceDataState = function(info) {
	//var label, val, vol;
	var label = "";
	var val = "";
	$('#instInfoDeriv .state').text("");
	$('#instInfoDeriv .stateVal').text("");
	var mktstate = info.state.toLowerCase();
	if(mktstate == "Pre-Open 1".toLowerCase()) {
		label = "Prj-O1 (Price, Vol)";
		val = info.projOpen1;
	} else if (mktstate == "Open 1".toLowerCase()) {
		label = "Open 1";
		val = info.openPrice1;
	} else if (mktstate == "Pre-Open 2".toLowerCase()) {
		label = "Prj-O2 (Price, Vol)";
		val = info.projOpen2;						// EQUITY uses projectedOpen1 for Proj-O2
	} else if (mktstate == "Open 2".toLowerCase()) {
		label = "Open 2";
		val = info.openPrice2;
	} else if (mktstate == "Settle".toLowerCase()) {
		label = "Settle";
		val = info.settlePrice;						// EQUITY uses projectedOpen1 for Proj-O2
	} else if (mktstate == "Close".toLowerCase()) {
		label = "Close";
		val = info.last;
	} else if (mktstate == "Previous Settle".toLowerCase()) {
		label = "P.Settle";
		val = info.prevSettle;
	} else if (mktstate == "Pre-Open 0".toLowerCase()) {
		label = "Prj-O (Price, Vol)";
		val = info.projOpen0;
	} else if (mktstate == "Open 0".toLowerCase()) {
		label = "Open 0";
		val = info.openPrice0;
	} else {
		label = "";
		val = "";
	}
	$('#instInfoDeriv .state').text(label);
	$('#instInfoDeriv .stateVal').text(val);
};
InstQuoteDisplayDeriv.replaceDataTicker = function(tickers) {
	$('#instTickerDeriv').find('td.time, td.side, td.volume, td.price').html("<span>&nbsp;</span>");
	$('#instTickerDeriv tr:gt(0)').each(function(i) {
		if(i>=tickers.length) return;
		$(this).children('td.time').text(tickers[i].time);
		$(this).children('td.side').text(tickers[i].side == "NS" ? "" : tickers[i].side);
		$(this).children('td.volume').text(tickers[i].vol);
		$(this).children('td.price').text(tickers[i].price);
	});
};
InstQuoteDisplayDeriv.replaceDataBuySell = function(info) {
	$('#instBuySellDeriv .label .pBuy').text('Buy ' + info.pBuy + '%');
	$('#instBuySellDeriv .label .pSell').text(info.pSell + '% Sell');
	if(info.pBuy != 0) {
		$('#instBuySellDeriv .bar .pBuy').css('width', info.pBuy + '%');
	} else {
		$('#instBuySellDeriv .bar .pBuy').css('width', '1%');
	}
	if(info.pSell != 0) {
		$('#instBuySellDeriv .bar .pSell').css('width', info.pSell + '%');
	} else {
		$('#instBuySellDeriv .bar .pSell').css('width', '1%');
	}
	if(info.pNonSide != 0) {
		$('#instBuySellDeriv .bar .pNonside').css('width', info.pNonSide + '%');
		$('#instBuySellDeriv .bar .pNonside').css('border', 'solid 1px #b4b4b4');
	} else {
		$('#instBuySellDeriv .bar .pNonside').css('width', '0%');
		$('#instBuySellDeriv .bar .pNonside').css('border', '');
	}
};
InstQuoteDisplayDeriv.styleBidOffer = function(prevSettle, priceDigit) {
	var bo = $('#instBidOfferDeriv');
	bo.find('.volBid, .volOffer').each(function() {
		if($(this).text().trim().length  >0) {
			Display.styleVol(this);
		}
	});
	bo.find('.bid, .offer').each(function() {
		Display.styleBidOffer(this, prevSettle, priceDigit);
	});
};
InstQuoteDisplayDeriv.styleInfo = function(info) {
	//var close = info.close;
	var last = info.last;
	var prevSettle = info.prevSettle;
	var priceDigit = info.priceDigit;
	var state = info.state;
	var instInfo = $('#instInfoDeriv');
	instInfo.find('.last, .high, .low, .ceil, .floor, .avg').each(function() {
		Display.stylePrice(this, prevSettle, priceDigit);
	});
	instInfo.find('.stateVal').each(function() {
		if(state == "Settle") {
			Display.stylePrice(this, prevSettle, info.settleDigit);
		} else {
			Display.stylePrice(this, prevSettle, priceDigit);
		}
	});
	instInfo.find('.oi, .volume').each(function() {
		Display.styleVol(this);
	});
	instInfo.find('.prevSettle').each(function() {
		Display.styleClose(this, priceDigit);
	});
	var color;
	instInfo.find('.chg').each(function() {
		Display.styleChg(this, last, priceDigit);
		color = $(this).css('color');
		$(this).parent().css('color', color);
	});
	instInfo.find('.pChg').each(function() {
		Display.stylePChg(this, last);
	});
	//instInfo.find('td.symbol input.symbol').css('color',color);
	instInfo.find('td.symbol input.symbol').css('color', '#000');
	instInfo.find('td.symbol input.symbol').css('font-weight', 'bold');
};
InstQuoteDisplayDeriv.styleTicker = function(prevSettle, priceDigit) {
	var t = $('#instTickerDeriv');
	t.find('.price').each(function() {
		var val = $(this).text();
		if(val.trim().length!=0) {
			Display.stylePrice(this, prevSettle, priceDigit);
		}
	});
	t.find('.volume').each(function() {
		Display.styleVol(this);
	});
	t.find('.side').each(function() {
		var bs = $(this).text();
		var color = Style.Color.side(bs);
		$(this).css('color', color);
		$(this).next().css('color', color);
	});
};
InstQuoteDisplayDeriv.visible = function(visible) {
	if(visible == undefined) {
		return this._visible();
	}
	if(visible) $('#instQuoteDeriv').show();
	else $('#instQuoteDeriv').hide();
};
InstQuoteDisplayDeriv._visible = function() {
	return $('#instQuoteDeriv').css('display') != 'none';
};

function InstQuoteDisplayEq() {}
InstQuoteDisplayEq.bindUi = function() {
	$('#instQuoteEq td.symbol input.symbol').keyup(function(e) {
		if(e.keyCode == ENTER_KEY_CODE) {
			InstQuoteDisplayEq.onSubmitSymbolInput();
			MktSumDisplay.refreshData();
		}
	});
	$('#instQuoteEq td.symbol input.symbol').focus(function() {
		if(this.value=='Enter Symbol') {
			this.value = '';
			$(this).css('color', '#000');
			$(this).css('font-weight', 'bold');
		}
	});
	$('#instQuoteEq td.symbol input.symbol').blur(function() {
		if(this.value=='') {
			this.value = 'Enter Symbol';
			$(this).css('color', '#999');
			$(this).css('font-weight', '');
		}
	});
	$('#instQuoteEq .refreshQuoteBtn').click(function() {
			InstQuoteDisplayEq.onSubmitSymbolInput();
			MktSumDisplay.refreshData();
	});
};
InstQuoteDisplayEq.clear = function() {
	$('#instBidOfferEq .bid').text('');
	$('#instBidOfferEq .offer').text('');
	$('#instBidOfferEq .volBid').text('');
	$('#instBidOfferEq .volOffer').text('');
	$('#instInfoEq td.symbol input.symbol').val('');
	$('#instInfoEq input.symbol').val('');
	$('#instInfoEq .last').text('');
	$('#instInfoEq .chgGrp').css('visibility', 'hidden');
	$('#instInfoEq .chg').text('');
	$('#instInfoEq .pChg').text('');
	$('#instInfoEq .volume').text('');
	$('#instInfoEq .val').text('');
	$('#instInfoEq .high').text('');
	$('#instInfoEq .low').text('');
	$('#instInfoEq .ceil').text('');
	$('#instInfoEq .floor').text('');
	$('#instInfoEq .avg').text('');
	$('#instInfoEq .close').text('');
	$('#instInfoEq .state').text('');
	$('#instInfoEq .stateVal').text('');
	$('#instInfoEq .stateVol').text('');
	$('#instTickerEq td.time').html('&nbsp;');
	$('#instTickerEq td.side').html('&nbsp;');
	$('#instTickerEq td.volume').html('&nbsp;');
	$('#instTickerEq td.price').html('&nbsp;');
	$('#instBuySellEq .label .pBuy').text('Buy ');
	$('#instBuySellEq .label .pSell').text(' Sell');
	$('#instBuySellEq .bar .pBuy').css('width', '1%');
	$('#instBuySellEq .bar .pSell').css('width', '1%');
};
InstQuoteDisplayEq.getSymbol = function() {
	//[ BLISS (NP, NC, SP) ]
	var symbol = $('#instQuoteEq td.symbol input.symbol').val().toUpperCase();
	var index = symbol.indexOf('(');
	if(index > -1) {
		symbol = symbol.substring(0, index).trim();
	}
	return symbol;
};
InstQuoteDisplayEq.handleInstQuote = function(data) {
	var info = FastQuoteDecoder.getInstInfoEq(data);
	InstQuoteDisplayEq.lastUpdate();
	var ticker = FastQuoteDecoder.getInstShortTicker(data);
	InstQuoteDisplayEq.replaceDataInfo(info);
	InstQuoteDisplayEq.replaceDataState(info);
	InstQuoteDisplayEq.replaceDataBidOffer(info);
	InstQuoteDisplayEq.replaceDataBuySell(info);
	InstQuoteDisplayEq.replaceDataTicker(ticker);
	var close = info.close;
	var priceDigit = info.priceDigit;
	InstQuoteDisplayEq.styleBidOffer(close, priceDigit);
	InstQuoteDisplayEq.styleInfo(close, priceDigit);
	InstQuoteDisplayEq.styleTicker(close, priceDigit);
	if(PlaceDisplayEq.isVisible()) {
		PlaceDisplayEq.setSymbol(info.instrument);
	}
};
InstQuoteDisplayEq.lastUpdate = function() {
	$('#instQuoteEq .lastUpdate').html(lastUpdate());
};
InstQuoteDisplayEq.onSubmitSymbolInput = function() {
	var symbol = this.getSymbol();
	InstQuoteDisplay.submitSymbol(symbol);
};
InstQuoteDisplayEq.replaceDataBidOffer = function(info) {
	$('#instBidOfferEq .bid').each(function(i) {
		$(this).text(info.bid[i]);
	});
	$('#instBidOfferEq .offer').each(function(i) {
		$(this).text(info.offer[i]);
	});
	$('#instBidOfferEq .volBid').each(function(i) {
		$(this).text(info.volBid[i]);
	});
	$('#instBidOfferEq .volOffer').each(function(i) {
		$(this).text(info.volOffer[i]);
	});
};
InstQuoteDisplayEq.replaceDataInfo = function(info) {
	var status = info.sStatus ? ' (' + info.sStatus + ')' : ''; 
	$('#instInfoEq td.symbol input.symbol').val(info.instrument + status);
	$('#instInfoEq .last').text(info.last);
	$('#instInfoEq .chgGrp').css('visibility', 'visible');
	$('#instInfoEq .chg').text(info.chg);
	$('#instInfoEq .pChg').text(info.pChg);
	$('#instInfoEq .volume').text(info.totalVol);
	$('#instInfoEq .val').text(info.valK);
	$('#instInfoEq .high').text(info.high);
	$('#instInfoEq .low').text(info.low);
	$('#instInfoEq .ceil').text(info.ceil);
	$('#instInfoEq .floor').text(info.floor);
	$('#instInfoEq .avg').text(info.avg);
	$('#instInfoEq .close').text(info.close);
};
InstQuoteDisplayEq.replaceDataState = function(info) {
	var label, val, vol;
	if(info.state == "Prj-Open1(Price,Vol)") {
		label = "Prj-O1 (Price, Vol)";
		val = info.projOpen1;
		vol = info.projVol;
	} else if (info.state == "Open 1") {
		label = "Open 1";
		val = info.openPrice1;
		vol = '';
	} else if (info.state == "Prj-Open2(Price,Vol)") {
		label = "Prj-O2 (Price, Vol)";
		val = info.projOpen1;						// EQUITY uses projectedOpen1 for Proj-O2
		vol = info.projVol;
	} else if (info.state == "Open 2") {
		label = "Open 2";
		val = info.openPrice2;
		vol = '';
	} else if (info.state == "Prj-Close(Price,Vol)") {
		label = "Prj-C (Price, Vol)";
		val = info.projOpen1;						// EQUITY uses projectedOpen1 for Proj-O2
		vol = info.projVol;
	} else if (info.state == "Close") {
		label = "Close";
		val = info.last;
		vol = '';
	} else if (info.state == "Prj-Open(Price,Vol)") {
		label = "Prj-O (Price, Vol)";
		val = info.projOpen1;						// EQUITY uses projectedOpen1 for Proj-O2
		vol = info.projVol;
	} else {
		label = info.state;
		val = '';
		vol = '';
	}
	$('#instInfoEq .state').text(label);
	$('#instInfoEq .stateVal').text(val);
	$('#instInfoEq .stateVol').text(vol);
};
InstQuoteDisplayEq.replaceDataTicker = function(tickers) {
	$('#instTickerEq').find('td.time, td.side, td.volume, td.price').html("<span>&nbsp;</span>"); 
	$('#instTickerEq tr:gt(0)').each(function(i) {
		if(i>=tickers.length) return;
		$(this).children('td.time').text(tickers[i].time);
		$(this).children('td.side').text(tickers[i].side == "NS" ? "" : tickers[i].side);
		$(this).children('td.volume').text(tickers[i].vol);
		$(this).children('td.price').text(tickers[i].price);
	});
};
InstQuoteDisplayEq.replaceDataBuySell = function(info) {
	$('#instBuySellEq .label .pBuy').text('Buy ' + info.pBuy + '%');
	$('#instBuySellEq .label .pSell').text(info.pSell + '% Sell');
	if(info.pBuy != 0) {
		$('#instBuySellEq .bar .pBuy').css('width', info.pBuy + '%');
	} else {
		$('#instBuySellEq .bar .pBuy').css('width', '1%');
	}
	if(info.pSell != 0) {
		$('#instBuySellEq .bar .pSell').css('width', info.pSell + '%');
	} else {
		$('#instBuySellEq .bar .pSell').css('width', '1%');
	}
	if(info.pNonSide != 0) {
		$('#instBuySellEq .bar .pNonside').css('width', info.pNonSide + '%');
		$('#instBuySellEq .bar .pNonside').css('border', 'solid 1px #b4b4b4');
	} else {
		$('#instBuySellEq .bar .pNonside').css('width', '0%');
		$('#instBuySellEq .bar .pNonside').css('border', '');
	}
};
InstQuoteDisplayEq.styleBidOffer = function(close, priceDigit) {
	var bo = $('#instBidOfferEq');
	bo.find('.volBid, .volOffer').each(function() {
		Display.styleVol(this);
	});
	bo.find('.bid, .offer').each(function() {
		Display.styleBidOffer(this, close, priceDigit);
	});
};
InstQuoteDisplayEq.styleInfo = function(close, priceDigit) {
	var info = $('#instInfoEq');
	info.find('.last, .high, .low, .ceil, .floor, .avg, .stateVal').each(function() {
		Display.stylePrice(this, close, priceDigit);
	});
	info.find('.val, .volume, .stateVol').each(function() {
		Display.styleVol(this);
	});
	info.find('.close').each(function() {
		Display.styleClose(this, priceDigit);
	});
	info.find('.floor').each(function() {
		Display.stylePrice(this, close, priceDigit);
	});
	var lastColor = info.find('.last').css('color');
	info.find('.chg, .pChg').each(function() {
		Display.styleChg(this, close, priceDigit);
		$(this).css('color', lastColor);
		$(this).parent().css('color', lastColor);
	});
	//info.find('td.symbol input.symbol').css('color', lastColor);
	info.find('td.symbol input.symbol').css('font-weight', 'bold');
	info.find('td.symbol input.symbol').css('color', '#000');
};
InstQuoteDisplayEq.styleTicker = function(close, priceDigit) {
	var t = $('#instTickerEq');
	t.find('.price').each(function() {
		var val = $(this).text();
		if(val.trim().length!=0) {
			Display.stylePrice(this, close, priceDigit);
		}
	});
	t.find('.volume').each(function() {
		Display.styleVol(this);
	});
	t.find('.side').each(function() {
		var bs = $(this).text();
		var color = Style.Color.side(bs);
		$(this).css('color', color);
		$(this).next().css('color', color);
	});
};
InstQuoteDisplayEq.submitSymbol = function(symbol) {
	var data = {"sector":"ENERG","last":282,"type":"stock","d5":"301.00 / 275.00","close":275,"open":0,"bo":["282.00","284.00",281,287,280,0,279,0,0,0],"mktstatus":"Close","ticker":["14:15:57","S",2000,282,"13:23:03","S",500,282,"13:07:50","B",1000,283],"avg":282.29,"settleDecimal":2,"symbol":"PTT","mkt":"equity","open2":282,"chg":7,"pbuy":"28.57","pe":"7.16","eps":"23.52","pchg":2.5454545454545454,"priceDecimal":2,"pbv":"1.51","floor":192.5,"bsp":[283,282],"openopendata":0,"language":"en","low":282,"avgbuy":"283.00","val":0.988,"industryname":"Resources","dy":"3.68","ceil":357,"bsv":[1,1000,0,0,1000,28.571428571428573,0,0,2500,2,2500,71.42857142857143],"par":"10.00","vol":3500,"sectorbarBuy":30.555555555555557,"name":"PTT PUBLIC CO.,LTD.","marketbarBuy":69.76744186046511,"psell":"71.43","avgsell":"282.00","symbolbarBuy":28.571428571428573,"openopen":"Open 1","mktlabel":"SET","sStatus":"","sectorname":"Energy & Utilities","bov":[33000,11500,8000,6000,4000,0,50000,0,0,0],"cur":"(Baht)","high":283,"spread":1};
	InstQuoteDisplayEq.handleInstQuote(data);
	// var listener = new ConnListener();
	// var conn = new FQInstInfoConn(listener);
	// listener.success = function(conn, data) {
		// InstQuoteDisplayEq.handleInstQuote(data);
	// PlaceDisplayEq.status('');
	// };
	// conn.requestEq(symbol);
	// PlaceDisplayEq.status("Fetching Data...");
};
InstQuoteDisplayEq.visible = function(visible) {
	if(visible==undefined) {
		return this._visible();
	}
	if(visible) $('#instQuoteEq').show();
	else $('#instQuoteEq').hide();
};
InstQuoteDisplayEq._visible = function() {
	return $('#instQuoteEq').css('display') != 'none';
};

function MenuDisplay() {}
MenuDisplay.Home = "Home";
MenuDisplay.Port = "Port";
MenuDisplay.current = MenuDisplay.Home;
MenuDisplay.bindUi = function() {
	$('#menu a.home').click(function() {
		MenuDisplay.onClickHome();
		return false;
	});
	$('#menu a.port').click(function() {
		MenuDisplay.onClickPort();
		return false;
	});
};
MenuDisplay.onClickHome = function() {
	MenuDisplay.current = MenuDisplay.Home;
	$('#menu li').removeClass('selected');
	$('#menu li.home').addClass('selected');
	PortDisplay.visible(false);
	InstQuoteDisplay.refresh();
};
MenuDisplay.onClickPort = function() {
	MenuDisplay.current = MenuDisplay.Port;
	$('#menu li').removeClass('selected');
	$('#menu li.port').addClass('selected');
	InstQuoteDisplay.visible(false);
	PortDisplay.refresh();
};

function MktSumDisplay() {}
MktSumDisplay.handleMktSum = function(data) {
	var mktStatus = MktSumDecoder.getMktStatus(data);
	this.replaceMktStatus(mktStatus);
};
MktSumDisplay.refreshData = function() {
	var listener = new ConnListener();
	var conn = new MktSumConn(listener);
	listener.success = function(conn, data) {
		MktSumDisplay.handleMktSum(data);
	};
	conn.request();
	/*Config.Platform.isEq*/
};
MktSumDisplay.replaceMktStatus = function(mktStatus) {
	$('#mktStatus').html('&nbsp;');
	var statusHtml = '';
	if(Config.Platform.isEq) {
		statusHtml += "SET : <span class='vol'>" + mktStatus.setStatus + "</span>";	
	}
	if(Config.Platform.isDeriv) {
		statusHtml += "  TFEX-Equity Index : <span class='vol'>" + mktStatus.eqStatus + "</span>";	
		statusHtml += "  TFEX-Metal : <span class='vol'>" + mktStatus.metalStatus + "</span>";
		if (mktStatus.energyStatus!=undefined && mktStatus.energyStatus.length > 0) {
			statusHtml += "  TFEX-Energy : <span class='vol'>" + mktStatus.energyStatus + "</span>";
		}
		statusHtml += "  TFEX-Currency : <span class='vol'>" + mktStatus.currencyStatus + "</span>";	
		statusHtml += "  TFEX-Interest Rate : <span class='vol'>" + mktStatus.irStatus + "</span>";	
		statusHtml += "  TFEX-Single Stock : <span class='vol'>" + mktStatus.singleStockStatus + "</span>";	
		if (mktStatus.agriculturalStatus!=null && mktStatus.agriculturalStatus.length > 0)
			statusHtml += "  TFEX-Agricultural : <span class='vol'>" + mktStatus.agriculturalStatus + "</span>";
		if (mktStatus.physicalstatus!=null && mktStatus.physicalstatus.length > 0)
			statusHtml += "  TFEX-Deferred : <span class='vol'>" + mktStatus.physicalstatus + "</span>";
		statusHtml = "<marquee behavior='scroll' direction='left' scrollamount='2'>" + statusHtml + "</marquee>";
	}
	$('#mktStatus').html(statusHtml);
};

function OrderDisplay() {
}
OrderDisplay.bindUi = function() {
	$(window).resize(function() {
		OrderDisplay.fitBottomScreen();
	});
};
OrderDisplay.clear = function() {
	OrderDisplayDeriv.clear();
	OrderDisplayEq.clear();
};
OrderDisplay.onChangeAcc = function(acc) {
	this.refresh();
};
OrderDisplay.fitBottomScreen = function() {
	var topOrderEq = $('#orderEq div.order').position().top;
	var topOrderDeriv = $('#orderDeriv div.order').position().top;
	var DisclaimerSize = $('#disclaimer').height();
	var topOrder = topOrderEq > 0 ? topOrderEq : topOrderDeriv;
	var orderH = $(window).height() - topOrder - DisclaimerSize;
	if(orderH<100) orderH=100;
	OrderDisplay.setHeight(orderH);
};
OrderDisplay.refresh = function() {
	// alert("order display");
	// var acc = AccDisplay.currentAcc();
	// this.refreshDisplay(acc.system);
	// this.refreshData(acc);
};
OrderDisplay.refreshDisplay = function(system) {
	OrderDisplay.fitBottomScreen();
	this.visible(false);
	if(system == Account.SYSTEM_EQUITY) {
		OrderDisplayEq.visible(true);
	} else {
		OrderDisplayDeriv.visible(true);
	}
};
OrderDisplay.refreshData = function(acc) {
	if(acc.system == Account.SYSTEM_EQUITY) {
		OrderDisplayEq.refreshData(acc);
	} else {
		OrderDisplayDeriv.refreshData(acc);
	}
};
OrderDisplay.setHeight = function(h) {
	$('div.order').css('height', h+'px');
};
OrderDisplay.visible = function(visible) {
	OrderDisplayEq.visible(visible);
	OrderDisplayDeriv.visible(visible);
};

function OrderDisplayDeriv() {}
OrderDisplayDeriv.orders;
OrderDisplayDeriv.selectedOrderIndex = -1;
OrderDisplayDeriv.checkedOrders;
OrderDisplayDeriv.bindUi = function() {
	$('table#orderHeadDeriv .checkAll').change(function() {
		OrderDisplayDeriv.onCheckCancelAll(this.checked);
	});
	$("table#orderBodyDeriv").delegate('tr','mouseover mouseout click', OrderDisplayDeriv.onMouse);
};
OrderDisplayDeriv.clear = function() {
	$('table#orderBodyDeriv').html('');
};
OrderDisplayDeriv.selectedOrder = function() {
	return this.orders[this.selectedOrderIndex];
};
OrderDisplayDeriv.cancelChecked = function() {
	var checked = $('table#orderBodyDeriv :checked');
	if(checked.length==0) {
		alert("Please select at least 1 order.");	
	} else {
		var checkedOrders = new Array();
		var confirmText = "Confirm cancel following " + checked.length + " order(s):<br/>";
		for(var i=0;i<checked.length;i++) {
			var orderIndex = parseInt(checked[i].value);
			var order = this.orders[orderIndex];
			checkedOrders.push(order);
			confirmText += "Order : {" + order.orderNo + "} (" + order.seriesId + " : " + order.side + " : " + order.time + ")<br/>";
		}
		//var pin = prompt(confirmText);
		ConfirmCancelDialog.setMsg(confirmText);
		var isMkt = Session.user.isMkt();
		var pin = PlaceDisplayDeriv.getPin();
		ConfirmCancelDialog.open(isMkt, PlaceDisplayDeriv.onConfirmCancel, pin);
		PlaceDisplayDeriv.checkedOrders = checkedOrders;
	}
};
OrderDisplayDeriv.handleOrder = function(acc, data) {
	var err = StreamingDecoderDeriv.getErr(data);
	if(err!=undefined) alert(err);
	OrderDisplayDeriv.orders = StreamingDecoderDeriv.getOrders(data);
	if(OrderDisplayDeriv.orders != undefined) {
		OrderDisplayDeriv.replace(acc, OrderDisplayDeriv.orders);
		OrderDisplayDeriv.styleOrders(OrderDisplayDeriv.orders);
	}
};
OrderDisplayDeriv.onCheckCancelAll = function(checked) {
	if(checked) {
		$('table#orderBodyDeriv :checkbox').attr('checked', true);
	} else {
		$('table#orderBodyDeriv :checkbox').removeAttr('checked');
	}
};
OrderDisplayDeriv.gotoSelectedDetail = function() {
	var acc = AccDisplay.currentAcc();
	var order = this.selectedOrder();
	if(order != undefined) {
		var orderDetailURL = Config.Host.deriv + "/Derivatives/C15_OrderDetail.jsp";
		if(Session.user.isMkt()) orderDetailURL = Config.Host.deriv + "/Derivatives/C16_OrderDetail.jsp";
		orderDetailURL += "?orderNo=" + order.orderNo;
		orderDetailURL += "&accountNo=" + acc.accNo;		//for mktrep
		orderDetailURL += "&sendDate=" + order.tradeDate;
		var windowAttr = "location=0,width=680,height=500,scrollbars=yes";
		dWindow = window.open(orderDetailURL,"OrderDetail", windowAttr);
	};
};
OrderDisplayDeriv.onMouse = function(e) {
	if (e.type == 'mouseover') {
		$(this).addClass('hover');
	} else if (e.type == 'mouseout') {
		var index = $(this).index();
		if(OrderDisplayDeriv.selectedOrderIndex != index) {
			$(this).removeClass('hover');
		}
	} else if (e.type == 'click') {
		var selectedIndex = OrderDisplayDeriv.selectedOrderIndex;
		if(selectedIndex!=-1) {
			$(this).parent().children(':eq('+selectedIndex+')').removeClass('hover');
		}
		$(this).addClass('hover');
		OrderDisplayDeriv.selectedOrderIndex = $(this).index();
	}
};
OrderDisplayDeriv.visible = function(visible) {
	if(visible) $('div#orderDeriv').show();
	else $('div#orderDeriv').hide();
};
OrderDisplayDeriv.refreshData = function(acc) {
	/*
	var data = "DerivativeResponse#Pull#4#Derivative@OrderInfo@T@3@00353@70146452|S50H12|13:44:20|Long|660.00|1|0|0|1.00|Day| |Cancelled(CS)|N|N|Close| |pand|N|N|2|null|N|19/10|@70146451|S50H12|11:04:12|Long|660.00|100|0|0|100.00|Day| |Cancelled(CS)|N|N|Close| |pand|N|N|2|null|N|19/10|@70146450|S50H12|11:03:51|Long|660.00|100|0|0|100.00|Day| |Cancelled(CS)|N|N|Close| |pand|N|N|2|null|N|19/10|#";
	var orderDisplay = this;
	orderDisplay.orders = StreamingDecoderDeriv.getOrders(data);
	orderDisplay.replace(acc, orderDisplay.orders);
	*/
	var listener = new ConnListener();
	var conn = new S4OrderConnDeriv(listener);
	listener.success = function(conn, data) {
		OrderDisplayDeriv.handleOrder(acc, data);
		PlaceDisplay.status(acc.system, '');
	};
	listener.fail = function(conn, data) {
		alert("OrderDisplayDeriv.refreshData Cannot connect to server");
		PlaceDisplay.status(acc.system, '');
	};
	conn.reqOrder(acc);
	PlaceDisplay.status(acc.system, "Fetching Data...");
};
OrderDisplayDeriv.replace = function(acc, orders) {
	$('#orderDeriv .checkAll').removeAttr('checked');
	var tr = "";
	// alert(orders.side);
	for(var i=0;i<orders.length;i++) {
		var order = orders[i];
		tr += "<tr class='" + (order.side=="Long"?"b":"s") + "'>";
		tr += "<td class='cancelBox'>" + (order.canCancelled?"<input type='checkbox' value='" + i + "' />":"&nbsp;") + "</td>";
		tr += "<td class='orderNo'>" + order.orderNo + "</td>";
		tr += "<td class='date'>" + order.date + "</td>";
		tr += "<td class='position'>" + order.position + "</td>";
		tr += "<td class='symbol'>" + order.seriesId + "</td>";
		tr += "<td class='time'>" + order.time + "</td>";
		tr += "<td class='side " + (order.side=="Long"?"buy":"sell") + "'>" + order.side + "</td>";
		tr += "<td class='price'>" + order.price + "</td>";
		tr += "<td class='volume'>" + order.vol + "</td>";
		tr += "<td class='matchedVol'>" + order.matchedVol + "</td>";
		tr += "<td class='balanceVol'>" + order.balanceVol + "</td>";
		tr += "<td class='cancelledVol'>" + order.cancelledVol + "</td>";
		tr += "<td class='validity'>" + order.validity + "</td>";
		tr += "<td class='stop'>" + ((order.stop=="Y")?"Stop":"&nbsp;") + "</td>";
		tr += "<td class='status'>" + order.status + "</td>";
		tr += "</tr>";
	}
	$('table#orderBodyDeriv').html(tr);
};
OrderDisplayDeriv.styleOrders = function(orders) {
	var tr = $('table#orderBodyDeriv tr');
	tr.children('.price').each(function(i) {
		var price = $(this).text();
		if(price.toLowerCase() != 'market') {
			var priceDigit = orders[i].priceDigit;
			$(this).text(S4Fmt.formatPrice(price, priceDigit));
		}
	});
	tr.children('.volume, .matchedVol, .balanceVol, .cancelledVol').each(function() {
		Display.styleVol(this);
	});
};

function OrderDisplayEq() {}
OrderDisplayEq.orders;
OrderDisplayEq.selectedOrderIndex = -1;
OrderDisplayEq.checkedOrders;
OrderDisplayEq.bindUi = function() {
	$('table#orderHeadEq .checkAll').change(function() {
		OrderDisplayEq.onCheckCancelAll(this.checked);
	});
	$("table#orderBodyEq").delegate('tr','mouseover mouseout click', OrderDisplayEq.onMouse);
};
OrderDisplayEq.clear = function() {
	$('table#orderBodyEq').html('');
};
OrderDisplayEq.selectedOrder = function() {
	return this.orders[this.selectedOrderIndex];
};
OrderDisplayEq.cancelChecked = function() {
	var checked = $('table#orderBodyEq :checked');
	if(checked.length==0) {
		alert("Please select atleast 1 order.");	
	} else {
		var checkedOrders = new Array();
		var confirmText = "Confirm cancel following " + checked.length + " order(s):<br/>";
		for(var i=0;i<checked.length;i++) {
			var orderIndex = parseInt(checked[i].value);
			var order = this.orders[orderIndex];
			checkedOrders.push(order);
			confirmText += "Order : {" + order.orderNo + "} (" + order.symbol + order.nvdrFlag + " : " + order.side + " : " + order.time + ")<br/>";
		}
		//var pin = prompt(confirmText);
		ConfirmCancelDialog.setMsg(confirmText);
		var isMkt = Session.user.isMkt();
		var pin = PlaceDisplayEq.getPin();
		ConfirmCancelDialog.open(isMkt, OrderDisplayEq.onConfirmCancel, pin);
		OrderDisplayEq.checkedOrders = checkedOrders;
	}
};
OrderDisplayEq.onConfirmCancel = function(ok) {
	// alert(1);
	if(ok) {
		var pin = ConfirmCancelDialog.getPin();
		PlaceDisplayEq.resetForm();
		PlaceDisplayEq.cancel(AccDisplay.currentAcc(), OrderDisplayEq.checkedOrders, pin);
	}
	OrderDisplayEq.checkedOrders = undefined;
};
OrderDisplayEq.gotoSelectedDetail = function() {
	var acc = AccDisplay.currentAcc();
	var order = this.selectedOrder();
	if(order!=undefined) {
		var _td = order.tradeDate.split('/');
		var day = _td[0], month = _td[1], year = _td[2];
		var tradeDate = (year != undefined) ? (year + '-' + month + '-' + day) : '';
		if(order != undefined) {
			var orderDetailURL = "/daytradeflex/streamingOrderDetail.jsp";
			if(Session.user.isMkt()) orderDetailURL = "/SEOS_MktOutstandingOrderDetail.jsp";
			var orderNo = order.seosOrderNo;
			if (acc.system == Account.FRONT_TYPE_DGW || Session.user.isMkt() || order.seosOrderNo == undefined) {
				orderNo = order.orderNo;
			}
			var extOrderNo = (order.fisOrderNo != undefined) ? order.fisOrderNo : '';
			orderDetailURL += "?orderNo=" + orderNo;
			orderDetailURL += "&extOrderNo=" + extOrderNo;
			orderDetailURL += "&txtAccountNo=" + acc.accNo;
			orderDetailURL += "&tradeDate=" + tradeDate;
			orderDetailURL += "&opener=streaming";
			
			var windowAttr = "location=0,width=680,height=500,scrollbars=yes";
			dWindow = window.open(orderDetailURL,"OrderDetail", windowAttr);
		}
	}
	/*
	function openEquityChangeWindow(seosOrderNo, fisOderNo, accountNo){
		var url = "daytradeflex/streamingOrderDetail.jsp?orderNo="+seosOrderNo+"&extOrderNo="+fisOderNo+"&txtAccountNo="+accountNo+"&opener=streaming";
		dWindow = window.open("https://tcdev2.settrade.set/"+url,"ChangeOrder", 'location=0,width=550,height=500,scrollbars=yes');
	} 
	function openEquityDGWChangeWindow(seosOrderNo, tradedate, accountNo){
		var url = "daytradeflex/streamingOrderDetail.jsp?orderNo="+seosOrderNo+"&txtAccountNo="+accountNo+"&tradeDate="+tradedate+"&opener=streaming";
		dWindow = window.open("https://tcdev2.settrade.set/"+url,"ChangeOrder", 'location=0,width=550,height=500,scrollbars=yes');
	}
	function openEquityMktRepChangeWindow(seosOrderNo, accountNo){
		var url = "/SEOS_MktOutstandingOrderDetail.jsp?orderNo="+seosOrderNo+"&txtAccountNo="+accountNo+"&opener=streaming";
		dWindow = window.open("https://tcdev2.settrade.set/"+url,"ChangeOrder", 'location=0,width=550,height=500,scrollbars=yes');
	} 
	*/
};
OrderDisplayEq.handleOrders = function(acc, data) {
	var err = StreamingDecoderEq.getErr(data);
	if(err!=undefined) alert(err);
	OrderDisplayEq.orders = StreamingDecoderEq.getOrders(data);
	if(OrderDisplayEq.orders != undefined) {
		OrderDisplayEq.replace(acc, OrderDisplayEq.orders);
		OrderDisplayEq.styleOrders();
	}
};
OrderDisplayEq.onCheckCancelAll = function(checked) {
	if(checked) {
		$('table#orderBodyEq :checkbox').attr('checked', true);
	} else {
		$('table#orderBodyEq :checkbox').removeAttr('checked');
	}
};
OrderDisplayEq.onMouse = function(e) {
	//var class = $(this).attr('class');
	// alert("OrderDisplayEq.onMouse");
	if (e.type == 'mouseover') {
		//$(this).attr('class', class + 'hover');
		$(this).addClass('hover');
	} else if (e.type == 'mouseout') {
		var index = $(this).index();
		if(OrderDisplayEq.selectedOrderIndex != index) {
			//$(this).attr('class', class.substring(0,1));
			$(this).removeClass('hover');
		}
	} else if (e.type == 'click') {
		var selectedIndex = OrderDisplayEq.selectedOrderIndex;
		if(selectedIndex!=-1) {
			var tr = $(this).parent().children(':eq('+selectedIndex+')');
			//tr.attr('class', class.substring(0,1));
			tr.removeClass('hover');
		}
		//$(this).attr('class', class + 'hover');
		$(this).addClass('hover');
		OrderDisplayEq.selectedOrderIndex = $(this).index();
	}
};
OrderDisplayEq.refreshData = function(acc) {
	var listener = new ConnListener();
	var conn = new S4OrderConnEq(listener);
	listener.success = function(conn, data) {
		OrderDisplayEq.handleOrders(acc, data);
		PlaceDisplay.status(acc.system, '');
	};
	listener.fail = function(conn, data) {
		alert("OrderDisplayEq.refreshData Cannot connect to server");
		PlaceDisplay.status(acc.system, '');
	};
	conn.reqOrder(acc);
	PlaceDisplay.status(acc.system, "Fetching Data...");
};
OrderDisplayEq.replace = function(acc, orders) {
	$('#orderHeadEq .checkAll').removeAttr('checked');
	var tr = "";
	// alert("OrderDisplayEq.replace");
	// alert(orders.length);
	// alert(orders.canCancelled);
	j=0
	for(var i=0;i<orders.length;i++) {
		// alert("loop length");
		
		var order = orders[i];
		// alert(order.side)
		// alert(order)
		// alert(i)
		tr += "<tr class='" + (order.side=="B"?"b":"s") + "'>";
		tr += "<td class='cancelBox'>" + (order.canCancelled?"<input type='checkbox' value='" + i + "' />":"&nbsp;") + "</td>";
		tr += "<td class='orderNo'>" + order.orderNo + "</td>";
		tr += "<td class='time'>" + order.time + "</td>";
		tr += "<td class='symbol'>" + order.symbol + order.nvdrFlag + "</td>";
		tr += "<td class='side " + (order.side=="B"?"buy":"sell") + "'>" + order.side + "</td>";
		tr += "<td class='price'>" + order.price + "</td>";
		tr += "<td class='volume'>" + order.vol + "</td>";
		tr += "<td class='matchedVol'>" + order.matchedVol + "</td>";
		tr += "<td class='balanceVol'>" + order.balanceVol + "</td>";
		tr += "<td class='cancelledVol'>" + order.cancelledVol + "</td>";
		tr += "<td class='status'>" + order.status + "</td>";
		tr += "</tr>";
		// j=j+1
	}
	// alert(tr);
	$('table#orderBodyEq').html(tr);
	// alert("finish refresh")

};
OrderDisplayEq.styleOrders = function() {
	var tr = $('table#orderBodyEq tr');
	tr.children('.price, .volume, .matchedVol, .balanceVol').each(function() {
		var str = $(this).text();
		$(this).text(StrNumFmt.addComma(str));
	});
};
OrderDisplayEq.visible = function(visible) {
	if(visible) $('div#orderEq').show();
	else $('div#orderEq').hide();
};

function PlaceDisplay() {}
PlaceDisplay.place = function(form) {
	var acc = AccDisplay.currentAcc();
	if(acc.system == Account.SYSTEM_EQUITY) {
		PlaceDisplayEq.place(acc, form);
	} else {
		PlaceDisplayDeriv.place(acc, form);
	}
};
PlaceDisplay.cancel = function(acc, orders, pin) {
	var acc = AccDisplay.currentAcc();
	if(acc.system == Account.SYSTEM_EQUITY) {
		PlaceDisplayEq.cancel(acc, form);
	} else {
		PlaceDisplayDeriv.cancel(acc, form);
	}
};
PlaceDisplay.onChangeAcc = function(acc) {
	this.refreshDisplay(acc.system);
};
PlaceDisplay.refresh = function() {
	var acc = AccDisplay.currentAcc();
	this.refreshDisplay(acc.system);
};
PlaceDisplay.refreshDisplay = function(system) {
	if(system == Account.SYSTEM_EQUITY) {
		PlaceDisplayEq.visible(true);
		PlaceDisplayDeriv.visible(false);
	} else {
		PlaceDisplayEq.visible(false);
		PlaceDisplayDeriv.visible(true);
	}
};
PlaceDisplay.status = function(system, str) {
	if(system == Account.SYSTEM_EQUITY) {
		PlaceDisplayEq.status(str);
	} else {
		PlaceDisplayDeriv.status(str);
	}
};
PlaceDisplay.statusAllSystem = function(str) {
	PlaceDisplayEq.status(str);
	PlaceDisplayDeriv.status(str);
};

function PlaceDisplayDeriv() {}
PlaceDisplayDeriv.isProcessing = false;
PlaceDisplayDeriv.bindUi = function() {
	$('#placeDerivForm').submit(function() {
		return false;
	});
	$('#placeDeriv .submitBtn').click(function() {
		alert(1);
		var acc = AccDisplay.currentAcc();
		var form = $('#placeDerivForm')[0];
		PlaceDisplayDeriv.place(acc, form);
		return false;
	});
	$('#placeDeriv .buyRadio').click(function() {
		$('#placeDeriv').css('background-image', 'url(images/thead_buy.png)');
		$('#placeDeriv input.symbol').focus();
		$('#placeDeriv input.symbol').select();
		$('#placeDeriv .submitBtn').val('Buy');
	});
	$('#placeDeriv .sellRadio').click(function() {
		$('#placeDeriv').css('background-image', 'url(images/thead_sell.png)');
		$('#placeDeriv input.symbol').focus();
		$('#placeDeriv input.symbol').select();
		$('#placeDeriv .submitBtn').val('Sell');
	});
	$('#placeDeriv input[type="checkbox"].stopOrder').change(function() {
		PlaceDisplayDeriv.stopOrderVisible(this.checked);
	});
	/*$('#placeDeriv .priceType').change(function() {
		var form = $('#placeDerivForm')[0];
		var isMarket = this.value == "M";
		form.price.disabled = isMarket;
		if(isMarket) {
			form.price.value = '';
			$(form.price).addClass('is-disabled');		//fix-ie.css
		} else {
			$(form.price).removeClass('is-disabled');		//fix-ie.css
		}
	});*/
	$('#placeDeriv .refreshBtn').click(function() {
		
		// AccCredDisplay.refresh();
		OrderDisplay.refresh();
		PortDisplay.refresh();
		InstQuoteDisplay.refreshData();
		MktSumDisplay.refreshData();
	});
	$('#placeDeriv .cancelBtn').click(function() {
		OrderDisplayDeriv.cancelChecked();
	});
	$('#placeDeriv .detailBtn').click(function() {
		OrderDisplayDeriv.gotoSelectedDetail();
	});
	$('#placeDeriv input.symbol').keydown(function(e) {
		if(e.keyCode == ENTER_KEY_CODE || (e.keyCode == TAB_KEY_CODE && !e.shiftKey)) {
			$('#placeDeriv input.volume').focus();
			$('#placeDeriv input.volume').select();
			InstQuoteDisplay.submitSymbol($(this).val());
			return false;
		}
	});
	$('#placeDeriv input.volume').keydown(function(e) {
		if(e.keyCode == ENTER_KEY_CODE || (e.keyCode == TAB_KEY_CODE && !e.shiftKey)) {
			$('#placeDeriv input.price').focus();
			$('#placeDeriv input.price').select();
			return false;
		}
	});
	$('#placeDeriv input.price').keydown(function(e) {
		if(e.keyCode == ENTER_KEY_CODE || (e.keyCode == TAB_KEY_CODE && !e.shiftKey)) {
			if(Session.user.isMkt()) {
				$('#placeDeriv .submitBtn').click();
			} else {
				$('#placeDeriv input.pin').focus();
				$('#placeDeriv input.pin').select();
				return false;
			}
		}
	});
	
	$('#placeDeriv input.pin').keypress(function(e) {
		if(e.keyCode == ENTER_KEY_CODE) {
			$('#placeDeriv .submitBtn').click();
		}
	});
	$('#placeDeriv .clearBtn').click(function() {
		PlaceDisplayDeriv.resetForm();
	});
	$('#placeDeriv input.volume').numeric({decimal: false, negative: false});
	$('#placeDeriv input.price').numeric({negative: true});
	
	
	//$('#placeDeriv input.symbol').watermark('Enter Symbol', {useNative: false});
};
PlaceDisplayDeriv.cancel = function(acc, orders, pin) {
	var listener = new ConnListener();
	var conn = new S4BuySellConnDeriv(listener);
	listener.success = function(conn, data) {
		PlaceDisplayDeriv.handleCancel(acc, data);
		PlaceDisplayDeriv.status('');
	};
	listener.fail = function(conn, data) {
		alert("Cannot connect to server");
		PlaceDisplayDeriv.status('');
	};
	conn.cancel(acc, orders, pin);
	this.status("Fetching Data...");
};
PlaceDisplayDeriv.confirm = function(form) {
	var bs = form.side[0].checked ? "Buy" : "Sell";
	var symbol = form.seriesId.value;
	var vol = form.volume.value;
	var price = (form.priceType.value == 'M')?"Market" : form.price.value;
	var pbVol = form.publishVolume.value;
	var confirmData = bs + ": " + symbol + "\n" +
				"Volume: " + vol + "\n" +
				"Price: " + price + "\n" +
				(pbVol!=""? "P/B Volume :  " + pbVol + "\n" : "") +
				"\n" +
				"(Commision and VAT not included)";
	// alert(2)
	return confirm(confirmData);
};
PlaceDisplayDeriv.getPin = function() {
	return $('#placeDeriv input.pin').val();
};
PlaceDisplayDeriv.handleCancel = function(acc, data) {
	var result = StreamingDecoderDeriv.getPlaceOrderResult(data);
	alert(result.message);
	OrderDisplayDeriv.refreshData(acc);
	InstQuoteDisplay.refreshData();
};
PlaceDisplayDeriv.handlePlace = function(conn, data, acc, order, pin) {
	var result = StreamingDecoderDeriv.getPlaceOrderResult(data);
	if(result.status == PlaceOrderResult.STATUS_W) {
		if(confirm(result.message)) {
			conn.place(acc, order, pin, true);
		}
	} else {
		alert(result.message);
	}
	OrderDisplayDeriv.refreshData(acc);
	InstQuoteDisplay.refreshData();
};
PlaceDisplayDeriv.isVisible = function() {
	return $('#placeDerivForm').is(':visible');
};
PlaceDisplayDeriv.onConfirmCancel = function(ok) {
	if(ok) {
		var pin = ConfirmCancelDialog.getPin();
		PlaceDisplayDeriv.resetForm();
		PlaceDisplayDeriv.cancel(AccDisplay.currentAcc(), PlaceDisplayDeriv.checkedOrders, pin);
	}
	PlaceDisplayDeriv.checkedOrders = undefined;
};




PlaceDisplayDeriv.place = function(acc, form) {
	// for check place order 2 times
	// if(PlaceDisplayDeriv.isProcessing){
	// 	alert('You can not place order twice in the same time');
	// 	return false;
	// }
	if(this.validate(acc, form)) {
		alert("click ok");
		if(this.confirm(form)) {
			var order = this.serializeForm(form);
			var pin = form.pin.value;
			var listener = new ConnListener();
			var conn = new S4BuySellConnDeriv(listener);
			listener.success = function(conn, data) {
				PlaceDisplayDeriv.isProcessing = false;
				PlaceDisplayDeriv.handlePlace(conn, data, acc, order, pin);
				PlaceDisplayDeriv.status('');
			};
			listener.fail = function(conn, data) {
				PlaceDisplayDeriv.isProcessing = false;
				alert("PlaceDisplayDeriv.place Cannot connect to server");
				PlaceDisplayDeriv.status('');
			};
			conn.place(acc, order, pin, false);
			PlaceDisplayDeriv.isProcessing = true;
			this.status("Fetching Data...");
			this.resetForm();
		}
	}
};
PlaceDisplayDeriv.resetForm = function() {
	//form.reset();
	var form = $('#placeDerivForm')[0];
	form.seriesId.value = '';
	form.volume.value = '';
	form.price.value = '';
	form.price.disabled = false;
	form.pin.value = '';
	form.position.selectedIndex = 0;
	form.priceType.selectedIndex = 1;
	form.validityType.selectedIndex = 2;
	form.publishVolume.value = '';
	form.stopOrder.checked = false;
	this.stopOrderVisible(false);
	form.stopSeriesId.value = '';
	form.stopCond.selectedIndex = 0;
	form.stopPrice.value = '';
	form.seriesId.focus();
	$(form.price).removeClass('is-disabled');		//fix-ie.css
};
PlaceDisplayDeriv.serializeForm = function(form) {
	var order = new PlaceOrderDeriv();
	order.vol = form.volume.value;
	order.pbVol = form.publishVolume.value;
	order.position = form.position.value;
	order.validity = form.validityType.value;
	order.date = "";
	order.seriesId = form.seriesId.value;
	order.price = form.price.value;
	order.side = form.side[0].checked ? form.side[0].value : form.side[1].value;
	order.priceType = form.priceType.value;
	order.stopCond = form.stopCond.value;
	order.stopSeriesId = form.stopSeriesId.value;
	order.stopPrice = form.stopPrice.value;
	order.stopOrder = form.stopOrder.checked;
	return order;
};
PlaceDisplayDeriv.setSide = function(side) {
	$('#placeDeriv .buyRadio')[0].checked = side == 'B';
	$('#placeDeriv .sellRadio')[0].checked = side == 'S';
};
PlaceDisplayDeriv.setSymbol = function(symbol) {
	$('#placeDeriv input.symbol').val(symbol);
};
PlaceDisplayDeriv.status = function(str) {
	if(str=='') {
		$('#placeDeriv .status .text').html("&nbsp;");	
	} else {
		$('#placeDeriv .status .text').text(str);	
	}
};
PlaceDisplayDeriv.stopOrderVisible = function(visible) {
	var stopOrderInput = $('#placeDeriv tr.stopOrder');
	if(visible) {
		stopOrderInput.show();
	} else {
		stopOrderInput.hide();
	}
};
PlaceDisplayDeriv.validate = function(acc, form) {
	if(acc.accNo == '') {
		alert("Please insert Trading Account");
		return false;
	}
	var checkedStop = form.stopOrder.checked;
	if(checkedStop) {
		//if (!checkfield(form.stopSeriesId, 's', 0, true, 'Stop SeriesId')) {
		if (form.stopSeriesId.value.length==0) {
			alert("Please insert Symbol Stop Condition");
			return false;
		} else if (!checkfield(form.stopPrice, 'n', 0, true, 'Stop Price')) {
			return false;
		} else if (form.stopCond.value == '') {
			alert("You must select Stop Condition");
			return false;
		}
	}
	var returnFlag = true;
	var isMkt = Session.user.isMkt();
	if (!form.side[0].checked && !form.side[1].checked) {
		alert("You must select Buy or Sell");
		returnFlag = false;
	} else if (!checkfield(form.seriesId, 's', 0, true, 'SeriesId')) {
		returnFlag = false;
	} else if (!checkfield(form.volume, 'i', 0, true, 'Volume')) {
		returnFlag = false;
	} else if (form.priceType[form.priceType.selectedIndex].value == 'L' &&
		!checkfield(form.price, 'n-', 0, true, 'Price')) {
		returnFlag = false;
	} else if (!isMkt && !checkMaxfield(form.pin, 'i', 6, true, 'PIN No')) {
		returnFlag = false;
	} else if (!checkfield(form.publishVolume, 'i', 0, false, 'Publish Volume')) {
		returnFlag = false;
	} else if (form.validityType[form.validityType.selectedIndex].value == '4') {
		if (!checkfield(form.date, 's', 8, true, 'Date')) {
			returnFlag = false;
		} else if (!isDate(form.date.value, form.date, 'Date')) {
			returnFlag = false;
		}
	}
	return returnFlag;
};
PlaceDisplayDeriv.visible = function(visible) {
	if(visible) $('#placeDerivForm').show();
	else $('#placeDerivForm').hide();
};

function PlaceDisplayEq() {}
PlaceDisplayEq.isProcessing = false;
PlaceDisplayEq.bindUi = function() {


	$('#placeEqForm').submit(function() {
		return false;
	});
	$('#placeEq .submitBtn').click(function() {
		
		// alert("Hi this is ok click btn");

  //   	$.post("http://localhost:8000/dummyrt/", { name: "John", time: "2pm" },function(data) {
  // 			alert(jQuery.parseJSON(data)["result"]);
		// });


		// alert("test ok");

		var acc = AccDisplay.currentAcc();
		var form = $('#placeEqForm')[0];
		PlaceDisplayEq.place(acc, form);
		return false;
	});
	$('#placeEq .buyRadio').click(function() {
		$('#placeEq').css('background-image', 'url(images/thead_buy.png)');
		$('#placeEq input.symbol').focus();
		$('#placeEq input.symbol').select();
		$('#placeEq .submitBtn').val('Buy');
	});
	$('#placeEq .sellRadio').click(function() {
		$('#placeEq').css('background-image', 'url(images/thead_sell.png)');
		$('#placeEq input.symbol').focus();
		$('#placeEq input.symbol').select();
		$('#placeEq .submitBtn').val('Sell');
	});
	$('#placeEq .clearBtn').click(function() {
		PlaceDisplayEq.resetForm();
	});
	/*	new trading
	$('#placeEq #atoAtc').change(function() {
		PlaceDisplayEq.onCheckAtoAtc(this.checked);
	});
	$('#placeEq #mp').change(function() {
		PlaceDisplayEq.onCheckMp(this.checked);
	});
	*/
	$('#placeEq .priceType').change(function(){
		PlaceDisplayEq.onChangePriceType(this.value);
	});
	$('#placeEq [name=txtCondition]').change(function(){
		PlaceDisplayEq.onChangeValidity(this.value);
	});
	//$('#condBtn').click(function() {		//not work in ie8
	$('#placeEq #condBtn').mouseup(function() {
		if($('.cond').css('visibility') == "hidden") {
			$('.cond').css('visibility', 'visible');
		} else {
			$('.cond').css('visibility', 'hidden');
		}
	});
	$('#placeEq .detailBtn').click(function() {
		OrderDisplayEq.gotoSelectedDetail();
	});
	$('#placeEq .refreshBtn').click(function() {
		

		// alert("this is refresh button work in here");	
		acc="1";
		

		var orders=PlaceDisplayEq.myorder;
		// $.ajaxSetup({
  //   		cache: false
  // 		});

		$.get("http://localhost:8000/dummyrt/",{"menu":"refresh"},function(data) {
				
				$.each(data,function(key,value){
					// alert(value);
    				// PlaceDisplayEq.myorder.unshift(JSON.parse(value));
    				orders.unshift(JSON.parse(value));
				});
		OrderDisplayEq.replace(acc,orders);	
		PlaceDisplayEq.myorder=orders;
		},"json");

		orders=[];
		// alert("pass get method")
		// OrderDisplayEq.replace(acc,PlaceDisplayEq.myorder);

		// var orders = [
		// {
		// 	side: "B",
		// 	canCancelled:1,
		// 	orderNo:"123",
		// 	symbol:"WHA",
		// 	nvdrFlag:"",
		// 	time:"00:00:00",
		// 	price:"4.02",
		// 	vol:"1000",
		// 	matchedVol:"0",
		// 	balanceVol:"0",
		// 	cancelledVol:"0",
		// 	status:"Pending(S)"

		// }, 
		// {
		// 	side: "S"
		// },
		// PlaceDisplayEq.myorder
		// ];

		






		// OrderDisplayEq.clear();

		// AccCredDisplay.refresh();
		// OrderDisplay.refresh();
		// PortDisplay.refresh();
		// InstQuoteDisplay.refreshData();
		// MktSumDisplay.refreshData();
	});
	$('#placeEq .cancelBtn').click(function() {
		OrderDisplayEq.cancelChecked();
	});
	$('#placeEq input.symbol').keydown(function(e) {	//keypress not support e.keyCode == TAB_KEY_CODE in IE
		if(e.keyCode == ENTER_KEY_CODE || (e.keyCode == TAB_KEY_CODE && !e.shiftKey)) {
			$('#placeEq input.volume').focus();
			$('#placeEq input.volume').select();
			InstQuoteDisplay.submitSymbol($(this).val());
			return false;
		}
	});
	$('#placeEq input.volume').keydown(function(e) {
		if(e.keyCode == ENTER_KEY_CODE || (e.keyCode == TAB_KEY_CODE && !e.shiftKey)) {
			var price = $('#placeEq input.price');
			if(price.attr('disabled')) {		//is MP or ATO/ATC ?
				if(Session.user.isMkt()) {
					$('#placeEq .submitBtn').click();
				} else {
					$('#placeEq input.pin').focus();
					$('#placeEq input.pin').select();
					return false;
				}
			} else {
				$('#placeEq input.price').focus();
				$('#placeEq input.price').select();
			}
			return false;
		}
	});
	$('#placeEq input.price').keydown(function(e) {
		if(e.keyCode == ENTER_KEY_CODE || (e.keyCode == TAB_KEY_CODE && !e.shiftKey)) {
			if(Session.user.isMkt()) {
				$('#placeEq .submitBtn').click();
			} else {
				$('#placeEq input.pin').focus();
				$('#placeEq input.pin').select();
				return false;
			}
		}
	});
	$('#placeEq input.pin').keypress(function(e) {
		if(e.keyCode == ENTER_KEY_CODE) {
			$('#placeEq .submitBtn').click();
		}
	});
	$('#placeEq input.volume').numeric({decimal: false, negative: false});
	$('#placeEq input.price').numeric({negative: false});
};
PlaceDisplayEq.cancel = function(acc, orders, pin) {
	var listener = new ConnListener();
	var conn = new S4BuySellConnEq(listener);
	listener.success = function(conn, data) {
		// PlaceDisplayEq.handleCancel(acc, data);
		PlaceDisplayEq.status('');
	};
	listener.fail = function(conn, data) {
		alert("Cannot connect to server");
		PlaceDisplayEq.status('');
	};
	conn.cancel(acc, orders, pin);
	this.status("Fetching Data...");
};
PlaceDisplayEq.confirm = function(form) {
	var bs = form.txtBorS[0].checked ? "Buy" : "Sell";
	var symbol = form.txtSymbol.value;
	var nvdrFlag = form.txtNvdr.checked? "-R" : "";
	var vol = form.txtQty.value;
	var price = form.txtPrice.value;
	var validity = form.txtCondition.value;
	var pbVol = form.txtPublishVol.value;
	var amount;
	/*if(form.txtATOATC.checked) {
		price = "ATO/ATC";
		amount = "N/A";
	} else if(form.txtMP.checked) {
		price = "MP";
		amount = "N/A";
	}*/
	if(form.txtPriceType.value != 'limit') {
		price = $(form).find('select[name=txtPriceType]>option:selected').text();
		if (price == 'ATO') {
			price += ' (At the Open)';
		} else if (price == 'ATC') {
			price += ' (At the Close)';
		}
		amount = "N/A";
	} else {
		var _amount = parseFloat(vol) * parseFloat(price);
		amount = S4Fmt.formatPrice(_amount, 2);
		price = S4Fmt.formatPrice(price, 2);
	}
	var confirmData = bs + ": " + symbol + nvdrFlag + "\n" +
				"Volume: " + vol + "\n" +
				"Price: " + price + "\n" +
				(validity=="DAY" ? "" : "Validity :  " + validity + "\n") +
				(pbVol!=""? "Iceberg Volume :  " + pbVol + "\n" : "") +
				"\n" +
				"Total Amount: " + amount + " Baht\n" +
				"(Commision and VAT not included)";
	return confirm(confirmData);
};
PlaceDisplayEq.getPin = function() {
	return $('#placeEq input.pin').val();
};
PlaceDisplayEq.handleCancel = function(acc, data) {
	var result = StreamingDecoderEq.getPlaceOrderResult(data);
	alert(result.message);
	OrderDisplayEq.refreshData(acc);
	InstQuoteDisplay.refreshData();
};
PlaceDisplayEq.handlePlace = function(conn, data, acc, order, pin) {
	var result = StreamingDecoderEq.getPlaceOrderResult(data);
	if(result.status == PlaceOrderResult.STATUS_W) {
		if(confirm(result.message)) {
			conn.place(acc, order, pin, true);
			this.status("Fetching Data...");
		}
	} else {
		alert(result.message);
	}
	OrderDisplayEq.refreshData(acc);
	InstQuoteDisplay.refreshData();
};
PlaceDisplayEq.isVisible = function() {
	return $('#placeEqForm').is(':visible');
};
/*
PlaceDisplayEq.onCheckAtoAtc = function(checked) {
	var form = $('#placeEqForm')[0];
	form.txtPrice.disabled = checked;
	form.txtPublishVol.disabled = checked;
	form.txtCondition.disabled = checked;
	form.txtMP.disabled = checked;
	if(checked) {
		form.txtPrice.value = '';
		form.txtPublishVol.value = '';
		$(form.txtPrice).addClass('is-disabled');		//fix-ie.css
		$(form.txtPublishVol).addClass('is-disabled');	//fix-ie.css
	} else {
		$(form.txtPrice).removeClass('is-disabled');		//fix-ie.css
		$(form.txtPublishVol).removeClass('is-disabled');	//fix-ie.css
	}
}
PlaceDisplayEq.onCheckMp = function(checked) {
	var form = $('#placeEqForm')[0];
	form.txtPrice.disabled = checked;
	form.txtPublishVol.disabled = checked;
	form.txtCondition.disabled = checked;
	form.txtATOATC.disabled = checked;
	if(checked) {
		form.txtPrice.value = '';
		form.txtPublishVol.value = '';
		$(form.txtPrice).addClass('is-disabled');		//fix-ie.css
		$(form.txtPublishVol).addClass('is-disabled');	//fix-ie.css
	} else {
		$(form.txtPrice).removeClass('is-disabled');		//fix-ie.css
		$(form.txtPublishVol).removeClass('is-disabled');	//fix-ie.css
	}
}
*/
PlaceDisplayEq.onChangePriceType = function(value) {
	var form = $('#placeEqForm')[0];
	var checked = value != 'limit';
	form.txtPrice.disabled = checked;
	form.txtPublishVol.disabled = checked;
	form.txtCondition.disabled = checked;
	if(checked) {
		form.txtPrice.value = '';
		form.txtPublishVol.value = '';
		form.txtCondition.selectedIndex = 0;
		$(form.txtPrice).addClass('is-disabled');		//fix-ie.css
		$(form.txtPublishVol).addClass('is-disabled');	//fix-ie.css
	} else {
		$(form.txtPrice).removeClass('is-disabled');		//fix-ie.css
		$(form.txtPublishVol).removeClass('is-disabled');	//fix-ie.css
	}
};
PlaceDisplayEq.onChangeValidity = function(value) {
	var form = $('#placeEqForm')[0];
	var isDay = value == 'DAY';
	form.txtPublishVol.disabled = !isDay;
	if(!isDay) {
		form.txtPublishVol.value = '';
		$(form.txtPublishVol).addClass('is-disabled');	//fix-ie.css
	} else {
		$(form.txtPublishVol).removeClass('is-disabled');	//fix-ie.css
	}
};

////////////////////////////////////////////////////
// this function to make sell or buy confirm diaglog
///////////////////////////////////////////////////
PlaceDisplayEq.myorder=[];
PlaceDisplayEq.place = function(acc, form) {
	// if(this.isProcessing) {
	// 	alert('You can not place order twice in the same time');
	// 	return;
	// }
	// alert("click ok");
	if(this.validate(acc, form)) {
		if(this.confirm(form)) {

			// alert("Hi click ok to me not sure where to call this");
			
			var order = this.serializeForm(form);
			var pin = form.txtPIN_new.value;
			var listener = new ConnListener();
			var conn = new S4BuySellConnEq(listener);

			// console.dir(order);
			// alert(order.symbol);



			listener.success = function(conn, data) {
				PlaceDisplayEq.status('');
				PlaceDisplayEq.isProcessing = false;
				// PlaceDisplayEq.handlePlace(conn, data, acc, order, pin);
			};
			listener.fail = function(conn, data) {
				PlaceDisplayEq.status('');
				PlaceDisplayEq.isProcessing = false;
				// alert("Cannot connect to server");
			};
			this.isProcessing = true;

			////////////////////////////////////////////////////////
			//my own modified
			///////////////////////////////////////////////////////
			var dt = new Date();
			hh=dt.getHours();
			mm=dt.getMinutes();
			ss=dt.getSeconds();
    		var currentTime = ( hh < 10 ? "0" : "" ) + hh  + ( mm < 10 ? ":0" : ":" ) + mm + ( ss < 10 ? ":0" : ":" ) + ss;


			order["time"]=currentTime;
			order["orderNo"]= Math.floor(100000 + Math.random() * 900000); //"12345";
			order["nvdrFlag"]="";
			order["status"]="Pending(S)";
			order["matchedVol"]="0";
			order["balanceVol"]="0";
			order["cancelledVol"]="0";	
			order["nvdr"]="False";

			
			PlaceDisplayEq.myorder.unshift(order);
			var orders=PlaceDisplayEq.myorder;
			var acc="1";



			// var orders=[{side:"S"},
			// order
			// ];
			OrderDisplayEq.replace(acc,orders);

			$.post("http://localhost:8000/dummyrt/",JSON.stringify(orders),function(data) {
				// what to do with response data
  				// alert(jQuery.parseJSON(data)["result"]);
			});


			// alert("test ok");


			// conn.place(acc, order, pin, false);
			// this.status("Fetching Data...");
			this.resetForm();
		}
	}
};
PlaceDisplayEq.resetForm = function() {
	var form = $('#placeEqForm')[0];
	form.txtSymbol.value = '';
	form.txtQty.value = '';
	form.txtPrice.value = '';
	form.txtPrice.disabled = false;
	form.txtNvdr.checked = false;
	/*
	form.txtATOATC.checked = false;
	form.txtATOATC.disabled = false;
	form.txtMP.checked = false;
	form.txtMP.disabled = false;
	*/
	form.txtPriceType.selectedIndex = 0;
	form.txtPIN_new.value = '';
	$('#placeEq .cond').css('visibility', 'hidden');
	form.txtPublishVol.value = '';
	form.txtPublishVol.disabled = false;
	form.txtCondition.selectedIndex = 0;
	form.txtCondition.disabled = false;
	form.txtSymbol.focus();
	$(form.txtPrice).removeClass('is-disabled');		//fix-ie.css
	$(form.txtPublishVol).removeClass('is-disabled');	//fix-ie.css
};
PlaceDisplayEq.serializeForm = function(form) {
	var order = new PlaceOrderEq();
	/*
	order.atoAtc = form.txtATOATC.checked;
	order.mp = form.txtMP.checked;
	*/
	order.priceType = form.txtPriceType.value;
	order.nvdr = form.txtNvdr.checked;
	order.pbVol = form.txtPublishVol.value;
	order.price = form.txtPrice.value;
	order.side = form.txtBorS[0].checked? form.txtBorS[0].value : form.txtBorS[1].value;
	order.symbol = form.txtSymbol.value;
	order.validity = form.txtCondition.value;
	order.vol = form.txtQty.value;
	return order;	
};
PlaceDisplayEq.setSide = function(side) {
	if(side == 'B') {
		$('#placeEq .buyRadio').click();
	} else if(side == 'S') {
		$('#placeEq .sellRadio').click();
	}
};
PlaceDisplayEq.setSymbol = function(symbol) {
	$('#placeEq input.symbol').val(symbol);
};
PlaceDisplayEq.status = function(str) {
	if(str=='') {
		$('#placeEq .status .text').html("&nbsp;");	
	} else {
		$('#placeEq .status .text').text(str);	
	}
};
PlaceDisplayEq.validate = function(acc, form) {
	if(acc.accNo == '') {
		alert("Please insert Trading Account");
		return false;
	}
	if(!form.txtBorS[0].checked && !form.txtBorS[1].checked) {
		alert("Please select Buy or Sell");
		return false;
	}
	if(Config.Broker.isGoldETF && $.inArray(form.txtSymbol.value.toUpperCase(), Global.etfSymbols)==-1) {
		alert("Stock not found");
		return false;
	}
	if (checkfield(form.txtSymbol, 's', 0, true, 'Symbol')==false) {

		form.txtSymbol.focus();
		return false;
	}
	if (checkfield(form.txtQty, 'i', 0, true, 'Order Vol')==false) {
		form.txtQty.focus();
		return false;
	}
	if(form.txtPublishVol.disabled == false && form.txtPublishVol.value != ''){
		if (checkfield(form.txtPublishVol, 'i', 0, true, 'Iceberg Vol')==false){
			form.txtPublishVol.focus();
			return false;
		}
	}
	if(form.txtPriceType.value == 'limit' /*form.txtATOATC.checked == false && form.txtMP.checked == false*/){
		if (checkfield(form.txtPrice, 'n', 0, true, 'Order Price')==false){
			form.txtPrice.focus();
			return false;
		} else {
			var price = form.txtPrice.value;
			var stock_symbol = form.txtSymbol.value;
			stock_symbol = stock_symbol.toUpperCase();
			var index = price.indexOf(".");
			var lengthPrice = price.length;
			if(index != -1 && price.substring(index+1,price.length) != "00")
			{
				if(lengthPrice - index > 3)
				{
					form.txtPrice.focus();
					alert("This price requires two decimal digits");
					return false;
				}
			}
		}
	}
	var isMkt = Session.user.isMkt();
	if(!isMkt) {
		if (checkMaxfield(form.txtPIN_new, 's', 6, true, 'PIN No')==false) {
			return false;
		}
	}
	if(!isMkt) {
		var strsPIN = form.txtPIN_new.value;
		if(! validatePin(strsPIN)) {
			alert("Invalid PIN format");
			return false;
		}
	}
	return true;
};
PlaceDisplayEq.visible = function(visible) {
	if(visible) $('#placeEqForm').show();
	else $('#placeEqForm').hide();
};

function PortDisplay() {}
PortDisplay.clear = function() {
	PortDisplayDeriv.clear();
	PortDisplayEq.clear();
};
PortDisplay.onChangeAcc = function(acc) {
	this.refreshDisplay(acc.system);
	this.refreshData(acc);
};
PortDisplay.refresh = function() {
	var acc = AccDisplay.currentAcc();
	if(acc != undefined) {
		this.refreshDisplay(acc.system);
		this.refreshData(acc);
	}
};
PortDisplay.refreshDisplay = function(system) {
	if(MenuDisplay.current == MenuDisplay.Port) {
		this.visible(false);
		if(system == Account.SYSTEM_EQUITY) {
			PortDisplayEq.visible(true);
		} else {
			PortDisplayDeriv.visible(true);
		}
	}
};
PortDisplay.refreshData = function(acc) {
	if(acc.system == Account.SYSTEM_EQUITY) {
		PortDisplayEq.refreshData(acc);
	} else {
		PortDisplayDeriv.refreshData(acc);
	}
};
PortDisplay.visible = function(visible) {
	PortDisplayEq.visible(visible);
	PortDisplayDeriv.visible(visible);
};

function PortDisplayDeriv() {}
PortDisplayDeriv.clear = function() {
	$('#portDeriv tbody table').html('');
};
PortDisplayDeriv.handlePortSum = function(acc, data) {
	var err = StreamingDecoderDeriv.getErr(data);
	if(err!=undefined) alert(err);
	var portSum = StreamingDecoderDeriv.getPortSummary(data);
	if(portSum != undefined)
		this.replacePortSum(acc, portSum);
};
PortDisplayDeriv.lastUpdate = function() {
	$('#portDeriv .lastUpdate').html(lastUpdate());
};
PortDisplayDeriv.refreshData = function(acc) {
	/*
	var data = "DerivativeResponse#Pull#1#Derivative@PortInfo@T@3@00436@S50H12|Long|1000|1000|1000|660.00|658.50|660000000.00|658500000.00|-1500000.00|-0.23|0.00|1000.00|0.00|-1500000.00|-0.23|0.00|660.00|660000000.00|2|@S50H12|Short|1000|1000|1000|660.00|658.50|660000000.00|658500000.00|1500000.00|0.23|-|1000.00|0.00|1500000.00|0.23|-|660.00|660000000.00|2|@_TOTAL|null|0|0|0|0.00|0.00|1320000000.00|1317000000.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|1320000000.00|2|#";
	var json = { 'derivatives': [ data ] };
	PortDisplayDeriv.handlePortSum(json);
	*/
	
	var listener = new ConnListener();
	var conn = new S4PortConnDeriv(listener);
	listener.success = function(conn, data) {
		PortDisplayDeriv.handlePortSum(acc, data);
		// PlaceDisplay.status(acc.system, '');
	};
	listener.fail = function(conn, data) {
		alert("PortDisplayDeriv.refreshData Cannot connect to server");
		PlaceDisplay.status(acc.system, '');
	};
	conn.reqPort(acc);
	PlaceDisplay.status(acc.system, "Fetching Data...");
};
PortDisplayDeriv.replacePortSum = function(acc, portSum) {
	this.lastUpdate();
	this.replacePorts(portSum.ports);
	this.replaceTotal(acc, portSum.total);
	this.stylePorts();
};
PortDisplayDeriv.replacePorts = function(ports) {
	var tr = "";
	for(var i=0;i<ports.length;i++) {
		var port = ports[i];
		tr += "<tr>";
		tr += "<td class='symbol'>" + port.instrument + "</td>";
		tr += "<td class='side'>" + port.side + "</td>";
		tr += "<td class='startVol'>" + port.startVol + "</td>";
		tr += "<td class='availVol'>" + port.availVol + "</td>";
		tr += "<td class='actVol'>" + port.actVol + "</td>";
		tr += "<td class='prcAvg'>" + port.prcAvg + "</td>";
		
		tr += "<td class='mktPrice'>" + port.mktPrice + "</td>";
		tr += "<td class='amtPrice'>" + port.prcAmtVal + "</td>";
		tr += "<td class='mktVal' style='white-space: nowrap'>" + port.mktVal + "</td>";
		tr += "<td class='optVal' style='white-space: nowrap'>" + port.optVal + "</td>";
		tr += "<td class='unrealizedPL' style='white-space: nowrap'>" + port.prcUnrealizedPL + "</td>";
		tr += "<td class='pUnrealizedPL'>" + port.prcPUnrealizedPL + "</td>";
		tr += "<td class='realizedPL'>" + port.prcRealizedPL + "</td>";
		tr += "</tr>";
	}
	$('#portDeriv tbody table').html(tr);
};
PortDisplayDeriv.replaceTotal = function(acc, total) {
	$('#portDeriv tfoot td span.accNo').text(acc.accNo);
	$('#portDeriv tfoot td.amtPrice').text(total.prcAmtVal);
	$('#portDeriv tfoot td.mktVal').text(total.mktVal);
	$('#portDeriv tfoot td.optVal').text(total.optVal);
	$('#portDeriv tfoot td.unrealizedPL').text(total.prcUnrealizedPL);
	$('#portDeriv tfoot td.pUnrealizedPL').text(total.prcPUnrealizedPL);
	$('#portDeriv tfoot td.realizedPL').text(total.prcRealizedPL);
};
PortDisplayDeriv.visible = function(visible) {
	if(visible) $('#portDeriv').show();
	else $('#portDeriv').hide();
};
PortDisplayDeriv.stylePorts = function() {
	var tr = $('#portDeriv tr');
	tr.children('.unrealizedPL, .pUnrealizedPL, .realizedPL').each(function() {
		Display.styleRealizedPL(this);
	});
	tr.children('.startVol, .availVol, .actVol, .prcAvg, .mktPrice, .mktVal, .optVal').each(function() {
		var td = $(this);
		var str = td.text();
		td.text(StrNumFmt.addComma(str));
	});
	tr.children('.amtPrice').each(function() {
		var td = $(this);
		var str = td.text();
		str = StrNumFmt.formatDecimal(str, 0);
		td.text(StrNumFmt.addComma(str));
	});
};

function PortDisplayEq() {}
PortDisplayEq.clear = function() {
	$('#portEq tbody table').html('');
};
PortDisplayEq.lastUpdate = function() {
	$('#portEq .lastUpdate').html(lastUpdate());
};
PortDisplayEq.refreshData = function(acc) {
	
	var listener = new ConnListener();
	var conn = new S4PortConnEq(listener);
	listener.success = function(conn, data) {
		PortDisplayEq.handlePortSum(acc, data);
		PlaceDisplay.status(acc.system, '');
	};
	listener.fail = function(conn, data) {
		alert("PortDisplayEq.refreshData Cannot data Cannot connect to server");
		PlaceDisplay.status(acc.system, '');
	};
	conn.reqPort(acc);
	PlaceDisplay.status(acc.system, "Fetching Data...");
};
PortDisplayEq.handlePortSum = function(acc, data) {
	var err = StreamingDecoderEq.getErr(data);
	if(err!=undefined) alert(err);
	var portSum = StreamingDecoderEq.getPortSummary(data);
	if(portSum != undefined)
		this.replacePortSum(acc, portSum);
};
PortDisplayEq.replacePortSum = function(acc, portSum) {
	this.lastUpdate();
	this.replacePorts(portSum.ports);
	this.replaceTotal(acc, portSum.total);
	this.stylePorts();
};
PortDisplayEq.replacePorts = function(ports) {
	var tr = "";
	for(var i=0;i<ports.length;i++) {
		var port = ports[i];
		var symbol = port.instrument + port.nvdrFlag;
		if(port.type.trim() != '') {
			if(port.type.indexOf('(') >= 0) {
				symbol += ' ' + port.type;				   
			} else {
				symbol += " (" + port.type + ")";
			}
		}
		tr += "<tr>";
		tr += "<td class='symbol'>" + symbol + "</td>";
		tr += "<td class='availVol'>" + port.availVol + "</td>";
		tr += "<td class='actVol'>" + port.actVol + "</td>";
		tr += "<td class='avgCost'>" + port.avgCost + "</td>";
		tr += "<td class='mktPrice'>" + port.mktPrice + "</td>";
		tr += "<td class='amtPrice'>" + port.amtPrice + "</td>";
		tr += "<td class='mktVal' style='white-space: nowrap'>" + port.mktVal + "</td>";
		tr += "<td class='unrealizedPL' style='white-space: nowrap'>" + port.unrealizedPL + "</td>";
		tr += "<td class='pUnrealizedPL'>" + port.pUnrealizedPL + "</td>";
		tr += "<td class='realizedPL'>" + port.realizedPL + "</td>";
		tr += "</tr>";
	}
	$('#portEq tbody table').html(tr);
};
PortDisplayEq.replaceTotal = function(acc, total) {
	$('#portEq tfoot td span.accNo').text(acc.accNo);
	$('#portEq tfoot td.amtPrice').text(total.amtPrice);
	$('#portEq tfoot td.mktVal').text(total.mktVal);
	$('#portEq tfoot td.unrealizedPL').text(total.unrealizedPL);
	$('#portEq tfoot td.pUnrealizedPL').text(total.pUnrealizedPL);
	$('#portEq tfoot td.realizedPL').text(total.realizedPL);
};
PortDisplayEq.stylePorts = function() {
	var tr = $('#portEq tr');
	tr.children('.unrealizedPL, .pUnrealizedPL, .realizedPL').each(function() {
		Display.styleRealizedPL(this);
	});
	tr.children('.availVol, .actVol, .avgCost, .mktPrice, .amtPrice, .mktVal').each(function() {
		var td = $(this);
		var str = td.text();
		td.text(StrNumFmt.addComma(str));
	});
};
PortDisplayEq.visible = function(visible) {
	if(visible) $('#portEq').show();
	else $('#portEq').hide();
};

function validatePin(pin) {
	return /\d{1,6}/.test(pin);
}

/*** DATE FORMAT ***/
var gsMonthNames = new Array(
'January',
'February',
'March',
'April',
'May',
'June',
'July',
'August',
'September',
'October',
'November',
'December'
);
 
var gsDayNames = new Array(
'Sunday',
'Monday',
'Tuesday',
'Wednesday',
'Thursday',
'Friday',
'Saturday'
);
 
String.prototype.zf = function(l) { return '0'.string(l - this.length) + this; };
String.prototype.string = function(l) { var s = '', i = 0; while (i++ < l) { s += this; } return s; };
Number.prototype.zf = function(l) { return this.toString().zf(l); };
 
// the date format prototype
Date.prototype.format = function(f) {
	if (!this.valueOf())
		return 'n.a.';//&nbsp;
	
	var d = this;
	return f.replace(/(yyyy|yy|y|MMMM|MMM|MM|M|dddd|ddd|dd|d|HH|H|hh|h|mm|m|ss|s|t|x)/gi,
		function($1) {
			switch ($1) {
				case 'yyyy':	return d.getFullYear();
				case 'yy':		return (d.getFullYear()%100).zf(2);
				case 'y':		return (d.getFullYear()%100);
				case 'MMMM':	return gsMonthNames[d.getMonth()];
				case 'MMM':		return gsMonthNames[d.getMonth()].substr(0, 3);
				case 'MM':		return (d.getMonth() + 1).zf(2);
				case 'M':		return (d.getMonth() + 1);
				case 'dddd':	return gsDayNames[d.getDay()];
				case 'ddd':		return gsDayNames[d.getDay()].substr(0, 3);
				case 'dd':		return d.getDate().zf(2);
				case 'd':		return d.getDate();
				case 'HH':		return d.getHours().zf(2);
				case 'H':		return d.getHours();
				case 'hh':		return ((d.getHours() % 12) ? d.getHours() % 12 : 12).zf(2);
				case 'h':		return ((d.getHours() % 12) ? d.getHours() % 12 : 12);
				case 'mm':		return d.getMinutes().zf(2);
				case 'm':		return d.getMinutes();
				case 'ss':		return d.getSeconds().zf(2);
				case 's':		return d.getSeconds();
				case 't':		return d.getHours() < 12 ? 'am' : 'pm';
				case 'x':		var i = d.getDate() % 10; return 'thstndrd'.substr(2 * (i < 4) * i, 2);
			}
		}
	);
};