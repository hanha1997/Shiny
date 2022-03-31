import uvicorn

if __name__ == '__main__':
    uvicorn.run('route.route:router', host = "localhost", port=8000,  reload = True)
