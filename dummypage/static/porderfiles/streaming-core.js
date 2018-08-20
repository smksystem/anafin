var DELIMITER_LV1 = '^';
var DELIMITER_LV2 = '|';
var DELIMITER_LV3 = '~';
var DELIMITER_LV4 = '$';

function Config() {}
Config.Broker = function() {};
Config.Host = function() {};
Config.Platform = function() {};
Config.URL = function() {};

function Global() {}

function Session() {
	this.user;
}

function StreamingDecoderDeriv() {
	this.accInfoListener;
	this.orderListener;
	this.portListener;
	this.errListener;
	
	this.decodeDeriv = function(token) {
		var msgNum = parseInt(token[2]);
		for(var i=0; i<msgNum; i++) {
			var msg = token[i + 3];
			var msgToken = msg.split(DELIMITER_LV1);
			var service = msgToken[1];
			var status = msgToken[2];
			if(status == 'F') {
				if(this.errListener != undefined) {
					this.errListener.trigger(msgToken[3]/*[5]*/);	
				}
				continue;
			} else if (status != 'T') {
				continue;
			}
			if(service == "AccountInfo") {
				if(this.accInfoListener == undefined) continue;
				var accInfo = AccountInfoDeriv.deserialize(msgToken[5]);
				this.accInfoListener.trigger(accInfo);
			} else if(service == "OrderInfo") {
				if(this.orderListener == undefined) continue;
				var orderNum = parseInt(msgToken[3]);
				var orders = new Array();
				for(var i=0;i<orderNum;i++) {
					var order = OrderStatusDeriv.deserializePull(msgToken[i + 5]);
					orders.push(order);
				}
				this.orderListener.trigger(orders);
			} else if(service == "PortInfo") {
				if(this.portListener == undefined) continue;
				var portSum = PortSummaryDeriv.deserialize(msg);
				this.portListener.trigger(portSum);
			}
		}
	};
	this.processData = function(data) {
		if(StrUtil.startsWith(data, "F" + DELIMITER_LV2)) {
			if(this.errListener != undefined) {
				this.errListener.trigger(data.split('|')[1]);
			}
			return;
		}
		var token = data.split(DELIMITER_LV3);
		var statusFlag = token[0];
		if (statusFlag == "DerivativeResponse") {
			 this.decodeDeriv(token);
		}
	};
}
StreamingDecoderDeriv.getAccInfo = function(data) {
	var accInfos = new Array();
	var listener = new DecoderListener();
	listener.trigger = function(accInfo) {
		accInfos.push(accInfo);
	};
	var decoder = new StreamingDecoderDeriv();
	decoder.setAccInfoListener(listener);
	decoder.processData(data);
	return accInfos[0];
};
StreamingDecoderDeriv.getErr = function(data) {
	var error = undefined;
	var listener = new DecoderListener();
	listener.trigger = function(err) {
		error = err;
	};
	var decoder = new StreamingDecoderDeriv();
	decoder.setErrListener(listener);
	decoder.processData(data);
	return error;
};
StreamingDecoderDeriv.getOrders = function(data) {
	var orders = undefined;
	var listener = new DecoderListener();
	listener.trigger = function(_orders) {
		orders = _orders;
	};
	var decoder = new StreamingDecoderDeriv();
	decoder.setOrderListener(listener);
	decoder.processData(data);
	return orders;
};
StreamingDecoderDeriv.getPlaceOrderResult = function(data) {
	var msgToken = data.split(DELIMITER_LV3);
	var token = msgToken[3].split(DELIMITER_LV1);
	if(!token[1] == "PlaceOrder") {
		return undefined;
	}
	var result = new PlaceOrderResult();
	result.status = token[2];
	if(result.status == PlaceOrderResult.STATUS_T) {
		result.message = token[5];
	} else {
		result.message = token[3];
	}
	return result;
};
StreamingDecoderDeriv.getPortSummary = function(data) {
	var portSums = new Array();
	var listener = new DecoderListener();
	listener.trigger = function(portSum) {
		portSums.push(portSum);
	};
	var decoder = new StreamingDecoderDeriv();
	decoder.setPortListener(listener);
	decoder.processData(data);
	return portSums[0];
};

StreamingDecoderDeriv.prototype.setAccInfoListener = function(listener) {
	this.accInfoListener = listener;
};
StreamingDecoderDeriv.prototype.setErrListener = function(listener) {
	this.errListener = listener;
};
StreamingDecoderDeriv.prototype.setOrderListener = function(listener) {
	this.orderListener = listener;
};
StreamingDecoderDeriv.prototype.setPortListener = function(listener) {
	this.portListener = listener;
};

function StreamingDecoderEq() {
	this.acc;
	this.accInfoListener;
	this.orderListener;
	this.portListener;
	this.errListener;
	this.decodeEq = function(token) {
		var msgNum = parseInt(token[1]);
		for(var msgIndex=0;msgIndex<msgNum;msgIndex++) {
			var msg = token[msgIndex+2];
			var msgToken = msg.split(DELIMITER_LV1);
			var service = msgToken[1];
			var status = msgToken[2];
			if(status == 'F') {
				if(this.errListener != undefined) {
					this.errListener.trigger(msgToken[5]);
				}
				continue;
			} else if (status != 'T') {
				continue;
			}
			if (service == 'AccountInfo') {
				if(this.accInfoListener == undefined) continue;
				var accInfo = AccountInfo.deserialize(msgToken[5], this.acc);
				this.accInfoListener.trigger(accInfo);
			} else if(service=='OrderStatus') {
				if(this.orderListener == undefined) continue;
				var orderNum = parseInt(msgToken[3]);
				var orders = new Array();
				for(var i=0;i<orderNum;i++) {
					var order = OrderStatusEq.deserializePull(msgToken[i + 5]);
					orders.push(order);
				}
				this.orderListener.trigger(orders);
			} else if (service == 'Portfolio') {
				if(this.portListener == undefined) continue;
				var portSum = PortSummaryEq.deserialize(msg);
				this.portListener.trigger(portSum);
			}
		}
	};
	this.processData = function(data) {
		var token = data.split(DELIMITER_LV3);
		var statusFlag = token[0];
		if(statusFlag == "StreamingResponse") {
			this.decodeEq(token);
		}
	};
}
StreamingDecoderEq.getAccInfo = function(str, acc) {
	var accInfos = new Array();
	var listener = new DecoderListener();
	listener.trigger = function(accInfo) {
		accInfos.push(accInfo);
	};
	var decoder = new StreamingDecoderEq();
	decoder.setAccInfoListener(listener, acc);
	decoder.processData(str);
	return accInfos[0];
};
StreamingDecoderEq.getAccList = function(str) {
	var strToken = str.split('|');
	var token = strToken.length > 2 && strToken[2].length > 0 ? strToken[2].split(',') : [];
	var accs = new Array();
	for(var i=0;i<token.length;i++) {
		var accToken = token[i].split(DELIMITER_LV3);
		var acc = new Account();
		acc.accNo = accToken[0];
		acc.frontType = accToken[1];
		acc.accType = accToken[2];
		acc.system = Account.SYSTEM_EQUITY;
		accs.push(acc);
	}
	return accs;
};
StreamingDecoderEq.getErr = function(str) {
	var error = undefined;
	var listener = new DecoderListener();
	listener.trigger = function(err) {
		error = err;
	};
	var decoder = new StreamingDecoderEq();
	decoder.setErrListener(listener);
	decoder.processData(str);
	return error;
};
StreamingDecoderEq.getOrders = function(str) {
	var orders = undefined;
	var listener = new DecoderListener();
	listener.trigger = function(_orders) {
		orders = _orders;
	};
	var decoder = new StreamingDecoderEq();
	decoder.setOrderListener(listener);
	decoder.processData(str);
	return orders;
};
StreamingDecoderEq.getPlaceOrderResult = function(str) {
	var msgToken = str.split(DELIMITER_LV3);
	var token = msgToken[2].split(DELIMITER_LV1);
	if(!token[1] == "PlaceOrder") {
		return undefined;
	}
	var result = new PlaceOrderResult();
	result.status = token[2];
	result.message = token[5];
	return result;
};
StreamingDecoderEq.getPortSummary = function(str) {
	var portSums = new Array();
	var listener = new DecoderListener();
	listener.trigger = function(portSum) {
		portSums.push(portSum);
	};
	var decoder = new StreamingDecoderEq();
	decoder.setPortListener(listener);
	decoder.processData(str);
	return portSums[0];
};

StreamingDecoderEq.prototype.setAccInfoListener = function(listener, acc) {
	this.accInfoListener = listener;
	this.acc = acc;
};
StreamingDecoderEq.prototype.setErrListener = function(listener) {
	this.errListener = listener;
};
StreamingDecoderEq.prototype.setOrderListener = function(listener) {
	this.orderListener = listener;
};
StreamingDecoderEq.prototype.setPortListener = function(listener) {
	this.portListener = listener;
};

function DecoderListener() {
	this.trigger = function(obj) {};
};

function FastQuoteDecoder() {}
FastQuoteDecoder.getError = function(json) {
	json = $.parseJSON(json);
	var err = FastQuoteError.deserialize(json);
	return err;
};
FastQuoteDecoder.getInstInfo = function(json) {
	json = $.parseJSON(json);
	if(json.mkt == "equity") {
		return this.getInstInfoEq(json);
	} else {
		return this.getInstInfoDeriv(json);
	}
};
FastQuoteDecoder.isEquity = function(json) {
	json = $.parseJSON(json);
	return json.mkt == "equity";
};
FastQuoteDecoder.getInstInfoEq = function(json) {
	var instInfo = InstInfoEq.deserializeFQ(json);
	return instInfo;
};

FastQuoteDecoder.getInstInfoDeriv = function(json) {
	var instInfo = InstInfoDeriv.deserializeFQ(json);
	return instInfo;
};
FastQuoteDecoder.getInstShortTicker = function(json) {
	json = $.parseJSON(json);
	if(json.exception) return;
	var tickers = new Array();
	for(var i=0;i<json.ticker.length;) {
		var ticker = new InstShortTicker();
		ticker.time = json.ticker[i++];
		ticker.side = json.ticker[i++];
		ticker.vol = json.ticker[i++];
		ticker.price = json.ticker[i++];
		tickers.push(ticker);
	}
	return tickers;
};

function FastQuoteError() {
	this.message;	
}
FastQuoteError.deserialize = function(json) {
	if(json.mkt == "no") {
		var err = new FastQuoteError();
		err.message = "Stock not found";
		return err;
	}
	if(json.error == undefined) return undefined;
	var err = new FastQuoteError();
	err.message = json.error;
	return err;
};

function MktSumDecoder() {}
MktSumDecoder.getError = function(json) {
	json = $.parseJSON(json);
	var err = FastQuoteError.deserialize(json);
	return err;
};
MktSumDecoder.getMktStatus = function(json) {
	json = $.parseJSON(json);
	var mktSt = new MktStatus();
	mktSt.setStatus = json.estatus;
	mktSt.eqStatus = json.dstatus;
	mktSt.singleStockStatus = json.ststatus;
	mktSt.metalStatus = json.mtstatus;
	mktSt.energyStatus = json.enstatus;
	mktSt.irStatus = json.irstatus;
	mktSt.currencyStatus = json.ccstatus;
	mktSt.agriculturalStatus = json.agriculturalstatus;
	mktSt.physicalstatus = json.physicalstatus;
	return mktSt;
};

function ConnListener() {};
ConnListener.prototype.success = function(conn, data) {};
ConnListener.prototype.fail = function(conn, textStatus, errorThrown) {};

function ServiceConn(_listener) {
	this.listener = _listener;
}
ServiceConn.prototype.loadJSON = function(_url, param) {
	var listener = this.listener;
	var conn = this;
	$.ajax({
		url: _url,
		type: "post",
		data: param,
		success: function(data){
			if(listener.success) {
				listener.success(conn, data);
			}
		},
		error: function(jqXHR, textStatus, errorThrown) {
			if(listener.fail) {
				listener.fail(conn, textStatus, errorThrown);
			}
		}
	});
};
ServiceConn.prototype.loadJSONBySystem = function(system, _url, param) {
	if(system == Config.Host.current) {
		this.loadJSON(_url, param);
	}else{
		this.loadJSONPS4(_url, param);
	}
};
ServiceConn.prototype.loadJSONP = function(_url, param, listener) {
	if(listener == undefined) listener = this.listener;
	var conn = this;
	$.ajax({
		url: _url,
		data: param,
		dataType: "jsonp",
		success: function(data){
			if(listener.success) {
				listener.success(conn, data);
			}
		},
		error: function(jqXHR, textStatus, errorThrown) {
			if(listener.fail) {
				listener.fail(conn, textStatus, errorThrown);
			}
		}
	});
};
ServiceConn.prototype.loadJSONPS4 = function(_url, param) {
	var origListener = this.listener;
	var listener = new ConnListener();
	listener.success = function(conn, json) {
		if(origListener.success) {
			var data = json.derivatives[0];
			origListener.success(conn, data);
		}
	};
	listener.fail = function(conn, textStatus, errorThrown) {
		if(origListener.fail) {
			origListener.fail(conn, textStatus, errorThrown) ;
		}
	};
	param += "&json=true";
	param += "&jsoncallback=?";
	this.loadJSONP(_url, param, listener);
};

S4AccListConnEq.prototype = new ServiceConn;
S4AccListConnEq.prototype.constructor = S4AccListConnEq;
function S4AccListConnEq(listener) {
	ServiceConn.call(this, listener);
}
S4AccListConnEq.prototype.reqAcc = function() {
	var url = Config.URL.streamingAccEq;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_EQUITY, url, '');
};

S4AccInfoConnEq.prototype = new ServiceConn;
S4AccInfoConnEq.prototype.constructor = S4AccInfoConnEq;
function S4AccInfoConnEq (listener) {
	ServiceConn.call(this, listener);
}
S4AccInfoConnEq.prototype.reqAcc = function(acc) {
	var user = Session.user;
	if(user.isInternet()) {
		this.reqAccInv(acc);
	} else {
		this.reqAccMkt(acc);
	}
};
S4AccInfoConnEq.prototype.reqAccInv = function(acc) {
	var param = "Service=AccountInfo";
	param += "&txtAccountNo=" + acc.accNo;
	param += "&txtAccountType=" + acc.accType;
	param += "&NewMode=Pull";
	var url = Config.URL.streamingEq;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_EQUITY, url, param);
};
S4AccInfoConnEq.prototype.reqAccMkt = function(acc) {
	var param = "Service=AccountInfo";
	param += "&txtAccountNo=" + acc.accNo;
	param += "&txtAccountType=" + acc.accType;
	param += "&NewMode=Pull";
	var url = Config.URL.streamingEqMkt;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_EQUITY, url, param);
};

S4AccInfoConnEqName.prototype = new ServiceConn;
S4AccInfoConnEqName.prototype.constructor = S4AccInfoConnEqName;
function S4AccInfoConnEqName (listener) {
	ServiceConn.call(this, listener);
}
S4AccInfoConnEqName.prototype.reqAccName = function(acc) {
	var param = "market=E";
	param += "&accountNo=" + acc.accNo;
	var url = Config.URL.streamingEqName;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_EQUITY, url, param);
};

S4AccInfoConnDeriv.prototype = new ServiceConn;
S4AccInfoConnDeriv.prototype.constructor = S4AccInfoConnDeriv;
function S4AccInfoConnDeriv (listener) {
	ServiceConn.call(this, listener);
}
S4AccInfoConnDeriv.prototype.reqAcc = function(acc) {
	if(Session.user.isInternet()) {
		this.reqAccInv(acc);
	} else if(Session.user.isMkt()) {
		this.reqAccMkt(acc);
	}
};
S4AccInfoConnDeriv.prototype.reqAccInv = function(acc) {
	var param = "Service=OrderInfo";
	param += "&OrderMode=AccountInfo";
	param += "&accountNo=" + acc.accNo;
	var url = Config.URL.streamingDeriv;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_DERIV, url, param);
};
S4AccInfoConnDeriv.prototype.reqAccMkt = function(acc) {
	var param = "Service=MktRepOrderInfo";
	param += "&OrderMode=AccountInfo";
	param += "&accountNo=" + acc.accNo;
	var url = Config.URL.streamingDeriv;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_DERIV, url, param);
};

S4BuySellConnDeriv.prototype = new ServiceConn;
S4BuySellConnDeriv.prototype.constructor = S4BuySellConnDeriv;
function S4BuySellConnDeriv (listener) {
	ServiceConn.call(this, listener);
}
S4BuySellConnDeriv.prototype.cancel = function(acc, orders, pin) {
	var user = Session.user;
	if(user.isInternet()) {
		this.cancelInv(acc, orders, pin);
	}else {
		this.cancelMkt(acc, orders, pin);
	}
};
S4BuySellConnDeriv.prototype.cancelInv = function(acc, orders, pin) {
	var param = "mode=cancel";
	param += "&accno=" + acc.accNo;
	param += "&pin=" + pin;
	param += "&orderNo=" + joinOrdersDeriv(orders);
	param += "&seriesId=" + joinSeriesId(orders);
	if (acc.frontType == "DGW") {
		param += "&sendDate=" + joinSendDate(orders);
	}
	param += "&txtTerminalType=jsp";
	var url = Config.URL.orderDeriv;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_DERIV, url, param);
};
S4BuySellConnDeriv.prototype.cancelMkt = function(acc, orders, pin) {
	var param = "mode=cancel";
	param += "&accountNo=" + acc.accNo;
	param += "&pin=" + pin;
	param += "&orderNo=" + joinOrdersDeriv(orders);
	param += "&seriesId=" + joinSeriesId(orders);
	if (acc.frontType == "DGW") {
		param += "&sendDate=" + joinSendDate(orders);
	}
	param += "&txtTerminalType=jsp";
	var url = Config.URL.orderDerivMkt;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_DERIV, url, param);
};
S4BuySellConnDeriv.prototype.place = function(acc, orders, pin, confirmWarn) {
	var user = Session.user;
	if(user.isInternet()) {
		this.placeInv(acc, orders, pin, confirmWarn);
	} else {
		this.placeMkt(acc, orders, pin, confirmWarn);
	}
};
S4BuySellConnDeriv.prototype.placeInv = function(acc, order, pin, confirmWarn) {	
	var param = "mode=placePro";
	param += "&accno=" + acc.accNo;
	param += "&volume=" + order.vol;
	param += "&publishVolume=" + order.pbVol;
	param += "&pin=" + pin;
	param += "&position=" + order.position;
	param += "&validityType=" + order.validity;
	param += "&date=" + order.date;
	param += "&seriesId=" + escape(order.seriesId);
	param += "&price=" + order.price;
	param += "&side=" + order.side;
	param += "&priceType=" + order.priceType;
	if(order.stopOrder) {
		param += "&stopCondition=" + order.stopCond;
		param += "&stopSeriesId=" + order.stopSeriesId;
		param += "&stopPrice=" + order.stopPrice;
	}
	if(confirmWarn) param += "&confirmedWarn=Y";
	var url = Config.URL.orderDeriv;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_DERIV, url, param);
};
S4BuySellConnDeriv.prototype.placeMkt = function(acc, order, pin, confirmWarn) {
	var param = "mode=placePro";
	param += "&accountNo=" + acc.accNo;
	param += "&volume=" + order.vol;
	param += "&publishVolume=" + order.pbVol;
	param += "&pin=" + pin;
	param += "&position=" + order.position;
	param += "&validityType=" + order.validity;
	param += "&date=" + order.date;
	param += "&seriesId=" + escape(order.seriesId);
	param += "&price=" + order.price;
	param += "&side=" + order.side;
	param += "&priceType=" + order.priceType;
	if(order.stopOrder) {
		param += "&stopCondition=" + order.stopCond;
		param += "&stopSeriesId=" + order.stopSeriesId;
		param += "&stopPrice=" + order.stopPrice;
	}
	if(confirmWarn) param += "&confirmedWarn=Y";
	var url = Config.URL.orderDerivMkt;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_DERIV, url, param);
};

S4BuySellConnEq.prototype = new ServiceConn;
S4BuySellConnEq.prototype.constructor = S4BuySellConnEq;
function S4BuySellConnEq (listener) {
	ServiceConn.call(this, listener);
}
S4BuySellConnEq.prototype.cancel = function(acc, orders, pin) {
	var user = Session.user;
	if(user.isInternet()) {
		this.cancelInv(acc, orders, pin);
	}else {
		this.cancelMkt(acc, orders, pin);
	}
};
S4BuySellConnEq.prototype.cancelInv = function(acc, orders, pin) {
	var txtOrders = '';
	var txtExtOrders = '';
	var txtSymbols = joinSymbols(orders);
	if(acc.frontType == Account.FRONT_TYPE_DGW) {
		txtOrders = joinOrdersDGW(orders);
	} else {
		txtOrders = joinOrdersEq(orders);
		txtExtOrders = joinOrdersFis(orders);
	}
	var param = "Service=PlaceOrder";
	param += "&type=cancel";
	param += "&txtAccountNo=" + acc.accNo;
	param += "&txtPIN_new=" + pin;
	param += "&txtOrderNo=" + txtOrders;
	param += "&extOrderNo=" + txtExtOrders;
	param += "&txtCancelSymbol=" + escape(txtSymbols);
	var url;
	if(acc.accType == Account.FRONT_TYPE_DGW) {
		url = Config.URL.streamingDGW;
	} else {
		url = Config.URL.streamingEq;
	}
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_EQUITY, url, param);
};
S4BuySellConnEq.prototype.cancelMkt = function(acc, orders, pin) {
	var txtOrders = '';
	var txtExtOrders = '';
	var txtSymbols = joinSymbols(orders);
	if(acc.frontType == Account.FRONT_TYPE_DGW) {
		txtOrders = joinOrdersDGW(orders);
	} else {
		txtOrders = joinOrdersEq(orders);
		txtExtOrders = joinOrdersFis(orders);
	}
	var param = "Service=PlaceOrder";
	param += "&type=cancel";
	param += "&txtAccountNo=" + acc.accNo;
	param += "&txtPIN_new=" + pin;
	param += "&txtOrderNo=" + txtOrders;
	param += "&extOrderNo=" + txtExtOrders;
	param += "&txtCancelSymbol=" + escape(txtSymbols);
	var url = Config.URL.streamingEqMkt;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_EQUITY, url, param);
};
S4BuySellConnEq.prototype.place = function(acc, order, pin, confirmWarn) {
	var user = Session.user;
	if(user.isInternet()) {
		this.placeInv(acc, order,pin, confirmWarn);
	} else {
		this.placeMkt(acc, order,pin, confirmWarn);
	}
};
S4BuySellConnEq.prototype.placeInv = function(acc, order, pin, confirmWarn) {
	var param = "Service=PlaceOrder";
	param += "&type=place";
	param += "&txtTerminalType=jsp";
	param += "&txtQty=" + order.vol;
	param += "&txtPIN_new=" + pin;
	param += "&txtPrice=" + order.price;
	param += "&txtAccountNo=" + acc.accNo;
	param += "&txtClientType=" + acc.clientType;
	param += "&txtBorS=" + order.side;
	param += "&txtPublishVol=" + order.pbVol;
	param += "&txtSymbol=" + escape(order.symbol);
	param += "&txtCondition=" + order.validity;
	param += "&txtPriceType=" + order.priceType;
	if(order.nvdr) param += "&txtNvdr=2";
	/*if(order.mp) param += "&txtMP=mp";
	if(order.atoAtc) param += "&txtNewATOATC=atoatc";*/
	if(confirmWarn) param += "&confirmedWarn=Y";
	var url;
	if(acc.accType == Account.FRONT_TYPE_DGW) {
		url = Config.URL.streamingDGW;
	} else {
		url = Config.URL.streamingEq;
	}
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_EQUITY, url, param);
};
S4BuySellConnEq.prototype.placeMkt = function(acc, order, pin, confirmWarn) {
		var param = "Service=PlaceOrder";
	param += "&type=place";
	param += "&txtTerminalType=jsp";
	param += "&txtQty=" + order.vol;
	param += "&txtPIN_new=" + pin;
	param += "&txtPrice=" + order.price;
	param += "&txtAccountNo=" + acc.accNo;
	param += "&txtClientType=" + acc.clientType;
	param += "&txtBorS=" + order.side;
	param += "&txtPublishVol=" + order.pbVol;
	param += "&txtSymbol=" + escape(order.symbol);
	param += "&txtCondition=" + order.validity;
	param += "&txtPriceType=" + order.priceType;
	if(order.nvdr) param += "&txtNvdr=2";
	/*if(order.mp) param += "&txtMP=mp";
	if(order.atoAtc) param += "&txtNewATOATC=atoatc";*/
	if(confirmWarn) param += "&confirmedWarn=Y";
	var url = Config.URL.streamingEqMkt;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_EQUITY, url, param);
};
function joinOrdersDGW(orders) {
	var txtOrders = "";
	for(var i=0;i<orders.length;i++) {
		var order = orders[i];
		txtOrders += order.orderNo + '|' + order.sequenceId + '|' + order.tradeDate +',';
	}
	if(txtOrders.length > 0)
		txtOrders = txtOrders.substring(0, txtOrders.length-1);
	return txtOrders;
}
function joinOrdersEq(orders) {
	var txtOrders = "";
	for(var i=0;i<orders.length;i++) {
		var order = orders[i];
		if(order.seosOrderNo != undefined) {
			txtOrders += order.seosOrderNo + ',';
		} else {
			txtOrders += order.orderNo + ',';
		}
	}
	if(txtOrders.length > 0)
		txtOrders = txtOrders.substring(0, txtOrders.length-1);
	return txtOrders;
}
function joinOrdersFis(orders) {
	var txtOrders = "";
	for(var i=0;i<orders.length;i++) {
		var order = orders[i];
		if(order.fisOrderNo != '') {
			txtOrders += order.fisOrderNo + ',';
		} else {
			txtOrders += order.orderNo + ',';
		}
	}
	if(txtOrders.length > 0)
		txtOrders = txtOrders.substring(0, txtOrders.length-1);
	return txtOrders;
}
function joinSymbols(orders) {
	var txtSymbols = "";
	for(var i=0;i<orders.length;i++) {
		var order = orders[i];
		txtSymbols += order.symbol + ',';
	}
	if(txtSymbols.length > 0)
		txtSymbols = txtSymbols.substring(0, txtSymbols.length-1);
	return txtSymbols;
}
function joinOrdersDeriv(orders) {
	var txtOrders = "";
	for(var i=0;i<orders.length;i++) {
		txtOrders += orders[i].orderNo + ",";
	}
	if(txtOrders.length > 0)
		txtOrders = txtOrders.substring(0, txtOrders.length-1);
	return txtOrders;
}
function joinSeriesId(orders) {
	var txtSeriesId = "";
	for(var i=0;i<orders.length;i++) {
		txtSeriesId += orders[i].seriesId + ",";
	}
	if(txtSeriesId.length > 0)
		txtSeriesId = txtSeriesId.substring(0, txtSeriesId.length-1);
	return txtSeriesId;
}
function joinSendDate(orders) {
	var txtSendDate = "";
	for (var i = 0 ; i < orders.length ; i++) {
		txtSendDate += orders[i].tradeDate + ",";
	}
	if (txtSendDate.length > 0) {
		txtSendDate = txtSendDate.substring(0, txtSendDate.length - 1);
	}
	return txtSendDate;
}

FQInstInfoConn.prototype = new ServiceConn;
FQInstInfoConn.prototype.constructor = FQInstInfoConn;
function FQInstInfoConn (listener) {
	ServiceConn.call(this, listener);
}
FQInstInfoConn.prototype.request = function(symbol) {
	var param = "symbol=" + escape(symbol);
	param += "&key=" + aj;
	var url = Config.URL.fastQuote;
	ServiceConn.prototype.loadJSON.call(this, url, param);
};
FQInstInfoConn.prototype.requestEq = function(symbol) {
	this.request(symbol);
};
FQInstInfoConn.prototype.requestDeriv = function(symbol) {
	this.request(symbol);
};

MktSumConn.prototype = new ServiceConn;
MktSumConn.prototype.constructor = MktSumConn;
function MktSumConn (listener) {
	ServiceConn.call(this, listener);
}
MktSumConn.prototype.request = function() {
	var param = "key=" + aj;
	var url = Config.URL.mktsum;
	ServiceConn.prototype.loadJSON.call(this, url, param);
};

S4OrderConnDeriv.prototype = new ServiceConn;
S4OrderConnDeriv.prototype.constructor = S4OrderConnDeriv;
function S4OrderConnDeriv (listener) {
	ServiceConn.call(this, listener);
}
S4OrderConnDeriv.prototype.reqOrder = function(acc) {
	var user = Session.user;
	if(user.isInternet()) {
		this.reqOrderInv(acc);
	} else {
		this.reqOrderMkt(acc);
	}
};
S4OrderConnDeriv.prototype.reqOrderInv = function(acc) {
	var param = "Service=OrderInfo";
	param += "&OrderMode=OrderInfo";
	param += "&accountNo=" + acc.accNo;
	var url = Config.URL.streamingDeriv;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_DERIV, url, param);
};
S4OrderConnDeriv.prototype.reqOrderMkt = function(acc) {
	var param = "Service=MktRepOrderInfo";
	param += "&OrderMode=OrderInfo";
	param += "&accountNo=" + acc.accNo;
	var url = Config.URL.streamingDeriv;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_DERIV, url, param);
};

S4OrderConnEq.prototype = new ServiceConn;
S4OrderConnEq.prototype.constructor = S4OrderConnEq;
function S4OrderConnEq (listener) {
	ServiceConn.call(this, listener);
}
S4OrderConnEq.prototype.reqOrder = function(acc) {
	var user = Session.user;
	if(user.isInternet()) {
		this.reqOrderInv(acc);
	} else {
		this.reqOrderMkt(acc);
	}
};
S4OrderConnEq.prototype.reqOrderInv = function(acc) {
	var param = "Service=OrderStatus";
	param += "&txtAccountNo=" + acc.accNo;
	param += "&txtAccountType=" + acc.accType;
	param += "&NewMode=Pull";
	var url = Config.URL.streamingEq;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_EQUITY, url, param);
};
S4OrderConnEq.prototype.reqOrderMkt = function(acc) {
	var param = "Service=OrderStatus";
	param += "&txtAccountNo=" + acc.accNo;
	param += "&txtAccountType=" + acc.accType;
	param += "&NewMode=Pull";
	var url = Config.URL.streamingEqMkt;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_EQUITY, url, param);
};

S4PortConnDeriv.prototype = new ServiceConn;
S4PortConnDeriv.prototype.constructor = S4PortConnDeriv;
function S4PortConnDeriv (listener) {
	ServiceConn.call(this, listener);
}
S4PortConnDeriv.prototype.reqPort = function(acc) {
	var user = Session.user;
	if(user.isInternet()) {
		this.reqPortInv(acc);
	} else {
		this.reqPortMkt(acc);
	}
};
S4PortConnDeriv.prototype.reqPortInv = function(acc) {
	var param = "Service=OrderInfo";
	param += "&OrderMode=PortInfo";
	param += "&accountNo=" + acc.accNo;
	var url = Config.URL.streamingDeriv;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_DERIV, url, param);
};
S4PortConnDeriv.prototype.reqPortMkt = function(acc) {
	var param = "Service=MktRepOrderInfo";
	param += "&OrderMode=PortInfo";
	param += "&accountNo=" + acc.accNo;
	var url = Config.URL.streamingDeriv;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_DERIV, url, param);
};

S4PortConnEq.prototype = new ServiceConn;
S4PortConnEq.prototype.constructor = S4PortConnEq;
function S4PortConnEq (listener) {
	ServiceConn.call(this, listener);
}
S4PortConnEq.prototype.reqPort = function(acc) {
	var user = Session.user;
	if(user.isInternet()) {
		this.reqPortInv(acc);
	} else {
		this.reqPortMkt(acc);
	}
};
S4PortConnEq.prototype.reqPortInv = function(acc) {
	var param = "Service=Portfolio";
	param += "&txtAccountNo=" + acc.accNo;
	param += "&txtAccountType=" + acc.accType;
	param += "&NewMode=Pull";
	var url = Config.URL.streamingEq;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_EQUITY, url, param);
};
S4PortConnEq.prototype.reqPortMkt = function(acc) {
	var param = "Service=Portfolio";
	param += "&txtAccountNo=" + acc.accNo;
	//param += "&txtAccountType=" + acc.accType;
	param += "&NewMode=Pull";
	var url = Config.URL.streamingEqMkt;
	ServiceConn.prototype.loadJSONBySystem.call(this, Account.SYSTEM_EQUITY, url, param);
};

function PlaceOrderResult() {
	this.status;
	this.message;
}
PlaceOrderResult.STATUS_T = "T";
PlaceOrderResult.STATUS_W = "W";
PlaceOrderResult.STATUS_F = "F";

function PlaceOrderEq() {
	/*this.atoAtc;
	this.mp;*/
	this.priceType;
	this.nvdr;
	this.pbVol;
	this.price;
	this.side;
	this.symbol;
	this.validity;
 	this.vol;
}
function PlaceOrderDeriv() {
	this.vol;
	this.pbVol;
	this.position;
	this.validity;
	this.date;
	this.seriesId;
	this.price;
	this.side;
	this.priceType;
	this.stopOrder;	//boolean
	this.stopCond;
	this.stopSeriesId;
	this.stopPrice;

}

function Account() {
	this.accNo;
	this.accType;
	this.frontType;
	this.system;
	this.canTrade;
	this.system;
}
Account.SYSTEM_EQUITY = "E";
Account.SYSTEM_DERIV = "D";

Account.FRONT_TYPE_SEOS = "SEOS";
Account.FRONT_TYPE_DGW = "DGW";
Account.FRONT_TYPE_FIS = "FIS";

Account.ACC_TYPE_CREDIT_BAL = "CREDIT_BALANCE";
Account.ACC_TYPE_CASH_BAL = "CASH_BALANCE";

function User() {
	this.role;
	this.isEq;
	this.isDeriv;
}
User.prototype.isMkt = function() {
	return this.role == User.ROLE_MARKETREP1 || this.role == User.ROLE_MARKETREP2;
};
User.prototype.isInternet = function() {
	return this.role == User.ROLE_INTERNET;
};
User.isMkt = function(role) {
	return role == User.ROLE_MARKETREP1 || role == User.ROLE_MARKETREP2;
};
User.isInternet = function(role) {
	return role == User.ROLE_INTERNET;
};
User.ROLE_INTERNET = "INTERNET";
User.ROLE_MARKETREP1 = "MARKETREP1";
User.ROLE_MARKETREP2 = "MARKETREP2";

function OrderStatusDeriv() {
	this.orderNo;
	this.seriesId;
	this.time;
	this.side;
	this.price;
	this.vol;
	this.matchedVol;
	this.balanceVol;
	this.cancelledVol;
	this.validity;
	this.until;
	this.status;
	this.canCancelled;
	this.canChanged;
	this.position;
	this.priceDigit;
	this.date;
	this.tradeDate;
}
OrderStatusDeriv.deserializePull = function(str) {
	var orderToken = str.split('|');
	var order = new OrderStatusDeriv();
	order.orderNo = orderToken[0];
	order.seriesId = orderToken[1];
	order.time = orderToken[2];
	order.side = orderToken[3];
	order.price = orderToken[4];
	order.vol = orderToken[5];
	order.matchedVol = orderToken[6];
	order.balanceVol = orderToken[7];
	order.cancelledVol = orderToken[8];
	order.validity = orderToken[9];
	order.until = orderToken[10];
	order.status = orderToken[11];
	order.canCancelled = orderToken[12] == "Y";
	order.canChanged = orderToken[13] == "Y";
	order.position = orderToken[14];
	order.priceDigit = parseInt(orderToken[19]);
	order.date = orderToken[22];
	order.stop = orderToken[23];
	order.tradeDate = orderToken[26];
	return order;
};

function OrderStatusEq() {
	this.priceDigit = 2;
	this.orderNo;
	this.seosOrderNo;
	this.fisOrderNo;
	this.time;
	this.side;
	this.price;
	this.vol;
	this.matchedVol;
	this.balanceVol;
	this.cancelledVol;
	this.priceType;
	this.canCancelled;
	this.canChanged;
	this.sequenceId;
	this.symbol;
	this.nvdrFlag;
	this.status;
	this.accNo;
	this.tradeDate;
}
OrderStatusEq.deserializePull = function(str) {
	var orderToken = str.split(DELIMITER_LV2);
	var order = new OrderStatusEq();
	//order.orderNo = parseInt(orderToken[0]);
	order.orderNo = orderToken[0];
	order.nvdrFlag = orderToken[1];
	order.symbol = orderToken[2];
	order.time = orderToken[3];
	order.side = orderToken[4];
	order.price = orderToken[5];
	order.vol = orderToken[6];
	order.matchedVol = orderToken[7];
	order.balanceVol = orderToken[8];
	order.cancelledVol = orderToken[9];
	order.status = orderToken[10];
	order.canCancelled = orderToken[12] == "Y";
	order.canChanged = orderToken[13] == "Y";
	order.tradeDate = orderToken[14];
	order.sequenceId = orderToken[15];
	if(orderToken[18] != "null")
		order.seosOrderNo = orderToken[18];
	if(orderToken[19] != "null") 
		order.fisOrderNo = orderToken[19];
	return order;
};

function PortfolioDeriv() {
	this.instrument;
	this.side;
	this.priceDigit;
	this.costAvg;
	this.costAmtVal;
	this.costUnrealizedPL;
	this.costPUnrealizedPL;
	this.costRealizedPL;
	this.prcAvg;
	this.prcAmtVal;
	this.prcUnrealizedPL;
	this.prcPUnrealizedPL;
	this.prcRealizedPL;
	this.startVol;
	this.availVol;
	this.actVol;
	this.mktPrice;
	this.mktVal;
	this.optVal;
	this.multiplier;
}
PortfolioDeriv.deserialize = function(str) {
	var portToken = str.split('|');
	var port = new PortfolioDeriv();
	port.instrument = portToken[0].trim();
	port.side = portToken[1];
	port.priceDigit = parseInt(portToken[19]);
	port.costAvg = portToken[17];	
	port.costAmtVal = portToken[18];	
	port.costUnrealizedPL = portToken[14];
	port.costPUnrealizedPL = portToken[15];
	port.costRealizedPL = portToken[16];
	port.prcAvg = portToken[5];				//Average (Price)
	port.prcAmtVal = portToken[7];			//Amount Value (Price)
	port.prcUnrealizedPL = portToken[9];
	port.prcPUnrealizedPL = portToken[10];
	port.prcRealizedPL = portToken[11];
	port.startVol = portToken[2];
	port.availVol = portToken[3];
	port.actVol = portToken[4];
	port.mktPrice = portToken[6];
	port.mktVal = portToken[8];
	port.optVal = portToken[13];
	port.multiplier = portToken[12];
	return port;
};

function PortfolioEq() {
	this.instrument;
	this.nvdrFlag;
	this.type;
	this.availVol;
	this.actVol;
	this.avgCost;
	this.mktPrice;
	this.amtPrice;
	this.mktVal;
	this.unrealizedPL;
	this.pUnrealizedPL;
	this.realizedPL;
}
PortfolioEq.deserialize = function(str) {
	var portToken = str.split('|');
	var port = new PortfolioEq();
	port.instrument = portToken[0];
	port.nvdrFlag = portToken[1];
	port.type = portToken[12];
	port.availVol = portToken[9];
	port.actVol = portToken[10];
	port.avgCost = portToken[11];
	port.mktPrice = portToken[2];
	port.amtPrice = portToken[3];
	port.mktVal = portToken[4];
	port.unrealizedPL = portToken[5];
	port.pUnrealizedPL = portToken[6];
	port.realizedPL = portToken[7];
	return port;
};

function PortSummaryDeriv() {
	this.ports;
	this.total;
}
PortSummaryDeriv.deserialize = function(str) {
	var token = str.split(DELIMITER_LV1);
	var num = parseInt(token[3]);
	var ports = new Array();
	for(var i=0;i<num-1;i++) {
		var port = PortfolioDeriv.deserialize(token[i + 5]);
		ports.push(port);
	}
	var total = PortfolioDeriv.deserialize(token[num + 5 -1]);
	var sum = new PortSummaryDeriv();
	sum.ports = ports;
	sum.total = total;
	return sum;
};

function PortSummaryEq() {
	this.ports;
	this.total;
}
PortSummaryEq.deserialize = function(str) {
	var token = str.split(DELIMITER_LV1);
	var num = parseInt(token[3]);
	var ports = new Array();
	for(var i=0;i<num-1;i++) {
		var port = PortfolioEq.deserialize(token[i + 5]);
		ports.push(port);
	}
	var total = PortfolioEq.deserialize(token[num + 5 -1]);
	var sum = new PortSummaryEq();
	sum.ports = ports;
	sum.total = total;
	return sum;
};

function AccountInfo() {
	this.line;
	this.cash;
	this.credit;
	this.ee;
	this.clientType;
}
AccountInfoDGW.prototype = new AccountInfo;
AccountInfoDGW.prototype.constructor = AccountInfo;
function AccountInfoCredBalDGW() {
	this.credit;
	this.ee;	//purchasing power
}
function AccountInfoDGW() {
	this.credit;
	this.pp;	//purchasing power
	this.cashAvail;
}
function AccountInfoCredBal() {
	this.credit;
	this.line;
	this.ee;
}
AccountInfo.deserialize = function(str, acc) {
	var token = str.split('|');
	var accType = token[3];
	if(accType=='null') accType = acc.accType;
	var info;
	if(acc.frontType == Account.FRONT_TYPE_DGW) {
		if(accType == Account.ACC_TYPE_CREDIT_BAL) {
			info = new AccountInfoCredBalDGW();
			info.credit = token[0];
			info.ee = token[2];
		} else {
			info = new AccountInfoDGW();
			info.credit = token[0];
			info.cashAvail = token[1];
			info.pp = token[2];
		}
	} else {
		if(accType == Account.ACC_TYPE_CREDIT_BAL) {
			info = new AccountInfoCredBal();
			info.credit = token[0];
			info.ee = token[1];
			info.line = token[2];
			acc.accType = accType;
		} else {
			info = new AccountInfo();
			info.credit = token[0];
			info.cash = token[1];
			info.line = token[2];
			acc.accType = accType;
		}	
	}
	info.clientType = token[5];
	return info;
};
function AccountInfoDeriv() {
	this.line;
	this.ee;
	this.equity;
	this.name;
	this.autoNet;
}
AccountInfoDeriv.deserialize = function(str) {
	var token = str.split(DELIMITER_LV2);
	var info = new AccountInfoDeriv();
	info.line = token[0];
	info.ee = token[1];
	info.equity = token[2];
	info.name = token[3];
	if (token[8] != undefined) {
		info.autoNet = token[8];
	}
	return info;
};

function InstInfo() {}
InstInfo.STATE_PO1 = "PreOpen1";
InstInfo.STATE_O1 = "Open1";
InstInfo.STATE_PO2 = "PreOpen2";
InstInfo.STATE_PC = "PreClose";
InstInfo.STATE_C = "Close";

InstInfo.STATE_ST = "Settle";
InstInfo.STATE_PST = "PrevSettle";
InstInfo.STATE_PO0 = "PreOpen0";
InstInfo.STATE_O0 = "Open0";

function InstInfoEq() {
	this.last;
	this.chg;
	this.pChg;
	this.high;
	this.low;
	this.avg;
	this.totalVol;
	this.bid = new Array();
	this.offer = new Array();
	this.volBid = new Array();
	this.volOffer = new Array();
	this.projOpen1;
	this.openPrice1;
	this.openPrice2;
	this.pBuy;
	this.pSell;
	this.pNonSide;
	this.state;
	this.close;
	this.ceil;
	this.floor;
	this.val;
	this.valK;
	this.projVol;
	this.instrument;
	this.status;
	this.priceDigit;
	this.settleDigit;
}
InstInfoEq.deserializeFQ = function(json) {
	json = $.parseJSON(json);
	var inst = new InstInfoEq();
	inst.last = json.last;
	inst.chg = json.chg;
	inst.pChg = json.pchg;
	inst.high = json.high;
	inst.low = json.low;
	inst.avg = json.avg;
	inst.totalVol = json.vol;
	inst.bid[0] = json.bo[0];
	inst.bid[1] = json.bo[2];
	inst.bid[2] = json.bo[4];
	inst.bid[3] = json.bo[6];
	inst.bid[4] = json.bo[8];
	inst.offer[0] = json.bo[1];
	inst.offer[1] = json.bo[3];
	inst.offer[2] = json.bo[5];
	inst.offer[3] = json.bo[7];
	inst.offer[4] = json.bo[9];
	inst.volBid[0] = json.bov[0];
	inst.volBid[1] = json.bov[2];
	inst.volBid[2] = json.bov[4];
	inst.volBid[3] = json.bov[6];
	inst.volBid[4] = json.bov[8];
	inst.volOffer[0] = json.bov[1];
	inst.volOffer[1] = json.bov[3];
	inst.volOffer[2] = json.bov[5];
	inst.volOffer[3] = json.bov[7];
	inst.volOffer[4] = json.bov[9];
	inst.projOpen1 = json.openopendata;;
	inst.state = json.openopen;
	inst.openPrice1 = json.open;
	inst.openPrice2 = json.open2;
	inst.pBuy = json.pbuy;
	inst.pSell = json.psell;
	inst.pNonSide = json.pnonside;
	inst.close = json.close;
	inst.ceil = json.ceil;
	inst.floor = json.floor;
	inst.val = json.val;
	inst.valK = inst.val * 1000;
	inst.projVol = json.openopendata2;
	inst.instrument = json.symbol;
	inst.status = json.dwStatus;
	inst.priceDigit = json.priceDecimal;
	inst.settleDigit = json.settleDecimal;
	inst.sStatus = json.sStatus;
	return inst;
};

function InstInfoDeriv() {
	this.last;
	this.chg;
	this.pChg;
	this.high;
	this.low;
	this.avg;
	this.totalVol;
	this.bid = new Array();
	this.offer = new Array();
	this.volBid = new Array();
	this.volOffer = new Array();
	this.projOpen1;
	this.openPrice1;
	this.openPrice2;
	this.pBuy;
	this.pSell;
	this.pNonSide;
	this.state;
	this.close;
	this.ceil;
	this.floor;
	this.projOpen2;
	this.oi;
	this.settlePrice;
	this.projOpen0;
	this.openPrice0;
	this.prevSettle;
	this.instruement;
	this.status;
	this.priceDigit;
	this.settleDigit;
}
InstInfoDeriv.deserializeFQ = function(json) {
	json = $.parseJSON(json);
	if(json.exception) return;
	var inst = new InstInfoDeriv();
	//var priceDecimal = json.priceDecimal;
	inst.last = json.last;
	inst.chg = json.chg;
	inst.pChg = json.pchg;
	inst.high = json.high;
	inst.low = json.low;
	inst.avg = json.avg;
	inst.totalVol = json.vol;
	inst.bid[0] = json.bo[0];
	inst.bid[1] = json.bo[2];
	inst.bid[2] = json.bo[4];
	inst.bid[3] = json.bo[6];
	inst.bid[4] = json.bo[8];
	inst.offer[0] = json.bo[1];
	inst.offer[1] = json.bo[3];
	inst.offer[2] = json.bo[5];
	inst.offer[3] = json.bo[7];
	inst.offer[4] = json.bo[9];
	inst.volBid[0] = json.bov[0];
	inst.volBid[1] = json.bov[2];
	inst.volBid[2] = json.bov[4];
	inst.volBid[3] = json.bov[6];
	inst.volBid[4] = json.bov[8];
	inst.volOffer[0] = json.bov[1];
	inst.volOffer[1] = json.bov[3];
	inst.volOffer[2] = json.bov[5];
	inst.volOffer[3] = json.bov[7];
	inst.volOffer[4] = json.bov[9];
	inst.state = json.openopen;
	if(inst.state == "Pre-open 1")
		inst.projOpen1 = json.openopendata;
	inst.openPrice1 = json.openfix1;
	inst.openPrice2 = json.openfix2;
	inst.pBuy = json.pbuy;
	inst.pSell = json.psell==undefined?'0.00':json.psell;
	inst.pNonSide = json.pnonside;
	inst.close = json.dclose;
	inst.ceil = json.ceil;
	inst.floor = json.floor;
	if(inst.state == "Pre-open 2")
		inst.projOpen2 = json.openopendata;
	inst.oi = json.openi;
	if(inst.state == "Settle")
		inst.settlePrice = json.openopendata;
	if(inst.state == "Pre-open 0")
		inst.projOpen0 = json.openopendata;
	inst.openPrice0 = json.openfix0;
	inst.prevSettle = json.psettle;
	inst.instrument = json.symbol;
	inst.status = json.sStatus;
	inst.priceDigit = json.priceDecimal;
	inst.settleDigit = json.settleDecimal;
	return inst;
};

function InstBidOfferEq() {
	
}
InstBidOfferEq.deserialize = function(str) {
	
};

function InstShortTicker() {
	this.priceDigit;
	this.side;
	this.price;
	this.vol;
}

function MktStatus() {
	this.setStatus;
	this.eqStatus;
	this.singleStockStatus;
	this.metalStatus;
	this.energyStatus;
	this.irStatus;
	this.currencyStatus;
	this.agriculturalStatus
	this.physicalstatus
}

function S4Fmt() {}
S4Fmt.formatChg = function(chg, priceDigit) {
	var fmt = this.formatPrice(chg, priceDigit);
	var isMinus = StrUtil.startsWith(fmt, '-');
	var isZero = parseFloat(chg) == 0;
	if(!isMinus && !isZero)
		fmt = '+' + fmt;
	return fmt;
};
S4Fmt.formatPrice = function(num, priceDigit) {
	var round = StrNumFmt.formatDecimal(num, priceDigit);
	var comma = StrNumFmt.addComma(round);
	return comma;
};
S4Fmt.formatVol = function(num) {
	return this.formatPrice(num, 0);
};

function StrNumFmt() {}
StrNumFmt.addComma = function(num) {
	if(typeof num != "string") 
		num += '';
	return this.addCommaStr(num);
};
StrNumFmt.addCommaStr = function(str) {
	str += '';
	x = str.split('.');
	x1 = x[0];
	x2 = x.length > 1 ? '.' + x[1] : '';
	var rgx = /(\d+)(\d{3})/;
	while (rgx.test(x1)) {
		x1 = x1.replace(rgx, '$1' + ',' + '$2');
	}
	return x1 + x2;
};
//Todo - reduce complicate and time used
StrNumFmt.formatDecimal = function(num, decimalDigit) {
	if(typeof num != "number") 
		num = parseFloat(num);
	var pow = Math.pow(10, decimalDigit);
	var round = Math.round(num * pow) / pow;
	var strNum = round + '';
	var split = strNum.split('.');
	var integer = split[0];
	var decimal = split[1];
	if(decimal == undefined) decimal = '';
	if(decimalDigit == 0) return integer;
	if(decimalDigit > decimal.length) {
		var padNum = decimalDigit - decimal.length;
		decimal = StrUtil.padRight(decimal, '0', padNum);
	}
	return integer + '.' + decimal;
};

function StrUtil() {}
StrUtil.padRight = function(str, padStr, num) {
	while(num-- > 0)
		str += padStr;
	return str;
};
StrUtil.startsWith = function(str, start) {
	if(str.length >= start.length) {
		return str.substring(0,start.length) == start;
	}
	return false;
};

function EventUtil() {}
EventUtil.charFromEvent = function(e) {
	var keynum = undefined;
	if(window.event) {// IE
		keynum = e.keyCode;
	} else if(e.which) {// Netscape/Firefox/Opera
		keynum = e.which;
	}
	var keychar = String.fromCharCode(keynum);
	return keychar;
};
function InputUtil() {}
InputUtil.getSelection = function(el) {		//copy from internet
	var start = 0, end = 0, normalizedValue, range,
		textInputRange, len, endRange;

	if (typeof el.selectionStart == "number" && typeof el.selectionEnd == "number") {
		start = el.selectionStart;
		end = el.selectionEnd;
	} else {
		range = document.selection.createRange();

		if (range && range.parentElement() == el) {
			len = el.value.length;
			normalizedValue = el.value.replace(/\r\n/g, "\n");

			// Create a working TextRange that lives only in the input
			textInputRange = el.createTextRange();
			textInputRange.moveToBookmark(range.getBookmark());

			// Check if the start and end of the selection are at the very end
			// of the input, since moveStart/moveEnd doesn't return what we want
			// in those cases
			endRange = el.createTextRange();
			endRange.collapse(false);

			if (textInputRange.compareEndPoints("StartToEnd", endRange) > -1) {
				start = end = len;
			} else {
				start = -textInputRange.moveStart("character", -len);
				start += normalizedValue.slice(0, start).split("\n").length - 1;

				if (textInputRange.compareEndPoints("EndToEnd", endRange) > -1) {
					end = len;
				} else {
					end = -textInputRange.moveEnd("character", -len);
					end += normalizedValue.slice(0, end).split("\n").length - 1;
				}
			}
		}
	}

	return {
		start: start,
		end: end
	};
};
InputUtil.removeSelection = function(input) {
	var sel = this.getSelection(input);
	var val = input.value;
	input.value = val.substring(0, sel.start) + val.substring(sel.end, val.length);
};
InputUtil.setCaretPosition = function(ctrl, pos) {
	if(ctrl.setSelectionRange) {
		ctrl.focus();
		ctrl.setSelectionRange(pos,pos);
	}
	else if (ctrl.createTextRange) {
		var range = ctrl.createTextRange();
		range.collapse(true);
		range.moveEnd('character', pos);
		range.moveStart('character', pos);
		range.select();
	}
};

function Style() {}
Style.Color = function() {};
Style.Color.symbol = function(chg, close) {
	return this.chg(chg, close);
};
Style.Color.chg = function(chg, close) {
	return this.colorChg(chg, close);
};
Style.Color.last = function(last, close) {
	return this.colorPrice(last, close);
};
Style.Color.avg = function(avg, close) {
	return this.colorPrice(avg, close);
};
Style.Color.high = function(high, close) {
	return this.colorPrice(high, close);
};
Style.Color.low = function(low, close) {
	return this.colorPrice(low, close);
};
Style.Color.ceil = function(ceil, close) {
	return this.colorPrice(ceil, close);
};
Style.Color.floor = function(floor, close) {
	return this.colorPrice(floor, close);
};
Style.Color.bidOffer = function(bidOffer, close) {
	return this.colorPrice(bidOffer, close);
};
Style.Color.side = function(bs) {
	if(bs.toUpperCase() == "B")
		return '#68A4B1';
	if(bs.toUpperCase() == "S")
		return '#E25B89';
	if(bs.toUpperCase() == "")
		return '#B4B4B4';
	return '';
};
Style.Color.colorChg = function(chg, close) {
	if(typeof chg != "number")
		chg = parseFloat(chg);
	if(typeof close != "number")
		close = parseFloat(close);
	if(close == 0) return '';
	if(chg>0) return '#3D7D3C';
	if(chg<0) return '#E11E2D';
	return '#9A812F';
};

Style.Color.colorPrice = function(val, base) {
	if(typeof val != "number") 
		val = parseFloat(val);
	if(typeof base != "number") 
		base = parseFloat(base);
	if(val==0) return '';
	return this.colorChg(val-base, base);
};
Style.Color.unrealizedPL = function(unrealizedPL) {
	if(unrealizedPL != "number") {
		unrealizedPL = parseFloat(unrealizedPL);
	}
	if(unrealizedPL > 0) return '#3D7D3C';
	if(unrealizedPL < 0) return '#E11E2D';
	return '#9A812F';
};
Style.Color.realizedPL = function(realizedPL) {
	return this.unrealizedPL(realizedPL);
};
