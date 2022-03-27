apt update

apt install python-pip -y
python2 -m pip install requests

apt install python3-pip -y
python3 -m pip install -r Tools_Information_Gathering/dirsearch/requirements.txt

mv Tools_Information_Gathering/GitHacker/.git.bak Tools_Information_Gathering/GitHacker/.git
