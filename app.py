import os
from lmdeploy.serve.gradio.turbomind_coupled import run_local
from lmdeploy.messages import TurbomindEngineConfig
# 获取个人 token
git_token = os.getenv('GIT_READ_TOKEN')
# 下载微调后的模型
base_path = './ft-model'
os.system(f'git clone https://ZK-Jackie:{git_token}@code.openxlab.org.cn/ZK-Jackie/my-internlm.git {base_path}')
os.system(f'cd {base_path} && git lfs pull')
# 部署模型
model_path = f'{__file__}/ft-model'
run_local(model_path, server_port=7860)