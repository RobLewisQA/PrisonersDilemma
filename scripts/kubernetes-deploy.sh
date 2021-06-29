cd deployments/kubernetes
aws eks --region eu-west-1 update-kubeconfig --name eks_cluster_prisonersdilemma
kubectl apply -f tournament.yaml
kubectl apply -f ./nginx/service.yaml
kubectl apply -f ./nginx/deployment.yaml
kubectl apply -f ./nginx/configmap.yaml
kubectl get pods
kubectl get services