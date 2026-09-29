from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Base de datos temporal en memoria
inventario = [
    {"id": 1, "nombre": "Laptop HP", "cantidad": 5, "precio": 650.00},
    {"id": 2, "nombre": "Mouse Inalámbrico", "cantidad": 15, "precio": 15.50}
]

@app.route('/')
def inicio():
    # Lee una variable de entorno para demostración de configuración
    entorno = os.environ.get("ENTORNO", "Desarrollo Local")
    return render_template('index.html', inventario=inventario, entorno=entorno)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form.get('nombre')
    cantidad = int(request.form.get('cantidad', 0))
    precio = float(request.form.get('precio', 0.0))
    
    nuevo_id = len(inventario) + 1
    inventario.append({"id": nuevo_id, "nombre": nombre, "cantidad": cantidad, "precio": precio})
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    # Puerto dinámico asignado por el proveedor PaaS
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)