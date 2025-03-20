Linux 

git clone https://github.com/Unity-Technologies/ml-agents

cd ml-agents
pip install -e ./ml-agents-envs
pip install -e ./ml-agents



git-lfs
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | os=debian dist=jessie sudo -E bash
sudo apt-get install git-lfs


Mac only:
after downloading app you need to add exex attributes:
xattr -cr training-envs-executables/SoccerTwos/SoccerTwos.app


Linux version, there was a broken venv which not installed properly and I did not have a relative paths
python3 ml-agents/mlagents/trainers/learn.py ./config/poca/SoccerTwos.yaml --env=./training-envs-executables/SoccerTwos/SoccerTwos.x86_64 --run-id="SoccerTwos" --no-graphics


Mac version of learning with correct venv:
mlagents-learn ./config/poca/SoccerTwos.yaml --env=./training-envs-executables/SoccerTwos/SoccerTwos.app --run-id="SoccerTwos" --no-graphics


huggingface-cli login
mlagents-push-to-hf  --run-id="SoccerTwos" --local-dir="./results/SoccerTwos" --repo-id="togu6669/poca-SoccerTwos" --commit-message="First Push"`

