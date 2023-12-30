from flask import Flask, render_template, request
import subprocess
app = Flask(__name__)

username = ""
password = ""
ip = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        global username, password, ip
        username = request.form['username']
        password = request.form['password']
        ip = request.form['ip']
        create_lv(username+"_drive")
        return render_template('success.html')

@app.route("/submitReq", methods=['POST'])
def usrReq():
    if request.method == 'POST':
        size = request.form['size']
        size = size+'G'
        dirname = request.form['dirname']
        dirname = "/"+dirname
        extend_lv(size,username+"_drive")
        shared_dir = mount_lv(username+"_drive")

        line =shared_dir+" "+ip+"(rw,sync,no_subtree_check)"
        with open('/etc/exports','a') as file:
            file.write(line)
        export_lv()
        start_nfs_server()
        server_ip ="172.16.11.128"
        path_to_share = "/dev/my_local_drive/"+username+"_drive"
        mount_on_client_ip(dirname,server_ip,path_to_share)
        return render_template('submitReq.html')



def mount_lv(name_of_lv):
    dirname = "/shared_"+name_of_lv
    cmd = ['mkdir',dirname]
    subprocess.run(cmd)
    cmd2 = ['mkfs.ext4','/dev/my_local_drive/'+name_of_lv]
    subprocess.run(cmd2)
    cmd3 = ['mount','/dev/my_local_drive/'+name_of_lv,dirname]
    subprocess.run(cmd3)
    return dirname

def mount_on_client_ip(dirname,server_ip,path_to_share):
    cmd = ['sshpass','-p',password,
            'ssh','-o','stricthostkeychecking=no',
            username+"@"+ip,
            "echo "+password+" | sudo -S mkdir -p "+dirname,
            "echo 260103 | sudo -S mount -t nfs "+server_ip+":"+path_to_share+" "+dirname]
    output = subprocess.run(cmd)

def start_nfs_server():
    cmd = ['systemctl','start','nfs-kernel-server']
    subprocess.run(cmd)

def export_lv():
    cmd = ['sudo','exportfs','-a']
    subprocess.run(cmd)


def create_lv(name):
    cmd = ['lvcreate','-L','1','-n',name,'my_local_drive']
    subprocess.run(cmd)

def extend_lv(size,name):
    size_fmt = '+'+size
    lv_loc = '/dev/my_local_drive/'+name
    cmd = ['lvextend','-L',size_fmt,lv_loc]
    subprocess.run(cmd)





if __name__ == '__main__':
    app.debug = True
    app.run()



