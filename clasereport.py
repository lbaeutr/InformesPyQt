from fpdf import FPDF
import os

title = "Informe de Datos"
logo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "logo.png"))

class PDFBase(FPDF):
    def header(self):
        if os.path.exists(logo_path):
            self.image(logo_path, 10, 10, 25)  
            self.set_font("Arial", "B", 25)
        self.set_y(18) 
        self.set_text_color(50, 50, 50)
        self.cell(0, 10, title, ln=True, align="C")
        self.ln(10)  

    def footer(self):
        self.set_y(-20)
        self.set_font("Arial", "I", 10)
        self.set_text_color(100)
        self.cell(0, 10, f"Página {self.page_no()}", align="R")

    def add_section(self, title, content):
        """Añade una sección sin centrar el contenido"""
        self.ln(10) 
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, title, ln=True, align="L")  
        self.ln(5)
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 7, content, align="L")  
        self.ln(5)

    def add_code_block(self, code):
        """Añade un bloque de código con formato especial"""
        self.set_fill_color(30, 30, 30)  
        self.set_text_color(255, 255, 255)  
        self.set_font("Courier", "", 10)
        
        left_margin = 30
        right_margin = 30
        self.set_x(left_margin)  
        max_width = self.w - left_margin - right_margin  

        self.multi_cell(max_width, 7, code, border=1, fill=True, align="L")

        self.set_text_color(0, 0, 0)  
        self.ln(10)
        

class PDF1(PDFBase):
    def add_table(self, headers, data):
        """Añade una tabla con encabezados y datos, ajustando el ancho de las columnas al contenido."""
        # Calcular el ancho máximo de cada columna
        col_widths = []
        for i in range(len(headers)):
            max_width = self.get_string_width(headers[i])  # Ancho inicial basado en los encabezados
            for row in data:
                item_width = self.get_string_width(str(row[i]))
                if item_width > max_width:
                    max_width = item_width
            col_widths.append(max_width + 10)  # Añadir un pequeño margen
        
        page_width = self.w - 2 * self.l_margin
        total_width = sum(col_widths) + len(headers) * 2  
        if total_width > page_width:
            scale_factor = page_width / total_width
            col_widths = [int(width * scale_factor) for width in col_widths]

        # Dibujar los encabezados
        self.set_fill_color(50, 50, 150)  
        self.set_text_color(255, 255, 255)  
        self.set_font('Arial', 'B', 12)
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, border=1, align='C', fill=True)
        self.ln()

        # Dibujar los datos
        self.set_fill_color(240, 240, 240)  
        self.set_text_color(0)  
        self.set_font('Arial', '', 12)
        fill = False
        for row in data:
            for i, item in enumerate(row):
                self.cell(col_widths[i], 10, str(item), border=1, align='L', fill=fill)
            self.ln()
            fill = not fill

class PDF2(PDFBase):
    def add_table(self, headers, data):
        table_width = self.get_string_width(headers[0]) + self.get_string_width(headers[1]) + 20
        page_width = self.w - 2 * self.l_margin
        x_offset = (page_width - table_width) / 2
        self.set_x(self.l_margin + x_offset)
        
        self.set_fill_color(50, 50, 150)  
        self.set_text_color(255, 255, 255)  
        self.set_font('Arial', 'B', 12)
        for header in headers:
            self.cell(40, 10, header, 1, 0, 'C', fill=True)
        self.ln()
        
        self.set_fill_color(240, 240, 240)  
        self.set_text_color(0) 
        self.set_font('Arial', '', 12)
        fill = False
        for row in data:
            self.set_x(self.l_margin + x_offset)
            for item in row:
                self.cell(40, 10, item, 1, 0, 'C', fill=fill)
            self.ln()
            fill = not fill

    def footer(self):
        self.set_y(-20)  
        
        if os.path.exists(logo_path):
            self.image(logo_path, x=10, y=275, w=10, h=10) 
        
        self.set_font("Arial", "I", 10)
        self.set_text_color(100)
        self.cell(0, 10, f"Página {self.page_no()}", align="R")

class PDF3(PDFBase):
    def add_bullet_list(self, title, items):
        """Añade una lista con viñetas"""
        self.set_font('Arial', 'B', 14)
        self.set_text_color(0, 102, 102)  # Color azul oscuro
        self.cell(0, 10, title, ln=True, align='L')
        
        self.set_draw_color(0, 102, 102)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

        self.set_text_color(0, 0, 0)  # Color de texto negro
        self.set_font('Arial', '', 12)
        for i, item in enumerate(items, 1):
            self.cell(10)
            self.cell(0, 8, f"{i}. {item}", ln=True, align='L')
        self.ln(10)

class PDF4(FPDF):
    def header(self):
        self.set_y(10)
        
        # Añadir el logo
        if os.path.exists(logo_path):
            self.image(logo_path, 10, 10, 25)  # Logo en la esquina superior izquierda
        
        self.set_draw_color(150, 150, 150)  
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())

        self.set_font('Times', 'B', 20)
        self.set_text_color(50, 50, 50)  
        self.set_y(self.get_y() + 5)
        self.cell(0, 10, "Informe de Evaluación", ln=True, align='C')

        self.set_font('Times', 'I', 12)
        self.set_text_color(80, 80, 80)  
        self.set_y(self.get_y() + 3)
        self.cell(0, 10, "Reporte de Distribución de Preguntas por Nivel", ln=True, align='C')

        self.set_y(self.get_y() + 5)
        self.set_draw_color(150, 150, 150)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_fill_color(150, 150, 150)  
        self.cell(0, 6, "", ln=True, fill=True)  
        
        # Número de página
        self.set_font("Times", "I", 10)
        self.set_text_color(255, 255, 255)  
        self.set_y(-12)
        self.cell(0, 6, f'Página {self.page_no()}', align='C', fill=True)

    def add_section(self, title, content):
        self.set_fill_color(240, 240, 240)  
        self.set_text_color(30, 30, 30)  
        self.set_font('Times', 'B', 14)
        self.cell(0, 10, title, ln=True, align='L', fill=True)
        self.ln(5)

        self.set_font('Times', '', 12)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 8, content)
        self.ln(10)

    def add_code_block(self, code):
        """Código en bloque con bordes finos"""
        self.set_font('Courier', '', 10)
        self.set_fill_color(230, 230, 230)  
        self.set_text_color(20, 20, 20)  

        self.cell(0, 8, 'Código SQL:', ln=True, align='L')
        self.ln(2)
        
        self.multi_cell(0, 8, code.encode('latin-1', 'ignore').decode('latin-1'), border=1, fill=True)
        self.ln(10)

    def add_table(self, headers, data):
        """Tabla minimalista con bordes finos"""
        self.set_font('Times', 'B', 12)
        self.set_fill_color(220, 220, 220)  
        self.set_text_color(0, 0, 0)

        for header in headers:
            self.cell(65, 10, header.encode('latin-1', 'ignore').decode('latin-1'), border=1, align='C', fill=True)
        self.ln()

        self.set_font('Times', '', 12)
        for row in data:
            for item in row:
                self.cell(65, 10, item.encode('latin-1', 'ignore').decode('latin-1'), border=1, align='C')
            self.ln()
        self.ln(10)

class PDF5(FPDF):
    def header(self):
        if os.path.exists(logo_path):
            self.image(logo_path, 10, 8, 15)  
        # Encabezado principal
        self.set_fill_color(0, 51, 102)  
        self.rect(30, 10, 8, 20, 'F')  # Rectángulo decorativo movido a la derecha

        self.set_font('Helvetica', 'B', 18)
        self.set_text_color(0, 51, 102)  
        self.set_y(12)  
        self.set_x(40)  
        self.cell(0, 10, "Reporte de Respuestas Específicas", ln=True, align='L')

        # Línea decorativa
        self.set_draw_color(0, 51, 102)
        self.line(40, self.get_y(), 200, self.get_y())  
        self.ln(10)

    def footer(self):
        self.set_y(-20)
        self.set_draw_color(0, 51, 102)  
        self.set_line_width(1)
        self.line(10, self.get_y(), 200, self.get_y())  

        self.set_y(-15)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(0, 51, 102)
        self.cell(0, 8, f'Página {self.page_no()}', border=1, align='C')

    def add_section(self, title, content):
        """Sección con fondo gris claro y borde lateral"""
        self.set_fill_color(230, 230, 230)  
        self.set_text_color(0, 0, 0)  
        self.set_font('Helvetica', 'B', 14)
        self.cell(0, 10, title, ln=True, align='L', fill=True)
        self.ln(5)

        self.set_font('Helvetica', '', 12)
        self.multi_cell(0, 8, content)
        self.ln(10)

    def add_code_block(self, code):
        self.set_fill_color(50, 50, 50)  
        self.set_text_color(255, 255, 255)  
        self.set_font('Courier', '', 10)

        self.cell(0, 8, 'Consulta SQL:', ln=True, align='L')
        self.ln(2)

        self.multi_cell(0, 8, code.encode('latin-1', 'ignore').decode('latin-1'), border=1, fill=True)
        self.ln(10)

        self.set_text_color(0, 0, 0)

    def add_table(self, headers, data):
        table_width = len(headers) * 60  
        x_start = (self.w - table_width) / 2  
        self.set_x(x_start)

        self.set_font('Helvetica', 'B', 12)
        self.set_fill_color(0, 51, 102)  
        self.set_text_color(255, 255, 255) 

        for header in headers:
            self.cell(60, 10, header.encode('latin-1', 'ignore').decode('latin-1'), border=1, align='C', fill=True)
        self.ln()

        self.set_text_color(0)
        self.set_font('Helvetica', '', 12)

        for row in data:
            self.set_x(x_start)  
            for item in row:
                self.cell(60, 10, item.encode('latin-1', 'ignore').decode('latin-1'), border=1, align='C')
            self.ln()
        self.ln(10)