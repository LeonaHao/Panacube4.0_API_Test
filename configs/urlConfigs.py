# -*- coding = utf-8 -*-
# @author = Leona
'''
配置系统中需要的url地址信息
'''
#http://192.168.2.200/v1/
basePanaCubeUrl = 'http://192.168.5.170/v1/'

'''登录接口'''
loginUrl = basePanaCubeUrl+'account/login'
'''退出登录接口'''
logoutUrl = basePanaCubeUrl + 'account/logout'

#*********************************云中心-业务管理*******************************************
'''云中心-业务管理-业务池列表'''
cloudPoolListUrl = basePanaCubeUrl + 'cloud/projects'



'''智能存储》概况》获取存储情况'''
overViewStorage = basePanaCubeUrl + 'cloud/pools/intel/storage/'



#*********************************智能存储-存储池管理*******************************************
'''智能存储》存储池管理》获取全部存储池列表(包含default池)'''
storagePoolListUrl = basePanaCubeUrl + 'storage/pools'
'''智能存储》存储池管理》获取全部业务池列表(不包含default池)'''
projectListUrl = basePanaCubeUrl + 'cloud/projects'




#*********************************快照管理*******************************************
'''智能存储》快照管理》业务池快照'''
poolSnap = basePanaCubeUrl + 'storage/snapshots/pool'
'''智能存储》快照管理》业务池快照'''
instanceSnap = basePanaCubeUrl + 'storage/snapshots/instance'
'''智能存储》快照管理》云硬盘快照'''
diskSnap = basePanaCubeUrl + 'storage/snapshots/file'
'''智能存储》快照管理》删除业务池快照'''
delPoolSnap = basePanaCubeUrl + 'storage/snapshots/pool/batch-delete'
'''智能存储》快照管理》删除云组件快照'''
delInstanceSnap = basePanaCubeUrl + 'cloud/instances/'
'''智能存储》快照管理》删除云硬盘快照'''
delDiskSnap = basePanaCubeUrl + 'storage/snapshots/file/batch-delete'

#*********************************云硬盘管理*******************************************
'''智能存储》云硬盘管理》获取云硬盘'''
cloudDisk = basePanaCubeUrl + 'storage/volumes'
'''智能存储》云硬盘管理》卸载云硬盘'''
cloudDiskDetach = basePanaCubeUrl + 'storage/volumes/action'
'''智能存储》云硬盘管理》删除云硬盘'''
batchDeleteCloudDisk = basePanaCubeUrl + 'storage/volumes/batch-delete'
'''智能存储》块存储》云硬盘》创建快照'''
cloudDiskSnapshot = basePanaCubeUrl + 'storage/snapshots/'
'''智能存储》块存储》云硬盘》批量删除快照'''
batchDeleteSnapshot = basePanaCubeUrl + 'storage/snapshots/batch-delete/'
'''智能存储》块存储》云硬盘》加载的云硬盘'''
attachCDInfo = basePanaCubeUrl + 'storage/detach-volumes/'
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
# #*********************************服务管理*******************************************
# '''智能存储》服务管理》获取服务列表'''
# serviceUrl = baseGatewayUrl + 'services/'
# '''智能存储》服务管理》开启服务'''
# startServiceUrl = baseGatewayUrl + 'services/start/'
# '''智能存储》服务管理》关闭启服务'''
# stopServiceUrl = baseGatewayUrl + 'services/stop/'
#
#
#
# '''智能存储》块存储》快照》删除快照'''
# delBlockSnapshotUrl = basePanaCubeUrl + 'storage/snapshots/'
#


