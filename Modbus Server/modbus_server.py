import random
import time
from threading import Thread
from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusDeviceContext, ModbusServerContext

store = ModbusDeviceContext(
    di=ModbusSequentialDataBlock(0, [0]*10),
    co=ModbusSequentialDataBlock(0, [0]*10),
    hr=ModbusSequentialDataBlock(0, [0]*10),
    ir=ModbusSequentialDataBlock(0, [0]*10),
)

context = ModbusServerContext(devices=store, single=True)

# 🔥 Dynamic temperature simulation
def update_temperature():
    while True:
        temp = random.randint(20, 80)
        store.setValues(3, 1, [temp])
        time.sleep(2)

Thread(target=update_temperature).start()

print("🔥 Modbus Server Running with LIVE temperature...")

StartTcpServer(context, address=("0.0.0.0", 1502))
