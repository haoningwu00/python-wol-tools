import fastapi
import uvicorn
import logging
import mods.wol

_LOGGER = logging.getLogger(__name__)
app = fastapi.FastAPI()


@app.get("/api/wol/{mac}")
async def read_mac_addr(mac):
    n_mac = mods.wol.normalization_mac(mac)
    repo = mods.wol.send_magic_pack(n_mac)
    r_json = {
        "Return": repo
    }

    return r_json


def start_wol_server():
    uvicorn.run(app, host="0.0.0.0", port=20000)
    _LOGGER.info('启动uvicron服务器')
