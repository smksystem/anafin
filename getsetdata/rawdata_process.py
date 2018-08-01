
from urllib import request as urlrequest,parse
from bs4 import BeautifulSoup
from getsetdata.rawdata_models import ManageRawData
from getsetdata import rawdata_models
from ctypes.wintypes import BOOLEAN
import os, stat, errno
#from distutils import text_file
class getrawdata(ManageRawData):
    # To get stock element one equity
    def getCompSet(self,data='all'):
       
        if data=='all':
            # print ("get all symbole")
            symbolelist=self.GetAllSymbole_CompSetNameTab()
            # print (symbolelist)
        

        return symbolelist
    # load data from internet or from file    
    def loadAllComSet(self,modeofcollection='file'):
        allsetname={}
        for one in range(65,91):
            #print (chr(one))
            allsetname[chr(one)]=self.loadTableData(chr(one),modeofcollection)
        
        #setmodel=ManageSetData()   
        self.InsertCompSet(allsetname)
      # load data from internet or from file with  each stock 
    def loadTableData(self,prefix,way='file'):
        url_string ="https://www.set.or.th/set/commonslookup.do?language=eng&country=TH&prefix="+prefix
        
        
        if (way=='file'):
            
            with open('rawurldata/outputurl_prefix'+prefix+".txt", 'r') as myfile:
                page=myfile.read()
                
        elif(way=='online'):
            
            page = urlrequest.urlopen(url_string).read()
            with open('rawurldata/outputurl_prefix'+prefix+".txt", 'w') as myfile:
                print(page,file=myfile)
        
        soup = BeautifulSoup(page, 'lxml')
        table_element =soup.find('table', class_='table table-profile table-hover table-set-border-yellow')
        mystock={}
        
        temparray=[]
        i=0
        j=0
        
        for stockcom in table_element.find_all("td"):
            
            result = {
                      0: {stockcom.get_text()},
                      1: { stockcom.get_text()},
                      2: {stockcom.get_text()}
                    }
            temparray.append(result[i].pop())
            
            i+=1
            if (i==3):
                i=0
                mystock[j]=temparray
                temparray=[]
                j+=1
        return (mystock)      
                 
    def dorowlist(self,stockcom,rowname):
        mylist=[]
        mark=[]
        chkasof=stockcom.get_text()
        #print(chkasof)
        if (chkasof==rowname):
                    #print("loop as of")
                    stockvalue=stockcom.find_parent("tr")
                    #print (stockvalue.find_all('th'))
                    if  (stockvalue.find_all('th')): ### for header
                        #print("found header")
                        for eachval in stockvalue.find_all('strong'):
                            # print(eachval.get_text())


                            # print(eachval.get_text() )
                            # print(eachval.br)
                            try:
                                if (mark=='findstatistic'):
                                    mylist.append(eachval.get_text())

                                # if  (eachval.br.next_sibling != ' as of'):
                                if (mark=='findperiodasof'):
                                    # print("found period as of")
                                    mylist.append(eachval.br.next_sibling)
 
                                # if  eachval.get_text() is not None :
                                #     # print("found statistic")
                                #     mylist.append(eachval.get_text() )

                            except (AttributeError, KeyError):
                                pass
                            if (eachval.get_text() == "Period  as of"):
                                # print("found period as of here")
                                mark="findperiodasof"
                            if (eachval.get_text() == "Statistics as of"):
                                mark="findstatistic"
                                # print("found statistic as of here")

                        # print(mylist)
                        # exit()
                    elif (stockvalue.find_all('td')) : ### for row
                        for eachval in stockvalue.find_all('td'):
                            # print (eachval)
                            # print(eachval.get_text())
                            ########## u'\xa0' mean &nbsp; space in html
                            if (eachval.get_text()==u'\xa0'u'\xa0'):
                                # print("found empty String")
                                mylist.append("-")
                                # exit()
                            # print(eachval.get_text().replace(u'\xa0', u''))
                            if (eachval.get_text()!=rowname):
                                getval=eachval.get_text().replace(u'\xa0', u'')
                                
                                # print("###value###")
                                # print(getval)
                                if getval:
                                    mylist.append(getval)
        
        #exit()               #hifinperiodasof_tab[prefix+'.'+yeardate]=assval.get_text()
        return (mylist)
                
    def loadFinHighLight(self,prefix,way='file'):
        # print ('start get fin hightlight')
        #prefix='br'
        resultprefix=""

        # Loop to protect special character like "&" for example F&D
        for chars in prefix:
            if chars.isalpha():
                # print (chars)
                resultprefix+=chars
            else:
                # print("found one not alphabet" + parse.quote(chars))
                resultprefix+=parse.quote(chars)
        # print(resultprefix)
        url_string="https://www.set.or.th/set/companyhighlight.do?symbol="+resultprefix+"&ssoPageId=5&language=en&country=US"
        
        # print(url_string)
        # exit()

        if (way=='file'):
            
            with open('rawurldata/outputfinhighlight_prefix_'+prefix+".txt", 'r') as myfile:
                page=myfile.read()
                
        elif(way=='online'):
            
            page = urlrequest.urlopen(url_string).read()
            with open('rawurldata/outputfinhighlight_prefix_'+prefix+".txt", 'w') as myfile:
                print(page,file=myfile)
                    
        soup = BeautifulSoup(page, 'lxml')        
        table_element =soup.find('table', class_='table table-hover table-info')
        mystock={}
        
        temparray=[]
        i=0
        j=0
        #foundas=BOOLEAN
        
        
        mastershare=[]
        assets=[]
        liabilities=[]
        equity=[]
        paidcapital=[]
        revenue=[]
        netprofit=[]
        epsbath=[]
        roa=[]
        roe=[]
        netprofitmargin=[]

        masterstatstock=[]
        lastprice=[]
        marketcap=[]
        fsperiodasof=[]
        p_e=["-"]
        p_bv=["-"]
        p_nav=["-"]
        nav=["-"]
        bookvaluepershare=["-"]
        dvdyield=["-"]



        hifinperiodasof_tab={}
        hifinstatasof_tab={}
        
        #print (table_element)
        for stockcom in table_element.find_all( ["th","td"]):
            #print (stockcom)
            chkasof=stockcom.get_text()
            # print("####################Print Chkasof")
            # print(chkasof)
            #a=stockcom.br.next_sibling
            #print (a.find('as'))

            if (chkasof == "Period  as of"):
                mastershare=self.dorowlist(stockcom, "Period  as of")                
            if (chkasof=="Assets"):
                assets=self.dorowlist(stockcom, "Assets")
            if (chkasof=="Liabilities"):
                liabilities=self.dorowlist(stockcom, "Liabilities")
            if (chkasof=="Equity"):
                equity=self.dorowlist(stockcom, "Equity")
            if (chkasof=="Paid-up Capital"):
                paidcapital=self.dorowlist(stockcom, "Paid-up Capital")
            if (chkasof=="Revenue"):
                revenue=self.dorowlist(stockcom, "Revenue")    
            if (chkasof=="Net Profit"):
                netprofit=self.dorowlist(stockcom, "Net Profit")
            if (chkasof=="EPS (Baht)"):
                epsbath=self.dorowlist(stockcom, "EPS (Baht)")
            if (chkasof=="ROA(%)"):
                roa=self.dorowlist(stockcom, "ROA(%)")
            if (chkasof=="ROE(%)"):
                roe=self.dorowlist(stockcom, "ROE(%)")
            if (chkasof=="Net Profit Margin(%)"):
                netprofitmargin=self.dorowlist(stockcom, "Net Profit Margin(%)")
            
            if (chkasof=="Statistics as of"):
                # print ("Found statistic as of")
                # print(stockcom)
                masterstatstock=self.dorowlist(stockcom, "Statistics as of")
            if(chkasof=="Last Price(Baht)"):
                lastprice=self.dorowlist(stockcom, "Last Price(Baht)")
            if(chkasof=="Market Cap."):
                marketcap=self.dorowlist(stockcom, "Market Cap.")
            if(chkasof=="F/S Period (As of date)"):
                fsperiodasof=self.dorowlist(stockcom, "F/S Period (As of date)")    
                # print(fsperiodasof)

            if(chkasof=="P/E"):
                p_e=self.dorowlist(stockcom, "P/E")    
            # else:
            #     p_e="0"
            # Sometime stock has difference value P/BV does not have then P/NAV instead    
            if(chkasof=="P/BV"):
                # print("###################################Start to get P_BV")
                p_bv=self.dorowlist(stockcom, "P/BV")   
            # else:
            #     p_bv="0"

            if(chkasof=="P/NAV"):
                p_nav=self.dorowlist(stockcom, "P/NAV")   
            # else:
            #     p_nav="0"

            if(chkasof=="NAV"):
                nav=self.dorowlist(stockcom, "NAV")   
            # else:
            #     nav="0"
            # How to archive above value ? 

            if(chkasof=="Book Value per share (Baht)"):
                bookvaluepershare=self.dorowlist(stockcom, "Book Value per share (Baht)")      
            # else:
            #     bookvaluepershare="0"  
            if(chkasof=="Dvd. Yield(%)"):
                dvdyield=self.dorowlist(stockcom, "Dvd. Yield(%)")            
            # else:
            #     dvdyield="0"
        
        ################ Should check value here....    

        # print(len(p_e))
        # print(len(nav))
        # print(len(p_nav))
        chkarray=len(masterstatstock) - len(p_nav)

        if (chkarray)!=0 :
            # print("need to add more array")
            for i in range(chkarray):
                p_nav.append("-")

        chkarray=len(masterstatstock) - len(nav)
        
        if (chkarray)!=0 :
            # print("need to add more array")
            for i in range(chkarray):
                nav.append("-")            

        chkarray=len(masterstatstock) - len(p_e)
        
        if (chkarray)!=0 :
            # print("need to add more array")
            for i in range(chkarray):
                p_e.append("-")

        chkarray=len(masterstatstock) - len(p_bv)
        
        if (chkarray)!=0 :
            # print("need to add more array")
            for i in range(chkarray):
                p_bv.append("-")

        chkarray=len(masterstatstock) - len(bookvaluepershare)
        
        if (chkarray)!=0 :
            # print("need to add more array")
            for i in range(chkarray):
                bookvaluepershare.append("-")
        # print(p_nav)
        # exit()


        # exit()


            
        statdetail={
                    'prefix':prefix,
                    'masterstatstock':masterstatstock,
                    'lastprice':lastprice,
                    'marketcap':marketcap,
                    'fsperiodasof':fsperiodasof,
                    'p_e':p_e,
                    'p_bv':p_bv,
                    'p_nav':p_nav,
                    'nav':nav,
                    'bookvaluepershare':bookvaluepershare,
                    'dvdyield':dvdyield,

                    }
        

        # print(statdetail)

        sharedetail={
                    'prefix': prefix, 
                    'mastershare':mastershare,
                     'assets':assets,
                     'liabilities':liabilities,
                     'equity':equity,
                     'paidcapital':paidcapital,
                     'revenue':revenue,
                     'netprofit':netprofit,
                     'epsbath':epsbath,
                     'roa':roa,
                     'roe':roe,
                     'netprofitmargin':netprofitmargin
                     }
        # print(sharedetail)
        '''
        #######################################################
        ######### Start upload to database ####################
        ######### table getsetdata_hlfinstatisticasof;
        ######### table getsetdata_hlfinperiodasof;
        #######################################################
        '''
        self.InsertHighLight(sharedetail)
        self.InsertStatistic(statdetail)

        # exit()

   