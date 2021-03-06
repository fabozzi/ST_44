import os,coral,re
from RecoLuminosity.LumiDB import nameDealer
def applyfinecorrectionBX(bxlumi,avglumi,norm,constfactor,afterglowfactor,nonlinearfactor):
    if bxlumi<=0:
        return bxlumi
    correctbxlumi=bxlumi*norm*constfactor*afterglowfactor
    if constfactor!=1.0 and nonlinearfactor!=0:
        if avglumi<0:
            avglumi=0.0
        nonlinearTerm=1.0+avglumi*nonlinearfactor#0.076/ncollidinbunches
        correctbxlumi=correctbxlumi/nonlinearTerm
        #print 'avglumi,nonlinearfactor,nonlinearTerm ',avglumi,nonlinearfactor,nonlinearTerm
    #print 'bxlumi,avglumi,norm,const,after',bxlumi,avglumi,norm,constfactor,afterglowfactor,correctbxlumi
    return correctbxlumi

def applyfinecorrection(avglumi,constfactor,afterglowfactor,nonlinearfactor):
    instlumi=avglumi*afterglowfactor*constfactor
    if nonlinearfactor!=0 and constfactor!=1.0:
        nonlinearTerm=1.0+avglumi*nonlinearfactor#0.076/ncollidinbunches
        instlumi=instlumi/nonlinearTerm
    #print 'avglumi,const,after,nonlinear,instlumi ',avglumi,constfactor,afterglowfactor,nonlinearfactor,instlumi
    return instlumi

def correctionsForRange(schema,inputRange):
    '''
    select fillschemepattern,correctionfactor from fillscheme; 
       [(fillschemepattern,afterglow),...]
    select fillnum,runnum,fillscheme,ncollidingbunches,egev from cmsrunsummary where amodetag='PROTPYHS' and egev>3000
        {runnum: (fillnum,fillscheme,ncollidingbunches),...}
    output:
        {runnum:(constantfactor,afterglowfactor,nonlinearfactor)}
    '''
    runs=[]
    result={}
    if isinstance(inputRange,str):
        runs.append(int(inputRange))
    else:
        runs=inputRange
    for r in runs:
        if r<160442 :
            result[r]=(1.0,1.0,0.0)
    afterglows=[]
    s=nameDealer.fillschemeTableName()
    r=nameDealer.cmsrunsummaryTableName()
    qHandle=schema.newQuery()
    try:
        qHandle.addToTableList(s)
        qResult=coral.AttributeList()
        qResult.extend('FILLSCHEMEPATTERN','string')
        qResult.extend('CORRECTIONFACTOR','float')
        qHandle.defineOutput(qResult)
        qHandle.addToOutputList('FILLSCHEMEPATTERN')
        qHandle.addToOutputList('CORRECTIONFACTOR')
        cursor=qHandle.execute()
        while cursor.next():
            fillschemePattern=cursor.currentRow()['FILLSCHEMEPATTERN'].data()
            afterglowfac=cursor.currentRow()['CORRECTIONFACTOR'].data()
            afterglows.append((fillschemePattern,afterglowfac))
    except :
        del qHandle
        raise
    del qHandle
    qHandle=schema.newQuery()
    try:
        qHandle.addToTableList(r)
        qHandle.addToOutputList('FILLNUM', 'fillnum')
        qHandle.addToOutputList('RUNNUM', 'runnum')
        qHandle.addToOutputList('FILLSCHEME','fillscheme')
        qHandle.addToOutputList('NCOLLIDINGBUNCHES','ncollidingbunches')
        qResult=coral.AttributeList()
        qResult.extend('fillnum','unsigned int')
        qResult.extend('runnum','unsigned int')
        qResult.extend('fillscheme','string')
        qResult.extend('ncollidingbunches','unsigned int')
        qConditionStr='AMODETAG=:amodetag AND EGEV>=:egev'
        qCondition=coral.AttributeList()
        qCondition.extend('amodetag','string')
        qCondition.extend('egev','unsigned int')
        qCondition['amodetag'].setData('PROTPHYS')
        qCondition['egev'].setData(3000)
        qHandle.defineOutput(qResult)
        qHandle.setCondition(qConditionStr,qCondition)
        cursor=qHandle.execute()
        while cursor.next():
            runnum=cursor.currentRow()['runnum'].data()
            #print 'runnum ',runnum 
            if runnum not in runs or result.has_key(runnum):
                continue
            fillnum=cursor.currentRow()['fillnum'].data()
            constfactor=1.141
            afterglow=1.0
            nonlinear=0.076
            nonlinearPerBX=0.0
            ncollidingbunches=0
            if cursor.currentRow()['ncollidingbunches']:
                ncollidingbunches=cursor.currentRow()['ncollidingbunches'].data()
            fillscheme=''
            if cursor.currentRow()['fillscheme']:
                fillscheme=cursor.currentRow()['fillscheme'].data()
            if fillscheme and len(fillscheme)!=0:
                afterglow=afterglowByFillscheme(fillscheme,afterglows)
            if ncollidingbunches and ncollidingbunches!=0:
                nonlinearPerBX=float(1)/float(ncollidingbunches)
            nonlinear=nonlinearPerBX*nonlinear           
            result[runnum]=(constfactor,afterglow,nonlinear)
    except :
        del qHandle
        raise
    del qHandle
    for run in runs:
        if run not in result.keys():
            result[run]=(1.0,1.0,0.0)
    return result

def afterglowByFillscheme(fillscheme,afterglowPatterns):
    for (apattern,cfactor) in afterglowPatterns:
        if re.match(apattern,fillscheme):
            return cfactor
    return 1.0

if __name__ == "__main__":
    import sessionManager
    myconstr='oracle://cms_orcoff_prod/cms_lumi_prod'
    svc=sessionManager.sessionManager(myconstr,authpath='/afs/cern.ch/user/x/xiezhen',debugON=False)
    session=svc.openSession(isReadOnly=False,cpp2sqltype=[('unsigned int','NUMBER(10)'),('unsigned long long','NUMBER(20)')])
    runrange=[163337,163387,163385,163664,163757,163269,1234,152611]
    schema=session.nominalSchema()
    session.transaction().start(True)
    result=correctionsForRange(schema,runrange)
    session.transaction().commit()
    del session
    print result
