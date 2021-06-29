curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz"| tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
eksctl version
#install kubectl
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.18.0/bin/linux/amd64/kubectl 
chmod +x ./kubectl 
sudo mv ./kubectl /usr/local/bin/kubectl 
kubectl version --client