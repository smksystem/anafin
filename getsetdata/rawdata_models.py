from getsetdata.models import ComSetName,HLFinPeriodasof,HLFinStatisticasof
import symbol
    
class ManageRawData:
    
    def InsertStatistic(self,statdata):
        row_no=0
        for master_row in statdata['masterstatstock']:
            rowtoinsert=[]
            # print(statdata['prefix']+'.'+statdata['masterstatstock'][row_no])
            rowtoinsert.append(statdata['prefix']+'.'+statdata['masterstatstock'][row_no])
            rowtoinsert.append(statdata['lastprice'][row_no])
            rowtoinsert.append(statdata['marketcap'][row_no])
            rowtoinsert.append(statdata['fsperiodasof'][row_no])
            rowtoinsert.append(statdata['p_e'][row_no])
            rowtoinsert.append(statdata['p_bv'][row_no])
            rowtoinsert.append(statdata['p_nav'][row_no])
            rowtoinsert.append(statdata['nav'][row_no])
            rowtoinsert.append(statdata['bookvaluepershare'][row_no])
            rowtoinsert.append(statdata['dvdyield'][row_no])

            for index,comma in enumerate(rowtoinsert):
                # print(comma)
                comma=comma.replace(",","")
                # This need to identify more for "N.A." and "-" consider to change in database as string.
                comma=comma.replace("N.A.","0")
                comma=comma.replace("N/A","0")
                comma=comma.replace("*","")
                if len(comma)==1:
                    comma=comma.replace("-","0")
                # print(comma)
                rowtoinsert[index]=comma
                # print(item)
                
            # print (rowtoinsert)
            STATTB=HLFinStatisticasof(mastershare=rowtoinsert[0],
                                lastprice=float(rowtoinsert[1]),
                                marketcap=float(rowtoinsert[2]),
                                fsperiodasof=rowtoinsert[3],
                                p_e=float(rowtoinsert[4]),
                                p_bv=float(rowtoinsert[5]),
                                p_nav=float(rowtoinsert[6]),
                                nav=float(rowtoinsert[7]),
                                bookvaluepershare=float(rowtoinsert[8]),
                                dvdyield=float(rowtoinsert[9]),
                                
                            )
            STATTB.save()
            row_no+=1

    def InsertHighLight(self,sharedata):

        row_no=0
        for master_row in sharedata['mastershare']:

            rowtoinsert=[]
            # print(sharedata['prefix']+'.'+sharedata['mastershare'][row_no])
            
            

            rowtoinsert.append(sharedata['prefix']+'.'+sharedata['mastershare'][row_no])
            rowtoinsert.append(sharedata['assets'][row_no])
            rowtoinsert.append(sharedata['liabilities'][row_no])
            rowtoinsert.append(sharedata['equity'][row_no])
            rowtoinsert.append(sharedata['paidcapital'][row_no])
            rowtoinsert.append(sharedata['revenue'][row_no])
            rowtoinsert.append(sharedata['netprofit'][row_no])
            rowtoinsert.append(sharedata['epsbath'][row_no])
            rowtoinsert.append(sharedata['roa'][row_no])
            rowtoinsert.append(sharedata['roe'][row_no])
            rowtoinsert.append(sharedata['netprofitmargin'][row_no])
           
            for index,comma in enumerate(rowtoinsert):
                # print("start debug")
                # print(comma)
                comma=comma.replace(",","")
                # This need to identify more for "N.A." and "-" consider to change in database as string.
                comma=comma.replace("N.A.","0")

                
                
                if len(comma)==1:
                    comma=comma.replace("-","0")
                # print(comma)
                rowtoinsert[index]=comma
                # print(item)
            
            print("##################")
            print(rowtoinsert)
            # exit()
            HL=HLFinPeriodasof(mastershare=rowtoinsert[0],
                                assets=float(rowtoinsert[1]),
                                liabilities=float(rowtoinsert[2]),
                                equity=float(rowtoinsert[3]),
                                paidcapital=float(rowtoinsert[4]),
                                revenue=float(rowtoinsert[5]),
                                netprofit=float(rowtoinsert[6]),
                                epsbath=float(rowtoinsert[7]),
                                roa=float(rowtoinsert[8]),
                                roe=float(rowtoinsert[9]),
                                netprofitmargin=float(rowtoinsert[10]),
                            )
            HL.save()
            
            row_no+=1
    def InsertCompSet(self,alldata):
        #print(alldata)
        i=1
        for alphabet,listvalue in alldata.items():
            #print(alphabet)
            #print (listvalue)
            for coltype,datavalue in listvalue.items():
                print (datavalue[0])
                
                test=ComSetName(comp_id=i,symbol=datavalue[0],fullname=datavalue[1],market=datavalue[2])
                test.save()
                i+=1
            #for element in alphabet:
             #   print (element)
            #
            #test.save()
    def GetAllSymbole_CompSetNameTab (self):
        
        my_list=[]
        symbolelist=ComSetName.objects.only('symbol')
        # print(symbolelist.query)
        # print (symbolelist.symbol)
        for my in symbolelist:
            # print (my.symbol)
            my_list.append(my.symbol)
        return my_list
        #print(a.filter().next())
        #exit()