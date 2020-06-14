#-*- coding: utf-8 -*-
#Vstream https://github.com/Kodi-vStream/venom-xbmc-addons
from resources.lib.handler.requestHandler import cRequestHandler 
from resources.lib.parser import cParser 
from resources.hosters.hoster import iHoster
from resources.lib.comaddon import dialog, isKrypton

UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'

class cHoster(iHoster):

    def __init__(self):
        if not (isKrypton() == True):
            self.__sDisplayName = '(Windows\Android Nécessite Kodi17)' + ' ' + 'Vidlox'
        else:
            self.__sDisplayName = 'Vidlox'        
        self.__sFileName = self.__sDisplayName
        self.__sHD = ''

    def getDisplayName(self):
        return  self.__sDisplayName

    def setDisplayName(self, sDisplayName):
        self.__sDisplayName = sDisplayName + ' [COLOR skyblue]'+self.__sDisplayName+'[/COLOR]'

    def setFileName(self, sFileName):
        self.__sFileName = sFileName
        
    def getFileName(self):
        return self.__sFileName

    def getPluginIdentifier(self):
        return 'vidlox'
        
    def setHD(self, sHD):
        self.__sHD = ''
        
    def getHD(self):
        return self.__sHD

    def isDownloadable(self):
        return True

    def setUrl(self, sUrl):
        self.__sUrl = str(sUrl)

    def getMediaLink(self):
        return self.__getMediaLinkForGuest()

    def __getMediaLinkForGuest(self):
    
        oParser = cParser()
        oRequest = cRequestHandler(self.__sUrl)
        sHtmlContent = oRequest.request()
        
        #accelère le traitement
        sHtmlContent = oParser.abParse(sHtmlContent, 'var player', 'vvplay')

        sPattern =  '([^"]+\.mp4)'
        oParser = cParser()
        aResult = oParser.parse(sHtmlContent, sPattern)
        if (aResult[0] == True):
            #initialisation des tableaux
            url=[]
            qua=["HD","SD"] #sd en 2eme pos generalement quand sd
            api_call = ''

            #Replissage des tableaux
            for i in aResult[1]:
                url.append(str(i))

            #dialog qualiter
            api_call = dialog().VSselectqual(qua,url)
  
        if (api_call):
            return True, api_call+ '|User-Agent=' + UA+'&verifypeer=false' 

        return False, False