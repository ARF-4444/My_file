import requests
import re

from flask import jsonify

# LM Studio 本地服务器的地址
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"


def chat(request):
    # 获取前端发送的消息
    data = request.json
    user_message = data.get("message", "")

    # 构造请求数据
    payload = {
        "messages": [{"role": "user", "content": user_message}],
        "temperature": 0.7,
        "max_tokens": -1,
        "max_tokens": -1,
        "stream": False
    }

    # 发送请求到 LM Studio 本地服务器
    try:
        response = requests.post(LM_STUDIO_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            # 使用正则表达式去除 <think>...</think> 标签及其内容
            cleaned_response = re.sub(r'<think>[\s\S]*?</think>', '', result["choices"][0]["message"]["content"])
            cleaned_response = re.sub(r"\n{2,}", "\n", cleaned_response)
            cleaned_response = cleaned_response.strip()
            return jsonify({"response": cleaned_response})
        else:
            return jsonify({"error": f"请求失败，状态码：{response.status_code}"})
    except Exception as e:
        return jsonify({"error": f"连接失败：{str(e)}"})
