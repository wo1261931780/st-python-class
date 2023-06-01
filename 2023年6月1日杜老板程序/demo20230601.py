import requests


def main():
    selected_text = input("请选中一句话：")

    # 发送选中的文本到后台进行处理
    response = process_selected_text(selected_text)

    if response.ok:
        formatted_text = response.json().get('formattedText')
        print("格式化后的文本：")
        print(formatted_text)
    else:
        print("处理失败，请重试！")


def process_selected_text(selected_text):
    # ChatGPT后台处理的URL
    url = 'https://api.openai.com/v1/engines/davinci-codex/completions'

    # ChatGPT API密钥
    api_key = 'YOUR_API_KEY'

    # ChatGPT请求参数
    params = {
        'prompt': selected_text,
        'temperature': 0.5,
        'max_tokens': 100,
        'n': 1,
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }

    # 发送请求到ChatGPT后台
    response = requests.post(url, json=params, headers=headers)

    return response


if __name__ == '__main__':
    main()
