import requests

def get_api_data():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": "فشل الاتصال بالـ API",
                "status_code": response.status_code
            }

    except requests.exceptions.RequestException as e:
        return {
            "error": "خطأ في الاتصال",
            "details": str(e)
        }

# 👇 هذا هو المهم
print(get_api_data())
