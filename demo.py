import os

def create_project_dir(folder_name):
     if not os.path.exists(folder_name):
        print("Cerating the directory "+folder_name)
        os.makedirs(folder_name)


def create_data_files(project_folder,base_url):
    queue=os.path.join(project_folder,"queue.txt")
    crawled=os.path.join(project_folder,"crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,"")

def write_file(path,data):
    with open(path,'w') as f:
        f.write(data+"\n")


def append_to_file(path,data):
    with open(path,'a') as f:
        f.write(data+"\n")


def delete_from_file(path):
    open(path,'w').close()


def file_to_set(file_name):
    results=set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results


def set_to_file(links,filename):
    with open(filename,'w') as f:
        for link in sorted(links):
            f.write(link+"\n")