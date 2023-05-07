import argparse
from hashlib import md5
import subprocess

parser = argparse.ArgumentParser(
				prog = 'split.py',
				description = 'this tool split any files to short size and merge tham again',
				epilog = 'hope U like our work')
				
parser.add_argument('-f', '--file', required = True, help = "insert file name") # true for recover the original file name in merge mode
parser.add_argument('-s', '--size', required = False, help = "insert size pieces per bytes") 
parser.add_argument('-m', '--mode', required = True, help = "Tool mode : 0 - split file , 1 - merge splited files") 


args = parser.parse_args() # returns list all args



if args.mode == '0': # user split files
	try:
		f = open(args.file, 'rb')
	except FileNotFound as e:
		print(e)
		exit()
		
		# save the original file as hash string inside a new file
	with open('md5.txt', 'x') as ash:
		md5 = md5()
		md5.update(f.read()) # this method read byets type only
		ash.write(md5.hexdigest() + '\n' + args.file) # save both the hash code and file name
	
	# write pieces from the file and split per SIZE mode
	f = open(args.file, 'rb')
	
	size = int(args.size) # get the size each piece
	
	byte = f.read(size) # get SIZE number first time 
	
	count = 0 # piece name
	
	
	while byte :
		
		piece_name = "" # for setting file name each piece
		
		if count < 10 :
			piece_name = '00' + str(count)
		elif count < 100 :
			piece_name = '0' + str(count)
		else :
			piece_name = str(count)
			
		open(piece_name + ".bin" , 'wb').write(byte) # open new file to write BYTE
		
		byte = f.read(size)
		
		count += 1
		
	f.close()
	
	# remove original file 
	ls = ['rm',args.file]
	subprocess.run(ls, stdout = subprocess.PIPE)
	
	print('split complete !')
	
	# -- stage one finish --
	# user get file split to args.size sizes with the md5 file
	
else: # user want to merge the pieces of binary files

	res = subprocess.run('ls', stdout = subprocess.PIPE) # res contain ls terminal method
	
	# ls return a sorted string
	res = res.stdout.decode("utf-8").split() # change ls to a list from str type
	
	# create a new file that contain the merge of all little files
	
	f1 = open('md5.txt', 'r').read().split() # f1 became list that contain hash code of original and the original file name
	
	nf = open(f1[1], 'wb') # new file for merge into will call like original file name 
	
	for item in res:
	
		if 'bin' == item[item.index('.')+1:]: # check if bin in file signture
		
			nf.write(open(item, 'rb').read()) # if bin in file name, nf get the the item content 
			
			ls = ['rm',item] # list contains remove file name terminal method
			
			subprocess.run(ls, stdout = subprocess.PIPE) # will delete the file after reading
			
	
	# check hash code both files to check if process end succssesfuly
	nf = open(f1[1], 'rb')
	
	with open('md5.txt', 'r') as ash: # ash contains the hash string from original file
	
		filename = ash.read().split()
		
		md5 = md5()
		
		md5.update(nf.read()) # md5 contains the MD5 encryption string 
		
		print(md5.hexdigest())
		print(filename[0])
		if md5.hexdigest() == filename[0]: # check current hash with original
			print('hash EQUAL !')
			print('thanks for semester from AYAL and REFAEL <3')
			
		else:
			print('hash NOT EQUAL !')
			print("teacher doesn't teach right")
			
	 # removing the file that create first stage		
	ls = ['rm','md5.txt']
	subprocess.run(ls, stdout = subprocess.PIPE)
	
	
	
	
	 
	
	
	
