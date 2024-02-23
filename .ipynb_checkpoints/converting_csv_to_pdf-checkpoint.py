import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Load the CSV file
def load_csv(csv_path):
    return pd.read_csv(csv_path)

# Create a PDF document from the DataFrame
def create_pdf(dataframe, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter  # Get the width and height of the page
    x_offset = 50  # Starting x position
    y_offset = height - 50  # Starting y position, from the top down

    # Set up a simple header
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_offset, y_offset, "Student Information")
    c.setFont("Helvetica", 12)
    
    # Column headers
    columns = ['id', 'name', 'city', 'nationality','gender','age','english.grade','math.grade','sciences.grade','language.grade','portfolio.rating','coverletter.rating','refletter.rating']
    y_offset -= 20  # Move down to write the column names

    # Adjust these positions as necessary to fit your layout
    for column in columns:
        c.drawString(x_offset, y_offset, column)
        x_offset += 100  # Space out the column names
    
    y_offset -= 10  # Add a small gap before the first row
    c.setFont("Helvetica", 10)

    # Iterate over the rows in the DataFrame and print each student's info
    for index, row in dataframe.iterrows():
        x_offset = 50  # Reset x position for each new row
        y_offset -= 20  # Move to the next line
        c.drawString(x_offset, y_offset, str(row['id']))  # Adjust field names based on your CSV
        x_offset += 100
        c.drawString(x_offset, y_offset, str(row['name']))
        x_offset += 100
        c.drawString(x_offset, y_offset, str(row['city']))
        x_offset += 100
        c.drawString(x_offset, y_offset, str(row['nationality']))
        x_offset += 100
        c.drawString(x_offset, y_offset, str(row['gender']))
        x_offset += 100
        c.drawString(x_offset, y_offset, str(row['age']))
        x_offset += 100
        c.drawString(x_offset, y_offset, str(row['english.grade']))
        x_offset += 100
        c.drawString(x_offset, y_offset, str(row['sciences.grade']))
        x_offset += 100
        c.drawString(x_offset, y_offset, str(row['language.grade']))
        x_offset += 100
        c.drawString(x_offset, y_offset, str(row['portfolio.rating']))
        x_offset += 100
        c.drawString(x_offset, y_offset, str(row['coverletter.rating']))
        x_offset += 100
        c.drawString(x_offset, y_offset, str(row['refletter.rating']))
        if y_offset < 50:  # Check if we are at the bottom of the page
            c.showPage()  # Start a new page
            y_offset = height - 50  # Reset the y position

    c.save()

if __name__ == "__main__":
    csv_path = r"C:\Users\Sathish\machine learning\kriya\student-dataset.csv"
 # Update this to your CSV file path
    pdf_path = "students_info.pdf"  # The output PDF file name
    df = load_csv(csv_path)
    create_pdf(df, pdf_path)
