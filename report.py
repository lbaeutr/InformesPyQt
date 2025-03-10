import sys
import os
import webbrowser
from clasereport import PDF1, PDF2, PDF3 , PDF4 , PDF5
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic

class Ventana(QMainWindow):
    def __init__(self):
        super(Ventana, self).__init__()

        ui_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "report.ui"))
        uic.loadUi(ui_path, self)

        #! Conectar botones a funciones
        self.informe.clicked.connect(self.crea_informe1)
        self.informe2.clicked.connect(self.crea_informe2)
        self.informe3.clicked.connect(self.crea_informe3)
        self.informe4.clicked.connect(self.crea_informe4)
        self.informe5.clicked.connect(self.crea_informe5)

    def abrir_pdf(self, filename):
        """Abre automáticamente el informe PDF generado."""
        filepath = os.path.abspath(filename)
        if os.path.exists(filepath):
            webbrowser.open_new(filepath)

    def crea_informe1(self):
        """Informe 1: Preguntas y Respuestas Correctas"""
        pdf = PDF1()
        pdf.add_page()
        
        pdf.add_section("1. Preguntas y Respuestas Correctas", 
                        "Este informe muestra las preguntas junto con sus respuestas correctas.")

        code = """SELECT Pregunta.texto AS Pregunta, Respuesta.texto AS Respuesta
    FROM Pregunta
    JOIN Respuesta ON Pregunta.id = Respuesta.pregunta_id
    WHERE Respuesta.correcta = 1;"""
        pdf.add_code_block(code)

        headers = ["Pregunta", "Respuesta"]
        data = [
            ("¿Qué sigla representa la planificación de recursos empresariales?", "ERP"),
            ("¿Qué sistema gestiona clientes y ventas?", "CRM"),
            ("¿Qué sigla describe la cadena de suministro?", "SCM"),
            ("¿Qué módulo de un ERP se encarga de la contabilidad?", "Finanzas"),
            ("¿Qué sistema optimiza el control de almacenes?", "WMS"),
            ("¿Qué sigla identifica la planificación de producción?", "MRP"),
            ("¿Qué módulo administra las adquisiciones?", "Compras"),
            ("¿Qué sistema gestiona el capital humano?", "HRMS"),
            ("¿Qué sigla se asocia con la automatización de procesos?", "BPM"),
            ("¿Qué sistema facilita la gestión de proyectos?", "PPM"),
        ]
        pdf.add_table(headers, data)

        pdf.add_section("Análisis:",
                        "Este informe es útil para revisar las preguntas y respuestas correctas "
                        "en un examen o cuestionario. Permite a los estudiantes y profesores "
                        "verificar la precisión de las respuestas proporcionadas.")

        filename = "informe1.pdf"
        pdf.output(filename, 'F')
        self.abrir_pdf(filename)
        
    def crea_informe2(self):
        """Informe 2: Jugadores con Puntuaciones Más Altas"""
        pdf = PDF2()
        pdf.add_page()
        
        pdf.add_section("2. Jugadores con Puntuaciones Más Altas", 
                        "Este informe muestra los jugadores con sus puntuaciones más altas en formato de tabla.")

        code = """SELECT Jugador.nombre, MAX(Puntuacion.puntuacion) AS Puntuacion_Maxima
        FROM Jugador
        JOIN Puntuacion ON Jugador.id = Puntuacion.jugador_id
        GROUP BY Jugador.nombre
        ORDER BY Puntuacion_Maxima DESC;"""
        pdf.add_code_block(code)

        headers = ["Jugador", "Puntuación Máxima"]
        data = [
            ("user@gmail.com", "70"),
            ("admin@gmail.com", "30"),
        ]
        
        pdf.add_table(headers, data)

        pdf.add_section("Análisis:",
                        "Este informe permite visualizar de forma clara las puntuaciones "
                        "más altas obtenidas por los jugadores en el juego.")

        filename = "informe2.pdf"
        pdf.output(filename, 'F')
        self.abrir_pdf(filename)


    def crea_informe3(self):
        """Informe 3: Preguntas Difíciles"""
        pdf = PDF3()
        pdf.add_page()

        pdf.add_section("3. Preguntas Difíciles", 
                        "Este informe muestra todas las preguntas clasificadas como 'Difícil'.")

        code = """SELECT Pregunta.texto 
        FROM Pregunta
        JOIN Nivel ON Pregunta.nivel_id = Nivel.id
        WHERE Nivel.nombre = 'Difícil';"""
        pdf.add_code_block(code)

        preguntas_dificiles = [
            "¿Qué palabra clave define una interfaz?",
            "¿Qué tipo de dato inmutable se usa para cadenas?",
            "¿Qué símbolo se emplea para la herencia?",
            "¿Qué colección evita elementos duplicados?",
            "¿Qué estructura funciona como una pila?",
        ]
        pdf.add_bullet_list("Preguntas Difíciles:", preguntas_dificiles)

        pdf.add_section("Análisis:",
                        "Este informe permite identificar las preguntas más desafiantes "
                        "en un examen o cuestionario, lo que ayuda a enfocar los esfuerzos "
                        "de estudio en áreas críticas.")

        filename = "informe3.pdf"
        pdf.output(filename, 'F')
        self.abrir_pdf(filename)


    def crea_informe4(self):
        """Informe 4: Distribución de Preguntas por Nivel"""
        pdf = PDF4()
        pdf.add_page()

        pdf.add_section("4. Distribución de Preguntas por Nivel", 
                        "Este informe muestra la cantidad de preguntas por nivel de dificultad.")

        code = """SELECT Nivel.nombre AS Nivel, COUNT(Pregunta.id) AS Total_Preguntas
        FROM Nivel
        JOIN Pregunta ON Nivel.id = Pregunta.nivel_id
        GROUP BY Nivel.nombre;"""
        pdf.add_code_block(code)

        headers = ["Nivel", "Total de Preguntas"]
        data = [
            ("Fácil", "10"),
            ("Medio", "10"),
            ("Difícil", "10"),
        ]
        pdf.add_table(headers, data)

        pdf.add_section("Análisis:",
                        "Este informe permite evaluar la distribución de preguntas por nivel "
                        "de dificultad, asegurando un balance adecuado en las evaluaciones.")

        filename = "informe4.pdf"
        pdf.output(filename, 'F')
        self.abrir_pdf(filename)

    def crea_informe5(self):
        """Informe 5: Respuestas de una Pregunta Específica"""
        pdf = PDF5()
        pdf.add_page()

        pdf.add_section("5. Respuestas de una Pregunta Específica", 
                        "Este informe muestra todas las respuestas de una pregunta específica.")

        code = """SELECT Respuesta.texto, Respuesta.correcta
        FROM Respuesta
        JOIN Pregunta ON Respuesta.pregunta_id = Pregunta.id
        WHERE Pregunta.texto = '¿Qué lenguaje se utiliza en PyQt6?';"""
        pdf.add_code_block(code)

        headers = ["Respuesta", "Correcta"]
        data = [
            ("Python", "Sí"),
        ]
        pdf.add_table(headers, data)

        pdf.add_section("Análisis:",
                        "Este informe permite revisar las respuestas de una pregunta específica, "
                        "lo que es útil para verificar la precisión de las opciones proporcionadas.")

        filename = "informe5.pdf"
        pdf.output(filename, 'F')
        self.abrir_pdf(filename)


def main():
    app = QApplication(sys.argv)
    window = Ventana()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
