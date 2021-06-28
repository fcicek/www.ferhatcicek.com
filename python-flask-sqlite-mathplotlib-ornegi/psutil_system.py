import psutil

print('MEM  % used:', psutil.virtual_memory()[2])
print('CPU % used:', psutil.cpu_percent(2))
