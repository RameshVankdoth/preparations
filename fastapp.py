from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()


@app.websocket("/ws")
async def socket(websocket: WebSocket):
    await websocket.accept()
    input_txt = input()
    await websocket.send_text(input_txt)

    try:
        while True:
            data = await websocket.receive_text()
            print("Data recieved is:", data)
            await websocket.send_json({"Message": f"Data recieved {data}"})
    except Exception as e:
        await websocket.send_json({"Message": e})
    finally:
        await websocket.close()


@app.get("/names")
def names():
    return {"Name": "Ramesh", "Age": 20}
