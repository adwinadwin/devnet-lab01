# Có 2 vendor: Cisco và Juniper.
# - Thiết kế class để có thể tương tác được nó như:
	# + Hiển thị file cấu hình
	# + Cấu hình VLAN

class Router(object):
	def __init__(self, vendor):
		self.vendor = vendor

class cisco(Router):
	def config_file(self, config_file, vlan):
		print('File config cua thiet bi Cisco la: {0}' .format(config_file))
		print ('Vlan cua thiet bi la:{0}' .format(vlan))


class juniper(Router):
	def config_file(self, config_file, vlan):
		print('File config cua thiet bi Juniper la: {0}' .format(config_file))
		print ('Vlan cua thiet bi la:{0}' .format(vlan))

cisco1 = cisco('Cisco')
juniper1 = juniper('Juniper')
cisco1.config_file('Cisco_v1.bin', 100)
juniper1.config_file('juniper_v1.bin', 200)
