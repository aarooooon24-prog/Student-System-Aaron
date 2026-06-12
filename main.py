import model
import controller

model.init_db()   # 👈 creates table if not exists
controller.run()