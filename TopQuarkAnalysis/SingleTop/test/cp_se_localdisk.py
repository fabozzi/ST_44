import os, commands


#To run after  "source ~fabozzi/setdpm_host.csh cmsse02"

#dirnames =  ['MuRun2012A', 'DYJetsToLL_M-50']
#indirnames =  ['Run2012A_v3', 'DYJetsToLL_M-50_v1']

repo_dict = {}

dpm_path = "/dpm/na.infn.it/home/cms/store/user/fabozzi/SingleTop/Analysis/44XNEW/"

updirs = ['Fall11', 'ReReco']

# --> in one shot: read repo_dict from dpm
#for dd in updirs:
#    mydirs = (commands.getoutput("rfdir " + dpm_path + dd)).split(os.linesep) 
#    for longdir in mydirs:
#        dir = (longdir.split())[-1]
#        print dd, dir
#        repo_dict[dir] = dd+"/"+dir
#print repo_dict

# --> just for few samples: define repo_dict by hand!!!
repo_dict['Mu_2011B_19Nov'] = 'ReReco/Mu_2011B_19Nov'

dirnames = repo_dict.keys()
print dirnames

#outpath = '/data3/scratch/users/decosa/Higgs/Summer12/'
outpath = '/data3/scratch/users/fabozzi/SingleTop/'
ntpdir = '/ntp14apr14/'


for a in dirnames:
    print a
    cmdLocalDisk = "mkdir "+ outpath 
    os.system(cmdLocalDisk)
    cmdLocalDisk = cmdLocalDisk + ntpdir
    os.system(cmdLocalDisk)   
    cmdLocalDisk = cmdLocalDisk + a 
    os.system(cmdLocalDisk)
    cmdPermission = "chmod 775 " + outpath + ntpdir + a
    os.system(cmdPermission)
    cmdClean = "rm "+ outpath + ntpdir + a + "/*"
    os.system(cmdClean)
    print cmdLocalDisk
    print cmdPermission
    print  cmdClean
    cmd = "rfdir " + dpm_path + repo_dict[a]
    status,ls_la = commands.getstatusoutput( cmd )    
#    print ls_la
    files = []
    list = ls_la.split(os.linesep)
    for l in list:
        b = l.split()
        for c in b:
            if c.endswith('.root'):
                print "FILE"
                print c
                cmd = "rfcp " +  dpm_path + repo_dict[a] +"/"+ c + " " + outpath +ntpdir + a + "/"
                os.system(cmd)
                print cmd
                files.append(c)
print len(files)                
print files
                   
