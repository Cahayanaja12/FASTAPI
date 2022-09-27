import json
from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

with open("mahasiswa.json", "r") as read_file:
    data = json.load(read_file)
app = FastAPI()
@app.get('/')
def root():
    return {'Mahasiswa':'Item'}

@app.get('/mahasiswa')
async def read_all_mahasiswa():
    return data

@app.get('/mahasiswa/{item_nim}')
async def read_mahasiswa(item_nim: int):
    for mahasiswa_item in data['mahasiswa']:
        if mahasiswa_item['nim'] == item_nim:
            return mahasiswa_item
    raise HTTPException(
        status_code=404, detail=f'Item tidak ditemukan'
    )

@app.post('/mahasiswa')
async def post_mahasiswa(nim:int, name:str):
    id=1
    if(len(data['mahasiswa'])>0):
        id=data['mahasiswa'][len(data['mahasiswa'])-1]['id']+1
    new_data={'id':id, 'nim' :nim, 'name':name}
    data['mahasiswa'].append(dict(new_data))
    read_file.close()
    with open("mahasiswa.json", "w") as write_file:
        json.dump(data,write_file,indent=4)
    write_file.close()

    return (new_data)
    raise HTTPException(
        status_code=404, detail=f'Internal Server Error'
    )

@app.put('/mahasiswa/{item_id}')
async def update_mahasiswa(item_id: int, nim: int, name:str):
    for mahasiswa_item in data['mahasiswa']:
        if mahasiswa_item['id'] == item_id:
            mahasiswa_item['nim'] =nim
            mahasiswa_item['name']=name
            read_file.close()
            with open("mahasiswa.json", "w") as write_file:
                json.dump(data,write_file,indent=4)
            write_file.close()

            return{"message":"Data berhasil diperbarui"}
    raise HTTPException(
        status_code=404, detail=f'Item tidak ditemukan'
    )

@app.post('/mahasiswa')
async def post_mahasiswa(nim:int, name:str):
    id=1
    if(len(data['mahasiswa'])>0):
        id=data['mahasiswa'][len(data['mahasiswa'])-1]['id']+1
    new_data={'id':id,'nim':nim,'name':name}
    data['mahasiswa'].append(dict(new_data))
    read_file.close()
    with open("mahasiswa.json", "w") as write_file:
        json.dump(data,write_file,indent=4)
    write_file.close()

    return (new_data)
    raise HTTPException(
        status_code=404, detail=f'Internal Server Error'
    )

@app.put('/mahasiswa/{item_id}')
async def update_mahasiswa(item_id: int, nim:int, name:str):
    for mahasiswa_item in data['mahasiswa']:
        if mahasiswa_item['id'] == item_id:
            mahasiswa_item['nim'] =nim
            mahasiswa_item['name']=name
            read_file.close()
            with open("mahasiswa.json", "w") as write_file:
                json.dump(data,write_file,indent=4)
            write_file.close()

            return{"message":"Data berhasil diperbarui"}
    raise HTTPException(
        status_code=404, detail=f'Item tidak ditemukan'
    )

@app.delete('/mahasiswa/{item_id}')
async def delete_mahasiswa(item_id: int):
    for mahasiswa_item in data['mahasiswa']:
        if mahasiswa_item['id'] == item_id:
            data['mahasiswa'].remove(mahasiswa_item)
            read_file.close()
            with open("mahasiswa.json", "w") as write_file:
                json.dump(data,write_file,indent=4)
            write_file.close()

            return{"message":"Data berhasil dihapus"}
    raise HTTPException(
        status_code=404, detail=f'Item tidak ditemukan'
    )