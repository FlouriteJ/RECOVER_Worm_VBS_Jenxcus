import os
path_list=[]
Path=input('Disk:')+":\\"
path_list.append(Path)
i=0

while path_list != []:
	path_i=path_list.pop()
	if os.path.exists(path_i):
		i+=1
		print(i,'\t',path_i)
		if path_i != Path:
			os.system("attrib \""+path_i+"\" -s -h")
		
		if os.path.isdir(path_i):
			path_i_list=os.listdir(path_i)
			if path_i_list != []:
				path_list.extend([os.path.join(path_i, filename) for filename in path_i_list])