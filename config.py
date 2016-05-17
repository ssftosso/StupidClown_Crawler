# -*- coding: utf8 -*-

## Show log
    #  top: 0
    # down: 5 (default)
RunningLogLevel = 2

## Multi-Thread set
EnableMultiThread = False
MaxMultiThreadNum = 3

ThreadCountCheckDelay           = 1 # for waiting all thread finished
MaxMultiThreadNum_CheckDelay    = 1

## DelayTime
GetAndStorePushList_ErrorDelay = 2

#### Delay time config
ERROR_xpath_delay = 1

## URL config
RootURL = "https://www.ptt.cc"

##Database config
DB_DatabaseName = "STORE.db"

DB_TableName    = "PushList"

DBC_TypeName    = "type"
DBC_AccountName = "account"
DBC_PushContent = "content"
DBC_PostTitle   = "posttitle"
DBC_PostAccount = "postaccountname"
DBC_BoardName   = "board"
DBC_PushTime    = "pushtime"



## Xpath pattern
Pattern_SubPageURL              = '//div[@class="title"]/a/@href'
Pattern_PrePageURL              = '//a[@class="btn wide"]/@href'
Pattern_PrePageName             = '//a[@class="btn wide"]/text()'

#### Sub page content
Pattern_SubPageTitle            = '//div[@class="title"]/a/text()'
Pattern_TitleInSubPage          = '//*[@id="main-content"]/div[3]/span[@class="article-meta-value"]/text()'
Pattern_PostAccountInSubPage    = '//*[@id="main-content"]/div[1]/span[@class="article-meta-value"]/text()'

#### Push content
Pattern_PushType                = '//*[@id="main-content"]/div[@class="push"]/span[1]/text()'
Pattern_PushAccount             = '//*[@id="main-content"]/div[@class="push"]/span[2]/text()'
Pattern_PushContent             = '//*[@id="main-content"]/div[@class="push"]/span[@class="f3 push-content"]'
Pattern_PushTime                = '//*[@id="main-content"]/div[@class="push"]/span[4]/text()'

#### File set
UserAgentList_Path              = 'item/UserAgentList.txt'



