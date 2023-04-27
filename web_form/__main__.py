import uvicorn

def start_react_app():
    pass

def start_server():
    uvicorn.run("web_form:app", host='0.0.0.0', port=8000, reload=True)

if __name__ == "__main__":
    start_server()