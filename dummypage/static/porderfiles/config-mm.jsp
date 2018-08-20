


Session.user = new User();
Session.user.role = "INTERNET";
Session.user.isEq = true;
Session.user.isDeriv = false;
Session.user.accsEq = [];
Session.user.accsDeriv = [];
Session.user.defaultAccNo = "01475000";
Session.user.defaultAccSystem = "E";

Config.URL.streamingEq = "https://wen060.settrade.com/daytradeflex/streamingSeos.jsp";
Config.URL.streamingEqMkt = "https://wen060.settrade.com/daytradeflex/streamingSeos_mktrep.jsp";
Config.URL.streamingDGW = "https://wen060.settrade.com/daytradeflex/streamingSeos_dgw.jsp";
Config.URL.streamingEqName = "https://wen060.settrade.com/realtime/streaming4/getAccountName.jsp";
Config.URL.fastQuote = "https://wen060.settrade.com/webrealtime/data/fastquote.jsp";
Config.URL.mktsum = "https://wen060.settrade.com/webrealtime/data/marketsummary.jsp";
Config.URL.orderDeriv = "https://wdn002.settrade.com/Derivatives/streaming/order.jsp";
Config.URL.orderDerivMkt = "https://wdn002.settrade.com/Derivatives/streaming/mktreporder.jsp";
Config.URL.streamingDeriv = "https://wdn002.settrade.com/Derivatives/streaming/streaming.jsp";
Config.Broker.isGoldETF = false;
Config.Host.current = Account.SYSTEM_EQUITY;
Config.Host.deriv = "https://wdn002.settrade.com";
Config.Host.eq = "https://wen060.settrade.com";
Config.Platform.isEq = true;
Config.Platform.isDeriv = true;

var user = Session.user;

        var acc = new Account();
        acc.accNo = "01475000";
        acc.accType = "CASH_BALANCE";
        acc.frontType = "FIS";
        acc.system = Account.SYSTEM_EQUITY;
        acc.clientType = "";
        user.accsEq.push(acc);
    


    

