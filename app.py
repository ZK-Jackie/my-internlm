import os
from lmdeploy.serve.gradio.turbomind_coupled import run_local
from lmdeploy.messages import TurbomindEngineConfig
# 获取个人 token
git_token = os.getenv('GIT_READ_TOKEN')
# 当前文件路径
base_path = os.path.dirname(__file__)
# 模型路径
model_path = f'{base_path}/ft-model'
# 下载小文件
os.system(f'git clone https://ZK-Jackie:{git_token}@code.openxlab.org.cn/ZK-Jackie/my-internlm.git {model_path}')
# 下载模型文件
os.system(f'cd {model_path} && git lfs pull')
# 部署模型
run_local(model_path, server_port=7860)
