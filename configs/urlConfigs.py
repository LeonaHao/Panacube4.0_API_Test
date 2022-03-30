# -*- coding = utf-8 -*-
# @author = Leona
'''
配置系统中需要的url地址信息
'''

basePanaCubeUrl = 'http://192.168.2.140/v1/'

'''登录接口'''
loginUrl = basePanaCubeUrl+'account/login'
'''退出登录接口'''
logoutUrl = basePanaCubeUrl + 'account/logout'

#*********************************云中心-业务管理*******************************************
'''云中心-业务管理-业务池列表'''
cloudPoolListUrl = basePanaCubeUrl + 'cloud/projects'
'''云中心-业务管理-业务池列表'''
instanceUrl = basePanaCubeUrl + 'cloud/instances'
'''智能存储》概况》获取存储情况'''
overViewStorage = basePanaCubeUrl + 'cloud/pools/intel/storage/'


#*********************************云中心-网络管理*******************************************
'''云中心-网络管理-网络'''
networktUrl = basePanaCubeUrl + 'cloud/networks'

subnetUrl = basePanaCubeUrl + 'cloud/subnets'

'''云中心-网络管理-路由'''
routertUrl = basePanaCubeUrl + 'cloud/routers'

'''云中心-网络管理-虚拟网卡'''
virtualNetCardUrl = basePanaCubeUrl + 'cloud/ports'


'''云中心-网络管理-公网IP'''
pubNetIP = basePanaCubeUrl + 'cloud/floatingips'

'''云中心-网络管理-安全组'''
securityGroupUrl = basePanaCubeUrl + 'cloud/securitygroups'


#*********************************云中心-镜像管理*******************************************
'''云中心-镜像管理'''
imageUrl = basePanaCubeUrl + 'cloud/images'


#*********************************智能存储-存储池管理*******************************************
'''智能存储》存储池管理》获取全部存储池列表(包含default池)'''
storagePoolUrl = basePanaCubeUrl + 'storage/pools'
'''智能存储》存储池管理》获取全部业务池列表(不包含default池)'''
projectUrl = basePanaCubeUrl + 'cloud/projects'
'''智能存储》存储池管理》存储池详情'''
storagePoolInfoUrl = basePanaCubeUrl + 'storage/pools'
'''智能存储》存储池管理》系统配额'''
systemQuotasUrl = basePanaCubeUrl + 'sysmgmt/quotas'
'''智能存储》存储池管理》存储剩余空间'''
storageRemain = basePanaCubeUrl + 'cloud/storage-pools/remain'
'''智能存储》存储池管理》监控'''
storageMonitor = basePanaCubeUrl + 'storage/pools/monitor'
'''智能存储》存储池管理》存储流量监控'''
storageFlowMonitor = basePanaCubeUrl + 'storage/pools/monitor/flow'




#*********************************快照管理*******************************************
'''智能存储》快照管理》业务池快照'''
poolSnap = basePanaCubeUrl + 'storage/snapshots/pool'
'''智能存储》快照管理》云组件快照'''
instanceSnap = basePanaCubeUrl + 'storage/snapshots/instance'
'''智能存储》快照管理》云硬盘快照'''
diskSnap = basePanaCubeUrl + 'storage/snapshots/file'
'''智能存储》快照管理》删除业务池快照'''
delPoolSnap = basePanaCubeUrl + 'storage/snapshots/pool/batch-delete'
'''智能存储》快照管理》删除云组件快照'''
cloudInstanceSnap = basePanaCubeUrl + 'cloud/instances/'
'''智能存储》快照管理》删除云硬盘快照'''
delDiskSnap = basePanaCubeUrl + 'storage/snapshots/file/batch-delete'

#*********************************云硬盘管理*******************************************
'''智能存储》云硬盘管理》获取云硬盘'''
cloudDisk = basePanaCubeUrl + 'storage/volumes'
'''智能存储》云硬盘管理》卸载云硬盘'''
cloudDiskDetach = basePanaCubeUrl + 'storage/volumes/action'
'''智能存储》云硬盘管理》删除云硬盘'''
batchDeleteCloudDisk = basePanaCubeUrl + 'storage/volumes/batch-delete'
'''智能存储》云硬盘》数据盘》创建快照'''
dataDiskSnapshot = basePanaCubeUrl + 'storage/snapshots/file'
'''智能存储》块存储》云硬盘》批量删除快照'''
batchDeleteSnapshot = basePanaCubeUrl + 'storage/snapshots/batch-delete/'
'''智能存储》块存储》云硬盘》加载的云硬盘'''
attachCDInfo = basePanaCubeUrl + 'storage/detach-volumes/'
'''智能存储》块存储》云硬盘》强制删除云硬盘'''
forceDelCD = basePanaCubeUrl + '/storage/volumes/force-delete'

#
#*********************************文件存储*******************************************
'''智能存储》文件存储》文件共享'''
shareUrl = basePanaCubeUrl + 'storage/shares'
'''智能存储》文件存储》删除文件共享'''
shareDelUrl = basePanaCubeUrl + 'storage/shares/batch-delete'

'''智能存储》共享用户管理》用户'''
userUrl = basePanaCubeUrl + 'storage/users'
'''智能存储》共享用户管理》用户组'''
userGroupUrl = basePanaCubeUrl + 'storage/groups'
'''智能存储》共享用户管理》删除用户'''
userDelUrl = basePanaCubeUrl + 'storage/users/batch-delete'
'''智能存储》共享用户管理》删除用户组'''
userGroupDelUrl = basePanaCubeUrl + 'storage/groups/batch-delete'
# '''智能存储》共享用户管理》删除用户组''''''智能存储》对象存储》对象共享'''
# objShareUrl = baseGatewayUrl + 'buckets/'
# '''智能存储》共享用户管理》删除对象共享'''
# objShareDelUrl = baseGatewayUrl + 'buckets/batch-delete/'
#
# userGroupDelUrl = baseGatewayUrl + 'group/action/'
#
# #*********************************对象存储*******************************************
#
#
#
#*********************************服务管理*******************************************
'''智能存储》服务管理》获取服务列表'''
serviceUrl = basePanaCubeUrl + 'storage/services'
'''智能存储》服务管理》开启服务 or 关闭服务'''
magServiceUrl = basePanaCubeUrl + 'storage/services/S3/action'

#
#
#
# '''智能存储》块存储》快照》删除快照'''
# delBlockSnapshotUrl = basePanaCubeUrl + 'storage/snapshots/'
#


