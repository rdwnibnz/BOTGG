# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(token="ElVtEgoRR0UI5UoO4F83.4C+Fc/6C5Ub8QiEJN0MBiW.G9hXOLP8Wmq9ZpiZBaxQlf0iEdDBzWucg55cOfzukus=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="ElgOCJ1ch0AAp1ABFMa7.DaiQwgTGNlaH0BREmT+F9W.hiUX+sHkLJAk5jrNhCWSKhTAs456fC1OO4by0f0b+Q8=")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token="ElWoaQE3njvsCVbDYkE5.cxuvQ/k4I3PonUnaBiQQTq./PJUxbDyhKgxcgDwTbZhYQRU2XASrcDExsoPWZMNJwE=")
kk.loginResult()

kc = LINETCR.LINE()
kc.login(token="Elb1jWw3o3E5YufNQEic.s6/kRpVaDyccAb2TI9xada.QrU1uuVsdkXtj3ZjyhKqpsPmj/wjJf/DDN48Aa7wVVM=")
kc.loginResult()

kx = LINETCR.LINE()
kx.login(token="ElTU9I6wChNLaSGaMzF5.fa4ltAHdLkO2pc2kSf/efq.rS1nTDmAieAMdGV0CF5Fzzo6DFVdQy3vQZXOrCeN0Zg=")
kx.loginResult()

ky = LINETCR.LINE()
ky.login(token="ElxjBK3X08RotOcFSvo3.VUHKteWikY+XShQkJ55KeW.xD2yUpM45ADbhOii7RAcAYS59ryEhyUWIlngufsZOIk=")
ky.loginResult()

kf = LINETCR.LINE()
kf.login(token="ElcJs1rXKgxkXfEI8zCb.U2pGFs/vLK0nJkG5J/aIUW.CK42JXMMBIGE6G/No3gtDhTUhtSdwexKqSdBWZadUws=")
kf.loginResult()

kg = LINETCR.LINE()
kg.login(token="ElPBN6G4qPO01QNgV4y1.vHfzTb2LLAHrUeCgOByFqq.qrrqsTRX6AToHPuWtwuZjWDH8TwXhauwKiaL4ZNKXRY=")
kg.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" Frankenstein Bot\nGada key buat yang pengenan kaya lu """

KAC=[cl,ki,kk,kc]
KIC=[kx,ky,kf,kg]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kx.getProfile().mid
Emid = ky.getProfile().mid
Fmid = kf.getProfile().mid
Gmid = kg.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid]
admin=["u965c42ef1d49430b56734b1a40da96a7"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"Estes ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True,
    "atjointicket":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        if op.type == 11:
                if op.param2 not in Bots:
                    try:
                        ky.kickoutFromGroup(op.param1,[op.param2])
                        if op.param2 in wait["blacklist"]:
                          pass
                    except:
                            try:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                if op.param2 in wait["blacklist"]:
                                  pass
                                else:
                                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                            except:
                                print ('Ada yang buka QR')
                            if op.param2 in wait["blacklist"]:
                                pass
                            else:
                                wait["blacklistlist"][op.param2] = True
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                            wait["blacklist"][op.param2] = True

        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = kx.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kx.updateGroup(X)
                        Ti = kx.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kx.updateGroup(X)
                        Ti = kx.reissueGroupTicket(op.param1)

                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = ky.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ky.updateGroup(X)
                        Ti = ky.reissueGroupTicket(op.param1)
                        kx.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ky.updateGroup(X)
                        Ti = ky.reissueGroupTicket(op.param1)

                if op.param3 in Emid:
                    if op.param2 in Fmid:
                        X = kf.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                        ky.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)

                if op.param3 in Fmid:
                    if op.param2 in Gmid:
                        X = kg.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                        kf.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)

                if op.param3 in Gmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kg.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 13:
                    if op.param2 not in admin:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                        kf.cancelGroupInvitation(op.param1,[op.param3])
                        pass

        if op.type == 17:
            if op.param2 not in Bots:
                group = cl.getGroup(op.param1)
                cb = Message()
                cb.to = op.param1
                cb.text = cl.getContact(op.param2).displayName + " Peler Selamat Datang di " + group.name
                cl.sendMessage(cb)

        if op.type == 32:
                    if op.param2 not in Bots:
                        kg.kickoutFromGroup(op.param1,[op.param2])
                        pass

        if op.type == 19:
            if op.param2 not in Bots:
                if op.param3 in Amid:
                        wait ["blacklist"][op.param2] = True
                        try:
                                X = cl.getGroup(op.param1)
                                X.preventJoinByTicket = False
                                cl.updateGroup(X)
                                Ti = cl.reissueGroupTicket(op.param1)
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                X.preventJoinByTicket = True
                                kk.updateGroup(X)
                                Ti = cl.reissueGroupTicket(op.param1)
                        except:
                                pass
                if op.param3 not in Bots:
                        wait ["blacklist"][op.param2] = True
                        try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                kk.kickoutFromGroupGroup(op.param1,[op.param2])
                        except:
                                try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                        pass

        if op.type == 19:
                    if op.param3 in admin:
                        cl.kickoutFromGroup(op.param1,[op.param3])
                        cl.inviteIntoGroup(op.param1,admin)
                    else:
                        pass

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KIC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kx.acceptGroupInvitationByTicket(op.param1,Ti)
                    ky.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KIC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kx.acceptGroupInvitationByTicket(op.param1,Ti)
                    ky.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kx.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kx.acceptGroupInvitationByTicket(op.param1,Ti)
                    ky.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kx.kickoutFromGroup(op.param1,[op.param2])
                        ky.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kx.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kx.updateGroup(X)
                    Ti = kx.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ky.kickoutFromGroup(op.param1,[op.param2])
                        kf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ky.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ky.updateGroup(X)
                    Ti = ky.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kx.acceptGroupInvitationByTicket(op.param1,Ti)
                    ky.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kx.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kx.updateGroup(G)
                    Ticket = kx.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                        kg.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kf.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kf.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kx.acceptGroupInvitationByTicket(op.param1,Ti)
                    ky.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ky.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ky.updateGroup(G)
                    Ticket = ky.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kg.kickoutFromGroup(op.param1,[op.param2])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KIC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kg.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kg.updateGroup(X)
                    Ti = kg.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kx.acceptGroupInvitationByTicket(op.param1,Ti)
                    ky.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kf.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kf.updateGroup(G)
                    Ticket = kf.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KIC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kx.acceptGroupInvitationByTicket(op.param1,Ti)
                    ky.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kg.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kg.updateGroup(G)
                    Ticket = kg.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")

               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
                if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        cl.updateGroup(X)
                    else:
                        cl.sendText(msg.to,"Lu bukan Admin ler")
            #elif ("jwuekegsi " in msg.text):
                #if msg.toType == 2:
                    #X = cl.getGroup(msg.to)
                    #X.name = msg.text.replace("Cv1 gn ","")
                    #ki.updateGroup(X)
                #else:
                    #ki.sendText(msg.to,"It can't be used besides the group.")
            #elif ("jwosneien " in msg.text):
                #if msg.toType == 2:
                    #X = cl.getGroup(msg.to)
                    #X.name = msg.text.replace("Cv2 gn ","")
                    #kk.updateGroup(X)
                #else:
                    #kk.sendText(msg.to,"It can't be used besides the group.")
            #elif ("neosnek " in msg.text):
                #if msg.toType == 2:
                    #X = cl.getGroup(msg.to)
                    #X.name = msg.text.replace("Cv3 gn ","")
                    #kc.updateGroup(X)
                #else:
                    #kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Kick ","")
                    cl.kickoutFromGroup(msg.to,[midd])
            #elif "Cv1 kick " in msg.text:
                #midd = msg.text.replace("Cv1 kick ","")
                #ki.kickoutFromGroup(msg.to,[midd])
            #elif "Cv2 kick " in msg.text:
                #midd = msg.text.replace("Cv2 kick ","")
                #kk.kickoutFromGroup(msg.to,[midd])
            #elif "Cv3 kick " in msg.text:
                #midd = msg.text.replace("Cv3 kick ","")
                #kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Invite ","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
            #elif "Cv1 invite " in msg.text:
                #midd = msg.text.replace("Cv1 invite ","")
                #ki.findAndAddContactsByMid(midd)
                #ki.inviteIntoGroup(msg.to,[midd])
            #elif "Cv2 invite " in msg.text:
                #midd = msg.text.replace("Cv2 invite ","")
                #kk.findAndAddContactsByMid(midd)
                #kk.inviteIntoGroup(msg.to,[midd])
            #elif "Cv3 invite " in msg.text:
                #midd = msg.text.replace("Cv3 invite ","")
                #kc.findAndAddContactsByMid(midd)
                #kc.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Gw"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text in ["Nez1 id"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif msg.text in ["Nez2 id"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
            elif msg.text in ["Kasih","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Nez1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Nez2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Nez3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
            elif msg.text in ["Begal","Cancel"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        if X.invitee is not None:
                            gInviMids = [contact.mid for contact in X.invitee]
                            cl.cancelGroupInvitation(msg.to, gInviMids)
                        else:
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"Gak ada orang tuan")
                            else:
                                cl.sendText(msg.to,"Sorry mblo")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Lu bukan admin ler")
                        else:
                            cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Nez cancel","Bot cancel"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        G = k3.getGroup(msg.to)
                        if G.invitee is not None:
                            gInviMids = [contact.mid for contact in G.invitee]
                            k3.cancelGroupInvitation(msg.to, gInviMids)
                        else:
                            if wait["lang"] == "JP":
                                k3.sendText(msg.to,"No one is inviting")
                            else:
                                k3.sendText(msg.to,"Sorry, nobody absent")
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"Lu bukan admin ler")
                        else:
                            k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl","Lepas"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Sudah Tuan")
                        else:
                            cl.sendText(msg.to,"Sudah Tuan")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Lu bukan admin ler")
                        else:
                            cl.sendText(msg.to,"Not for use less than group")
            #elif msg.text in ["Cv1 ourl","Cv1 link on"]:
                #if msg.toType == 2:
                    #X = cl.getGroup(msg.to)
                    #X.preventJoinByTicket = False
                    #ki.updateGroup(X)
                    #if wait["lang"] == "JP":
                        #ki.sendText(msg.to,"Done Chivas")
                    #else:
                        #ki.sendText(msg.to,"already open")
                #else:
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"Can not be used outside the group")
                   # else:
                        #cl.sendText(msg.to,"Not for use less than group")
            #elif msg.text in ["Cv2 ourl","Cv2 link on"]:
                #if msg.toType == 2:
                    #X = kk.getGroup(msg.to)
                    #X.preventJoinByTicket = False
                    #kk.updateGroup(X)
                    #if wait["lang"] == "JP":
                        #kk.sendText(msg.to,"Done Chivas")
                    #else:
                        #kk.sendText(msg.to,"already open")
                #else:
                    #if wait["lang"] == "JP":
                        #kk.sendText(msg.to,"Can not be used outside the group")
                    #else:
                        #kk.sendText(msg.to,"Not for use less than group")
            #elif msg.text in ["Cv3 ourl","Cv3 link on"]:
                #if msg.toType == 2:
                    #X = kc.getGroup(msg.to)
                    #X.preventJoinByTicket = False
                    #kc.updateGroup(X)
                    #if wait["lang"] == "JP":
                        #kc.sendText(msg.to,"Done Chivas")
                    #else:
                        #kc.sendText(msg.to,"already open")
                #else:
                    #if wait["lang"] == "JP":
                        #kc.sendText(msg.to,"Can not be used outside the group")
                    #else:
                        #kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Segel"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Sudah Tuan")
                        else:
                            cl.sendText(msg.to,"Sudah Tuan")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Lu bukan admin ler")
                        else:
                            cl.sendText(msg.to,"Not for use less than group")
            #elif msg.text in ["Cv1 curl","Cv1 link off"]:
                #if msg.toType == 2:
                    #X = ki.getGroup(msg.to)
                    #X.preventJoinByTicket = True
                    #ki.updateGroup(X)
                    #if wait["lang"] == "JP":
                        #ki.sendText(msg.to,"Done Chivas")
                    #else:
                        #ki.sendText(msg.to,"already close")
                #else:
                    #if wait["lang"] == "JP":
                        #ki.sendText(msg.to,"Can not be used outside the group")
                    #else:
                        #ki.sendText(msg.to,"Not for use less than group")
            #elif msg.text in ["Cv2 curl","Cv2 link off"]:
                #if msg.toType == 2:
                    #X = kk.getGroup(msg.to)
                    #X.preventJoinByTicket = True
                    #zkk.updateGroup(X)
                    #if wait["lang"] == "JP":
                        #kk.sendText(msg.to,"Done Chivas")
                    #else:
                        #kk.sendText(msg.to,"already close")
                #else:
                    #if wait["lang"] == "JP":
                        #kk.sendText(msg.to,"Can not be used outside the group")
                    #else:
                        #kk.sendText(msg.to,"Not for use less than group")
            #elif msg.text in ["Cv3 curl","Cv3 link off"]:
                #if msg.toType == 2:
                    #X = kc.getGroup(msg.to)
                    #X.preventJoinByTicket = True
                    #kc.updateGroup(X)
                    #if wait["lang"] == "JP":
                        #kc.sendText(msg.to,"Done Chivas")
                    #else:
                        #kc.sendText(msg.to,"already close")
                #else:
                    #if wait["lang"] == "JP":
                        #kc.sendText(msg.to,"Can not be used outside the group")
                    #else:
                        #kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.id,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                kx.sendText(msg.to,mid)
                ky.sendText(msg.to,Amid)
                kf.sendText(msg.to,Bmid)
                kg.sendText(msg.to,Cmid)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Nez mid" == msg.text:
                ki.sendText(msg.to,Amid)
            elif "Nez mid" == msg.text:
                kk.sendText(msg.to,Bmid)
            elif "Nez mid" == msg.text:
                kc.sendText(msg.to,Cmid)
            elif msg.text in ["Wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Galon"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Kuy lesbi"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Wc","Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            #elif msg.text in ["Cn "]:
                #string = msg.text.replace("Cn ","")
                #if len(string.decode('utf-8')) <= 20:
                    #profile = cl.getProfile()
                    #profile.displayName = string
                    #cl.updateProfile(profile)
                    #cl.sendText(msg.to,"name " + string + " done")
            #elif msg.text in ["Cv1 rename "]:
                #string = msg.text.replace("Cv1 rename ","")
                #if len(string.decode('utf-8')) <= 20:
                    #profile_B = ki.getProfile()
                    #profile_B.displayName = string
                    #ki.updateProfile(profile_B)
                    #ki.sendText(msg.to,"name " + string + " done")
            #elif msg.text in ["Cv2 rename "]:
                #string = msg.text.replace("Cv2 rename ","")
                #if len(string.decode('utf-8')) <= 20:
                    #profile_B = kk.getProfile()
                    #profile_B.displayName = string
                    #kk.updateProfile(profile_B)
                    #kk.sendText(msg.to,"name " + string + " done")
            #elif msg.text in ["Mc "]:
                #mmid = msg.text.replace("Mc ","")
                #msg.contentType = 13
                #msg.contentMetadata = {"mid":mmid}
                #cl.sendMessage(msg)
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            #elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
                #if wait["autoJoin"] == True:
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"already on")
                    #else:
                        #cl.sendText(msg.to,"done")
                #else:
                    #wait["autoJoin"] = True
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"already on")
                    #else:
                        #cl.sendText(msg.to,"done")
            #elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
                #if wait["autoJoin"] == False:
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"already off")
                    #else:
                        #cl.sendText(msg.to,"done")
                #else:
                    #wait["autoJoin"] = False
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"already off")
                    #else:
                        #cl.sendText(msg.to,"done")
            #elif msg.text in ["Gcancel:"]:
                #try:
                    #strnum = msg.text.replace("Gcancel:","")
                    #if strnum == "off":
                        #wait["autoCancel"]["on"] = False
                        #if wait["lang"] == "JP":
                            #cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        #else:
                            #cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    #else:
                        #num =  int(strnum)
                        #wait["autoCancel"]["on"] = True
                        #if wait["lang"] == "JP":
                            #cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        #else:
                            #cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                #except:
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"Value is wrong")
                    #else:
                        #cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Set"]:
                md = ""
                if wait["contact"] == True: md+=" Contact : on\n"
                else: md+=" Contact : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share : on\n"
                else:md+=" Share : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
                if wait["atjointicket"] == True: md+=" Auto Join Group by Ticket : on\n"
                else:md+=" Auto Join Group by Ticket : off\n"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeâ†’" in msg.text:
                gid = msg.text.replace("album removeâ†’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
                n = msg.text.replace("Change clock ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam Update")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")

            elif msg.text == "Rangkum":
                    ki.sendText(msg.to, "Terangkum Tuan")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "NSider":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "Sider %s\nthat's it\n\nSider jomblo\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
#-----------------------------------------------

#-----------------------------------------------

            elif msg.text in ["Kuchiyose"]:
                        if msg.from_ in admin:
                            G = cl.getGroup(msg.to)
                            ginfo = cl.getGroup(msg.to)
                            G.preventJoinByTicket = False
                            cl.updateGroup(G)
                            invsend = 0
                            Ticket = cl.reissueGroupTicket(msg.to)
                            ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                            time.sleep(0.2)
                            kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                            time.sleep(0.2)
                            kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                            time.sleep(0.2)
                            kx.acceptGroupInvitationByTicket(msg.to,Ticket)
                            time.sleep(0.2)
                            ky.acceptGroupInvitationByTicket(msg.to,Ticket)
                            time.sleep(0.2)
                            kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                            time.sleep(0.2)
                            kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                            time.sleep(0.2)
                            G = cl.getGroup(msg.to)
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                            print "laknat ok"
                            G.preventJoinByTicket(G)
                            cl.updateGroup(G)

            #elif msg.text in ["Cv1 join"]:
                  #X = cl.getGroup(msg.to)
                  #X.preventJoinByTicket = False
                  #cl.updateGroup(X)
                  #invsend = 0
                  #Ti = cl.reissueGroupTicket(msg.to)
                  #ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  #G = kk.getGroup(msg.to)
                  #G.preventJoinByTicket = True
                  #ki.updateGroup(G)
                  #Ticket = kk.reissueGroupTicket(msg.to)

            #elif msg.text in ["Cv2 join"]:
                  #X = cl.getGroup(msg.to)
                  #X.preventJoinByTicket = False
                  #cl.updateGroup(X)
                  #invsend = 0
                  #Ti = cl.reissueGroupTicket(msg.to)
                  #kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  #G = ki.getGroup(msg.to)
                  #G.preventJoinByTicket = True
                  #kk.updateGroup(G)
                  #Ticket = kk.reissueGroupTicket(msg.to)

#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            #elif msg.text in ["Cv3 join"]:
                        #G = cl.getGroup(msg.to)
                        #ginfo = cl.getGroup(msg.to)
                        #G.preventJoinByTicket = False
                        #cl.updateGroup(G)
                        #invsend = 0
                        #Ticket = cl.reissueGroupTicket(msg.to)
                        #kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #print "kicker ok"
                        #G.preventJoinByTicket = True
                        #kc.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["Izanami"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            ki.leaveGroup(msg.to)
                            kk.leaveGroup(msg.to)
                            kc.leaveGroup(msg.to)
                            kx.leaveGroup(msg.to)
                            ky.leaveGroup(msg.to)
                            kf.leaveGroup(msg.to)
                            kg.leaveGroup(msg.to)
                        except:
                            pass
            #elif msg.text in ["Bye 1"]:
                #if msg.toType == 2:
                    #ginfo = cl.getGroup(msg.to)
                    #try:
                        #ki.leaveGroup(msg.to)
                    #except:
                        #pass
            #elif msg.text in ["Bye 2"]:
                #if msg.toType == 2:
                    #ginfo = cl.getGroup(msg.to)
                    #try:
                        #ki.leaveGroup(msg.to)
                        #kk.leaveGroup(msg.to)
                    #except:
                        #pass
            #elif msg.text in ["Cv1 @bye"]:
                #if msg.toType == 2:
                    #ginfo = cl.getGroup(msg.to)
                    #try:
                        #ki.leaveGroup(msg.to)
                    #except:
                        #pass
            #elif msg.text in ["Cv2 @bye"]:
                #if msg.toType == 2:
                    #ginfo = cl.getGroup(msg.to)
                    #try:
                        #kk.leaveGroup(msg.to)
                    #except:
                        #pass
            #elif msg.text in ["Cv3 @bye"]:
                #if msg.toType == 2:
                    #ginfo = cl.getGroup(msg.to)
                    #try:
                        #kc.leaveGroup(msg.to)
                    #except:
                        #pass
#-----------------------------------------------

            elif "Tag" in msg.text:
                if msg.from_ in admin:
                    group = ky.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    cb = ""
                    cb2 = ""
                    strt = int(0)
                    akh = int(0)
                    for md in nama:
                        akh = akh + int(5)
                        cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                        strt = strt + int(6)
                        akh = akh + 1
                        cb2 += "@nrik\n"
                    cb = (cb[:int(len(cb)-1)])
                    msg.contentType = 0
                    msg.text = cb2
                    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                    try:
                        ky.sendMessage(msg)
                    except Exception as error:
                        print error

            elif "DARK SPEAR" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        print "ok"
                        _name = msg.text.replace("DARK SPEAR","")
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        gs = kx.getGroup(msg.to)
                        gs = ky.getGroup(msg.to)
                        gs = kf.getGroup(msg.to)
                        gs = kg.getGroup(msg.to)
                        ki.sendText(msg.to,"Tuan itu bahaya")
                        kk.sendText(msg.to,"Tuan?")
                        kc.sendText(msg.to,"Kalian Berisik")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                            kk.sendText(msg.to,"Not found.")
                            kc.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
                                try:
                                    klist=[ki,kk,kc,kx,ky,kf,kg]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Spear")
            elif "▄︻̷̿┻̿═━一 " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("▄︻̷̿┻̿═━一 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"dia jomblo tuant")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,kk,kc]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Terpental Bosque")
                                    kk.sendText(msg.to,"Dark Spear keisi pak") 
            elif "Spear:" in msg.text:
                    if msg.from_ in admin:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                klist=[ki,kk,kc,kx,ky,kf,kg]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                            except:
                                sendText(msg.to,"Dia ngehindar pak")
            elif "Cydukk @ " in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("Cydukk @ ","")
                    _kicktarget = _name.rstrip(' ')
                    gs = ki2.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _kicktarget == g.displayName:
                            targets.append(g.mid)
                            if targets == []:
                                cl.sendText(msg.to,"dia jomblo pak")
                            else:
                                for target in targets:
                                    try:
                                        wait["blacklist"][target] = True
                                        f=codecs.open('st2__b.json','w','utf-8')
                                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        cl.sendText(msg.to,"Sudah tuan")
                                    except:
                                        ki.sendText(msg.to,"error pak")
            elif "Cyduk @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        print "[Cyduk]ok"
                        _name = msg.text.replace("Cyduk @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Gak ada orangnya pak")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Sukses Pak")
                                except:
                                    ki.sendText(msg.to,"Error")
            elif "Uncyduk @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        print "[Uncyduk]ok"
                        _name = msg.text.replace("Uncyduk @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Gak ada pak")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Sukses Pak")
                                except:
                                    ki.sendText(msg.to,"Sukses Pak")
#-----------------------------------------------
            #elif msg.text in ["Test"]:
                #ki.sendText(msg.to,"Ok Cv 􀨁􀄻double thumbs up􏿿")
                #kk.sendText(msg.to,"Ok Cv 􀨁􀄻double thumbs up􏿿")
                #kc.sendText(msg.to,"Ok Cv 􀨁􀄻double thumbs up􏿿")
#-----------------------------------------------
            #elif "Bc " in msg.text:
				#bctxt = msg.text.replace("Bc ","")
				#ki.sendText(msg.to,(bctxt))
				#kk.sendText(msg.to,(bctxt))
				#kc.sendText(msg.to,(bctxt))
#-----------------------------------------------

            #elif msg.text in ["Cv say hi"]:
                #ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                #kk.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                #kc.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")

#-----------------------------------------------

            #elif msg.text in ["Cv say hinata pekok"]:
                #ki.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                #kk.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                #kc.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
            #elif msg.text in ["Cv say didik pekok"]:
                #ki.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                #kk.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                #kc.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
            #elif msg.text in ["Cv say bobo ah","Bobo dulu ah"]:
                #ki.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                #kk.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                #kc.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
            #elif msg.text in ["Cv say chomel pekok"]:
                #ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                #kk.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                #kc.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            #elif msg.text in ["#welcome"]:
                #ki.sendText(msg.to,"Selamat datang di Chivas Family Room")
                #kk.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------
            elif msg.text in ["Prajurit","Laknatque"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Hadir pak")
                    kk.sendText(msg.to,"Anda yang Tertsamvan")
                    kc.sendText(msg.to,"Selingkuhannya Segudang")
                    kx.sendText(msg.to,"Tuan? mantannya ketinggalan tuh")
                #kk.sendText(msg.to,"Cv2")
                #kc.sendText(msg.to,"Cv3")



#-----------------------------------------------

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Bentar ler")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))

#------------------------------------------------------------------
            elif msg.text in ["Cyduk"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"Kirim kontak pak")
            elif msg.text in ["Uncyduk"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"Kirim kontak pak")
            elif msg.text in ["Cyduklist"]:
                if msg.from_ in admin:
                    if wait["blacklist"] == {}:
                        cl.sendText(msg.to,"Kosong pak")
                    else:
                        cl.sendText(msg.to,"Daftar Cyduk")
                        mc = ""
                        for mi_d in wait["blacklist"]:
                            mc += "->" +cl.getContact(mi_d).displayName + "\n"
                        cl.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Bantai"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendText(msg.to,"Ulang pak")
                            return
                        for jj in matched_list:
                            cl.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            kk.kickoutFromGroup(msg.to,[jj])
                            kc.kickoutFromGroup(msg.to,[jj])
                        cl.sendText(msg.to,"Sudah pak")
            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "Random:" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        strnum = msg.text.replace("Random:","")
                        source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                        try:
                            num = int(strnum)
                            group = cl.getGroup(msg.to)
                            for var in range(0,num):
                                name = "".join([random.choice(source_str) for x in xrange(10)])
                                time.sleep(0.01)
                                group.name = name
                                cl.updateGroup(group)
                        except:
                            cl.sendText(msg.to,"Error")
            elif "albumâ†’" in msg.text:
                try:
                    albumtags = msg.text.replace("albumâ†’","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fake" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def autolike():
     for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like bngst\ndari bapak Frankenstein\n\nline.me/ti/p/~ridwanibnz")
            kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like bngst\nDari bapak Frankenstein\n\nline.me/ti/p/~ridwanibnz")
            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like bngst\ndari bapak Frankenstein\n\nline.me/ti/p/~ridwanibnz")
            kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like bngst\nDari bapak Frankenstein\n\nline.me/ti/p/~ridwanibnz")
            kx.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kx.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like bngst\ndari bapak Frankenstein\n\nline.me/ti/p/~ridwanibnz")
            ky.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ky.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like bngst\nDari bapak Frankenstein\n\nline.me/ti/p/~ridwanibnz")
            kf.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kf.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like bngst\ndari bapak Frankenstein\n\nline.me/ti/p/~ridwanibnz")
            kg.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kg.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like bngst\nDari bapak Frankenstein\n\nline.me/ti/p/~ridwanibnz")
            print "Like"
          except:
            pass
        else:
            print "Already Liked"
     time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
