from config import quota_file
import os
import re


#都按照G计数
class Quota(object):

	def __init__(self):
		pass

	#比较函数
	def __lt__(self,other):
		return self.quota<other.quota
			
	def setQuota(self,quota):
		self.quota=self.quota

	def getQuota(self,quota):
		return self.quota


class UserQuota(Quota):

	def __init__(self,path):
		self.quota=0
		with open(quota_file) as fo:
			for line in fo.readlines:
				data=line.split(",")
				if path==data[0]:
					self.quota=data[1]
					break

class ActualQuota(Quota):

	def __init__(self,path):
		self.quota=0
		cmd="df -sg "+path
		res=os.system(cmd)
		if res:
			self.quota=int(res.split()[0])


class QuotaHandler(object):
	def overControl(self,path):
		if UserQuota(path)>ActualQuota(path):
			FilePathController(path).acquire()


class FilePathController(object):

	def __init__(self,path):
		self.path=path

	def acquire(self):
		cmd="chattr +i "+self.path
		return os.system(cmd)

	def release(self):
		cmd="chattr -i "+self.path
		return os.system(cmd)

class Message(object):

	def __init__(self,**kwargs):
		pass

	def setHandle(self,Handler):
		self.handlers.append(Handler)

	def connection(self):
		


if __name__=="__main__":

	msgServer=Message(message_config)
	msgServer.setHandle(QuotaHandler)
	msgServer.listen()



