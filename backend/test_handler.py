from fastapi import FastAPI
import uvicorn
app_n=FastAPI()

from test import analyze_f
@app_n.post("/kuch_test")
async def waiting(text:str):
    return {"ans:":analyze_f(text)}


if __name__=="__main__":
    uvicorn.run(app_n,port = 8090)


