Linux 

git clone https://github.com/Unity-Technologies/ml-agents

cd ml-agents
pip install -e ./ml-agents-envs
pip install -e ./ml-agents


curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | os=debian dist=jessie sudo -E bash
sudo apt-get install git-lfs


python3 ml-agents/mlagents/trainers/learn.py ./config/poca/SoccerTwos.yaml --env=./training-envs-executables/SoccerTwos/SoccerTwos.x86_64 --run-id="SoccerTwos" --no-graphics


huggingface-cli login

mlagents-push-to-hf  --run-id="SoccerTwos" --local-dir="./results/SoccerTwos" --repo-id="togu6669/poca-SoccerTwos" --commit-message="First Push"`